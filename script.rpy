
label start:
    #show screen State_bar
    python:
        initVariables()
        # logging ("start")
    # call screen fonts_tast_screen
    jump main_map

label main_map:
    if game_over:
        python:
            lst_to_file ( toLocal, renpy.loader.transfn("resources/ru_localization.txt"))
            #renpy.quit(relaunch=True)
            renpy.full_restart()
    else:
        call screen general
