def lowupp(info):
    if len(info) > 0:
        if info.startswith("_"):
            return info.lower().lstrip(info[0])
        elif info.startswith("^"):
            return info.upper().lstrip(info[0])
        else:
            return info
