# init python:
#     def purge_saves():
#         saves = renpy.list_slots()
#         for save in saves:
#             renpy.unlink_save(save)
#         renpy.take_screenshot()
#         renpy.save("1-1", save_name)
#         return

#
# default stat_1 = 0
# default stat_2 = 0
#
# screen control():
#
#     frame:
#         xalign 0.95
#         yalign 0.7
#         textbutton "Stat Box" action If(renpy.get_screen("stat_box"), Hide("stat_box"), Show("stat_box"))
#
# screen stat_box():
#     frame:
#         align (0.5,0.5)
#         vbox:
#             text "Stat 1: [stat_1]"
#             text "Stat 2: [stat_2]"


    # import os
    # ls=[]
    # for i in map_by_types:
    #     ls.extend (i)
    # st= set(ls)
    # ls = list (st)
    # direct="D:/programs/RenPy/projects/Vampire/game/images/"
    # for f in ls:
    #     os.mkdir("%s/%s"%(direct, f))




#
#
# transform hello_t:
#     align (0.7, 0.5) alpha 0.0
#     linear 0.5 alpha 1.0
# define sec=0
# screen hello_title():
#
#     text "[sec]" at hello_t
#     text "Hello.":
#         at transform:
#             align (0.2, 0.5) alpha 0.0
#             linear 0.5 alpha 1.0
#     $sec+=1
#







# label NewDay:
#       $ day = day+1
#
#       "It's a new day, Good morning!"
#       return
# screen Day:
#      text "Day [day]" xpos 0.1 ypos 0.1
#
# label start:
#       $ day = 0
#       show screen Day
#       "Day happens"
#       "Day ends"
#       call NewDay
#       "Day happens"
#       "Day ends"
#       call NewDay
#       "Day happens"
#       "Day ends"
#       call NewDay
#       hide screen Day
#       "no more day display :("
#       return
#







    #     scene bg meadow
    # menu:
    #     "What should I do?"
    #
    #     "Drink coffee.":
    #         "I drink the coffee, and it's good to the last drop."
    #
    #     "Drink tea." if have_gun <5:
    #         $ drank_tea = True
    #
    #     "I drink the tea, trying not to make a political statement as I do."
    #
    #     "Genuflect.":
    #         "..."
    #
    # "After a short while, we reach the meadows just outside the neighborhood where we both live."
    # $ count = 4
    # while count != 0:
    #     if key:
    #         "key works"
    #         $key = False
    #     else:
    #         m "key sucks"
    #     $count-=1
    # show sylvie green smile
    #
    # "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."
    #
    # "I'll ask her...!"
    #
    # m "Ummm... Will you..."
    #
    # m "Will you be my artist for a visual novel?"
    #
    # show sylvie green surprised
    #
    # "Silence."
    # return

    ###################




    # screen planets():
    #     default tt = Tooltip("No button selected.")
    #     imagemap:
    #
    #
    #         # ground im.Scale("map.png", config.screen_width, config.screen_height)
    #         # hover im.Scale("images/map hover.png",  config.screen_width, config.screen_height)
    #         ground "map.png"
    #         hover "map hover.png"
    #         hotspot (252, 454, 287, 249): #the capital
    #             clicked Jump("capital")
    #             hovered tt.Action("The loneliest number.")
    #
    #         hotspot (337, 50, 137, 175) clicked Jump("top_castle") #top castle
    #         hotspot (470, 233, 55, 215) clicked Jump("the_road") #the road
    #         hotspot (556, 206, 238, 88) clicked Jump("field") #field
    #         hotspot (655, 300, 178, 167) clicked Jump("mid_castle") #mid castle
    #         hotspot (832, 493, 190, 191) clicked Jump("bot_castle") #bot castle
    #         hotspot (798, 4, 104, 144) clicked Jump("mine") #mine
    #         hotspot (883, 161, 101, 126) clicked Jump("free_town") #free town
    #         hotspot (1132, 333, 85, 88) clicked Jump("free_village") #free village
    #         hotspot (986, 172, 134, 159) clicked Jump("ruins") #ruins
    #         hotspot (1116, 443, 162, 275) clicked Jump("forest") #forest



    # screen tooltip_test():
    #
    #     default tt = Tooltip("No button selected.")
    #
    #     frame:
    #         xfill True
    #
    #         has vbox
    #
    #         textbutton "One.":
    #             action Return(1)
    #             hovered tt.Action("The loneliest number.")
    #
    #         textbutton "Two.":
    #             action Return(2)
    #             hovered tt.Action("Is what it takes.")
    #
    #         textbutton "Three.":
    #             action Return(3)
    #             hovered tt.Action("A crowd.")
    #
    #         text tt.value

    # screen test_frame():
    #     frame:
    #         xpadding 10
    #         ypadding 10
    #         xalign 0.5
    #         yalign 0.5
    #
    #         vbox:
    #             text "Display"
    #             null height 10
    #             textbutton "Fullscreen" action Preference("display", "fullscreen")
    #             textbutton "Window" action Preference("display", "window")
