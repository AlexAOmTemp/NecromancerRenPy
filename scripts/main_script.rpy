
define e = Character("Eileen", kind=nvl)



init -1 python: #before classes initiate, read some files and global variables
    import json
    import random



    slots = ("weapon", "armor", "helmet", "range_weapon", "boots", "left ring", "right ring", "amulet")
    rarity = ("poor","normal","magic","rare","legendary")

    effects_list = lst_from_file (renpy.loader.transfn("resources/effects.txt") )
    skill_list = lst_from_file (renpy.loader.transfn("resources/skills.txt") )
    units_list= lst_from_file (renpy.loader.transfn("resources/units.txt") )
    item_list = lst_from_file (renpy.loader.transfn('resources/items.txt') )

    resources_endless_list = lst_from_file(renpy.loader.transfn('resources/res_endless.txt') )
    resources_countable_list = lst_from_file (renpy.loader.transfn('resources/res_countable.txt') )


    events_list = lst_from_file (renpy.loader.transfn('resources/events.txt') )
    cell_types_list = lst_from_file (renpy.loader.transfn('resources/types.txt') ) #cell types parameters for every cell type
    map_by_types = lst_from_file (renpy.loader.transfn('resources/map.txt') ) #where cells of each type are placed on the map
    #list of all one_cell class instances


    scaling = float(config.screen_width)/1920 # for different resolutions (base is 1920x1080)
    config.menu_include_disabled = True #показывает недоступные варианты в меню



init 1 python:

    logging ("globals 2")
    #set of items names
    def initVariables():
        global reward_generator
        global currency
        global players_army
        global current_cell_name
        global event_started
        global event_ended
        global game_over

        reward_generator=reward_gen()
        currency= currency_class()
        players_army = army("Glory Army")
        players_army.add_unit( unit (search_in_list_by_name (units_list, "Necromancer") ) )
        players_army.add_unit( unit (search_in_list_by_name (units_list, "Sceleton") ) )

        current_cell_name = ""
        event_started = False
        event_ended = False
        game_over = False




init python:
    def onCellClicked (cell_name):
        global current_cell_name
        if currency.activity>0:
            current_cell_name = cell_name
            currency.activity-=1
            renpy.jump("cell_menu")
        else:
            renpy.jump("sleep")

    logging ("on button click")

label cell_menu:
    nvl clear
    python:
        global event_started
        unfinished_started = False
        current_cell = search ( map_cells_ls, current_cell_name)
        menu_items=[]
        menu_items.append ( (("Вы находитесь на клетке %s" % current_cell), None ))
        menu_items.append (("Искать приключений", 0))
        menu_items.append( ("Уйти", 1))
        if len(current_cell.unfinished_events) != 0:
            menu_items.append (("Найденные ранее объекты", None))
            i=2
            for ev in current_cell.unfinished_events:
                menu_items.append ( (ev.name, i) )
                i+=1
        choise =  renpy.display_menu( menu_items )
        if (choise==0):
            event_started=True
            current_cell.start_event() #this call works as a break instruction for unknown reasons and transfer control to the end of the python block
        elif (choise==1):
            renpy.jump("main_map")
        else:
            e("choise %s" % str(choise) )
            unfinished_started = True
            current_cell.start_unfinished(choise-2)
    python:
        if event_started:
            event_started = False
            current_cell.finish_event()
        elif unfinished_started:
            unfinished_started = False
            current_cell.finish_unfinished()
    nvl clear
    jump main_map

label sleep:
    "Вам нужно отдохнуть."
    jump main_map


label army:
    "You're in the army now."
    jump main_map


label person:
    nvl clear
    python:
        # menu:
        #     "Управление персонажем:"
        #     "Вещи": jump items

        st=currency.get_player_items_names()
        if len(st) == 0:
            e("У Вас пока нет вещей")
        else:
            e("Список вещей:\n%s"% st)
    jump main_map

label castle:
    "It is your castle."
    jump main_map

label journal:
    nvl clear
    $e(how_many())
    jump main_map

label next_day:
    $currency.activity=3
    $currency.day+=1
    jump main_map

label items:
    python:
        menu_items=[]
        for it in currency.items:
            menu_items
    #    if len(current_cell.unfinished_events) != 0:
    jump journal



label game_over:
    $game_over = True
    "e""The game is over, You lost."
    jump main_map
