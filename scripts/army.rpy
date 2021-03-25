init python:

    class Army:
        def __init__(self, name):
            self.name= name
            self.units= []
            self.frontline=0
            self.backline=0
            self.army_range=0
            self.army_cap = 20
            self.stillAlive = []
        def get_frontline_units(self):
            lst=[]
            for u in self.units:
                if u.line=="front":
                    lst.append(u)
            return lst

        def get_backline_units(self):
            lst=[]
            for u in self.units:
                if u.line=="back":
                    lst.append(u)
            return lst

        def check_range(self):
            self.army_range = 0
            for u in self.units:
                rng=u.getMaxRange()
                if rng > self.army_range:
                    self.army_range=rng

        def add_unit (self, unit):
            if len (self.units) >= self.army_cap:
                return False

            self.units.append(unit)
            if unit.line=="front":
                if self.frontline < self.army_cap/2:
                    self.frontline+=1
                else:
                    unit.line="back"
            if unit.line== "back":
                self.backline+=1;
            self.check_range()

        def regroup(self):
            for u in self.get_frontline_units():
                if u.priority_line == "back":
                    u.line= "back"
                    self.frontline-=1
                    self.backline+=1

            for u in self.get_backline_units():
                if self.frontline < self.army_cap/2:
                    if u.priority_line == "front":
                        u.line= "front"
                        self.frontline+=1
                        self.backline-=1

            while self.frontline<self.backline:
                for u in self.units:
                    if u.line == "back":
                        u.toFrontline()
                        self.backline-=1
                        self.frontline+=1
                        break

        def remove_unit (self, unit):
            if unit.line== "back":
                self.backline-=1
            else:
                self.frontline-=1
            self.units.remove(unit)


        def bring_out_your_dead (self):
            cnt=0
            str=""
            rem_ls=[]
            for s in self.units:
                if s.isDead():
                    if s.isAlive():
                        self.stillAlive.append (s)
                    cnt+=1
                    str+="%s " % s.name
                    rem_ls.append (s)
            for s in rem_ls:
                self.remove_unit(s)
            logging ("умерло юнитов: %d %s"% (cnt,str) )
            self.check_range()

        def __str__(self):
            str= self.name
            str+= "\n\rfrontline: "
            for u in self.get_frontline_units():
                str+=u.name+" "
            str+= "\n\rbackline: "
            for u in self.get_backline_units():
                str+=u.name+" "
            return str
