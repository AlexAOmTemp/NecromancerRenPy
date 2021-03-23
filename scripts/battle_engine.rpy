
init python:

    def cast(our_unit, enemy_army, skill):
        str = "%s is using a skill %s on: " % (our_unit.name, skill["name"] )
        if skill["target"]== "enemy":
            valid_targ = enemy_army.get_frontline_units()
            quant = min (skill["targets quant"],len(valid_targ))
            targets = random.sample (valid_targ, quant)
            for t in targets:
                str += "%s " % (t.name)
            value = skill["value"]
            dep_s = skill["depends self"] #if skill damage bases on our unit stat
            for d in dep_s:
                value+= vars (our_unit)[d] * dep_s[d]
            str += "with power %d" %  (value)
            logging(str)
            dep_e= skill["depends enemy"] #if skill damage bases on enemy unit stat
            add_dmg=[]
            for t in targets:
                ad=0
                for d in dep_e:
                    ad+=vars (t)[d] * dep_e[d]
                add_dmg.append(ad)

            ef=search_in_list_by_name(effects_list, skill["effect"])
            aff= ef["affect"]
            eff= ef["effect"]
            for t in targets:
                i=0;
                if eff=="+":
                    vars (t)[aff]+=value+add_dmg[i]
                elif eff=="-":
                    if aff=="health":
                       t.getDamage (value+add_dmg[i])
                    else:
                       vars (t)[aff]-=value+add_dmg[i]
                elif eff=="*":
                    vars (t)[aff]*=value+add_dmg[i]
                elif eff=="/":
                    vars (t)[aff]/=value+add_dmg[i]
                i+=1

    def battle (our_army, enemy_army):
        win = 0
        round = 1
        cur_range=max (our_army.army_range, enemy_army.army_range)

        while (True):
            logging ("round %d"% round)
            round+=1
            our_army.bring_out_your_dead()
            our_army.regroup()
            enemy_army.bring_out_your_dead()
            enemy_army.regroup()
            logging ("our army frontline %d, our army backline %d" % (our_army.frontline, our_army.backline) )
            logging ("enemy army frontline %d, enemy army backline %d" % (enemy_army.frontline, enemy_army.backline) )
            if len(our_army.units)<=0 and len(enemy_army.units)<=0:
                st="all units are dead\n"
                win=2
                break
            if len(our_army.units)<=0:
                st="we have lost the battle\n"
                win=0
                break
            if len(enemy_army.units)<=0:
                st="we have won the battle\n"
                win=1
                break
            nvl_clear()
            ln=len(our_army.units)
            str="our army %d units\n" % (ln)
            str+="enemy army %d units\n" % (len(enemy_army.units))
            str+="current range %d" % (cur_range)
            logging(str)
            for u in our_army.units:
                logging ("our unit attacks:")
                if u.maxRange>=cur_range:
                    sk=u.cast(cur_range)
                    if sk!=0:
                        cast(u, enemy_army, sk)
            logging ("\n")
            for u in enemy_army.units:
                logging ("enemy unit attacks:")
                if u.maxRange >= cur_range:
                    sk=u.cast(cur_range)
                    if sk!=0:
                        cast(u, our_army, sk)
            if cur_range>0:
                cur_range-=1;
        st+="The battle is over"
        logging(st)
        e(st)
        return win

        logging ("battle")





#
# label start:
#     "start"
#     $my_army = army("Glory Army")
#     $my_army.add_unit( unit (search(units_list, "Necromancer") ) )
#     $my_army.add_unit( unit (search(units_list, "Sceleton") ) )
#
#     $enemy_army = army("Bad guys")
#     $enemy_army.add_unit(unit (search(units_list, "Evil Peasant") ) )
#     $enemy_army.add_unit(unit (search(units_list, "Peasant's son") ) )
#
#
#     $battle (my_army, enemy_army)
#     "end"
#     scene bg room
#     "its a day"
#
#     return
