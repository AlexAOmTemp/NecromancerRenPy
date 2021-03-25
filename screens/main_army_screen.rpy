screen main_army_screen():
    tag main
    use army_screen(players_army)
    textbutton "OK" action Jump("main_map"):
        xalign 0.9
        yalign 0.9
