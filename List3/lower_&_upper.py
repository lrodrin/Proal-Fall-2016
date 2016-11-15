def lowupp(info):
    if len(info) != 0:
        if info.startswith("^"):
            return info.upper()[1:]
        elif info.startswith("_"):
            return info.lower()[1:]
        else:
            return info
    else:
        return info
