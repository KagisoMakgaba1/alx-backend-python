#!/usr/bin/env python3
'''Add type notations to the function
'''


from typing import TypeVar, Dict, Any, Optional


K = TypeVar('K')  # Type variable for dictionary keys
V = TypeVar('V')  # Type variable for dictionary values

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
