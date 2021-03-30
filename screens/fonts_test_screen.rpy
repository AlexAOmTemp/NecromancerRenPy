screen fonts_test_screen ( ):
    frame:
        vbox:
            for f in fonts_list:
                text "This is a new font! Вот это шрифт!":
                    font f
                    size 30
                text "{b}This is a new font! Вот это шрифт!{/b}":
                    font f
                    size 30
                text "{i}This is a new font! Вот это шрифт!\n{/i}":
                    font f
                    size 30
