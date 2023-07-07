
label start:
    #show screen State_bar
    scene scene_event
    nvl clear
    "Совет: Чтобы ознакомится с кратким руководством по игре нажмите кнопку Журнал"
    python:
        initVariables()
        # logging ("start")
    # call screen fonts_tast_screen
    jump main_map

label main_map:
    if game_over:
        python:
            lst_to_file ( toLocalSorted, renpy.loader.transfn("resources/ru_localization.txt"))
            #renpy.quit(relaunch=True)
            renpy.full_restart()
    else:
        call screen general
