#!/usr/bin/env python3


from typing import Any, List, Optional


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
