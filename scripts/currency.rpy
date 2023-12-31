init python:

    class Currency:
        def __init__(self):
            self.money = 0
            self.day = 0
            self.reputation = 0
            self.activity = 3
            self.maxday=1000
            self.maxrep=1000
            self.items = []

        def get_player_items_names(self):
            st='\n'.join([str(elem) for elem in self.items])
            return (st)

        def addItemByName (self, itemName):
            self.items.append( Item ( search_in_list_by_name ( item_templates_list, itemName ) ))

        def addItemByTemplate (self, item_template):
            self.items.append( Item (item_template) )

        def addItem (self, item):
            self.items.append( item )

        def sellAllItems (self):
            for i in reversed(self.items):
                i.sell()
    # logging ("currency")
