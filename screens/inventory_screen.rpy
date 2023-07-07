default currentItem = None
default equippedItem = None
default temp = None

style inventory_text is default:
    xalign 0.5
    size 30
    font fonts_list[0]

style inventory_button_text is army_text

style empty_slot is slot:
    background Frame ("empty square.png",0,0)

screen inventory_main_screen():
    tag main
    style_prefix "inventory"
    add "scene_event"
    textbutton local("OK") action Jump("main_map"):
         xalign 0.9
         yalign 0.9


    null height 20 #just a height set
    hbox:
        vbox:
            frame:
                side ("c r"):
                    area (1,0,scaled(400),scaled(600))
                    viewport id "my_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                        draggable True mousewheel True
                        vbox:
                            for itm in currency.items:
                                textbutton local(itm.name):
                                    action [SetVariable ("currentItem", itm), If (Player_hero.equipment.slots[itm.slot]!=None , SetVariable ("equippedItem", Player_hero.equipment.slots[itm.slot]) , SetVariable ("equippedItem",None))]

                    vbar value YScrollValue("my_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
            textbutton local('Sell all') action  (Function ( currency.sellAllItems), SetVariable ("currentItem", None))
        vbox:
            xsize scaled(400)
            text local("Selected:") xalign 0.5
            frame:
                style "slot"
                xalign 0.5
                if currentItem:
                    text local (currentItem.name) size 25
            use item_stats(currentItem)

            if currentItem:
                if currentItem.slot in Player_hero.equipment.slots:
                    textbutton local("Equip") action (Function (  Player_hero.equipment.equip, currentItem ), SetVariable ("temp", currentItem), SetVariable ("currentItem", equippedItem), SetVariable ("equippedItem", currentItem) ) xalign 0.5
                else:
                    text local("No slot for this item")
                textbutton local("Sell ([currentItem.sellCost])") action (Function ( currentItem.sell), SetVariable ("currentItem", None)  ) xalign 0.5
        vbox:
            xsize scaled(400)
            text local("Equipped:") xalign 0.5
            frame:
                style "slot"
                xalign 0.5
                if equippedItem:
                    text local(equippedItem.name) size 25
            if equippedItem:
                use item_stats(equippedItem)
                textbutton local("Unequip") action (Function (Player_hero.equipment.unequip, equippedItem ), SetVariable ("equippedItem", None)) xalign 0.5

            # if currentItem:
            #     if Player_hero.equipment.slots[currentItem.slot]:
            #         use item_stats(Player_hero.equipment.slots[currentItem.slot])
        vbox:
            xsize scaled(400)
            use unit_stats(Player_hero,equippedItem ,currentItem)
        vbox:
            for sl in Player_hero.equipment.slots:
                if Player_hero.equipment.slots[sl] == None:
                    frame:
                        style "empty_slot"
                        text local("%s empty"%sl) size 25
                else:
                    frame:
                        style "slot"
                        textbutton local(Player_hero.equipment.slots[sl].name) action (SetVariable ("equippedItem", Player_hero.equipment.slots[sl]),SetVariable ("currentItem", None)  ) text_size 25

style item_stats_text is default:
    xalign 0.0

screen item_stats(item):
    style_prefix "item_stats"
    if isinstance (item, Item):
        vbox:
            text local("Name: %s"%item.name)
            text local("Slot: %s"%item.slot)
            text local("Rarity: %s"%item.rarity)
            if len (item.stats) > 0:
                text local("Stats:")
                for i in item.stats:
                    text local("{color=#006400}%s{/color}"%i)
            if len (item.skills) > 0:
                text local("Skills:")
                for i in item.skills:
                    text local(i)
            text local("Sell cost: [item.sellCost]")
