
screen battle_screen ( battle):
    frame:
        text battle.player_army.name
        xalign 0.1
    frame:
        text battle.enemy_army.name
        xalign 0.9

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
            use line_screen ("front", army.get_frontline_units())
            use line_screen ("back", army.get_backline_units())
    else:
        hbox:
            spacing 10
            use line_screen ("back", army.get_backline_units())
            use line_screen ("front", army.get_frontline_units())


screen line_screen (army_line_name, army_line):
    vbox:
        spacing 10
        text army_line_name
        for u in army_line:
            use unit_screen (u)

screen unit_screen (unit):
    vbox:
        text unit.name
        bar:
            xysize(100, 10)
            range unit.max_health
            value unit.health
        null width 5
        $cur_hp= max (unit.health,0)
        text "[cur_hp] / [unit.max_health]" size 16
