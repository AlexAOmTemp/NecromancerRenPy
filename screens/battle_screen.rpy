image EnemyBack  = im.FactorScale(im.Scale("icons/EnemyBack.png",120,120), scaling)
image EnemyFront  = im.FactorScale(im.Scale("icons/EnemyFront.png",120,120), scaling)
image PlayerFront  = im.FactorScale(im.Scale("icons/PlayerFront.png",120,120), scaling)
image PlayerBack  = im.FactorScale(im.Scale("icons/PlayerBack.png",120,120), scaling)
image health_img  = im.FactorScale(im.Scale("icons/Health.png",20,20), scaling)
image melee_img = im.FactorScale(im.Scale("icons/Melee.png",20,20), scaling)
image range_img = im.FactorScale(im.Scale("icons/Range.png",20,20), scaling)

screen battle_screen ( battle):
    frame:
        text local(battle.enemy_army.name)
        xalign 0.9
    frame:
        text local(battle.player_army.name)
        xalign 0.1

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20+ 100 * battle.cur_range
        use army_screen (battle.player_army)
        use army_screen (battle.enemy_army, True)




screen army_screen (army, reverse = False):

    if reverse:
        hbox:
            spacing 10
            use line_screen ("EnemyFront", army.get_frontline_units())
            use line_screen ("EnemyBack", army.get_backline_units())

    else:
        hbox:
            spacing 10
            use line_screen ("PlayerBack", army.get_backline_units())
            use line_screen ("PlayerFront", army.get_frontline_units())



screen line_screen (army_line_image, army_line):
    vbox:
        spacing scaled(10)
        image army_line_image
        # text army_line_name
        for u in army_line:
            use unit_screen (u)

screen unit_screen (unit):
    frame:
        xpos 5
        ypos 5
        # size_group "Unit"
        maximum (scaled (235), scaled (83))
        minimum (scaled (235), scaled (83))
        # xpadding scaled(10)
        # ysize scaled (87)
        vbox:
            xalign 0.5
            text local(unit.name) color "#000000" xalign 0.5 size scaled(35)

            $cur_hp= max (int (round (unit.stats.current_health.val()) ), 0)
            $max_hp = int (round (unit.stats.max_health.val() ))
            $dmg_ml = unit.stats.dmg_melee.val()
            $dmg_rng = unit.stats.dmg_range.val()
            bar:
                xalign 0.5
                xysize ( scaled (215), scaled(10) )
                range max_hp
                value cur_hp
                left_bar "#f00"
                right_bar "#808080"
                # right_bar "#ffffffaa"
            null width 5
            hbox:
                xalign 0.5
                spacing 10
                hbox:
                    add "health_img"
                    text "[cur_hp] / [max_hp]" size scaled(20) color "#000000"
                if dmg_ml>0:
                    hbox:
                        add "melee_img"
                        text "[dmg_ml]" size scaled(20) color "#000000"
                if dmg_rng>0:
                    hbox:
                        add "range_img"
                        text "[dmg_rng]" size scaled(20) color "#000000"
