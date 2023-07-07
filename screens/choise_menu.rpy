define config.narrator_menu = False

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
define gui.choice_text_font = fonts_list[0]
define gui.choice_text_hover_color = '#000000'
define gui.choice_button_text_font = fonts_list[0]
define gui.choice_button_text_idle_color = '#000000'
define gui.choice_button_width = 990
define gui.choice_button_text_xalign = 0.5

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    # xsize 790
style choice_text is default:
    xsize 690
    xalign 0.5
    size 38
    font fonts_list[0]

style choice_button_text is choice_text
    # properties gui.button_text_properties("choice_button")


screen choice(items):
    style_prefix "choice"
    add "scene_event"
    vbox:
        yalign 0.5
        xalign 0.5
        text menu_title:
            xalign 0.5
            size 50
        for i in items:
            if i.action:
                textbutton i.caption action i.action
            else:
                text i.caption
