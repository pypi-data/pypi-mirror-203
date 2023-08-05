# This file is part of the Gudhi Library - https://gudhi.inria.fr/ - which is released under MIT.
#  See file LICENSE or go to https://gudhi.inria.fr/licensing/ for full license details.
#  Author(s):       Vincent Rouvreau
#
# Copyright (C) 2016  Inria
#
# Modification(s):
#   - YYYY/MM Author: Description of the modification

from importlib import import_module
from sys import exc_info

__author__ = "GUDHI Editorial Board"
__copyright__ = "Copyright (C) 2016 Inria"
__license__ = "https://gudhi.inria.fr/licensing/"
__version__ = "3.8.0rc3"
# This variable is used by doctest to find files
__root_source_dir__ = "/__w/gudhi-devel/gudhi-devel"
__debug_info__ =     "Pybind11 version 2.10.4 \n" \
    "Python version 3.10.10\n" \
    "Cython version 0.29.34 \n" \
    "Numpy version 1.21.6 \n" \
    "Eigen3 version 3.3.7\n" \
    "Boost version 107300\n" \
    "CGAL header only version 5.4.1\n" \
    "GMP_LIBRARIES = /usr/lib64/libgmp.so\n" \
    "GMPXX_LIBRARIES = /usr/lib64/libgmpxx.so\n" \
    "MPFR_LIBRARIES = /usr/lib64/libmpfr.so\n" \


__all__ = ['bottleneck', 'off_utils', 'simplex_tree', 'rips_complex', 'cubical_complex', 'periodic_cubical_complex', 'persistence_graphical_tools', 'reader_utils', 'witness_complex', 'strong_witness_complex', 'nerve_gic', 'subsampling', 'tangential_complex', 'alpha_complex', 'euclidean_witness_complex', 'euclidean_strong_witness_complex',  'hera', 'clustering', 'datasets', 'representations', 'sklearn', 'tensorflow', 'wasserstein', 'point_cloud', 'weighted_rips_complex', 'dtm_rips_complex', 'cover_complex', ]

__available_modules = ''
__missing_modules = ''

# Try to import * from gudhi.__module_name for default modules.
# Extra modules require an explicit import by the user (mostly because of
# unusual dependencies, but also to avoid cluttering namespace gudhi and
# speed up the basic import)
for __module_name in ['bottleneck', 'off_utils', 'simplex_tree', 'rips_complex', 'cubical_complex', 'periodic_cubical_complex', 'persistence_graphical_tools', 'reader_utils', 'witness_complex', 'strong_witness_complex', 'nerve_gic', 'subsampling', 'tangential_complex', 'alpha_complex', 'euclidean_witness_complex', 'euclidean_strong_witness_complex', ]:
    try:
        __module = import_module('gudhi.' + __module_name)
        try:
            __to_import = __module.__all__
        except AttributeError:
            __to_import = [name for name in __module.__dict__ if not name.startswith('_')]
        globals().update({name: __module.__dict__[name] for name in __to_import})
        __available_modules += __module_name + ";"
    except:
        __missing_modules += __module_name + ";"
