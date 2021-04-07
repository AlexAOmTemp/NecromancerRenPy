
image res_icon = im.FactorScale("res_Icon.png", scaling)
image map = im.FactorScale("map.jpg", scaling)
image map hover = im.FactorScale("map hover.jpg", scaling)
image main_background  = im.FactorScale("main_background.png", scaling)
image scene_battle = im.FactorScale("scene_battle.png", scaling)
image scene_blue  = im.FactorScale("scene_blue.png", scaling)
image scene_event  = im.FactorScale("scene_event.png", scaling)
image necromanser = im.FactorScale(im.Scale("necromanser.jpg",300,300), scaling)
image necromanser_border = im.FactorScale(im.Scale("map_border.png",340,340), scaling)
image map_border = im.FactorScale("map_border.png", scaling)
# image button = Frame ("board top.png")
image button = Frame ("map_border.png")
image status = Frame ("scene_event.png")

    # (scaled_x, int(643*scaling), scaled_w, scaled_h)
    # (60, 714, 320, 60)
    # (60, 782, 320, 60)
    # (60, 848, 320, 60)

style gen_button:
    text_align 1.0
    background  "button"
    xsize scaled(240)

style gen_button_text:
    size scaled (35)
    font fonts_list[3]
    xalign 0.5
    color "#000000"

style serv_text:
    size scaled (28)
    xalign 0.5
    color "#000000"
    font fonts_list[0]

style gen_text:
    size scaled (28)
    xalign 0.5
    color "#000000"

init python:
    def scaled (value):
        global scaling
        return int(value*scaling-0.5)


screen general():
    tag main
    default tt = Tooltip(" ")
    add "main_background"


    image "map_border":
        xpos int(50*scaling) ypos scaled (90)

    imagemap:
        xpos int(70*scaling) ypos scaled (110)
        $cell_size=int(150*scaling)
        for y in range(6):
            for x in range(9):
                $ls=list('ABCDEFJHI')
                $st="map_%s%d" % (ls[x],y+1)
                $cl = search(map_cells_ls, st)
                hotspot (0+cell_size*x, 0+cell_size*y, cell_size, cell_size):
                    clicked Function(onCellClicked,st)
                    hovered tt.Action("%s%d %s" % (ls[x],y+1,cl.type) )
        ground 'map'
        hover "map hover"

    add "necromanser_border":
        xpos scaled ( 1510)   ypos scaled (90)
    add "necromanser":
        xpos scaled ( (1920-50-1390-340)/2+1440+20)  ypos scaled (110)
    vbox:
        xpos scaled(1550)  ypos scaled (450)
        spacing scaled(20)
        frame:
            xpos scaled(8)

            xsize scaled(240)
            background "status"
            vbox:
                style_prefix "serv"
                spacing scaled(10)
                hbox:
                    text "Activity: "
                    text "[currency.activity]"
                hbox:
                    text "Day: "
                    text "[currency.day]"
                hbox:
                    text "Reputation: "
                    $rep= int(round(currency.reputation/10))
                    text "[rep]"
                hbox:
                    text "Health: "
                    $cur_hp= max (int (round (Player_hero.stats.current_health.val() ) ), 0)
                    $max_hp = int (round (Player_hero.stats.max_health.val() ))
                    text "[cur_hp] / [max_hp]"
        frame:
            background None
            vbox:
                spacing scaled(10)
                style_prefix "gen"
                textbutton 'Menu' action ShowMenu('game_menu',"Load") keysym 'K_ESCAPE'
                textbutton "Army" clicked Jump ("army")
                textbutton "Person" clicked Jump ("person")
                textbutton "Castle" clicked Jump ("castle")
                textbutton "Journal" clicked Jump ("journal")
                textbutton "Next day" action Function (next_day)


    if tt.value!=" ":
        frame: #bottom string
            style_prefix "serv"
            xpos scaled (70)
            ypos scaled (1035)
            text tt.value:
                xalign 0.5

    frame: #resourse panel
        xpos int(200*scaling)
        ypos int(10*scaling)
        style_prefix "gen"
        hbox:
            spacing scaled(20)
            vbox:
                text "Money"
                text  "[currency.money]"
            hbox:
                spacing scaled(20)
                for f in resources_endless_list:
                    add im.FactorScale( (im.Scale (f["image"],40,40)) , scaling):
                        ypos scaled(10)
