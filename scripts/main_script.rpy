
define e = Character("Eileen", kind=nvl)
define narrator = Character (None, what_slow_cps=0)
# permanent = {
# "name": "Sceleton archer",
# "stat": ""
# }

default _game_menu_screen = 'load_screen'

# label game_menu:
#     call screen load
#     return

init -3 python: #before classes initiate, read some files and global variables
    import json
    import random
    import copy
    rarity = ["poor","normal","magic","rare","legendary"]
    rarity_color = {"poor":"{color=#2F4F4F}","normal":"{color=#ffffff}","magic":"{color=#000080}","rare":"{color=#ffff00}","legendary":"{color=#ffa500}"}

    effects_list = lst_from_file (renpy.loader.transfn("resources/effects.txt") )
    skill_list = lst_from_file (renpy.loader.transfn("resources/skills.txt") )
    units_list = lst_from_file (renpy.loader.transfn("resources/units.txt") )
    item_templates_list = lst_from_file (renpy.loader.transfn('resources/item_templates.txt') )
    army_list = lst_from_file (renpy.loader.transfn("resources/armies.txt"))
    generate_items_list = lst_from_file (renpy.loader.transfn("resources/item_generator.txt"))


    permanents_list=[]

    fonts_list= []
    for f in renpy.list_files():
        if f.startswith("fonts/"):
            fonts_list.append (f)



    resources_endless_list = lst_from_file(renpy.loader.transfn('resources/res_endless.txt') )
    resources_countable_list = lst_from_file (renpy.loader.transfn('resources/res_countable.txt') )


    events_list = lst_from_file (renpy.loader.transfn('resources/events.txt') )
    cell_types_list = lst_from_file (renpy.loader.transfn('resources/types.txt') ) #cell types parameters for every cell type
    map_by_types = lst_from_file (renpy.loader.transfn('resources/map.txt') ) #where cells of each type are placed on the map
    #list of all one_cell class instances


    scaling = float(config.screen_width)/1920 # for different resolutions (base is 1920x1080)

    config.menu_include_disabled = True #показывает недоступные варианты в меню
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    config.rollback_enabled = False

    config.autoreload = False

    config.keymap['game_menu'].remove('mouseup_3')
    # config.keymap['dismiss'].remove('mouseup_1')
    config.keymap['dismiss'].append('mouseup_3')

init 1 python:

    generate_standart_items_templates()
    #set of items names
    def initVariables():
        global reward_generator
        global currency
        global players_army
        global current_cell_name
        global event_started
        global event_ended
        global game_over
        global map_cells_ls
        global list_of_undead
        global Player_hero
        global menu_title #for chose screen
        global scout_report
        global list_of_current_local_effects
        global enemy_army
        global items_by_names

        enemy_army = None
        scout_report=""
        list_of_undead=[]
        list_of_current_local_effects = []

        for u in units_list:
            if u['tag'] == "undead":
                list_of_undead.append(u)

        items_by_names = init_items_by_names_list(item_templates_list)
        reward_generator=Reward_Generator()#after forming item_templates_list

        currency= Currency()
        players_army = Army("Glory Army")
        Player_hero =  Unit (search_in_list_by_name (units_list, "Necromancer") )
        players_army.add_unit( Player_hero)
        players_army.add_unit( Unit (search_in_list_by_name (units_list, "Sceleton") ) )
        # players_army.add_unit( Unit (search_in_list_by_name (units_list, "Lich") ) )

        current_cell_name = ""
        event_started = False
        event_ended = False
        game_over = False

        map_cells_ls = cells_list ()
        events_to_cells()
        menu_title=[]
        event_description=""
        fill_market()

        #test_item()
        #test_choises()
        # testStat()
        # testStatsParser()
        # # logging ("after all %s"%item_templates_list)
        # test_scouting_inString ()

        # for c in map_cells_ls:
        #     st= "%s [" %c.name
        #     for ev in c.saveble_events:
        #         st+=(ev.name+' ')
        #     st+= "]"
        #     # logging (st)
        #
        # test_army_gen()


init python:

    def onCellClicked (cell_name):
        global current_cell_name
        if currency.activity>0:
            current_cell_name = cell_name
            renpy.jump("cell_menu")
        else:
            renpy.jump("sleep")

