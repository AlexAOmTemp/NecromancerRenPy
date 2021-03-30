style slot:
    background Frame ("square.png",0,0)
    minimum (100,87)

screen army_main_screen():
    tag main

    add "main_background"
    # use army_screen(players_army)
    # textbutton "OK" action Jump("main_map"):
    #     xalign 0.9
    #     yalign 0.9
    # hbox:
    #     vbox:
    #         spacing 10
    #         for u in players_army.get_backline_units():
    #             frame:
    #                 style "slot"
    #                 button action (SetVariable(current_unit,u)):
    #                     child unit_screen (u)
