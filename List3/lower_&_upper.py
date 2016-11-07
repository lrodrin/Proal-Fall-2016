def lowupp(info):
    if info[0] == "_":
        return info.lower().lstrip(info[0])
    elif info[0] == "^":
        return info.upper().lstrip(info[0])
    else:
        return info
