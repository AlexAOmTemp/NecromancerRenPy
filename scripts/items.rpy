init python:

    def init_items_by_names_list( lst):
        return (set ([x['name'] for x in lst]) )

    # logging ("items")

    # for id, val in enumerate(items_by_names):
    #     # logging ("%d %s"%(id, val))

# "slot": "melee weapon",
# "name": "редкий меч",
# "rarity": "rare",
# "main stats": ["increase dmg_melee [12,14]]",
# "stats:":  ["increase max_health", "increase armor", "increase block"],
# "main skills": ["melee attack"],
# "skills": []

    class Item:
        def __init__(self, const_params):
            params = copy.deepcopy(const_params)
            self.name = params["name"]
            self.slot = params["slot"]
            self.rarity = params["rarity"]
            power= rarity.index(self.rarity)
            self.cost = 50*(2**power)
            self.stats = params["main stats"]
            self.isEquipped = False
            self.equippedTo = None
            self.can_sell = True

            additional_stats_quantity = random.randint ( 0, min (power, len(params["stats"])) ) #if additional stats exists limit by rarity
            if additional_stats_quantity>0:
                self.name += " of"
                self.cost+= 80*(1.5**additional_stats_quantity)
                additional_stats_choose = random.sample ( range(len(params["stats"])),additional_stats_quantity)
                for i in additional_stats_choose:
                    self.stats.append ( params["stats"][i])
                    name= params["stats"][i].split()
                    self.name += " %s"% name[1]

            self.skills = params["main skills"]
            pw = max (0, (power - 1) ) #additional skills (1 for magic, 2 for rare, 3 for legenfary)

            additional_skills_quantity = random.randint (0, min (pw, len( params["skills"]))   )#if skills exists and enought rarity
            if additional_skills_quantity> 0:
                self.cost+=200*(2**additional_skills_quantity)
                self.name.prepend ("skilled ")
                additional_skills_choose = random.sample ( range(len(params["skills"])), additional_skills_quantity)
                for i in additional_skills_choose:
                    self.skills.append ( params["skills"][i])

            self.name=self.name.replace("maximum","health")
            self.sellCost = int(round(self.cost/10))
            self.roll_stats()
            self.name="%s%s{/color}"%(rarity_color[self.rarity],self.name)

        def roll_stats(self):
            for i in range (len(self.stats)):
                ls= self.stats[i].split()
                for word in ls:
                    if "[" in word:
                        ind = ls.index(word)
                        val = json.loads(word)
                        val = random.randint(val[0],val[1])
                        ls[ind] = ("%d"% (val) )
                        self.stats[i]= " ".join(ls)
                # else:
                #     raise ValueError('item %s has wrong stat: %s'%(self.name, self.stats[i]) )

        def equip (self, target):
            self.isEquipped = True
            self.equippedTo = target

        def unequip (self):
            self.isEquipped = False
            self.equippedTo = None

        def sell (self):
            if self.isEquipped:
                target.equipment.unequip(self)
            currency.money += self.sellCost
            currency.items.remove(self)

        def canBeSold():
            return can_sell

        def __repr__(self):
            return self.name


    def generate_standart_items_templates():
        # Equipment.possibleSlots = ("melee weapon", "armor", "helmet", "range weapon", "boots", "left ring", "right ring", "amulet")
        possibleSlots = ("melee weapon", "armor", "helmet", "shield","range weapon", "boots", "left ring", "right ring", "amulet")
        power_with_rarity_mult = 1.5
        rarity = ["poor","normal","magic","rare","legendary"]
        for slot in possibleSlots:
            for gen in generate_items_list:
                if gen["slot"] == slot:
                    for r in rarity:
                        power = rarity.index(r)
                        powerMult = power_with_rarity_mult**power
                        itm = {}
                        itm["slot"] = slot
                        itm["rarity"] = r
                        # itm["name"] = "%s %s"% (r, gen["name"])
                        itm["name"] = "%s"% (gen["name"])
                        itm["stats"]=[]
                        value = [int (round( gen["main values"][0]*powerMult)),int (round(gen["main values"][1]*powerMult))]
                        str_val= ("%s"%value).replace(" ", "")
                        itm["main stats"] = ["%s %s"%(gen["main stats"], str_val)]
                        for i in range (len(gen["stats"])):
                            val=  [int (round(gen["values"][i][0]*powerMult)),int (round(gen["values"][i][1]*powerMult))]
                            st_vl=("%s"%val).replace(" ", "")
                            itm["stats"].append("%s %s"%(gen["stats"][i], st_vl) )
                        itm["main skills"] =  gen["main skills"]
                        itm["skills"] = gen["skills"]
                        item_templates_list.append (itm)

    def test_item():
        # global currency
        for i in item_templates_list:
            currency.addItemByTemplate(i)
