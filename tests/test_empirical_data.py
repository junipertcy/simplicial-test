#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# simplicial-test -- a python module to realize simplicial joint sequences
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


from simplicial_test import *


def test_crime_dataset():
    degree_list = list(map(int, "1 1 1 2 1 1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 2 1 4 2 1 1 1 1 1 1 1 2 1 2 1 1 1 1 8 3 1 1 2 1 2 6 5 2 2 1 1 3 2 1 2 1 1 2 3 1 1 1 1 1 1 1 1 2 1 2 2 4 1 1 4 1 3 1 1 1 4 2 1 1 1 1 1 1 1 3 2 1 1 3 7 2 1 2 1 1 2 2 1 2 1 1 2 2 2 14 1 3 1 1 2 1 4 1 3 1 1 1 1 2 2 2 1 1 2 2 2 2 2 2 2 1 1 1 1 3 1 1 1 1 1 3 1 2 1 1 2 1 2 1 2 2 1 2 1 3 1 1 1 1 1 1 2 1 3 1 1 1 3 2 1 1 2 1 1 1 1 1 2 1 3 1 1 2 5 1 1 1 2 2 2 3 2 2 2 2 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 2 1 2 2 1 1 1 1 1 1 1 1 2 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 2 2 1 2 1 1 2 1 2 1 1 2 1 1 2 4 2 1 3 2 1 1 1 1 1 1 3 1 1 3 2 1 2 1 2 1 3 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 2 1 1 1 2 2 4 2 1 1 2 2 1 2 1 1 1 2 1 3 1 1 1 1 1 1 1 1 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 2 2 1 1 2 3 3 1 1 2 1 2 1 2 1 2 1 2 2 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 2 2 1 1 2 2 1 1 1 1 1 1 1 2 1 1 1 1 2 2 1 2 2 1 1 1 1 2 1 1 2 1 2 3 4 2 4 1 1 1 1 2 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 1 1 1 1 1 3 1 2 1 1 1 1 2 1 1 1 1 2 3 2 1 1 1 1 1 1 1 2 2 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 2 2 2 1 2 1 2 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split(" ")))
    size_list = list(map(int, "25 22 18 17 14 12 11 11 11 10 10 9 9 9 9 9 9 9 8 8 8 8 8 7 7 7 7 7 7 7 7 7 7 6 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1".split(" ")))
    st = Test(degree_list, size_list)
    is_simplicial, facets = st.is_simplicial()
    assert is_simplicial is True
    joint_seqs = compute_joint_seq(facets)
    assert if_facets_simplicial(facets) is True
    assert joint_seqs[0] == sorted(degree_list, reverse=True)
    assert joint_seqs[1] == sorted(size_list, reverse=True)


def test_pollinator_dataset():
    degree_list = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 1 1 1 1 1 5 1 2 1 2 5 2 2 1 1 2 1 1 5 1 1 1 2 1 2 1 1 1 1 1 1 2 1 1 1 3 1 2 1 3 1 2 3 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 5 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 4 3 1 1 1 5 5 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 2 1 1 1 3 3 2 1 2 1 1 3 3 1 1 2 3 1 2 1 1 1 1 4 6 21 7 1 5 1 2 1 1 3 8 1 1 1 1 2 1 3 1 2 1 2 2 1 1 2 9 1 1 1 2 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 2 1 1 1 10 1 1 1 1 2 3 2 1 1 1 4 2 3 1 3 1 3 7 1 1 3 2 1 2 1 1 1 1 1 2 1 1 1 4 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 3 1 1 2 1 1 2 1 1 1 1 1 1 2 1 1 1 3 1 2 3 2 6 1 1 1 1 3 3 2 1 1 1 1 1 1 1 2 4 2 1 1 2 1 1 1 1 6 4 2 1 4 1 1 1 2 2 5 1 1 1 1 1 5 2 1 2 1 1 11 1 2 2 2 5 2 1 1 1 1 2 2 1 2 1 2 1 2 2 2 1 1 2 5 1 2 1 3 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 2 1 4 3 1 1 3 1 1 1 1 1 1 1 1 2 1 2 1 2 1 1 1 1 1 1 2 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 4 3 4 1 1 2 1 1 1 7 1 1 2 1 2 1 1 1 2 2 8 1 2 8 1 5 6 2 1 2 2 2 2 1 11 16 1 4 3 8 3 9 1 2 2 5 2 2 2 2 2 1 2 2 1 6 1 3 4 1 2 6 1 1 1 2 1 3 1 2 2 1 1 1 8 23 2 3 1 2 14 1 25 8 25 11 5 1 1 1 1 1 1".split(" ")))
    size_list = list(map(int, "2 2 2 2 1 1 11 11 2 40 1 189 5 8 40 1 2 7 12 1 25 1 10 1 1 17 19 1 1 30 1 1 66 4 11 2 6 46 50 77 1 3 20 4 5 6 17 1 4 1 1 10 7 20 1 15 1 1 23 18 20 2 29 13 21 3 3 2 8 4 2 17 1 1 8 2 9 3 29 1 1 1 42 1 10 10 12 45 34 1 2".split(" ")))
    st = Test(degree_list, size_list)
    is_simplicial, facets = st.is_simplicial()
    assert is_simplicial is True
    joint_seqs = compute_joint_seq(facets)
    assert if_facets_simplicial(facets) is True
    assert joint_seqs[0] == sorted(degree_list, reverse=True)
    assert joint_seqs[1] == sorted(size_list, reverse=True)


def test_diseasome_dataset():
    degree_list = list(map(int, "1 1 1 1 1 4 3 1 7 1 1 1 1 1 1 1 1 5 3 1 8 11 1 4 1 3 2 1 1 1 3 1 1 1 3 1 4 1 1 1 1 1 4 1 1 2 1 1 1 1 1 1 1 6 12 1 1 1 2 5 1 1 1 1 15 3 3 2 5 10 6 1 1 1 1 1 1 7 1 6 2 1 1 1 1 2 1 1 1 1 1 2 8 1 2 1 1 1 1 1 5 2 1 1 1 2 1 1 1 1 2 1 6 1 1 2 1 1 1 1 1 2 4 1 1 1 1 1 1 1 1 1 3 1 2 1 3 2 1 4 3 1 1 3 1 2 2 2 1 1 1 2 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 7 1 5 1 1 3 7 1 1 1 1 1 1 1 1 1 1 2 4 1 1 1 1 1 3 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 3 1 1 1 3 3 1 1 3 1 1 3 1 1 1 5 1 1 1 3 1 1 1 7 4 1 3 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 3 1 1 3 4 1 1 2 1 1 1 2 1 1 1 1 1 1 1 1 1 1 2 1 3 2 1 1 1 2 1 1 1 1 2 1 1 2 3 1 2 1 1 1 1 1 1 1 1 1 1 7 1 3 1 1 2 1 1 1 3 1 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 4 1 1 1 1 1 1 1 2 3 1 1 1 1 1 1 1 1 1 1 2 2 1 3 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 2 3 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 3 1 4 1 1 2 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split(" ")))
    size_list = list(map(int, "10 8 8 7 7 7 7 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split(" ")))
    st = Test(degree_list, size_list)
    is_simplicial, facets = st.is_simplicial()
    assert is_simplicial is True
    joint_seqs = compute_joint_seq(facets)
    assert if_facets_simplicial(facets) is True
    assert joint_seqs[0] == sorted(degree_list, reverse=True)
    assert joint_seqs[1] == sorted(size_list, reverse=True)
