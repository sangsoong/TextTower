from Enemies import Enemy
from Asciis import Picture

class Vars:
    # class var
    stat = {
        "maxhealth":0,
        "health":0,
        "damage":0,
        "defense":0,
        "level":0,
        "maxexp":0,
        "exp":0,
        "action":0,
        "weaponp":0,
        "skill":0
        }
    
    armory = {
        0:0, # head
        1:0, # top
        2:0, # bottom
        3:0, # boots
        4:0, # weapon
        5:0  # accessory
        }
    
    skill = {
        "slash": 0,
        "smite": 0,
        "parry": 0
        }
    
    backpack = []
    maxitem = 15
    
    floor = 0
    
    enemy = Enemy("NONE")
    instantp = 0
    storedp = 0
    
    # instance var
    name = ""
    count = 0
    
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
    
    # =============== other func ===============
    # update status
    @classmethod
    def update_stat(self):
        head = self.armory[0].name
        top = self.armory[1].name
        bot = self.armory[2].name
        boots = self.armory[3].name
        weapon = self.armory[4].name
        acc = self.armory[5].name
        self.stat["defense"] = 0
        sum_def = 0
        self.stat["damage"] = 0
        sum_dmg = 0
        
        # health by level
        level = self.stat["level"]
        self.stat["maxhealth"] = 18 + 2*level
        
        if self.stat["health"] > self.stat["maxhealth"]:
            self.stat["health"] = self.stat["maxhealth"]
        
        # headgear
        if head == "leather helmet":
            sum_def += 1
        elif head == "bronze helmet":
            sum_def += 2
        elif head == "steel helmet":
            sum_def += 3
        elif head == "cast iron helmet":
            sum_def += 4
        
        # top
        if top == "leather breathplate":
            sum_def += 1
        elif top == "bronze breathplate":
            sum_def += 2
        elif top == "steel breathplate":
            sum_def += 3
        elif top == "cast iron breathplate":
            sum_def += 4
        
        # bottom
        if bot == "leather cuisse":
            sum_def += 1
        elif bot == "bronze cuisse":
            sum_def += 2
        elif bot == "steel cuisse":
            dum_def += 3
        elif bot == "cast iron cuisse":
            dum_def += 4
        
        # boots
        if boots == "leather boots":
            sum_def += 1
        elif boots == "bronze boots":
            sum_def += 2
        elif boots == "steel boots":
            sum_def += 3
        elif boots == "cast iron boots":
            sum_def += 4
        
        # weapon
        if weapon == "NONE":
            sum_dmg += 1
            self.stat["weaponp"] = 2
        # bronze
        elif weapon == "bronze longsword":
            sum_dmg += 5
            self.stat["weaponp"] = 5
        elif weapon == "bronze dagger":
            sum_dmg += 2
            self.stat["weaponp"] = 2
        elif weapon == "bronze scimitar":
            sum_dmg += 4
            self.stat["weaponp"] = 4
        elif weapon == "bronze rapier":
            sum_dmg += 3
            self.stat["weaponp"] = 3
        # steel
        elif weapon == "steel longsword":
            sum_dmg += 7
            self.stat["weaponp"] = 5
        elif weapon == "steel dagger":
            sum_dmg += 4
            self.stat["weaponp"] = 2
        elif weapon == "steel scimitar":
            sum_dmg += 6
            self.stat["weaponp"] = 4
        elif weapon == "steel rapier":
            sum_dmg += 5
            self.stat["weaponp"] = 3
        elif weapon == "steel hammer":
            sum_dmg += 9
            self.stat["weaponp"] = 6
        elif weapon == "steel sickle":
            sum_dmg += 7
            self.stat["weaponp"] = 4
        # cast iron
        elif weapon == "cast iron broadsword":
            sum_dmg += 8
            sum_def += 1
            self.stat["weaponp"] = 5
        elif weapon == "cast iron hammer":
            sum_dmg += 11
            self.stat["weaponp"] = 7
        # gold
        elif weapon == "gold katar":
            sum_dmg += 7
            self.stat["weaponp"] = 3
        
        # accessory
        if acc == "scabbard":
            sum_dmg += 2
        elif acc == "leather gauntlet":
            sum_def += 2
        elif acc == "steel gauntlet":
            sum_def += 4
        elif acc == "bronze ring":
            sum_dmg = int(sum_dmg*(110/100))
        elif acc == "silver ring":
            sum_dmg = int(sum_dmg*(115/100))
        elif acc == "gold ring":
            sum_dmg = int(sum_dmg*(120/100))
        elif acc == "diamond ring":
            sum_dmg = int(sum_dmg*(125/100))
        
        self.stat["defense"] = sum_def
        self.stat["damage"] = sum_dmg
    
    # print items
    @classmethod
    def backpack_items(self):
        Picture.backpack()
        print("@"+" "*58+"@")
        i = 0
        for i in range(0, len(self.backpack)):
            item = self.backpack[i]
            name = item.name
            count = item.count
            if i%2 == 0:
                print("@  ", end="")
            print("• {0:<25}".format(f"{name} × {count}"), end="")
            if i%2 == 1:
                print("  @")
        if i%2 == 0 and len(self.backpack) != 0:
            print(" "*27+"  @")
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
    
    # print status
    @classmethod
    def stat_info(self, mode):
        if mode == "general":
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"HP: {self.stat['health']} / {self.stat['maxhealth']}   AP: {self.stat['action']}   SP: {self.stat['skill']}   LV: {self.stat['level']}   EXP: {self.stat['exp']} / {self.stat['maxexp']}"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
        elif mode == "armory":
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"HP: {self.stat['health']} / {self.stat['maxhealth']}   ATK: {int(self.stat['damage']*0.7)}~{self.stat['damage']}   DFS: {int(self.stat['defense']*0.7)}~{self.stat['defense']}   ATP: {self.stat['weaponp']}"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
        elif mode == "combat":
            print("@"+" "*58+"@")
            print("@{0:<29}".format("  < You >") + "{0:>29}@".format(f"< {self.enemy.name} >  "))
            print("@{0:<21}".format(f"  HP: {self.stat['health']} / {self.stat['maxhealth']}")+ "{0:^16}".format("< Combat Point >") + "{0:>21}@".format(f"HP: {self.enemy.stat['maxhealth']} / {self.enemy.stat['health']}  "))
            print("@{0:<14}".format(f"  ATK: {int(self.stat['damage']*0.7)}~{self.stat['damage']}") + "{0:^30}".format(f"Instant Point: {self.instantp}") + "{0:>14}@".format(f"ATK: {int(self.enemy.stat['damage']*0.7)}~{self.enemy.stat['damage']}  "))
            print("@{0:<14}".format(f"  DFS: {int(self.stat['defense']*0.7)}~{self.stat['defense']}") + "{0:^30}".format(f"Stored Point: {self.storedp}") + "{0:>14}@".format(f"DFS: {int(self.enemy.stat['defense']*0.7)}%~{self.enemy.stat['defense']}%  "))
            status = []
            for state, turn in self.enemy.status.items():
                if turn > 0:
                    status.append(state)
            status_s = str(status).strip("[").strip("]")
            print("@{0:>58}@".format(f"STATUS: {status_s}  "))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
    
    # print attack message
    @classmethod
    def attack_msg(self):
        weapon = self.armory[4].name
        
        if weapon == "NONE":
            print("@{0:^58}@".format(f"I hit the {self.enemy.name} with my fist!"))
        elif weapon in ("bronze longsword", "steel longsword"):
            print("@{0:^58}@".format(f"I cut down the {self.enemy.name}!"))
        elif weapon in ("bronze dagget", "steel dagger"):
            print("@{0:^58}@".format(f"I stabbed the {self.enemy.name}!"))
        elif weapon in ("bronze scimitar", "steel scimitar"):
            print("@{0:^58}@".format(f"I sharply cut the {self.enemy.name}!"))
        elif weapon in ("bronze rapier", "steel rapier"):
            print("@{0:^58}@".format(f"I quickly stabbed the {self.enemy.name}!"))
        elif weapon in ("steel hammer", "cast iron hammer"):
            print("@{0:^58}@".format(f"I smashed the {self.enemy.name}!"))
        elif weapon in ("steel sickle"):
            print("@{0:^58}@".format(f"I deftly slashed the {self.enemy.name}!"))
        elif weapon in ("cast iron broadsword"):
            print("@{0:^58}@".format(f"I slashed the {self.enemy.name}!"))
        elif weapon in ("gold katar"):
            print("@{0:^58}@".format(f"I quickly stabbed the {self.enemy.name}!"))
    
    # =============== items ===============
    '''  helmet:
            leather helmet, bronze helmet,
            steel helmet, cast iron helmet
        breathplate:
            leather breathplate, bronze breathplate,
            steel breathplate, cast iron breathplate
        cuisee:
            leather cuisse, bronze cuisse,
            steel cuisse, cast iron breathplate
        boots:
            leather boots, bronze boots,
            steel boots, cast iron boots
        weapon:
            bronze longsword, bronze dagger,
            bronze scimitar, bronze rapier,
            steel longsword, steel dagger,
            steel scimitar, steel rapier,
            steel hammer, steel sickle,
            cast iron broadsword, cast iron hammer,
            gold katar
        accessory:
            scabbard,
            leather gauntlet, steel gauntlet,
            bronze ring, silver ring, gold ring, diamond ring
        consumable item:
            bread, healing potion, vigor potion
        loot item:
            money,
            wushroom piece, rat tail, log fragment, big rat foot,
            bat wing, mucus, thick bone, corrupted meat,
            spike, rusty scrap, filth, golem core,
            broken armor, broken weapon, dark core,
            paper, burnt book, broken clock,
            torn hood, shakle, priest's book, something,
            seal, medal, crown
        ingredients:
            short thread, normal thread, long thread,
            fabric, leather piece, intact leather,
            bronze scrap, bronze ingot,
            steel scrap, steel ingot,
            cast iron scrap, cast iron ingot
    '''
    
    # constructor
    def __init__(self, name, count):
        self.name = name
        self.count = count
    
    # add item to backpack
    @classmethod
    def add_item(self, item, amount):
        if item.name != "NONE":
            for i in range(0, len(self.backpack)):
                if self.backpack[i].name == item.name:
                    self.backpack[i].count += amount
                    return
            item.count = amount
            self.backpack.append(item)
    
    # remove item from backpack
    @classmethod
    def remove_item(self, item, amount):
        ritem = 0
        for bitem in self.backpack:
            if bitem.name == item.name:
                ritem = bitem
        
        if ritem.count > amount:
            ritem.count -= amount
        elif ritem.count == amount:
            self.backpack.remove(ritem)
    
    # use item
    def use(self):
        # items that can not be used
        if self.name in ("money", "wushroom piece", "rat tail", "log fragment", "rat foot", "bat wing", "mucus", "thick bone", "corrupted meat", "spike", "rusty scrap", "filth", "golem core", "broken armor", "broken weapon", "dark core", "paper", "burnt book", "broken clock", "torn hood", "shakle", "priest's book", "something", "seal", "medal", "crown", "short thread", "normal thread", "long thread", "fabric", "leather piece", "intact leather", "bronze scrap", "bronze ingot", "steel scrap", "steel ingot", "cast iron scrap", "cast iron ingot"):
            self.clt()
            self.backpack_items()
            self.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("It can't be used."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            return
        # armory
        elif self.name in ("leather helmet", "bronze helmet", "steel helmet", "cast iron helmet", "leather breathplate", "bronze breathplate", "steel breathplate", "cast iron breathplate", "leather cuisse", "bronze cuisse", "steel cuisse", "cast iron cuisse", "leather boots", "bronze boots", "steel boots", "cast iron boots","bronze longsword", "bronze dagger", "bronze scimitar", "bronze rapier", "steel longsword", "steel dagger", "steel scimitar", "steel rapier", "steel hammer", "steel sickle", "cast iron broadsword", "cast iron hammer", "gold katar", "scabbard", "leather gauntlet", "steel gauntlet", "bronze ring", "silver ring", "gold ring", "diamond ring"):
            self.item_func(self, "use", 1)
        # items that can be used many times
        else:
            while True:
                self.clt()
                self.backpack_items()
                self.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Use: {self.name}"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("How much?"))
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
                    if amount < 1 or amount > self.count:
                        continue
                except:
                    continue
                
                self.item_func(self, "use", amount)
                break
    
    # discard item
    def discard(self):
        while True:
            self.clt()
            self.backpack_items()
            self.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Discard: {self.name} × {self.count}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("How much?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER COUNT]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            amount = self.get()
            
            if amount == "cancel":
                break
            
            try:
                amount = int(amount)
                if amount < 1 or amount > self.count:
                    continue
            except:
                continue
            
            while True:
                self.clt()
                self.backpack_items()
                self.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Discard: {self.name} × {amount}"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("Should I really throw it away?"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                choice = self.get()
                    
                if choice == "accept":
                    self.remove_item(self, amount)
                    return
                elif choice == "cancel":
                    break
    
    # unequip item
    @classmethod
    def unequip(self, part):
        if self.armory[part].name != "NONE":
            self.add_item(self.armory[part], 1)
            self.armory[part] = Vars("NONE", 1)
            self.update_stat()
    
    @classmethod
    def item_func(self, item, way, amount):
        n = item.name
        
        if way == "use":
            # armor
            if n in ("leather helmet", "bronze helmet", "steel helmet", "cast iron helmet"):
                self.add_item(self.armory[0], 1)
                self.armory[0] = item
                self.remove_item(item, 1)
            elif n in ("leather breathplate", "bronze breathplate", "steel breathplate", "cast iron breathplate"):
                self.add_item(self.armory[1], 1)
                self.armory[1] = item
                self.remove_item(item, 1)
            elif n in ("leather cuisse", "bronze cuisse", "steel cuisse", "cast iron cuisse"):
                self.add_item(self.armory[2], 1)
                self.armory[2] = item
                self.remove_item(item, 1)
            elif n in ("leather boots", "bronze boots", "steel boots", "cast iron boots"):
                self.add_item(self.armory[3], 1)
                self.armory[3] = item
                self.remove_item(item, 1)
            # weapon
            elif n in ("bronze longsword", "bronze dagger", "bronze scimitar", "bronze rapier", "steel longsword", "steel dagger", "steel scimitar", "steel rapier", "steel hammer", "steel sickle", "cast iron broadsword", "cast iron hammer", "gold katar"):
                self.add_item(self.armory[4], 1)
                self.armory[4] = item
                self.remove_item(item, 1)
            # accessory
            elif n in ("scabbard", "leather gauntlet", "steel gauntlet", "bronze ring", "silver ring", "gold ring", "diamond ring"):
                self.add_item(self.armory[5], 1)
                self.armory[5] = item
                self.remove_item(item, 1)
            # consumable
            elif n == "bread":
                self.stat["health"] += 5*amount
                self.update_stat()
                self.remove_item(item, amount)
                
                self.clt()
                self.backpack_items()
                self.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"{5*amount} HP has recovered."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()
            elif n == "healing potion":
                self.stat["health"] += 10*amount
                self.update_stat()
                self.remove_item(item, amount)
                
                self.clt()
                self.backpack_items()
                self.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"{10*amount} HP has recovered."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()
            elif n == "vigor potion":
                self.storedp += 5*amount
                self.update_stat()
                self.remove_item(item, amount)
                
                self.clt()
                self.backpack_items()
                self.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"{5*amount} stored combat point has increased."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()