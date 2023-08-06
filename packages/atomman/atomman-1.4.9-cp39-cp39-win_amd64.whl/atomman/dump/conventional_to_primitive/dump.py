# coding: utf-8
# Standard Python libraries
from typing import Optional, Union, Tuple

# http://www.numpy.org/
import numpy as np
import numpy.typing as npt

# atomman imports
from ... import Box, System
from ...tools import miller

def dump(system: System,
         setting: str = 'p',
         smallshift: Optional[npt.ArrayLike] = None,
         rtol: float = 1e-05,
         atol: float = 1e-08,
         check_basis: bool = True,
         check_family: bool = True,
         return_transform: bool = False,
         ) -> Union[System, Tuple[System, np.ndarray]]:
    """
    Transforms a conventional unit cell system of a specified Bravais space
    lattice setting into a primitive unit cell. The
    primitive_to_conventional and conventional_to_primitive dump styles are
    meant to be inverse operations, within floating point precision, to provide
    compatible primitive and conventional unit cells.

    NOTE: This dump style expects that the original starting system is a
    conventional unit cell, and only limited checks are performed to assert
    this!  Use the 'primitive_cell' dump style for a more comprehensive
    primitive unit cell identifier.

    Parameters
    ----------
    system : atomman.System
        A conventional unit cell system to find the corresponding primitive
        unit cell for.
    setting : str, optional
        The conventional cell space lattice setting. Allowed values are
        'p' for primitive, 'f' for face-centered, 'i' for body centered, and
        'a', 'b', or 'c' for side-centered.
    smallshift : array-like object or None, optional
        A small rigid body shift to apply to the atomic positions when searching
        for which atoms are within the primitive cell.  This helps avoid
        identification issues when atoms are directly on the box boundaries.
        The default value of None will use a smallshift of [0.001, 0.001, 0.001].
    rtol : float, optional
        Relative tolerance to use for numpy.isclose.  This is used here to check
        that the conventional cell has atoms in the expected lattice positions
        for the given setting.
    atol : float, optional
        Absolute tolerance to use for numpy.isclose.  This is used here to check
        that the conventional cell has atoms in the expected lattice positions
        for the given setting.
    check_basis : bool, optional
        If True (default), a quick check will be performed on the system to see
        if it appears consistent with a Bravais space lattice with the given
        setting.  Turning this check off may be necessary for more complex
        cases, such as non-conventional cell representations and complex unit
        cells where no atoms are at the lattice site [0, 0, 0].
    check_family : bool, optional
        If True (default), then the Bravais space lattice check will include
        a check that the crystal family is consistent with a Bravais lattice
        of the given setting. For example, Bravais lattices with setting 'f'
        only exist for cubic and orthogonal cells.  This check is not done if
        either check_family or check_basis is False.  Turning this off allows
        for transformations of non-conventional cells.
    return_transform : bool, optional
        Indicates if the Cartesian transformation matrix associated with
        rotating from the conventional cell to primitive cell orientations is
        returned.  Default value is False.

    Returns
    -------
    p_ucell : atomman.System
        The primitive unit cell obtained by transforming the given conventional
        unit cell system.
    transform : numpy.ndarray
        The Cartesian transformation matrix associated with converting from the
        primitive cell orientation to the conventional cell orientation.  Only
        returned if return_transform is True.

    Raises
    ------
    ValueError
        If smallshift is not a 3D vector.
    AssertionError
        If the algorithm fails to find the expected number of atoms in the
        primitive cell.
    """

    # Handle smallshift parameter values
    if smallshift is None:
        smallshift = np.array([0.001, 0.001, 0.001])
    else:
        smallshift = np.asarray(smallshift)
        if smallshift.shape != 3:
            raise ValueError('smallshift must be a 3D vector')

    # Check that system is of the proper setting
    if check_basis:
        is_basis = check_setting_basis(system, setting=setting, rtol=rtol, atol=atol,
                                       check_family=check_family)
        if not is_basis:
            raise ValueError('system atoms do not seem to match indicated setting')

    # Get rotations to convert conventional to 2x2x2 primitive (ensures int uvws)
    c2p_uvws = miller.vector_primitive_to_conventional(2 * np.identity(3), setting=setting)

    # Construct a 2x2x2 primitive supercell by rotating the conventional cell
    p8_cell, transform = system.rotate(c2p_uvws, return_transform=True)

    # Create a box for the primitive unit cell using half of all three box vects of p8_cell
    box = Box(vects = p8_cell.box.vects / 2)

    # Apply the smallshift to p8_cell atomic positions to avoid boundary issues
    p8_cell.atoms.pos += smallshift
    p8_cell.wrap()

    # Identify atoms inside p_box
    keepindex = box.inside(p8_cell.atoms.pos)
    assert np.sum(keepindex) == p8_cell.natoms / 8

    # Reverse smallshift
    p8_cell.atoms.pos -= smallshift
    p8_cell.wrap()

    # Create Atoms by slicing from p8_cell
    atoms = p8_cell.atoms[keepindex]
    p_ucell = System(box=box, atoms=atoms, symbols=system.symbols)
    p_ucell.wrap()

    # Search for atom near periodic (0,0,0)
    dmag = np.array(p_ucell.dmag(range(p_ucell.natoms), np.zeros((p_ucell.natoms, 3))))
    if dmag.shape == ():
        dmag = np.array([dmag])
    zeroindex = np.isclose(dmag, 0.0)

    # Adjust atoms so identified atom is exactly at (0,0,0)
    if np.sum(zeroindex) == 1:
        zerocoord = p_ucell.atoms.pos[zeroindex]
        p_ucell.atoms.pos -= zerocoord

        p_ucell.wrap()

    if return_transform:
        return p_ucell, transform
    else:
        return p_ucell

