def lowupp(info):
    res = []
    if len(info) != 0:
        if info.startswith("^"):
            for i in range(1, len(info)):
                res.append(info[i].upper())
            return ''.join(res)
        elif info.startswith("_"):
            for i in range(1, len(info)):
                res.append(info[i].lower())
            return ''.join(res)
        else:
            res = info
            return ''.join(res)
