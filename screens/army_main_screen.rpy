default current_unit = ""
default show_addition_unit_stats = False
style army_text is default:
    xalign 0.5
    size 30
    font fonts_list[0]

style army_button_text is army_text
style army_button is default:
    background "textbutton_background"
style slot:
    background Frame ("square.png",0,0)
    maximum (scaled (250), scaled (93))
    minimum (scaled (250), scaled (93))
    xpadding scaled(5)


screen army_main_screen():
    tag main
    style_prefix "army"
    add "scene_event"
    # use army_screen(players_army)
    textbutton local("OK") action Jump("main_map"):
         xalign 0.9
         yalign 0.9
    hbox:
        xalign 0.5
        $title_text = [local("backline"), local("frontline")]
        $ls = [[],[]]
        $ls[0] = players_army.get_backline_units()
        $ls[1] = players_army.get_frontline_units()
        for k in range (2):
            vbox:
                spacing scaled (10)
                text title_text[k] xalign 0.5
                $i=0
                for u in ls[k]:
                    frame:
                        style "slot"
                        button:
                            use unit_screen(u)
                            action (SetVariable("current_unit",u))
                        $i+=1
                for i in range(len(ls[k]),10):
                    frame:
                        style "slot"


    vbox:
        text "Selected:" xalign 0.5
        frame:
            style "slot"
            xalign 0.5
            if current_unit:
                text local(current_unit.name)
        use unit_stats (current_unit)
        if current_unit:
            if current_unit != Player_hero:
                textbutton local("Dismiss") action (Function (players_army.remove_unit, current_unit), (SetVariable( "current_unit", None), (Function (players_army.regroup)) ) ) xalign 0.5
            textbutton local("Change Priority Line") action (Function (current_unit.changePriorityLine), (Function (players_army.regroup) ) ) xalign 0.5


style stats_button is default:
    background "textbutton_background"
style stats_button_text is default:

    xalign 0.5
    size 30
    font fonts_list[0]

style stats_text:
    xalign 0.0

init python:
    def stat_diff_to_string (diff_val):
        st = ""
        if diff_val>0:
            if isinstance (diff_val, int):
                st = '({color=#006400}%+d{/color})'%diff_val
            else:
                st = '({color=#006400}%+.1f{/color})'%diff_val
        elif diff_val<0:
            if  isinstance (diff_val, int):
                st = '({color=#f00}%+d{/color})'%diff_val
            else:
                st = '({color=#f00}%+.1f{/color})'%diff_val
        return st

screen unit_stats(unit, old_item= None, new_item = None):
    python:
        hp_diff = ""
        arm_diff = ""
        blk_diff = ""
        dmg_ml_diff = ""
        dmg_rng_diff = ""
        maxRange_diff = ""
        arm_pers_diff = ""

        if new_item and unit:
            new_it_copy = copy.deepcopy( new_item)
            currency.addItem( new_it_copy)
            if old_item:
                unit.equipment.unequip( old_item)
            un_copy = copy.deepcopy( unit)
            if old_item:
                unit.equipment.equip( old_item)
            un_copy.equipment.equip( new_it_copy)
            hp_diff = stat_diff_to_string ( un_copy.stats.max_health.val() -  unit.stats.max_health.val() )
            arm_diff = stat_diff_to_string ( un_copy.stats.armor.val() -  unit.stats.armor.val() )
            blk_diff = stat_diff_to_string ( un_copy.stats.block.val() - unit.stats.block.val() )
            dmg_ml_diff = stat_diff_to_string ( un_copy.stats.dmg_melee.val() - unit.stats.dmg_melee.val() )
            dmg_rng_diff = stat_diff_to_string ( un_copy.stats.dmg_range.val() - unit.stats.dmg_range.val() )
            maxRange_diff = stat_diff_to_string ( un_copy.maxRange - unit.maxRange )
            arm_pers_diff = (1-1/(1 + 0.01 * un_copy.stats.armor.val() ))*100 - (1-1/(1 + 0.01 *  unit.stats.armor.val()  ))*100
            arm_pers_diff = stat_diff_to_string (arm_pers_diff)


    style_prefix "stats"
    if unit:
        frame:
            vbox:
                xsize 300

                # for st in unit.displayble:
                #     text local("%s: %s"%(st, getattr(unit, st)) ) xalign 0.0
                $cur_hp= max (unit.stats.current_health.val(), 0)
                $max_hp = unit.stats.max_health.val()
                $armr = unit.stats.armor.val()
                $blk = unit.stats.block.val()
                $dmg_ml = unit.stats.dmg_melee.val()
                $dmg_rng = unit.stats.dmg_range.val()
                $arm_perc = round( (1-1/(1 + 0.01 * armr ))*100 , 1 )

                if not show_addition_unit_stats:
                    text local("Name: %s"%unit.name)
                    text local("Health: [cur_hp] / [max_hp] %s"% hp_diff)
                    if armr!=0 or arm_diff!="":
                        text local( ("Armor:[armr]%s([arm_perc]%s"%(arm_diff,arm_pers_diff) )+"%)")
                    if blk!=0 or blk_diff!="":
                        text local( ("Block chance: %s%s"%(blk,blk_diff)) + "%")
                    if dmg_ml!=0 or dmg_ml_diff!="":
                        text local("Melee damage: [dmg_ml]%s"%dmg_ml_diff)
                    if dmg_rng!=0 or dmg_rng_diff!="":
                        text local("Range damage: [dmg_rng]%s"%dmg_rng_diff)
                else:
                    text local("Name: %s"%unit.name)
                    text local("Type: %s"%unit.unit_type)
                    text local("Rarity: %s"%unit.rarity)
                    text local("Health: [cur_hp] / [max_hp] %s"% hp_diff)
                    text local( ("Armor:[armr]%s([arm_perc]%s"%(arm_diff,arm_pers_diff) )+"%)")
                    text local( ("Block chance: %s%s"%(blk,blk_diff)) + "%")
                    text local("Melee damage: [dmg_ml]%s"%dmg_ml_diff)
                    text local("Range damage: [dmg_rng]%s"%dmg_rng_diff)
                    text local("Maximum range: %s"%unit.maxRange)
                    text local("Priority line: %s"%unit.priority_line)
                    text local("Level: [unit.level] / [unit.level_cap]")
                    text local("Experience: [unit.experience] / [unit.required_exp]")
                    text local("Skills:")
                    for s in unit.skills:
                        text local(("%s"%s["name"]))
                $unit_txt_value=""
                if show_addition_unit_stats:
                    $unit_txt_value = local("Hide addition stats")
                else:
                    $unit_txt_value = local("Show addition stats")
                textbutton unit_txt_value action (SetVariable ("show_addition_unit_stats", not show_addition_unit_stats))
