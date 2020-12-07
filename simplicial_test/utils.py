import numpy as np
from collections import defaultdict, Counter
from copy import deepcopy


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


class NoSlotError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NoSlotError {self.message}'
        else:
            return 'NoSlotError has been raised'


class WeCanStopSignal(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'WeCanStopSignal {self.message}'
        else:
            return 'WeCanStopSignal has been raised'


class NoMoreBalls(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'NoMoreBalls has been raised'


class SimplexRegistrar(object):
    def __init__(self):
        self.pointer = 0
        self.name2id = dict()
        self.id2name = dict()
        self.facet_size_per_id = np.array([], dtype=np.int_)
        self.logbook = dict()

    def register(self, name) -> (tuple, int):
        name = tuple(sorted(name, reverse=True))
        if name not in self.name2id:
            self.name2id[name] = self.pointer
            self.id2name[self.pointer] = name
            self.pointer += 1
            self.facet_size_per_id = np.append(self.facet_size_per_id, [len(name)])
        return name, self.name2id[name]

    def log_forbidden(self, name, reason_id) -> None:
        self.logbook[tuple(name)] = {
            "is_simplicial": False,
            "reason": reason_id
        }


def update_deg_seq(deg_seq, facet, value):
    if value not in [+1, -1]:
        raise NotImplementedError
    for _ in facet:
        deg_seq[_] += value


def shrink_facets(facets, inv_map):
    _facets = []
    for facet in facets:
        transformed_facet = []
        for _ in facet:
            try:
                transformed_facet += [inv_map[_]]
            except KeyError:
                pass
        if len(sorted(transformed_facet)) > 0:
            _facets += [sorted(transformed_facet)]
    _facets.sort(key=len)
    return _facets


def shrink_degs(degs, inv_map):
    d = dict()
    for idx, _degs in enumerate(degs):
        try:
            d[inv_map[idx]] = _degs
        except KeyError:
            pass
    d_list = list()
    for idx, _d in enumerate(d.values()):
        d_list += [d[idx]]
    return np.array(d_list, dtype=np.int_)


def get_shielding_facets_when_vids_filled(current_facets, must_be_filled_vids, exempt_vids=list()) -> (bool, set, list):
    """
    TODO: this function can be further simplified, along with the function::validate_reduced_seq
    The function works when one have "must_be_filled_vids" -- it goes by searching already existing facets,
    And find out the slots that must not be chosen in order to avoid clashes.

    Parameters
    ----------
    both
    curent_sizes
    current_facets

    Returns
    -------

    """
    # print("-> must_be_filled_vids are ", must_be_filled_vids)
    shielding_facets = list()
    for facet in current_facets:  # for all existing facets
        if set(must_be_filled_vids).issubset(set(facet)) and set(exempt_vids).issubset(
                set(facet)):  # if a facet contains these must_be_filled_vids
            shielding_facets += [facet]
    return shielding_facets  # then we must avoid the slots in these shielding_facets


def get_nonshielding_vids(shielding_facets, both):
    nonshielding_vids = set()
    n = len(both)
    # print("-> shielding_facets = ", shielding_facets)
    for facet in shielding_facets:
        non_shielding_part = set(range(n)).difference(set(facet))  # non_shielding_part vertex_id's
        if len(nonshielding_vids) == 0:
            nonshielding_vids = non_shielding_part
        else:
            nonshielding_vids.intersection_update(non_shielding_part)
        # remaining number of facets must be able to "hide" in those non_shielding slots, at least
        # if remaining > np.sum(both[np.array(list(nonshielding_vids), dtype=np.int_)]):
        #     print(f"While checking if the remaining number of facets being able to hide in the nonshielding slots, ")
        #     print(f"We found that remaining={remaining} but nonshielding_vids={nonshielding_vids} (i.e., available sites to hide = {np.sum(both[np.array(list(nonshielding_vids), dtype=np.int_)])})")
        #     print("Therefore, we reject that the nodes being filled this way.")
        #     raise NoSlotError("The custom error in get_nshielding.")
    return nonshielding_vids


def basic_validations_degs_and_sizes(degs, sizes):
    if Counter(degs)[len(sizes)] == np.min(sizes):
        return False
    if len(degs) == np.max(sizes):
        return False
    return True


def remove_ones(s, both, choose_from=set()):
    # orig_both = deepcopy(both)
    # _both = deepcopy(both)
    # both = [_ for _ in both]
    # for _ in range(Counter(s)[1]):
    #     both.remove(1)
    # both = np.array(both)
    # print(type(choose_from), f"np.where(both == 1)[0] = {np.where(both == 1)[0]}")
    if len(choose_from) == 0:
        raise NoSlotError
    all_one_sites = np.where(both == 1)[0]
    if choose_from is not None and type(choose_from) is set:
        choose_from.intersection_update(set(all_one_sites))
        if not choose_from:
            raise NoSlotError
    # print(f"choose_from is {choose_from}")
    removed_sites = np.array(list(choose_from))[:Counter(s)[1]]  # todo, to figure out: you cannot do [-Counter(s)[1]:]
    both[removed_sites] = 0
    return both, removed_sites.tolist()


def trim_ones(size_list, degree_list) -> (list, list):
    size_list = list(size_list)
    degree_list = list(degree_list)
    _1 = Counter(size_list)[1]
    _2 = Counter(degree_list)[1]
    if _1 > _2:
        print("Too many 0-simplices. We cannot satisfy the inclusive constraint.")
    else:
        for _ in range(_1):
            size_list.remove(1)
            degree_list.remove(1)
    return size_list, degree_list


def get_slimmest_d(s):
    """

    Parameters
    ----------
    s: size list

    Returns
    -------

    """
    s = sorted(s)
    pool = set()
    tentative_ = []
    for _s in s:
        tentative = tentative_
        if len(tentative) == 0:
            idx = 0
            for _ in range(_s):
                tentative += [idx]
                idx += 1
            pool.add(tuple(tentative))
            tentative_ = tentative
            continue
        tentative[-1] += 1
        idx = tentative[-1]
        for _ in range(_s - len(tentative)):
            idx += 1
            tentative += [idx]

        pool.add(tuple(tentative))
        tentative_ = tentative
    return sorted(Counter(flatten(pool)).values(), reverse=True)


def sort_helper(st) -> list:
    d = defaultdict()
    for idx, _ in enumerate(st.DEGREE_LIST):
        d[idx] = _

    inv_map = defaultdict(list)

    for _ in d:
        inv_map[d[_]] += [_]
    joint_seq = st.compute_joint_seq_from_identifier(sorted_deg=False)
    if len(joint_seq[0]) == 0:
        raise ValueError("Invalid input instance. Perhaps execute SimplicialTest.is_simplicial() first?")
    old2new = dict()
    for idx, _ in enumerate(st.compute_joint_seq_from_identifier(sorted_deg=False)[1]):
        old2new[idx] = inv_map[_].pop(0)

    translated = []
    for facet in st.identifier2facets():
        translated += [sorted([old2new[_] for _ in facet])]
    return translated


def get_enlarged_seq(mapping2enlarged, facets) -> list:
    # _, mapping = get_seq2seq_mapping(degs)
    reduced_facets = list(map(lambda x: tuple(map(lambda y: mapping2enlarged[y], x)), facets))
    # print(f"The facets above have been `enlarged` (i.e., higher-level) to: {reduced_facets}")
    return reduced_facets


def sort_callback(facets):
    t = []
    for facet in facets:
        t += [tuple(sorted(facet, reverse=False))]
    return tuple(t)


def get_seq2seq_mapping(degs):
    old2new = dict()
    for idx, _deg in enumerate(degs):
        old2new[idx] = _deg
    inv_old2new = defaultdict(list)
    for key in old2new.keys():
        if old2new[key] != 0:
            inv_old2new[old2new[key]] += [key]
    _idx = 0
    _inv_old2new = deepcopy(inv_old2new)

    keys = sorted(inv_old2new.keys(), reverse=True)
    for key in keys:
        for idx, _ in enumerate(inv_old2new[key]):
            inv_old2new[key][idx] = _idx
            _idx += 1

    mapping2enlarged = dict()
    for key in inv_old2new.keys():
        for idx, new_key in enumerate(inv_old2new[key]):
            mapping2enlarged[new_key] = _inv_old2new[key][idx]

    mapping2shrinked = {v: k for k, v in mapping2enlarged.items()}
    return mapping2shrinked, mapping2enlarged


def compute_joint_seq(facets) -> (list, list):
    # print(facets)
    flattened_facets = [item for sublist in facets for item in sublist]
    n = max(flattened_facets) - min(flattened_facets) + 1
    degs = np.zeros(n, dtype=np.int_)
    sizes = []

    for facet in facets:
        sizes += [len(facet)]
        for vertex_id in facet:
            degs[vertex_id] += 1

    return sorted(sizes, reverse=True), sorted(degs, reverse=True)


def if_facets_simplicial(facets) -> bool:
    for idx1, facet1 in enumerate(sorted(facets, key=len)):
        for idx2, facet2 in enumerate(sorted(facets, key=len)):
            if idx2 > idx1:
                if set(list(facet1)).issubset(set(list(facet2))):
                    return False
    return True


def filter_blocked_facets(blocked_facets, exempt_vids):
    # print(f"in filter_blocked_facets (blocked_facets, exempt_vids) = {(blocked_facets, exempt_vids)}")
    filtered = []
    for facet in blocked_facets:
        if set(exempt_vids).issubset(facet):
            filtered += [facet]
    return filtered


def compute_joint_seq_from_facets(facets):
    n = max(flatten(facets)) + 1
    degs = np.zeros(n, dtype=np.int_)
    sizes = np.zeros(len(facets), dtype=np.int_)

    for idx, facet in enumerate(facets):
        for vid in facet:
            degs[vid] += 1
        sizes[idx] = len(facet)

    return degs, sizes


def accel_asc(n):
    """from: http://jeromekelleher.net/generating-integer-partitions.html"""
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


# DEPRECATED, possible use methods included
def get_inv_level_map(level_map):
    inv_level_map = dict()
    for key in level_map.keys():
        inv_level_map[key] = {v: k for k, v in level_map[key].items()}

    # In SimplicialTest.__init__()
    # self.inv_level_map = get_inv_level_map(self.level_map)
    #
    # self.level_ns = level_ns
    # if self.level_ns is None:
    #     self.level_ns = dict()
    #     self.level_ns[self._level] = set()
    #
    # In SimplicialTest.sample_simplex_greedy()
    # if_continue = False
    # candidate_facet_set = set(list(candidate_facet))
    #
    #
    # leftover_levelwise = dict()
    # for level in range(1, self._level):
    #     leftover = dict()
    #     for _id in self.level_ns[level]:
    #         try:
    #             id_at_current_level = self.inv_level_map[level - 1][_id]
    #             leftover[id_at_current_level] = self._sorted_d[id_at_current_level]
    #         except KeyError:
    #             pass
    #     leftover_levelwise[level] = leftover
    #     if leftover != dict():
    #         leftover_values_list = list(leftover.values())
    #         if np.sum(leftover_values_list) < len(self._sorted_s):
    #             raise NoMoreBalls()
    #
    #
    #     if leftover == dict():
    #         continue
    #     leftover_keys_list = list(leftover.keys())
    #     leftover_values_list = list(leftover.values())
    #     leftover_used = len(set(leftover_keys_list).intersection(candidate_facet_set))
    #     if np.sum(leftover_values_list) - leftover_used < len(self._sorted_s):
    #         if_continue = True
    #         print(f"(l={self._level}) leftover is {leftover}; len(self._sorted_s)={len(self._sorted_s)}")
    #         break
    # if if_continue:
    #     print(f"(l={self._level}) {candidate_facet_set} is not good. \n")
    #     continue
    #
    # for key in self.level_ns.keys():
    #     if key >= self._level:
    #         self.level_ns[key] = set()
    #
    # In SimplicialTest.validate()
    # self.level_ns[self._level] = set(list(range(len(np.nonzero(self._sorted_d)[0])))).difference(
    #     set(list(candidate_facet)))

    return inv_level_map