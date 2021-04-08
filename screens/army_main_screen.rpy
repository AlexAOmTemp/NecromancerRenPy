default current_unit = ""
style army_text is default:
    xalign 0.5
    size 30
    font fonts_list[0]

style army_button_text is army_text

style slot:
    background Frame ("square.png",0,0)
    maximum (scaled (250), scaled (93))
    minimum (scaled (250), scaled (93))
    xpadding scaled(5)


screen army_main_screen():
    tag main
    style_prefix "army"
    add "scene_blue"
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
        #     vbox:
        #         spacing scaled (10)
        #         text "backline" xalign 0.5
        #         $i=0
        #         for u in players_army.get_backline_units():
        #             frame:
        #                 style "slot"
        #                 button:
        #                     use unit_screen(u)
        #                     action (SetVariable("current_unit",u))
        #                 $i+=1
        #         for i in range(len(players_army.get_backline_units()),10):
        #             frame:
        #                 style "slot"
        # vbox:
        #     spacing scaled (10)
        #     text "frontline" xalign 0.5
        #     for u in players_army.get_frontline_units():
        #         frame:
        #             style "slot"
        #             button:
        #                 action  (SetVariable( "current_unit", u))
        #                 use unit_screen(u)
        #     for i in range(len(players_army.get_frontline_units()),10):
        #         frame:
        #             style "slot"

    vbox:
        text "Selected:" xalign 0.5
        frame:
            style "slot"
            if current_unit:
                text local(current_unit.name)
        use unit_stats (current_unit)
        if current_unit:
            if current_unit != Player_hero:
                textbutton local("Dismiss") action (Function (players_army.remove_unit, current_unit), (SetVariable( "current_unit", None) ) )
            textbutton local("Change Priority Line") action (Function (current_unit.changePriorityLine), (Function (players_army.regroup) ) )


style stats_text:
    xalign 0.0
screen unit_stats(unit):

    style_prefix "stats"
    if unit:
        frame:
            vbox:
                xsize 300

                for st in unit.displayble:
                    text local("%s: %s"%(st, getattr(unit, st)) ) xalign 0.0
                $cur_hp= max (int (round (unit.stats.current_health.val() ) ), 0)
                $max_hp = int (round (unit.stats.max_health.val() ))
                $armr = unit.stats.armor.val()
                $blk = unit.stats.block.val()
                $dmg_ml = unit.stats.dmg_melee.val()
                $dmg_rng = unit.stats.dmg_range.val()
                $arm_perc = round( (1-1/(1 + 0.01 * armr ))*100 , 1 )
                text local("Health: [cur_hp] / [max_hp]")
                text local("Armor: [armr] ([arm_perc]%)")
                text local("Block: [blk]")
                text local("Melee damage: [dmg_ml]")
                text local("Range damage: [dmg_rng]")

                text local("Priority line: [unit.priority_line]")
                text local("Level: [unit.level] / [unit.level_cap]")
                text local("Experience: [unit.experience] / [unit.required_exp]")
                text local("Skills:")
                for s in unit.skills:
                    text local(("%s"%s["name"]))
