
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
#





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
