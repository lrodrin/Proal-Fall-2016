def lowupp(info):
    if info[0] == "_":
        print(info.lower().lstrip(info[0]))
    elif info[0] == "^":
        print(info.upper().lstrip(info[0]))
    else:
        print(info)
