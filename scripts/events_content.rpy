
label a1_dialog:
    "its sucks to see you here"
    menu:
        "What should I do?"
        "Drink coffee.":
            "I drink the coffee, and it's good to the last drop."
        "Drink tea.":
            "suck"
    return

label castle_siege:
    "Вы приближаетесь к вражескому замку. Его охраняют рыцари и их слуги"
    menu:
        "Штурм":
            call battle_field
            $event_ended = True
        "Мудрое отступление":
            $event_ended = False
    return
label Mess_party:
    "Вы встретили группу лохов"
    menu:
        "Опустить":
            call battle_field
            $event_ended = True
        "В другой раз, лох не мамонт...":
            $event_ended = False
    return

label Peasants_party:
    "Кучка крестьян с вилами, выглядит устрашающе"
    menu:
        "Навалять им":
            call battle_field
            $event_ended = True
        "Вилы это грозное оружие, один удар - много дырок. Лучше свалю.":
            $event_ended = False
    return

label Peasant_and_co:
    "Крестьянин с семьей, отличный зомбак выйдет"
    menu:
        "Гасить!":
            call battle_field
            $event_ended = True
        "Да ну, чтобы я пролетария обидел?":
            $event_ended = False
    return

label Brave_alone:
    "Вы подглядываете из-за куста за каким то челом. Похоже это тренированный войн."
    menu:
        "Напасть из кустов":
            call battle_field
            $event_ended = True
        "Претвориться кабанчиком и по-тихому отвалить":
            $event_ended = False
    return
label My_pike_only:
    "Мужик несет кабанчика наколотого на пику. Одет в военную форму, наверно слабак!"
    menu:
        "Мужик, еда есть? А если найду?":
            call battle_field
            $event_ended = True
        "Кто я такой чтобы нарушать снабжение армии? Между прочим эти парни за нас кровь льют!":
            $event_ended = False
    return
label Pikemans_party:
    "Несколько парней сидят вокруг костра и жарят на пиках шашлык."
    menu:
        "Пахнет вкусно. Эй парни, огоньку не найдется?":
            call battle_field
            $event_ended = True
        "Я вообще то вегетарианец, пойду по своим делам.":
            $event_ended = False
    return
label Knight_alone:
    "Кажется это настоящий рыцарь. Можно сказать одинокий... ну не считая кортежа слуг конечно"
    menu:
        "Слыш паря, давай раз на раз! Только ты, я и моя армия!":
            call battle_field
            $event_ended = True
        "Нет, это, конечно, не Ланселот Озерный, о такую мелочь даже руки пачкать не буду.":
            $event_ended = False
    return
label One_poor_man:
    "Захудалый одинокий противник, можно поразмяться"
    menu:
        "К бою, моя великая орда!":
            call battle_field
            $event_ended = True
        "Неспортивно как то, мне бы сотню другую разогнать...":
            $event_ended = False
    return
