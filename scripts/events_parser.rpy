
# evnt = """
#         "evelin":"What the fuck is this?"
#         "menu":
#             {
#             "There is a lot of choises"
#             "You can go right":[],
#             "You can go left":[],
#             "You can go fuck yourself":[]
#             }
# """
init python:
    # evnt_describ = """{
    #         "menu":{
    #             "Вы встретили группу лохов"
    #             "[scout_report]"
    #             "Опустить":[
    #                 call battle_field,
    #                 $event_ended = True]
    #             "В другой раз, лох не мамонт...":
    #                 [$event_ended = False]
    #         }
    #     """
    #
    #
    # evnt = OrderedDict(evnt_describ)


    class Choise_item:
        def __init__ (self, caption, action):
            self.caption = caption
            self.action = action

    def test_choises():
        renpy.scene()
        renpy.show("scene_event")
        it=[]
        it.append( Choise_item ("test", [Function (Player_hero.stats.armor.grow, 1000), Return()] ) )
        it.append( Choise_item ("test1", None) )
        renpy.say("Eileen","What the fuck is this?")
        renpy.call_screen("choice",it)
