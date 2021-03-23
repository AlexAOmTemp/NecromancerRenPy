init python:

    class currency_class:
        def __init__(self):
            self.money = 0
            self.day = 0
            self.activity = 3
            self.items = []

        def get_player_items_names(self):
            st='\n'.join([str(elem) for elem in self.items])
            return (st)

    logging ("currency")
