image EnemyBack  = im.FactorScale(im.Scale("icons/EnemyBack.png",120,120), scaling)
image EnemyFront  = im.FactorScale(im.Scale("icons/EnemyFront.png",120,120), scaling)
image PlayerFront  = im.FactorScale(im.Scale("icons/PlayerFront.png",120,120), scaling)
image PlayerBack  = im.FactorScale(im.Scale("icons/PlayerBack.png",120,120), scaling)

screen battle_screen ( battle):
    frame:
        text battle.player_army.name
        yalign 0.9
    frame:
        text battle.enemy_army.name
        yalign 0.1

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20+ 100 * battle.cur_range
        use army_screen (battle.enemy_army)
        use army_screen (battle.player_army, True)



screen army_screen (army, reverse = False):

    if reverse:
        vbox:
            spacing 10
            use line_screen ("PlayerFront", army.get_frontline_units())
            use line_screen ("PlayerBack", army.get_backline_units())
    else:
        vbox:
            spacing 10
            use line_screen ("EnemyBack", army.get_backline_units())
            use line_screen ("EnemyFront", army.get_frontline_units())


screen line_screen (army_line_image, army_line):
    hbox:
        spacing scaled(10)
        image army_line_image
        # text army_line_name
        for u in army_line:
            use unit_screen (u)

screen unit_screen (unit):
    frame:
        size_group "Unit"
        ysize scaled (87)
        vbox:
            text unit.name color "#000000"

            $cur_hp= max (int (round (unit.health) ), 0)
            $max_hp = int (round (unit.max_health))
            bar:
                xysize(100, 10)
                range max_hp
                value cur_hp
            null width 5

            text "[cur_hp] / [max_hp]" size scaled(16) color "#000000"
