
label castle_siege:
    menu:
        "Вы приближаетесь к вражескому замку. Его охраняют рыцари и их слуги"
        "Штурм":
            call battle_field
            $event_ended = True
        "Мудрое отступление":
            $event_ended = False
    return

label Mess_party:
    menu:
        "Вы встретили группу лохов"
        "Опустить":
            call battle_field
            $event_ended = True
        "В другой раз, лох не мамонт...":
            $event_ended = False
    return

label Peasants_party:
    menu:
        "Кучка крестьян с вилами, выглядит устрашающе"
        "Навалять им":
            call battle_field
            $event_ended = True
        "Вилы это грозное оружие, один удар - много дырок. Лучше свалю.":
            $event_ended = False
    return

label Peasant_and_co:
    menu:
        "Крестьянин с семьей, отличный зомбак выйдет"
        "Гасить!":
            call battle_field
            $event_ended = True
        "Да ну, чтобы я пролетария обидел?":
            $event_ended = False
    return

label Brave_alone:
    menu:
        "Вы подглядываете из-за куста за каким то челом. Похоже это тренированный войн."
        "Напасть из кустов":
            call battle_field
            $event_ended = True
        "Претвориться кабанчиком и по-тихому отвалить":
            $event_ended = False
    return
label My_pike_only:
    menu:
        "Мужик несет кабанчика наколотого на пику. Одет в военную форму, наверно слабак!"
        "Мужик, еда есть? А если найду?":
            call battle_field
            $event_ended = True
        "Кто я такой чтобы нарушать снабжение армии? Между прочим эти парни за нас кровь льют!":
            $event_ended = False
    return
label Pikemans_party:
    menu:
        "Несколько парней сидят вокруг костра и жарят на пиках шашлык."
        "Пахнет вкусно. Эй парни, огоньку не найдется?":
            call battle_field
            $event_ended = True
        "Я вообще то вегетарианец, пойду по своим делам.":
            $event_ended = False
    return

label Knight_alone:
    menu:
        "Кажется это настоящий рыцарь. Можно сказать одинокий... ну не считая кортежа слуг конечно"
        "Слыш паря, давай раз на раз! Только ты, я и моя армия!":
            call battle_field
            $event_ended = True
        "Нет, это, конечно, не Ланселот Озерный, о такую мелочь даже руки пачкать не буду.":
            $event_ended = False
    return

label One_poor_man:
    menu:
        "Захудалый одинокий противник, можно поразмяться"
        "К бою, моя великая орда!":
            call battle_field
            $event_ended = True
        "Неспортивно как то, мне бы сотню другую разогнать...":
            $event_ended = False
    return

label Tumbstone:
    menu:
        "Вы нашли одинокую могилу, если ее раскопать можно попробовать создать скелета из давно иссохшегося трупа"
        "О да, я обожаю копать, в детстве мечтал стать шахтером!":
            $players_army.add_unit( unit (search_in_list_by_name (units_list, "Sceleton") ) )
            $players_army.regroup()
            "Вы создали скелета."
            if (dice_100() > 50):
                "Стоило вам закончить с ритуалом, как вы услышали голос сзади: Эй, чувак, а ты чего это с моим дедом делаешь?"
                call battle_field
            $event_ended = True
        "Осквернение могил? Я кто по вашему - Лора Крафт, известнейшая расхитительница мавзолеев?":
            $event_ended = False
    return

label warriors:
    menu:
        "Вы видите 3 парней с мечами на сцене цирка"
        "Эй парни, дай покажу как надо!":
            call battle_field
            $event_ended = True
        "Пусть прыгают, нам не до них.":
            $event_ended = False
    return