label cell_menu:
    nvl clear
    scene scene_event
    python:
        global event_started
        unfinished_started = False
        current_cell = search ( map_cells_ls, current_cell_name)
        menu_title = local ("Клетка %s, %s" % (current_cell.name[4:],current_cell.type) )
        menu_items=[]
        menu_items.append (("Искать приключений", 0))
        menu_items.append( ("Уйти", 1))
        if len(current_cell.unfinished_events) != 0:
            menu_items.append (("Найденные ранее объекты:", None))
            i=2
            for ev in current_cell.unfinished_events:
                menu_items.append ( (ev.name, i) )
                i+=1
        choise =  renpy.display_menu( menu_items )
        if (choise==0):
            currency.activity-=1
            event_started=True
            current_cell.start_event() #this call works as a break instruction for unknown reasons and transfer control to the end of the python block
        elif (choise==1):
            renpy.jump("main_map")
        else:
            unfinished_started = True
            current_cell.start_unfinished(choise-2)
    python:
        if event_started:
            event_started = False
            enemy_army=None
            current_cell.finish_event()
        elif unfinished_started:
            unfinished_started = False
            enemy_army=None
            current_cell.finish_unfinished()
    nvl clear
    jump main_map

label sleep:
    "Вам нужно отдохнуть."
    jump main_map


label army:
    call screen army_main_screen()
    jump main_map


label person:
    nvl clear

        # menu:
        #     "Управление персонажем:"
        #     "Вещи": jump items

    call screen inventory_main_screen()

        # st=currency.get_player_items_names()
        # if len(st) == 0:
        #     e("У Вас пока нет вещей")
        # else:
        #     e("Список вещей:\n%s"% st)
    jump main_map

label castle:
    scene scene_event
    "It is your castle. Пока в разработке"
    # $test_scouting_inString ()
    jump main_map

label journal:
    scene scene_event
    nvl clear
    e "Краткая справка:\n
    Сложность врагов на клетках: лес->поле->деревня->дорога->холмы->горы->город->замок\n
    На некоторых клетках пока нет событий. Самое сложное событие - осада замка.\n
    Когда у Вас заканчиваются действия нажмите кнопку Спать.\n
    Враги становятся сильнее с каждым днем и с ростом Вашей репутации.\n
    Если у Вас появляются предметы их можно одеть в меню Герой.\n
    Здоровье юнитов восполняется каждый день.\n
    На перекрестке есть магазин. в нем несколько вкладок предметов, разделенных по редкости.\n
    "
    nvl clear
    e "Подробная справка:\n
      Игра повествует о становлении великого некромата.\n
      Вы начинаете с одним скелетом и без обмундирования.\n
      Перед Вами карта, разделенная на клетки. Клетки разделены по типу: дороги, поля, горы и тд.\
    Чтобы узнать тип клетки наведите на нее и посмотрите на подсказку в левом нижнем углу.\n
      Кликнув на клетку Вы увидете выбор - искать приключений или уйти с клетки. Нажав Искать приключений\
    Вы столкнетесь с одним из событий. Список событий зависит от типа клетки, на разных клетках одного и того\
    же типа события будут одинаковые. Некоторые события сохраняются, например найдя на перекрестке однажды магазин,\
    он будет сохранен в списке событий клетки и Вам не нужно будет искать его снова.\n
      Большинство событий - встреча с врагами. Игра автоматически посчитает Ваши шансы на победу и риск потерь,\
    но нужно помнить что это вероятностная оценка, а не 100\% гарантия."
    nvl clear
    e "  Битвы в игре полностью автоматические, и проходят в несколько шагов.\
    Изначально армии расположены на расстоянии 3 клетки, и постепенно сближаются.\
    Вы можете кликать мышкой чтобы ускорить битву.\n
      Противостоящие армии поделены на 2 ряда каждая. Войны из первого ряда могут сражаться в ближнем бою, из дальнего - стрелять.\
    Соответственно войн ближнего боя поставленный во второй ряд будет простаивать, пока в первом ряду не освободится место.\
    Юниты во втором ряду не получают урона, весь урон принимает на себя первый ряд.\n
      Воины первого ряда как бы защищают стрелков из второго ряда, поэтому если количество войнов первого ряда станет\
    меньше чем второго, то юнит из второго ряда будет автоматически перемещен в первый, и сможет стать целью врагов.\n
      Победив в битве вы получите награду - деньги, опыт, возможно предмет. Иногда некоторые побежденные враги могут быть\
    обращены в Ваших войнов. Если это произойдет Вы увидите соответствующий экран сообщения."
    nvl clear
    "Удачной игры!"
    jump main_map


init python:
    def next_day ():
        fill_market()
        currency.activity=3
        currency.day+=1
        for u in players_army.units:
            u.stats.current_health.restore()

        renpy.retain_after_load()
        renpy.rename_save("1-2", "1-3")
        renpy.rename_save("1-1", "1-2")
        renpy.take_screenshot()
        renpy.save("1-1","Autosave day %d"%currency.day)
    # jump main_map

