init python:
    # army_list = [{
    # "name": "test_army_poor_1",
    # "units": ["test_unit2"],
    # "units_with_teg": ["human"],
    # "exclude_units": [],
    # "rarity": "poor",
    # "amount": 1
    # },{
    # "name": "test_army_magic_3",
    # "units": ["test_unit2"],
    # "units_with_teg": ["human"],
    # "exclude_units": [],
    # "rarity": "magic",
    # "amount": 3
    # }]

    def generate_army ( parameters):
        units = []
        new_army = Army(parameters["name"])
        availible_units=[]
        for u in units_list:
            if ( (u["teg"] in parameters["units_with_teg"]
                or u["name"] in parameters["units"])
                and u["name"] not in parameters["exclude_units"]
                and rarity.index(u["rarity"]) <= rarity.index(parameters["rarity"])):
                availible_units.append(u)

        persent = float(currency.day+currency.reputation) / float(currency.maxday+currency.maxrep)
        rar_ind = rarity.index (parameters["rarity"])
        units={}
        amount = parameters["amount"]
        mult = 2
        for f in range (rar_ind,-1,-1):
            ls=[]
            for au in availible_units:
                if au["rarity"]==rarity[f]:
                    ls.append(au)
            quant=0
            if (f==rar_ind):
                quant = int (max (round (amount*persent*mult),round(amount)) )
            else:
                quant = int (round (amount*persent*mult) )
            # logging ("%s: quant = %d, amount = %d, persent = %f, mult = %d "% (rarity[f], quant, amount, persent, mult) )
            mult*=2
            if len(ls)>0:
                for i in range (quant):
                    new_army.add_unit( Unit (random.choice(ls) ) )
                    if len(new_army.units)>=20:
                        return new_army
        return new_army

    def test_army_gen():
        saveday = currency.day
        saverep = currency.reputation
        while (currency.day<=currency.maxday):
            # logging ("\nday %d"% currency.day )
            for ar in army_test:
                army=generate_army(ar)
                st="%s "%army.name
                for u in army.units:
                    st+="%s : %s, " % (u.name, u.rarity)
                # logging (st)
            currency.day+=10
            currency.reputation+=10
        currency.day = saveday
        currency.reputation = saverep
    #generate_army(army_test)

#legendary (3) with 1000 rep and maxday = 4.5-6 legendary + 9-12 rare + 18-24 magic
#legendary (3) with 0 rep and 0 day = 3 legendary amount* random (1.5 ,2)
#legendary 1,  1-1.5 amount*((1.5 ,2))
#rare   0-0.5,   amount*((1.5 ,2)) 4
#magic  0-0.5,   amount*((1.5 ,2)) 8
#normal 0-0.5,   amount*((1.5 ,2)) 16
#poor   0-0.5,   amount*((1.5 ,2)) * 32
#rare (3)

#legendary 1 with 0 rep and 0 day = 3 legendary
#legendary 1-2,
#rare   = round (amount*persent*4)
#magic  0-8
#normal 0-16
#poor   0-32
# persent = day+rep / maxday+maxrep










#reputation 0 - 1000 + #day 0 - maxday
#army rarity
#army multiple

#quant (0 - 20)
#rarity (0-4)
#lvl
#weapon upgrades
