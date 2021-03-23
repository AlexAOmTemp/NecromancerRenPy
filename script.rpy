
label start:
    #show screen State_bar
    python:
        initVariables()
        logging ("start")
    jump main_map

label main_map:
    if game_over:
        python:
            #renpy.quit(relaunch=True)
            renpy.full_restart()
    else:
        call screen general
