
label a1_dialog:
    "its sucks to see you here"
    menu:
        "What should I do?"
        "Drink coffee.":
            "I drink the coffee, and it's good to the last drop."
        "Drink tea.":
            "suck"
    return

label event_one:
    menu:
        "this is event one"
        "Победить":
            "битва за средиземье начинается"

            $result = False
            $enemy_army = generate_army(army_test)
            if len (enemy_army.units) == 0:
                "вражеская армия трусливо сбежала"
            elif len (players_army.units) == 0:
                "у вас нет армии"
            else:
                "это будет легендарная битва"
                $result = battle ( players_army, enemy_army)

            if result:
                $event_ended = True
            else:
                $event_ended = False
                jump game_over
        "Сбежать":
            $event_ended = False
    return
label event_two:
    menu:
        "this is event 2"
        "Победить":
            $event_ended = True
        "Сбежать":
            $event_ended = False
    return

label event_three:
    menu:
        "this is event 3"
        "Победить":
            $event_ended = True
        "Сбежать":
            $event_ended = False
    return

label event_four:
    menu:
        "this is event 4"
        "Победить":
            $event_ended = True
        "Сбежать":
            $event_ended = False
    return
