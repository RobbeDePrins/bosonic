
from .aa_phi import aa_phi, aa_phi_lossy, aa_phi_restricted, fock_to_idx
from .aa_phi import permanent, permanent_vjp, aa_phi_vjp
from .fock import binom
from . import density
from . import reck
from . import fock
from . import clements
from . import qonn
# from .phi_dispatch import aa_phi, aa_phi_cpu, aa_phi_gpu

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__", "aa_phi", "aa_phi_lossy",
    "aa_phi_restricted", "density", "binom", "reck", "fock", "clements",
    "fock_to_idx", "permanent", "qonn", "permanent_vjp", "aa_phi_vjp"
]

__title__ = "bosonic"
__version__ = "0.3.0"
__description__ = "Library for fast indistinguishable boson computations"
__url__ = "https://github.com/steinbrecher/bosonic"

__author__ = "Greg Steinbrecher"
__email__ = "steinbrecher@alum.mit.edu"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2017-2019 Greg Steinbrecher"
