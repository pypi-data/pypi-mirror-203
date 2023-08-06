from dpath import util


def merge(dst: dict, src: dict):
    out = {}
    util.merge(out, dst)
    util.merge(out, src, flags=util.MERGE_REPLACE)
    return out
