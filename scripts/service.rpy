init -6 python:
    def dice_100():
        dice=random.randint(1,100)
        return dice

    def dice_20():
        dice = renpy.random.randint(1,20)
        return dice

    def lst_to_file (lst, filename):
        with codecs.open(filename, 'w', encoding='utf8') as json_file:
            json.dump(lst, json_file, ensure_ascii=False,indent=4)

    def lst_from_file (filename):
        with codecs.open(filename, encoding='utf-8') as fh:
            lst = json.load(fh)
            return (lst)

    def search_in_list_by_name (list, name):
            for p in list:
                if p["name"] == name:
                    return p

    def search(where, name):
            for p in where:
                if p.name == name:
                    return p
