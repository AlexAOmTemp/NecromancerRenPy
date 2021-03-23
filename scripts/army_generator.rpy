init python:
    army_test = {
    "name": "test_army",
    "units": ["test_unit1","test_unit2"],
    "units_with_teg": ["human", "undead"],
    "exclude_units": ["test_human1"]
    }

    def generate_army ( parameters):
        units = []
        new_army = army(parameters["name"])
        for f in units_list:
            if ( (f["type"] in parameters["units_with_teg"]
                or f["name"] in parameters["units"])
                and f["name"] not in parameters["exclude_units"] ):
                new_army.add_unit(unit(f))
        return new_army


    #generate_army(army_test)
