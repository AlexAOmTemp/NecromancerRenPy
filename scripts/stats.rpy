init -1 python:
    class Stats:
        possible_parameters=set ( ("health max_health armored_health armor block dmg_melee dmg_range ").split() )
        opposite_effects = {"increase":"decrease","decrease":"increase","divide":"multiply","multiply":"divide"}

        def __init__ (self, parameters):
            self.armored_health = 0
            self.armor = parameters ["armor"]
            self.block = parameters ["block"]
            self.health = parameters ["health"]
            self.max_health = self.health
            self.dmg_melee =  parameters ["dmg_melee"]
            self.dmg_range = parameters ["dmg_range"]

        def setEffect(self, eff):
            self.effects.append (eff)

        def removeEffect(self, effect):
            if effect in self.effects:
                self.effects.remove (effect)

        def getDamage (self, value ):
            changeParameter("decrease","armored_health",value)

        def setParameterFromStr (self, string= "decrease health 10"):
            ls= string.split()
            val = int (ls[2])
            self.changeParameter ( ls[0], ls[1], val)

        def resetParameterFromStr (self, string= "decrease health 10"):
            ls= string.split()
            ls[0] = reverse_eff(ls[0])
            val = int (ls[2])
            self.changeParameter ( ls[0], ls[1], val)

        def reverse_eff(self, effect):
            if effect in self.opposite_effects.keys():
                return (self.opposite_effects [effect])

        def changeParameter (self, effect, affect, value):
            if affect=="armored_health":
                self.armored_health = self.health  * (1 + 0.01 * self.armor)
            if affect in self.possible_parameters: ##and effect in local_effect.possible_effect:
                if effect=="increase":
                    vars (self)[affect]+=value
                elif effect=="decrease":
                    vars (self)[affect]-=value
                elif effect=="divide":
                    vars (self)[affect]/=value
                elif effect=="multiply":
                    vars (self)[affect]*=value
                elif effect=="set":
                    vars (self)[affect]=value
            else:
                raise ValueError
            if affect=="armored_health":
                self.health = round ( self.armored_health / (1 + 0.01 * self.armor) )

        def __repr__(self):
            members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
            st=""
            for m in members:
                if m!= "opposite_effects" and m !="possible_parameters" and m !="armored_health":
                    st+="%s: %s\n"%(m, getattr(self, m))
            return (st)
