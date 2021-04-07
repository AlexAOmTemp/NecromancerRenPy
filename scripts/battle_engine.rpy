
init python:

    class Battle:
        def __init__ (self, player_army, enemy_army ):
            self.player_army=player_army
            self.enemy_army = enemy_army
            self.round = 1
            self.win = False
            self.over = False
            self.cur_range = max (self.player_army.army_range, self.enemy_army.army_range)

        def isOver(self):
            return self.over

        def isPlayerWon(self):
            return self.win

        def next_round (self):
            global Player_hero
            # # logging ("round %d"% self.round)
            if self.isOver == True:
                return
            self.round+=1
            self.player_army.bring_out_your_dead()
            self.player_army.regroup()
            self.enemy_army.bring_out_your_dead()
            self.enemy_army.regroup()
            # # logging ("our army frontline %d, our army backline %d" % (self.player_army.frontline, self.player_army.backline) )
            # # logging ("enemy army frontline %d, enemy army backline %d" % (self.enemy_army.frontline, self.enemy_army.backline) )
            if len(self.player_army.units)<=0 or Player_hero.isDead():
                # # logging ("we have lost the battle\n")
                self.over = True
                self.win = False
                return
            if len(self.enemy_army.units)<=0:
                # # logging ("we have won the battle\n")
                self.over = True
                self.win = True
                return
            nvl_clear()

            # ln=len(self.player_army.units)
            # str="our army %d units\n" % (ln)
            # str+="enemy army %d units\n" % (len(self.enemy_army.units))
            # str+="current range %d" % (self.cur_range)
            # # logging(str)

            for u in self.player_army.units:

                # # logging ("our unit attacks:")

                if u.maxRange>=self.cur_range:
                    sk=u.cast(self.cur_range)
                    if sk!=0:
                        self.cast(u, self.enemy_army, sk)

            # # logging ("\n")
            for u in self.enemy_army.units:

                # # logging ("enemy unit attacks:")
                if u.maxRange >= self.cur_range:
                    sk=u.cast(self.cur_range)
                    if sk!=0:
                        self.cast(u, self.player_army, sk)
            if self.cur_range>0:
                self.cur_range-=1;



        def cast(self, caster, enemy_army, skill):
            str = "%s is using a skill %s on: " % (caster.name, skill["name"] )

            if skill["target"] == "enemy":
                valid_targ = enemy_army.get_frontline_units()
                quant = min (skill["targets quant"],len(valid_targ))
                targets = random.sample (valid_targ, quant)

                for t in targets:
                    str += "%s " % (t.name)

                value = skill["value"]
                depends_self = skill["depends self"] #if skill damage bases on caster unit stat
                for d in depends_self:
                    # # logging (d)
                    value+= vars (caster.stats)[d].val() * depends_self[d]

                str += "with power %d" %  (value)

                # # logging(str)

                depends_enemy = skill["depends enemy"] #if skill damage bases on enemy unit stat
                add_dmg=[] #targets can have different stats
                for targ in targets:
                    ad=0
                    for d in depends_enemy:
                        # # logging (d)
                        ad+=vars (targ.stats)[d].val() * depends_enemy[d]
                    add_dmg.append(ad)


                ef=search_in_list_by_name(effects_list, skill["effect"])

                # # logging (ef)

                for t in targets:
                    i=0;
                    Local_Effect( ef, value+add_dmg[i], skill["effect duration"], t)
                    i+=1

                # aff= ef["affect"]
                # eff= ef["effect"]
                # for t in targets:
                #     i=0;
                #     if eff=="+":
                #         vars (t)[aff]+=value+add_dmg[i]
                #     elif eff=="-":
                #         if aff=="health":
                #            t.getDamage (value+add_dmg[i])
                #         else:
                #            vars (t)[aff]-=value+add_dmg[i]
                #     elif eff=="*":
                #         vars (t)[aff]*=value+add_dmg[i]
                #     elif eff=="/":
                #         vars (t)[aff]/=value+add_dmg[i]
                #     i+=1


#
# label start:
#     "start"
#     $my_army = Army("Glory Army")
#     $my_army.add_unit( unit (search(units_list, "Necromancer") ) )
#     $my_army.add_unit( unit (search(units_list, "Sceleton") ) )
#
#     $enemy_army = Army("Bad guys")
#     $enemy_army.add_unit(unit (search(units_list, "Evil Peasant") ) )
#     $enemy_army.add_unit(unit (search(units_list, "Peasant's son") ) )
#
#К
#     $battle (my_army, enemy_army)
#     "end"
#     scene bg room
#     "its a day"
#
#     return
