$default
init -1 python:
    import re
    game_lang = "english"
    # game_lang = "russian"

    pattern = re.compile(r'[0-9]|\[.*\]')
    toLocal = lst_from_file (renpy.loader.transfn("resources/ru_localization.txt") )

    def local(str):
        if game_lang == "english":
            st = (re.sub(pattern, "", str)).rstrip()
            if not st in toLocal.keys():
                toLocal[st]=""
            return str
        elif game_lang == "russian":
            for loc in toLocal:
                if toLocal[loc]:
                    str=str.replace (loc, toLocal[loc])
            return str
