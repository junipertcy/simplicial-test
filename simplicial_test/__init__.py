#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# simplicial_test -- a python module to verify simplicial sequences
#
# Copyright (C) 2020-2021 Tzu-Chi Yen <tzuchi.yen@colorado.edu>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""``simplicial_test`` - Algorithm to check whether a joint sequence of degree/size distributions is simplicial
---------------------------------------------------------------------------------------------------------------

This module contains a greedy algorithm for checking simpliciality.

.. note::

   TODO.

"""
from .Test import *
from .utils import *
from .enumeration import *
from .sample import *
from .cm_count import *
from .draw import *

__package__ = 'simplicial_test'
__title__ = 'simplicial_test: a recursive, deterministic algorithm to check whether a joint sequence of ' \
            'degree/size distributions is simplicial'
__description__ = ''
__copyright__ = 'Copyright (C) 2020-2021 Tzu-Chi Yen'
__license__ = "The GNU Lesser General Public License, version 3.0 (LGPL-3.0)"
__author__ = """\n""".join([
    'Tzu-Chi Yen <tzuchi.yen@colorado.edu>',
])
__URL__ = "https://docs.netscied.tw/simplicialTest/index.html"
__version__ = '0.92.0'
__release__ = '0.92.0'

#  mark the class as not to be collected as pytest tests
Test.__test__ = False

__all__ = [
    "Test",
    "EnumRegistrar",
    "Enum",
    "get_hitting_sets",
    "compute_joint_seq",
    "flatten",
    "compute_dpv",
    "get_partition",
    "sort_facets",
    "get_relabeled_facets",
    "compute_entropy",
    "groupby_vtx_symm_class",
    "if_facets_simplicial",
    "gen_joint_sequence_from_sizes",
    "accel_asc",
    "NoMoreBalls",
    "draw_landscape",
    "draw_block",
    "__author__",
    "__URL__",
    "__version__",
    "__copyright__"
]
