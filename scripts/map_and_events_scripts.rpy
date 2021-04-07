
init python:
    map_cells_ls = []

    class event:
        def __init__(self, params):
            self.name = params["name"]
            self.max_times_happens = params["max_times_happens"]
            self.happened = 0
            self.blocks_events = params["blocks_events"]
            self.needs_events = params["needs_events"]
            self.jump_to_label = params["jump_to_label"]
            self.saveble = params["saveble"]
            self.level = params["level"]
            self.reward = params["reward"]
            self.army = params["army"]

        def happens (self):
            global event_ended
            global menu_title
            global scout_report
            event_ended = False
            # narrator ("Начало события \"%s\"."%(self.name))
            menu_title = "%s" % (self.name)
            scout_report = sc_report()
            renpy.call ( self.jump_to_label)

        def is_valid (self):
            if self.needs_events == [] and self.happened <= self.max_times_happens:
                return True
            else:
                return False

        def __str__(self):
            return ("%s" % (self.name))

        def __repr__ (self):
            return ('''event ( {\n\"name\":"%s",\n\"max_times_happens\":%s,\n\"blocks_events\":%s,\n\"needs_events\":%s,\n\"jump_to_label\":"%s",\n\"saveble\":%s\n})
            ''' % (self.name, self.max_times_happens, self.blocks_events, self.needs_events, self.jump_to_label, self.saveble) )


    class one_cell:
            def __init__(self, name, cell_type):
                self.name = name
                self.type = cell_type
                self.saveble_events=[]
                self.repetable_events_names=[]
                self.unfinished_events=[]
                self.current_event=0

            def start_event(self):
                choose=random.randint(0,100)
                if choose<100 and self.saveble_events!=[]:
                    posibble_events = self.saveble_events
                    #e ("сохраняемое событие")
                else:
                    posibble_events=self.repetable_events_names
                    #e ("Регулярное событие")
                # print (posibble_events)
                if posibble_events==[]:
                    e ("Нет событий")
                    global event_started
                    event_started = False
                    return
                dice=random.randint(0,len(posibble_events)-1)
                if isinstance (posibble_events[dice],str):
                    posibble_events[dice]= event (search_in_list_by_name (events_list, posibble_events[dice]))
                self.current_event=posibble_events[dice]
                ## logging("start_event\n"+repr(self)+"\n\n")
                self.current_event.happens()

            def finish_event (self):
                global event_ended
                event_cancelled= not event_ended
                if (event_ended):
                    self.getRewardforCurrentEvent()
                if self.current_event.saveble:
                    if event_cancelled:
                        self.unfinished_events.append (self.current_event)
                        e("событие сохранено")
                    self.saveble_events.remove(self.current_event)
                ## logging("finish_event\n"+repr(self)+"\n\n")

            def start_unfinished (self, position):
                # # logging("%s" % type(position))
                self.current_event=self.unfinished_events[int(position)]
                st=[]
                for i in range(len(self.unfinished_events)):
                    st+=self.unfinished_events[i].name
                ## logging("start_unfinished\nunfinished=%s"%(self.unfinished_events))
                ## logging("position=%d\nunfinished_events=%s\ncurrent_event=%s\n\n" % (position,st,self.current_event) )
                self.current_event.happens()

            def finish_unfinished (self):
                global event_ended
                if event_ended:
                    self.getRewardforCurrentEvent()
                    if self.current_event in self.unfinished_events:
                        self.unfinished_events.remove(self.current_event)
                    else:
                        e("событие не в списке незаконченных")
                        e("%s" % (str (len(self.unfinished_events))) )
                        if len(self.unfinished_events):
                            for ev in self.unfinished_events:
                                e("%s" % (ev) )
                        e("%s" % (self.current_event) )
                ## logging("finish_unfinished\n"+repr(self)+"\n\n")

            def getRewardforCurrentEvent(self):
                nvl_clear()
                st="событие завершено\n"
                it, gld = reward_generator.getReward(self.current_event.reward)
                for i in it:
                    currency.addItem (i)
                currency.money += gld

                if len (it)>0 or gld>0:
                    st+=("получена награда!")
                    if gld>0:
                        st+=("\nзолото: %d\n" % gld)
                    if len(it)>0:
                        toStr = ''.join(["{color=#00ff00}"+(str(elem)+'{/color}\n') for elem in it])
                        st+=toStr
                    e (st)



            def __str__(self):
                return ("%s,%s" % (self.name,self.type))
            def __repr__ (self):
                return ('''one_cell = ({\n"name":"%s",\n"type":"%s",\n"saveble_events":%s,\n"repetable_events_names":%s,\n"unfinished_events":%s,\n"current_event":%s\n})
                    ''' % ( self.name, self.type,self.saveble_events,self.repetable_events_names,self.unfinished_events,self.current_event) )



    def cells_list ():
        cl=[]
        for y in range(6):
            for x in range(9):
                ls=list('ABCDEFJHI')
                st="map_%s%d" % (ls[x],y+1)
                cl.append (one_cell (st, map_by_types[y][x]))
        return cl


    def events_to_cells():
        for ev in events_list:
                types=[] #list of types that contain event ev
                for t in cell_types_list:
                    if ev["name"] in t["events"]:
                        types.append(t["name"])
                cells=[] #list of cells with type from "types"
                for c in map_cells_ls:
                    if c.type in types:
                        cells.append(c)
                if ev["saveble"]:
                    i=0
                    j=0
                    random.shuffle(cells)
                    # # logging ( "%s %s" % (ev["name"],types) )
                    while (i<ev["max_times_happens"]):
                        cells[j].saveble_events.append(event(ev))
                        i+=1
                        j+=1
                        if j>= len(cells):
                            j=0
                else:
                    for c in cells:
                        c.repetable_events_names.append(ev["name"])


    def how_many_cells_on_map():
        st= "На карте:\n"
        fields=[]
        count=[]
        for line in map_by_types:
            for fld in line:
                if fld in fields:
                    count [fields.index(fld)]+=1
                else:
                    count.append(1)
                    fields.append(fld)
        for i in range (len(fields)):
            st+=("клеток типа %s: %d \n" % ( fields[i], count[i]))
        return st

    def some_pythonIDE_debug():
        while (1):
            print ("введи имя клетки например a1")
            x=input()
            x= "map_%s" % x
            cl = search(map_cells_ls, x)
            if cl!="":
                print("Найдена клетка %s" % cl)
            else:
                print("Не найдена клетка %s" % cl)
            while (1):
                print ("1 старт ивент\n2 выбрать другую клетку\n3 выбрать ивент")
                y=input()
                if y == '1':
                    cl.start_event()
                elif y=='2':
                    break
                elif y=='3':
                    while (1):
                        if cl.unfinished_events!=[]:
                            print (cl.unfinished_events)

                            print ("введите имя ивента")

                            ev = int(input())
                            if ev in range (len(cl.unfinished_events)):
                                cl.start_unfinished(ev)
                                break
                            else:
                                print ("неверное имя")

                        else:
                            print ("незаконченных событий нет")
                            break
                else:
                    print ("Неверный ввод")

    # logging ("map and events")
