init python:

    def init_items_list():
        return (set ([x['name'] for x in item_list]) )

    logging ("items")
    items_by_names = init_items_list()
    # for id, val in enumerate(items_by_names):
    #     logging ("%d %s"%(id, val))

    class Item:
        def __init__(self, params):
            self.name = params["name"]
            self.slot = params["slot"]
            self.rarity = params["rarity"]

            self.stats = params["stats"]
            self.cost = 10
            self.addSkills = params["addSkills"]

            self.isEquipped = False
            self.equippedTo = None
            self.roll_stats()

        def roll_stats(self):
            for i in range (len(self.stats)):
                ls= self.stats[i].split()
                val = json.loads(ls[2])
                if isinstance(val, list):
                    val = random.randint(val[0],val[1])
                self.stats[i] = ("%s %s %d"% (ls[0],ls[1],val) )

        def equip (self, target):
            self.isEquipped = True
            self.equippedTo = target

        def unequip (self):
            self.isEquipped = False
            self.equippedTo = None

        def sell (self):
            currensy.money += self.cost

        def __repr__(self):
            return self.name
