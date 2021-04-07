init -1 python:
    class Stats:
        possible_parameters=set ( ("max_health armor block dmg_melee dmg_range current_health").split() )
        opposite_effects = {"increment":"decrement","increase":"decrease",
                             "add":"sub","multiply":"divide","deal":"heal","set":"set"}
        replace_dict = {"range damage":"dmg_range", "melee damage":"dmg_melee",
                        "maximum health":"max_health","current health":"current_health", "%":"", "damage":"current_health" }
        displayble = ['block','dmg_melee', 'dmg_range']
        def __init__ (self, parameters):
            self.armor = Stat (parameters ["armor"], "Armor")
            self.block = Stat (parameters ["block"], "Block")
            self.max_health = Stat (parameters ["health"], "Health")
            self.dmg_melee = Stat (parameters ["dmg_melee"], "Melee damage")
            self.dmg_range = Stat (parameters ["dmg_range"], "Range damage")
            self.current_health = Current_health (self.max_health.val(), self )

        def setEffect(self, eff):
            self.effects.append (eff)

        def removeEffect(self, effect):
            if effect in self.effects:
                self.effects.remove (effect)

        def getDamage (self, value ):
            changeParameter("deal","damage",value)

        def _stringParser (self, const_string):
            st = copy.deepcopy(const_string)
            st = st.lower()
            for k in self.replace_dict.keys():
                st = st.replace(k, self.replace_dict[k])
            ls= st.split()
            # print (ls)
            return ls[0], ls[1], int (ls[2])

        def setParameterFromStr (self, const_string = "Add melee damage 0"):
            eff, aff, val = self._stringParser (const_string)
            self.changeParameter ( eff, aff, val)

        def resetParameterFromStr (self, const_string= "decrease maximum health 0%"):
            eff, aff, val = self._stringParser (const_string)
            eff = self.reverse_eff(eff)
            self.changeParameter ( eff, aff, val)

        def reverse_eff(self, effect):
            keys = list(self.opposite_effects.keys())
            vals = list(self.opposite_effects.values())
            if effect in keys:
                return (self.opposite_effects [effect])
            elif effect in vals:
                ind= vals.index(effect)
                return (keys[ind])
            else:
               raise ValueError ("Stats: cant reverse effect")

        def changeParameter (self, effect, affect, value):
            if affect in self.possible_parameters: ##and effect in local_effect.possible_effect:
                # print (affect,effect,value)
                to_call = getattr(vars (self)[affect], effect)
                to_call(value)
                if (affect)== "max_health" or (affect)== "armor":
                    self.current_health.max_health_changed(self.max_health.val())
            else:
                raise ValueError ("Stats: wrong affect %s"%affect)

        def __str__ (self):
            return ("armor: %s, max_health: %s, current_health: %s, dmg_melee: %s, dmg_range: : %s, block: %s"%(
            self.armor.val(), self.max_health.val(), self.current_health.val(), self.dmg_melee.val(), self.dmg_range.val(),  self.block.val()  ))

        def __repr__(self):
            members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
            st=""
            for m in members:
                if m!= "opposite_effects" and m !="possible_parameters" and m !="armored_health":
                    st+="%s: %s\n"%(m, getattr(self, m))
            return (st)

    def testStatsParser():
        stats = {"armor":100, "health":100, "dmg_melee":100,"dmg_range":100, "block":100}
        st = Stats (stats)
        test_str = ["Increase range damage 50%",
        "Deal damage 10",
        "Set current health 1",
        "Heal damage 20",
        "Add melee damage 10",
        "Increment maximum health 30",
        "Multiply range damage 100%",
        "Decrement armor 5",
        "Decrease armor 50%",
        "Decrease armor 30%",
        "increase armor 80%",
        "Increment armor 5",
        "Decrease block 80%"]
        for s in test_str:
            st.setParameterFromStr(s)
            # print (st)
            st.resetParameterFromStr(s)
            # print (st)
        st.setParameterFromStr ("Decrease block 80%")
        for i in range(10):
            st.setParameterFromStr ("Deal damage 10")
            # print (st)
