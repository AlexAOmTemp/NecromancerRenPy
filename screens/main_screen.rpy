
image res_icon = im.FactorScale("res_Icon.png", scaling)
image map = im.FactorScale("map.jpg", scaling)
image map hover = im.FactorScale("map hover.jpg", scaling)
image board left = im.FactorScale("board left.png", scaling)
image left_menu = im.FactorScale("menu.png", scaling)
image left_menu_hover = im.FactorScale("menu hover.png", scaling)
image board top = im.FactorScale("board top.png", scaling)
image board bottom  = im.FactorScale("board top.png", scaling)
    # (scaled_x, int(643*scaling), scaled_w, scaled_h)
    # (60, 714, 320, 60)
    # (60, 782, 320, 60)
    # (60, 848, 320, 60)

screen general():
    tag main
    default tt = Tooltip(" ")

    imagemap:
        xpos int(70*scaling) ypos int(90*scaling)
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

    imagemap:
        xpos int( (70+1350)*scaling) ypos 0
        ground 'left_menu'
        hover "left_menu_hover"
        $scaled_x = int(60*scaling)
        $scaled_w = int(320*scaling)
        $scaled_h = int(60*scaling)
        hotspot (scaled_x, int(643*scaling), scaled_w, scaled_h):
            clicked Jump ("army")
        hotspot (scaled_x, int(714*scaling), scaled_w, scaled_h):
            clicked Jump ("person")
        hotspot (scaled_x, int(782*scaling), scaled_w, scaled_h):
            clicked Jump ("castle")
        hotspot (scaled_x, int(848*scaling), scaled_w, scaled_h):
            clicked Jump ("journal")
        hotspot (scaled_x, int(901*scaling), scaled_w, scaled_h):
            clicked Jump ("next_day")

        text "activity" xalign 0.35 yalign 0.4
        text "[currency.activity]" xalign 0.40 yalign 0.44
        text "day" xalign 0.65 yalign 0.4
        text "[currency.day]" xalign 0.64 yalign 0.44

    add "board left" xpos 0 ypos int(90*scaling)
    add "board top" xpos 0 ypos 0
    add "board bottom" xpos 0 ypos int( (900+90)*scaling)
    text "Money" xpos int( 70*scaling) yalign 0
    text "[currency.money]" xpos int( 70*scaling) yalign 0.04

    if tt.value!=" ":
        frame: #bottom string
            xpos int(70*scaling)
            ypos int(1010*scaling)
            text tt.value:
                xalign 0.5

    frame: #resourse panel
        padding ( int(0*scaling), int(20*scaling))
        xpos int(200*scaling)
        ypos int(10*scaling)
        maximum (int(400*scaling), int(70*scaling) )
        $i=0
        for f in resources_endless_list:
            add im.FactorScale(f["image"], scaling) xpos 10+(20*i)
            $i+=1
