#!/usr/bin/env python3


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
