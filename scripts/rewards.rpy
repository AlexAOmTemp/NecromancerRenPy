
init python:

    rwd={
    "rare":3,
    "items":["poor_sword","ржавый меч"],
    "gold": [100, 300]
    }



    class reward_gen:
        def __init__ (self):
            self.items = {}
            for r in rarity:
                self.items[r]=[]
                for it in item_list:
                    if it["rarity"]==r:
                        self.items[r].append(it)
            self.gold={"poor":[1,10], "normal":[10,20], "magic":[20,30], "rare":[30,50], "legendary":[50,100] }

        def getReward (self,parameters):
            global items_by_names
            items=[]
            gold=0
            for key, value in parameters.items():
                if key in rarity:
                    if value>0:
                        for i in range (value):
                            it , gl =self.generate(key)
                            items+=it
                            gold+= gl
                elif key == "items":
                    for it in value:
                        if it in items_by_names:
                            items.append(it)
                elif key == "gold":
                    gold+= random.randint(value[0],value[1])
            return items , gold

        def generate(self, rew_rarity):
            it_quant = random.randint(0,1)
            items=[]
            if it_quant>0:
                for i in range (it_quant):
                    items.append ( ( random.choice (self.items[rew_rarity]) )["name"] )
            rand= self.gold [rew_rarity]
            gold = random.randint(rand[0],rand[1])
            return items , gold

    logging ("rewards")

    def test_rewards():
        it, gld = reward_generator.getReward(self.current_event.reward)
        currency.addItem()
    #it, gld = reward_generator.getReward(rwd)
    #e (it, gld)
