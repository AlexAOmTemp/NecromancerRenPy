init -2 python:
    class Current_health:
        def __init__ (self, max_health_val, owner):
            self.val_ = max_health_val
            self.max_hp = max_health_val
            self.owner = owner

        def deal (self, value):
            if random.randint(1,100) > self.owner.block.val():
                value*= 1.0/(1.0 + 0.01 * float(self.owner.armor.val()) )
                self.val_ -= value


        def heal (self, value):
            self.val_ += value

        def set (self, value):
            self.val_ = value

        def val (self):
            return int(round (self.val_))

        def max_health_changed (self, max_health_val):
            self.val_ = float(self.val_)/float(self.max_hp)*float(max_health_val)
            self.max_hp = max_health_val

        def remove_overhealth(self):
            self.val_ = min (self.val_, self.max_hp)

        def restore(self):
            self.val_ = self.max_hp

    # def testCurrentHealth():
    #     cur_hp = Current_health (100, None)
    #     if cur_hp.val() != 100:
    #         raise ValueError ("testCurrentHealth failed at stage 1")
    #
    #     cur_hp.max_health_changed(126)
    #     if cur_hp.val() != 126:
    #         raise ValueError ("testCurrentHealth failed at stage 2")
    #
    #     cur_hp.max_health_changed(106)
    #     if cur_hp.val() != 106:
    #         raise ValueError ("testCurrentHealth failed at stage 3")

        # cur_hp.deal(20)
        # cur_hp.deal(20)
        # if cur_hp.max_hp != 106:
        #     raise ValueError ("testCurrentHealth failed at stage 4a")
        # if cur_hp.val()!= 66:
        #     raise ValueError ("testCurrentHealth failed at stage 4b")

        # cur_hp.max_health_changed(50)
        # if cur_hp.max_hp != 31:
        #     raise ValueError ("testCurrentHealth failed at stage 5")
        #
        # cur_hp.heal(10)
        # cur_hp.heal(60)
        # if cur_hp.max_hp != 50:
        #     raise ValueError ("testCurrentHealth failed at stage 6a")
        # if cur_hp.val()!= 101:
        #     raise ValueError ("testCurrentHealth failed at stage 6b")
        #
        # cur_hp.remove_overhealth()
        # if cur_hp.val()!= 50:
        #     raise ValueError ("testCurrentHealth failed at stage 7")