label items:
    python:
        menu_items=[]
        for it in currency.items:
            menu_items
    #    if len(current_cell.unfinished_events) != 0:
    jump journal

default units_for_rec=[]
default gained_exp = 0
label battle_field:
    scene scene_battle
    $result = False
    if not enemy_army and current_cell.current_event.army:
        $enemy_army = generate_army( search_in_list_by_name (army_list, current_cell.current_event.army ) )

    if len (enemy_army.units) == 0:
        "вражеская армия трусливо сбежала"
    elif len (players_army.units) == 0:
        "у вас нет армии"
    else:
        $new_battle = Battle ( players_army, enemy_army)
        # $global units_for_rec
        # $global gained_exp
        $units_for_rec = []
        hide screen say
        window hide
        while (not new_battle.isOver()):
            # $renpy.show_screen("battle_screen",new_battle)
            show screen battle_screen (new_battle)
            pause(1)
            $new_battle.next_round()
        hide screen battle_screen
        scene scene_event
        $result = new_battle.isPlayerWon()
        $gained_exp = enemy_army.reward_exp
        if currency.reputation<1000:
            $currency.reputation = min ( currency.reputation+gained_exp/5, 1000)
        $units_for_rec=enemy_army.stillAlive
        $enemy_army=None
        if not result:
            jump game_over
        else:
            jump leveling

    return
label leveling:
    "Получено [gained_exp] опыта"
    python:
        global players_army
        exp = gained_exp // len (players_army.units)
        exp_rest = gained_exp % len (players_army.units)
        # print (exp, exp_rest)
        st=""
        for u in players_army.units:
            if exp_rest>0:
                exp_rest-=1
                ex=exp+1
            else:
                ex=exp
            # print (ex)
            if u==Player_hero:
                ex*=2
            s=u.addExp (ex)
            if s:
                st+=s
        if st:
            e(st)
    jump resurrection
    return

init python:
    def testResurrection():
        global units_for_rec
        units_for_rec.append( Unit (search_in_list_by_name (units_list, "Sceleton") ))
        units_for_rec.append( Unit (search_in_list_by_name (units_list, "Sceleton") ))
        renpy.jump ("resurrection")

label resurrection:
    #hide screen battle_screen
    # call screen reccurection_screen
    scene scene_event
    nvl clear
    python:
        global units_for_rec
        global players_army
        global list_of_undead
        if len (units_for_rec) > 0:
            if len(players_army.units) >= 20:
                e("Некоторые враги все еще живы, но в вашей армии больше нет места. Вы милосердно добиваете уцелевших")
            else:
                while (True):
                    menu_title="Пополнение"
                    menu_items=[]
                    menu_items.append ( (("Некоторые враги все еще живы, хотя тяжело ранены\nВы можете преобразить их в своих войнов."), None ))
                    menu_items.append (( ("Не нужны мне лузеры в армии!"), 0))
                    i=1
                    if len(units_for_rec)>0:
                        for u in units_for_rec:
                            menu_items.append ( ( local ("%s" %  u.name ) , i ))
                            i+=1
                    else:
                        break

                    choise =  renpy.display_menu( menu_items )

                    if choise == 0:
                        break
                    availible_units=[]
                    i=1
                    menu_it=[]
                    menu_it.append( ("Кого из него сделаем, босс?" , None) )
                    menu_it.append( ("Нафиг этого чмошника", 0) )
                    for u in list_of_undead:
                        urar=u["rarity"]
                        ch_urar= units_for_rec[choise-1].rarity
                        if rarity.index (urar) <= rarity.index(ch_urar):
                            availible_units.append(u)
                            menu_it.append( ( local( "%s"% u["name"]), i ) )
                            i+=1
                    ch =  renpy.display_menu( menu_it )
                    if (ch>0):
                        un=Unit(availible_units[ch-1])
                        players_army.add_unit( un )
                        players_army.regroup()
                        e( local("Вы создали [un.name]") )
                    units_for_rec.remove(units_for_rec[choise-1])
                    if len(players_army.units) >= 20:
                        e("Некоторые враги все еще живы, но в вашей армии больше нет места. Вы милосердно добиваете уцелевших")
                        break
                    if len(menu_items)<=2:
                        break
    return

label Menu_pressed:
    python:
        main_menu = False
    show screen game_menu("Load")
    return

label game_over:
    $game_over = True
    "Вот так славная история славного некроманта бесславно оборвалась. Рэст ин пис. Вайа кон диос. Аминь!"
    jump main_map
