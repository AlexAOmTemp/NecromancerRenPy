# effect = {
#     "name": "decrease health",
#     "image": "",
#     "effect": "decrease armored_health",
#     "time_mode": "each_turn",
#     "effect_lasts": "permanent"
# }
init python:
    class Local_Effect:
        possible_affect = Stats.possible_parameters
        possible_time_mode = set (["each_turn", "at_start"])
        possible_effect = set ( ("increase decrease divide multiply set").split() )
        possible_effect_lasts = set (["permanent", "while_exist"])
        possible_duration = set (["permanent", "instant"]) #or integer

        def __init__ (self, parameters, value, duration, target):
            global list_of_current_local_effects
            self.name = parameters["name"]

            self.effect = "%s %d"%(parameters["effect"], value)
            # # logging(self.effect)

            self.duration = duration
            self.target = target
            self.time_mode = parameters["time_mode"]
            self.effect_lasts =  parameters["effect_lasts"]
            self.total_value = 0
            if self.duration == "instant":
                self.duration = 0
            elif self.duration == "permanent":
                self.duration = 999

            if not self.target:
                raise ValueError
            if self.duration>0:
                list_of_current_local_effects.append(self)
                self.target.setEffect(self)
            if self.duration <=0 or self.time_mode == "at_start":
                self.make_effect()

        def make_effect(self):
            # if self.effect == "set":
            #     self.total_value = vars (self.target)[affect]
            # else:
            #     self.total_value += value

            self.target.stats.setParameterFromStr(self.effect)

        def reverse_effect(self):
            self.target.stats.resetParameterFromStr(self.effect)

            # if (self.effect == "increase")
            #     self.effect = "decrease"
            # elif (self.effect == "decrease"):
            #     self.effect = "increase"
            # elif self.effect == "divide":
            #     self.effect = "multiply"
            # elif self.effect == "multiply":
            #     self.effect = "divide":
            # self.target.stats changeParameter(self.effect, self.affect, self.total_value)

        def decrease_duration (self ):
            if self.target.isDead:
                self.target = None
                self.end()
            else:
                if self.time_mode == "each_turn":
                    self.make_effect()
                self.duration -= 1
                if self.duration <= 0:
                    self.end()

        def end(self):
            if self.target:
                if possible_effect_lasts == "while_exist":
                    self.reverse_effect()
                self.target.stats.removeEffect(self)
            if self in list_of_current_local_effects:
                list_of_current_local_effects.remove(self)
            # print ("removed")


        def __str__(self):
            return ("%s" % (self.name))

        def __repr__ (self):
            return ("%s" % (self.name))
