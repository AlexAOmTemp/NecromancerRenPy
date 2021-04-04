init python:

    class Equipment:
        possibleSlots = ("melee weapon", "armor", "helmet", "shield", "range weapon", "boots", "left ring", "right ring", "amulet")
        def __init__(self, owner, slots):
            self.slots={}
            for s in slots:
                self.slots[s] = None
            self.owner = owner

        def equip(self, item):
            if item.slot in self.slots:
                if self.slots[item.slot] != None:
                    self.unequip(self.slots[item.slot])
                item.equip(self)
                self.slots[item.slot]=item
                for i in item.stats:
                    self.owner.stats.setParameterFromStr(i)
                currency.items.remove(item) 
            else:
                raise NameError('Item with wrong slot: %s'%item.slot )

        def unequip (self, item):
            if self.slots[item.slot] == item:
                self.slots[item.slot] = None
                item.unequip()
                for i in item.stats:
                    self.owner.stats.resetParameterFromStr(i)
                currency.items.append(item)
            else:
                raise NameError('Item not in slot')
