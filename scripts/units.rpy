init python:
    class unit:
        def __init__(self, unit_params):
            self.unit_type = unit_params["type"]
            self.name = unit_params ["name"]
            self.armor = unit_params ["armor"]
            self.block = unit_params ["block"]
            self.health= unit_params ["health"]
            self.max_health = self.health
            self.dmg_melee =  unit_params ["dmg_melee"]
            self.dmg_range = unit_params ["dmg_range"]
            self.resurrectable = unit_params ["resurrectable"]
            self.alive_chanse = 10
            self.alive  = False
            self.line = unit_params ["line"]
            self.priority_line = self.line
            self.dead = False
            self.maxRange=0
            self.skills=[]
            self.rarity = unit_params["rarity"]

            for sc in unit_params ["skills"]:
                self.skills.append(search_in_list_by_name(skill_list, sc))

        def __str__(self):
            return self.name

        def getMaxRange(self):
            for sk in self.skills:
                if sk["max range"]> self.maxRange:
                    self.maxRange=sk["max range"];
            return self.maxRange

        def cast(self, cur_range):
            if self.line== "back":
                cur_range+=1
            for s in self.skills:
                if (s["max range"]>=cur_range) and (s["min range"]<=cur_range):
                    return s
            return 0
        def toFrontline(self):
            self.line = "front"

        def toBackline(self):
            self.line = "back"

        def checkHealth(self):
            if self.dead == False:
                if self.health<=0:
                    self.dead = True
                    if self.resurrectable:
                        if dice_100()<= self.alive_chanse:
                            self.alive = True

        def isAlive(self):
            return self.alive

        def getDamage (self, dmg_value ):
            str=""
            if self.block>=dice_100():
                dmg_value=0
            dmg=dmg_value*(100/100+self.armor)
            self.health-= dmg
            self.health=int(round(self.health))
            #str+=  "%s get %d damage. "% (self.name, dmg)
            self.checkHealth()
                #str+=  "He is dead. "
            #str+= "Its current health %d"% (self.health)
            #logging(str)

        def isDead(self):
            return self.dead
    logging ("units")
