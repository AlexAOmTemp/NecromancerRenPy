
style market_button_text is army_text
default currentItem_market = None
default market_list_number = 0
default market_list_of_items = []
default market_purchase_status = ""

init python:
    def fill_market() :
        global market_list_of_items
        market_list_of_items= []
        for r in rarity:
            lst = reward_generator.generate_item_templates (18 , r)
            i = rarity.index(r)
            market_list_of_items.append ([])
            for itm in lst:
                market_list_of_items[i].append ( Item(itm) )

    def market_buy():
        global currentItem_market
        global market_purchase_status
        logging ("here!")
        if currency.money >= currentItem_market.cost:
            currency.money -=  currentItem_market.cost
            currency.addItem( currentItem_market )
            ind = market_list_of_items[market_list_number].index(currentItem_market)
            market_list_of_items[market_list_number][ind]=None
            currentItem_market = None
            market_purchase_status = "Thanks you"
        else:
            market_purchase_status = "No money - no honey"
                # SetVariable ("currency.money", currency.money - currentItem_market.cost),
                # Function(currency.addItem, currentItem_market),
                # Function(market_list_of_items[market_list_number].remove, currentItem_market),
                # SetVariable("currentItem_market",None )
                # SetVariable("market_purchase_status","Thanks you" ),
                # SetVariable("market_purchase_status","No money - no honey" )

screen market_screen():
    tag main
    style_prefix "market"
    add "scene_event"
    # textbutton local("OK") action Jump("main_map"):

    textbutton local("OK") action (SetVariable("market_purchase_status","" ), Return()):
        xalign 0.9
        yalign 0.9
    hbox:
        vbox:
            xsize scaled(400)
            text local("Selected:") xalign 0.5
            frame:
                style "slot"
                xalign 0.5
                if currentItem_market:
                    text local (currentItem_market.name) size scaled (25) xalign 0.5
            if currentItem_market:
                use market_item_stats(currentItem_market)
                textbutton local ("Buy (%d)"%currentItem_market.cost):
                    action Function (market_buy)
                    xalign 0.5
            text local(market_purchase_status)
        vbox:
            hbox:
                for r in rarity:
                    textbutton local(r) action (SetVariable("market_list_number", rarity.index(r) ), SetVariable("currentItem_market",None ), SetVariable("market_purchase_status","")  ):
                        background Frame ("square.png",0,0)
            hbox:
                spacing scaled(20)
                for k in range (3):
                    vbox:
                        spacing scaled(60)
                        # text title_text[k] xalign 0.5
                        $ln = 0
                        if market_list_of_items:
                            for i in range( k*6 , (k+1)*6 ):
                                $it = market_list_of_items[market_list_number][i]
                                if it:
                                    frame:
                                        style "slot"
                                        button:
                                            use market_item_screen(it)
                                            action (SetVariable("currentItem_market", it ),SetVariable("market_purchase_status",""))
                                else:
                                    frame:
                                        style "empty_slot"
                                # frame:
                            #     style "slot"
                            #     $logging ("%d %s"%((k*6+i),market_list_of_items[market_list_number][k*6+i]))
                            #     button:
                            #         use market_item_screen(market_list_of_items[market_list_number][k*6+i])
                            #         action (SetVariable("currentItem_market",market_list_of_items[market_list_number][k*6+i] ))
                        # for i in range(ln,6):
                        #     frame:
                        #         style "empty_slot"
            text str (market_list_number)

screen market_item_screen(item):
    vbox:
        frame:
            maximum (scaled (235), scaled (83))
            minimum (scaled (235), scaled (83))
            vbox:
                xalign 0.5
                text local(item.name) color "#000000" xalign 0.5 size scaled(35)
        text local ("Prise: %d"%item.cost)

screen market_item_stats(item):
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
