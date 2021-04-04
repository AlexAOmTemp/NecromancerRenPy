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
    # use army_screen(players_army)
    textbutton "OK" action Jump("main_map"):
         xalign 0.9
         yalign 0.9


    null height 20 #just a height set
    hbox:
        vbox:
            frame:
                side ("c r"):
                    area (1,0,scaled(400),600)
                    viewport id "my_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                        draggable True mousewheel True
                        vbox:
                            for itm in currency.items:
                                textbutton itm.name:
                                    action [SetVariable ("currentItem", itm), If (Player_hero.equipment.slots[itm.slot]!=None , SetVariable ("equippedItem", Player_hero.equipment.slots[itm.slot]) , SetVariable ("equippedItem",None))]

                    vbar value YScrollValue("my_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
            textbutton 'Sell all' action  (Function ( currency.sellAllItems), SetVariable ("currentItem", None))
        vbox:
            xsize scaled(400)
            text "Selected:" xalign 0.5
            frame:
                style "slot"
                xalign 0.5
                if currentItem:
                    text currentItem.name size 25
            use item_stats(currentItem)

            if currentItem:
                if currentItem.slot in Player_hero.equipment.slots:
                    textbutton "Equip" action (Function (  Player_hero.equipment.equip, currentItem ), SetVariable ("temp", currentItem), SetVariable ("currentItem", equippedItem), SetVariable ("equippedItem", currentItem) ) xalign 0.5
                else:
                    text "No slot for this item"
                textbutton "Sell ([currentItem.sellCost])" action (Function ( currentItem.sell), SetVariable ("currentItem", None)  ) xalign 0.5
        vbox:
            xsize scaled(400)
            text "Equipped:" xalign 0.5
            frame:
                style "slot"
                xalign 0.5
                if equippedItem:
                    text equippedItem.name size 25
            if equippedItem:
                use item_stats(equippedItem)
                textbutton "Unequip" action (Function (Player_hero.equipment.unequip, equippedItem ), SetVariable ("equippedItem", None)) xalign 0.5

            # if currentItem:
            #     if Player_hero.equipment.slots[currentItem.slot]:
            #         use item_stats(Player_hero.equipment.slots[currentItem.slot])
        vbox:
            xsize scaled(400)
            use unit_stats(Player_hero)
        vbox:
            for sl in Player_hero.equipment.slots:

                    if Player_hero.equipment.slots[sl] == None:
                        frame:
                            style "empty_slot"
                            text "[sl] empty" size 25
                    else:
                        frame:
                            style "slot"
                            textbutton Player_hero.equipment.slots[sl].name action SetVariable ("equippedItem", Player_hero.equipment.slots[sl]) text_size 25

style item_stats_text is default:
    xalign 0.0
screen item_stats(item):
    style_prefix "item_stats"
    if isinstance (item, Item):
        vbox:
            text "Name: [item.name]"
            text "Slot: [item.slot]"
            text "Rarity: [item.rarity]"
            if len (item.stats) > 0:
                text "Stats:"
                for i in item.stats:
                    text "{color=#00ff00}[i]{/color}"
            if len (item.skills) > 0:
                text "Skills:"
                for i in item.skills:
                    text i
            text "Sell cost: [item.sellCost]"
