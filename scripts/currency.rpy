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

    logging ("currency")