def check_setting_basis(ucell: System,
                        setting: str = 'p',
                        rtol: float = 1e-05,
                        atol: float = 1e-08,
                        check_family: bool = True) -> bool:
    """
    Checks if a unit cell system is consistent with one of the standard 14
    Bravais space lattices.  For the indicated cell setting, a search is
    performed to verify that atoms of the same type are positioned at the
    lattice site(s), and that the lattice parameters are consistent with a
    crystal family that has that setting.

    NOTE: This is only meant as a quick check and does not perform a
    comprehensive symmetry analysis of the atomic coordinates.

    Parameters
    ----------
    ucell : atomman.System
        The unit cell system to check if it appears consistent with the given
        crystal space group lattice setting.
    setting : str
        The Bravais space lattice setting value.  Allowed values
        are 'p' for primitive, 'i' for body-centered, 'f' for face-centered,
        and 'a', 'b', or 'c' for side-centered.
    rtol : float, optional
        Relative tolerance to use for numpy.isclose.  This is used both to
        check for atoms in the equivalent lattice sites and the crystal family.
    atol : float, optional
        Absolute tolerance to use for numpy.isclose.  This is used both to
        check for atoms in the equivalent lattice sites and the crystal family.
    check_family : bool, optional
        If True (default), then the crystal family of the unit cell is checked
        to see if the family+setting is one of the 14 standard Bravais space
        lattices.

    Returns
    -------
    bool
        True if the unit cell appears consistent with the indicated Bravais
        lattice setting.  False if atoms are not found at the ideal lattice
        sites, or no Bravais space lattice exists with the family+setting.
    """

    family = ucell.box.identifyfamily(rtol=rtol, atol=atol)

    # Define relative positions based on setting and check crystal family
    if setting == 'p':
        relpos = np.array([[0.0, 0.0, 0.0]])
        families = ['cubic', 'hexagonal', 'tetragonal', 'rhombohedral',
                    'orthorhombic', 'monoclinic', 'triclinic']

    elif setting == 'i':
        relpos = np.array([[0.0, 0.0, 0.0],
                           [0.5, 0.5, 0.5]])
        families = ['orthorhombic', 'tetragonal', 'cubic']

    elif setting == 'f':
        relpos = np.array([[0.0, 0.0, 0.0],
                           [0.5, 0.5, 0.0],
                           [0.5, 0.0, 0.5],
                           [0.0, 0.5, 0.5]])
        families = ['orthorhombic', 'cubic']

    elif setting == 'a':
        relpos = np.array([[0.0, 0.0, 0.0],
                           [0.0, 0.5, 0.5]])
        families = ['monoclinic', 'orthorhombic']

    elif setting == 'b':
        relpos = np.array([[0.0, 0.0, 0.0],
                           [0.5, 0.0, 0.5]])
        families = ['monoclinic', 'orthorhombic']

    elif setting == 'c':
        relpos = np.array([[0.0, 0.0, 0.0],
                           [0.5, 0.5, 0.0]])
        families = ['monoclinic', 'orthorhombic']

    else:
        raise ValueError('invalid setting: must be p, i, f, a, b, or c')

    # Check that crystal family + setting is a Bravais space lattice
    if check_family and family not in families:
        return False

    pos = ucell.box.position_relative_to_cartesian(relpos)

    atype = None
    for p in pos:

        # Check for atom at pos
        index = index_of_pos(ucell, p, rtol=rtol, atol=atol)
        if np.sum(index) == 0:
            return False
        elif np.sum(index) > 1:
            raise ValueError('Multiple overlapping atoms found')

        # Check that atom's atype is same as other pos
        if atype is None:
            atype = ucell.atoms.atype[index][0]
        elif atype != ucell.atoms.atype[index][0]:
            return False

    return True

def index_of_pos(system, pos, rtol=1e-05, atol=1e-08):
    """
    Searches for atoms in a system to check if they correspond to the given position
    within rounding tolerances and accounting for periodic boundaries.

    Parameters
    ----------
    system : atomman.System
        The system to search.
    pos : array-like object
        The atomic position to search for in the system.
    atol : float, optional
        The absolute tolerance to use with numpy.isclose for identifying matches.
    rtol : float, optional
        The relative tolerance to use with numpy.isclose for identifying matches.

    Returns
    -------
    numpy.ndarray
        Bool values indicating which atoms in system have coordinates at pos.
    """
    # Compute dmag between all atoms in ucell and pos
    dmag = np.array(system.dmag(system.atoms.pos, np.asarray(pos)))

    # Reshape for single atom systems
    if dmag.shape == ():
        dmag = np.array([dmag])

    # Identify which atoms are at pos
    return np.isclose(dmag, 0.0, rtol=rtol, atol=atol)
