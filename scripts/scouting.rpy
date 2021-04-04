init -1 python:
    def scouting (player_army, enemy_army):
        # logging ("Внутри теста")
        player_win = 0
        player_unitsQuant = len (player_army.units)
        player_averageUnitsLoss=0
        for i in range (10):
            army_1 =  copy.deepcopy (player_army)
            army_2 =  copy.deepcopy (enemy_army)
            battle = Battle (army_1 , army_2)
            while (not battle.isOver()):
                battle.next_round()
            player_averageUnitsLoss += player_unitsQuant - len (army_1.units)
            if battle.isPlayerWon():
                player_win += 1
            # logging ("битва %d, wins = %d, len_1 = %d, len_2 = %d"% (i, player_win,  len (army_1.units),  len (army_2.units)) )
        player_averageUnitsLoss /=10
        player_units_loss_pers = int  (player_averageUnitsLoss*100/player_unitsQuant)
        player_winChanse = player_win*10
        # logging ("Возвращаю %d,%d"%(player_units_loss_pers, player_winChanse) )
        return player_units_loss_pers, player_winChanse


    def scouting_inString (player_army, enemy_army):
        # logging ("Тест начат")
        interv= [[0,10],[10,30],[30,60],[60,80],[80,101] ]
        loss=["{color=#00ff00}Минимальные{/color}","{color=#000080}Небольшие{/color}", "{color=#ffff00}Средние{/color}", "{color=#ffa500}Большие{/color}", "{color=#f00}Катастрофические{/color}"]
        win = ["{color=#f00}Стремяться к 0{/color}","{color=#ffa500}Мало{/color}", "{color=#ffff00}Средние{/color}", "{color=#000080}Выше среднего{/color}", "{color=#00ff00}Большие{/color}"]

        ch_loss, ch_win = scouting (player_army, enemy_army)

        loss_st=""
        win_st=""
        for i in range(5):
            # logging("%d,%d"%(ch_loss, interv[i][1]))
            if ch_loss >= interv[i][0] and ch_loss < interv[i][1]:
                loss_st= loss[i]
            if ch_win >= interv[i][0] and ch_win < interv[i][1]:
                win_st= win[i]
        # logging ("%d Превратил в строку: %s,%s"%(k, loss_st, win_st) )
        return loss_st, win_st

    def sc_report():
        global enemy_army
        global players_army
        enemy_army = generate_army( search_in_list_by_name (army_list, current_cell.current_event.army ) )
        loss, win = scouting_inString (players_army, enemy_army)
        return ("Вероятные потери: %s\nШансы победить: %s"%(loss, win) )


    def test_scouting_inString ():
        army_1= Army("Test army 1")
        army_2= Army("Test army 1")
        for i in range (10):
            army_1.add_unit_by_name ( "Sceleton")
        for i in range (4):
            army_2.add_unit_by_name ( "Lich")
        loss, win =scouting_inString (army_1, army_2)
        # logging ("Вероятные потери: %s, Шансы победить: %s"%(loss, win) )
