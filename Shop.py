from Variables import Vars
from Asciis import Picture

class ShopItem:
    # class var
    items = {
        # consumable items
        1: [["bread", 100], ["healing potion", 200], ["vigor potion", 300]],
        # weapons
        2: [["bronze longsword", 300], ["bronze dagger", 400], ["bronze scimitar", 500], ["bronze rapier", 600]],
        # armors
        3: [["leather helmet", 400], ["leather breathplate", 600], ["leather cuisse", 500], ["leather boots", 400]]
    }
    
    selling_items = {
        "wushroom piece": 7,
        "rat tail": 15,
        "log fragment": 45,
        "big rat foot": 50,
        "bat wing": 20,
        "mucus": 20,
        "thick bone": 80,
        "night core": 300
    }
    
    # =============== system ===============
    # clear text
    @classmethod
    def clt(self):
        print("\n"*100)
    
    # get input
    @classmethod
    def get(self):
        get = input("Enter 》")
        return get
    
    # =============== sub funcs ===============
    # show product list
    @classmethod
    def show_items(self, page):
        items = self.items[page]
        
        blank = 15
        i = 0
        print("@"+" "*58+"@")
        for i in range(0, len(items)):
            item = items[i]
            name = item[0]
            price = item[1]
            if i%2 == 0:
                print("@  ", end="")
                blank -= 1
            print("• {0:<25}".format(f"{name}: {price}°"), end="")
            if i%2 == 1:
                print("  @")
        if i%2 == 0 and len(items) != 0:
            print(" "*27+"  @")
        for i in range(0, blank):
            print("@"+" "*58+"@")
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
    
    # =============== main funcs ===============
    # buy
    @classmethod
    def buy(self, item, page):
        money = 0
        for bitem in Vars.backpack:
            if bitem.name == "money":
                money = bitem.count
                break
        
        while True:
            self.clt()
            Picture.shop()
            self.show_items(page)
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Buy: {item[0]}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("How much?"))
            print("@{0:^58}@".format(f"I have {money} money."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            amount = self.get()
            
            if amount == "cancel":
                break
            
            cost = 0
            try:
                amount = int(amount)
                cost = item[1]*amount
                if amount < 1 or money < cost:
                    continue
            except:
                continue
            
            Vars.remove_item(Vars("money", 1), cost)
            Vars.add_item(Vars(item[0], 1), amount)
            
            self.clt()
            Picture.shop()
            self.show_items(page)
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I bought {item[0]} × {amount}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"- {cost} money"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            break
    
    # sell
    @classmethod
    def sell(self, item, page):
        if not(item.name in list(self.selling_items.keys())):
            return
        
        money = 0
        for bitem in Vars.backpack:
            if bitem.name == "money":
                money = bitem.count
                break
        
        price = 0
        for sitem, sprice in self.selling_items.items():
            if sitem == item.name:
                price = sprice
                break
        
        while True:
            self.clt()
            Picture.shop()
            Vars.backpack_items()
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Sell: {item.name}"))
            print("@{0:^58}@".format(f"Price: {price}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("How much?"))
            print("@{0:^58}@".format(f"I have {money} money."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            amount = self.get()
            
            if amount == "cancel":
                break
            
            try:
                amount = int(amount)
                if amount < 1 or item.count < amount:
                    continue
            except:
                continue
            
            result = price*amount
            
            Vars.remove_item(Vars(item.name, 1), amount)
            Vars.add_item(Vars("money", 1), result)
            
            self.clt()
            Picture.shop()
            self.show_items(page)
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I sold {item.name} × {amount}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"+ {result} money"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            break