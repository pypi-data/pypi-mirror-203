# -*- coding: utf-8 -*-


def set_meaning_kv(d: dict, key: str, v):
    if v not in [None, '']:
        d[key] = v
