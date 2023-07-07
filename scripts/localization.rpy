$default
init -1 python:
    import re
    from collections import OrderedDict

    # game_lang = "english"
    game_lang = "russian"
    toLocal = {}
    pattern = re.compile(r'[0-9]|\[.*\]|\{[^\}]*\}|[A-Z]\s')
    toLocal = lst_from_file (renpy.loader.transfn("resources/ru_localization.txt") )

    # d={}
    # for i in (toLocal.keys()):
    #     new_key= (re.sub(pattern, "", i)).rstrip()
    #     d[new_key] = toLocal[i]
    # toLocalSorted = OrderedDict(sorted(d.items(), key=get_keylength, reverse=True))
    # lst_to_file ( toLocalSorted, renpy.loader.transfn("resources/ru_localization.txt"))
    def get_primaryKey(v):
        key, values = v
        return len(key.split())

    def get_secondaryKey(v):
        key, values = v
        return len(key)

    toLocalSorted = OrderedDict(sorted(toLocal.items(), key=get_secondaryKey, reverse=True)) #more characters first
    toLocalSorted = OrderedDict(sorted(toLocalSorted.items(), key=get_primaryKey, reverse=True))  #more words first


    def local(str):
        global toLocalSorted
        if game_lang == "english":
            st = (re.sub(pattern, "", str)).rstrip()
            st = (re.sub(pattern, "", st)).rstrip()
            if not st in toLocalSorted.keys():
                toLocalSorted[st]=""
                toLocalSorted = OrderedDict(sorted(toLocalSorted.items(), key=get_primaryKey, reverse=True))
            return str
        elif game_lang == "russian":
            for loc in toLocalSorted:
                if toLocalSorted[loc]:
                    str=str.replace (loc, toLocalSorted[loc])
            return str
