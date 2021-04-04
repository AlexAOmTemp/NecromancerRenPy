init -2 python:
    class Stat:
        def __init__ (self, base, name):
            self._bs = base
            self._increm = 0
            self._increa = 1
            self._mult = 1
            self._ad = 0
            self._tot = 0
            self.name = name
            self.total()

        def __str__(self):
            return ("total:%s, base: %s, increment:%s, increase: %s, add: %s, multiply: %s"
                    %(self._tot,self._bs,self._increm, self._increa, self._ad, self._mult))

        def total(self):
            self._tot = (( self._bs + self._increm ) * self._increa + self._ad ) * self._mult


        def val (self):
            return int(round(self._tot))

        def grow (self, value):
            self._bs += value
            self.total()

        def shrink (self, value):
            self._bs -= value
            self.total()

        def increment(self, value):
            self._increm += value
            self.total()

        def decrement(self, value):
            self._increm -= value
            self.total()

        def increase(self, value):
            self._increa += float(value)/100
            self.total()

        def decrease(self, value):
            self._increa -= float(value)/100
            self.total()

        def multiply(self, value):
            self._mult += float (value)/100
            self.total()

        def divide (self, value):
            self._mult -= float(value)/100
            self.total()

        def add(self, value):
            self._ad += value
            self.total()

        def sub(self, value):
            self._ad -= value
            self.total()

    def testStat():
        total = 100
        hp = Stat (100, "Health")
        if total != hp.val():
            raise ValueError ("testStat failed at stage 1")

        hp.increment (20)
        total = 120
        if total != hp.val():
            raise ValueError ("testStat failed at stage 2")

        hp.grow (10)
        total = 130
        if total != hp.val():
            raise ValueError ("testStat failed at stage 3")

        hp.increase(100)
        total = 260
        if total != hp.val():
            raise ValueError ("testStat failed at stage 4")

        hp.add(10)
        total = 270
        if total != hp.val():
            raise ValueError ("testStat failed at stage 5")

        hp.increase(100)
        total = 400
        if total != hp.val():
            raise ValueError ("testStat failed at stage 6")

        hp.multiply(100)
        total = 800
        if total != hp.val():
            raise ValueError ("testStat failed at stage 7")

        hp.shrink(10)
        total = 740
        if total != hp.val():
            raise ValueError ("testStat failed at stage 8")

        hp.decrement (10)
        total = 680
        if total != hp.val():
            raise ValueError ("testStat failed at stage 9")

        hp.decrease (100)
        total = 460
        logging (hp)
        if total != hp.val():
            raise ValueError ("testStat failed at stage 10")

        hp.divide(150)
        total = 115
        logging (hp)
        if total != hp.val():
            raise ValueError ("testStat failed at stage 11")

        hp.sub(20)
        total = 105
        if total != hp.val():
            raise ValueError ("testStat failed at stage 12")
