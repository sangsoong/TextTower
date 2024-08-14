import os
import time
import random

from Variables import Vars
import Loottable
from Skills import Skill
from Enemies import Enemy
from Shop import ShopItem
from Asciis import Picture

class Main:
    filename = ""
    file = 0
    
    # ============== system ================
    # clear text as os
    @classmethod
    def clt(self):
        print("\n"*100)
    
    # get input
    @classmethod
    def get(self):
        get = input("Enter 》")
        if get == "debug":
            self.debug()
        return get
    
    # debug
    @classmethod
    def debug(self):
        Vars.stat["action"] = 0
        Vars.stat["damage"] = 1000
    
    # initialize
    @classmethod
    def initialize(self):
        for key in Vars.stat.keys():
            Vars.stat[key] = 0
        
        for key in Vars.armory.keys():
            Vars.armory[key] = Vars("NONE", 1)
        
        Vars.backpack.clear()
    
    # level up and adjust max exp
    @classmethod
    def update_level(self):
        while Vars.stat["exp"] >= Vars.stat["maxexp"]:
            # exp
            Vars.stat["exp"] -= Vars.stat["maxexp"]
            Vars.stat["level"] += 1
            Vars.stat["maxexp"] += 4 + Vars.stat["level"]
            Vars.stat["skill"] += 1
            Vars.update_stat()
            
            self.clt()
            Picture.levelup()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"My level increased to {Vars.stat['level']}!"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
    
    # update
    @classmethod
    def update(self):
        self.update_level()
        Vars.update_stat()
        Skill.adjust()
    
    # ============== main screen ================
    # main
    @classmethod
    def start(self):
        repeat = True
            
        while repeat:
            self.clt()
            Picture.main()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[new]"+" "*5+"[load]"))
            print("@{0:^58}@".format("[help]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
        
            if choice == "new":
                self.new()
            elif choice == "load":
                self.load()
            elif choice == "help":
                self.help()
            elif choice == "exit":
                repeat = self.exit()
        
        self.clt()
    
    # new game
    @classmethod
    def new(self):
        while True:
            self.clt()
            Picture.main()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Enter name of new data."))
            print("@{0:^58}@".format("The name must be alphabetical."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            name = self.get()
                
            if name == "cancel":
                break
            elif os.path.exists(f"saves/{name}.txt"):
                self.clt()
                Picture.main()
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("Enter name of new data."))
                print("@{0:^58}@".format("The name must be alphabetical."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Name '{name}' is already exists."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                choice = self.get()
                continue
            else:
                cont = False
                for ch in name:
                    if not((65 <= ord(ch) and ord(ch) <= 90) or (97 <= ord(ch) and ord(ch) <= 122)):
                        self.clt()
                        Picture.main()
                        print("@"+" "*58+"@")
                        print("@{0:^58}@".format("Enter name of new data."))
                        print("@{0:^58}@".format("The name must be alphabetical."))
                        print("@"+" "*58+"@")
                        print("@{0:^58}@".format(f"Name '{name}' is not alphabetical."))
                        print("@"+" "*58+"@")
                        print("@{0:^58}@".format("[CHECK]"))
                        print("@"+" "*58+"@")
                        print("@"+"="*58+"@")
                        print()
                        choice = self.get()
                        cont = True
                        break
                if cont == True:
                    continue
            
            while True:
                self.clt()
                Picture.main()
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"'{name}', you sure?"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                choice = self.get()
                
                if choice == "accept":
                    # start setting
                    self.filename = name
                    file = open(f"saves/{name}.txt", "w")
                    
                    Vars.stat["maxhealth"] = 20
                    Vars.stat["health"] = 20
                    Vars.stat["damage"] = 0
                    Vars.stat["defense"] = 0
                    Vars.stat["level"] = 1
                    Vars.stat["maxexp"] = 10
                    Vars.stat["exp"] = 0
                    Vars.stat["action"] = 0
                    Vars.stat["weaponp"] = 0
                    Vars.stat["skill"] = 0
                    
                    Vars.armory[0] = Vars("NONE", 1)
                    Vars.armory[1] = Vars("leather breathplate", 1)
                    Vars.armory[2] = Vars("leather cuisse", 1)
                    Vars.armory[3] = Vars("leather boots", 1)
                    Vars.armory[4] = Vars("bronze longsword", 1)
                    Vars.armory[5] = Vars("NONE", 1)
                    
                    Vars.skill["slash"] = 1
                    
                    Vars.backpack.append(Vars("bread", 3))
                    
                    # save file
                    file.write("[stat]\n")
                    for i in range(0, len(Vars.stat)):
                        keys = list(Vars.stat.keys())
                        file.write(f"{i}, {Vars.stat[keys[i]]}\n")
                    
                    file.write("[armory]\n")
                    for i in range(0, len(Vars.armory)):
                        keys = list(Vars.armory.keys())
                        file.write(f"{i}, {Vars.armory[keys[i]].name}\n")
                    
                    file.write("[skill]\n")
                    for i in range(0, len(Vars.skill)):
                        keys = list(Vars.skill.keys())
                        file.write(f"{i}, {Vars.skill[keys[i]]}\n")
                    
                    file.write("[backpack]\n")
                    for item in Vars.backpack:
                        file.write(f"{item.name}, {item.count}\n")
                    
                    file.close()
                    self.update()
                    self.game_start()
                    return
                elif choice == "cancel":
                    break
    
    # load game
    @classmethod
    def load(self):
        while True:
            self.clt()
            Picture.main()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Enter name of the file."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            name = self.get()
            
            if name == "cancel":
                break
            else:
                if not(os.path.exists(f"saves/{name}.txt")):
                    self.clt()
                    Picture.main()
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("Enter name of the file."))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format(f"Name '{name}' doesn't exist."))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("[CHECK]"))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    self.get()
                else:
                    # load stats
                    self.filename = name
                    file = open(f"saves/{name}.txt", "r")
                    
                    data = file.readlines()
                    for i in range(0, len(data)):
                        data[i] = data[i].rstrip("\n").split(", ")
                    
                    mode = 0
                    for i in range(0, len(data)):
                        line = data[i]
                        
                        if line[0] == "[stat]":
                            mode = 0
                        elif line[0] == "[armory]":
                            mode = 1
                        elif line[0] == "[skill]":
                            mode = 2
                        elif line[0] == "[backpack]":
                            mode = 3
                        else:
                            if mode == 0:
                                keys = list(Vars.stat.keys())
                                key = keys[int(line[0])]
                                Vars.stat[key] = int(line[1])
                            elif mode == 1:
                                keys = list(Vars.armory.keys())
                                key = keys[int(line[0])]
                                Vars.armory[key] = Vars(line[1], 1)
                            elif mode == 2:
                                keys = list(Vars.skill.keys())
                                key = keys[int(line[0])]
                                Vars.skill[key] = int(line[1])
                            elif mode == 3:
                                Vars.backpack.append(Vars(line[0], int(line[1])))
                    
                    file.close()
                    self.update()
                    self.game_start()
                    break
    
    # help
    @classmethod
    def help(self):
        page = 1
        endpage = 3
        
        while True:
            self.clt()
            print("@"*60)
            print("@"+" "*58+"@")
            # maxline = 15
            if page == 1:
                print("@{0:^58}@".format("< Options >"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("This game is played by typing."))
                print("@{0:^58}@".format("Type same word in option."))
                print("@"+" "*58+"@")
                print("@  {0:<56}@".format("[option] - Type the same thing."))
                print("@  {0:<56}@".format("[blank option] - Type the same thing with blank."))
                print("@  {0:<56}@".format("[ENTER] - Type something freely."))
                print("@  {0:<56}@".format("[CHECK] - Type anything. Nothing will happen."))
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
            elif page == 2:
                print("@{0:^58}@".format("< Save and Load >"))
                print("@"+" "*58+"@")
                print("@  {0:<56}@".format("You can save by using bonfire in the campsite."))
                print("@  {0:<56}@".format("If you quit the game without save,"))
                print("@  {0:<56}@".format("the progress will be lost."))
                print("@  {0:<56}@".format("The file will be stored in 'saves' folder."))
                print("@"+" "*58+"@")
                print("@  {0:<56}@".format("You can load data from file."))
                print("@  {0:<56}@".format("You must type correct name of the file."))
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
            elif page == 3:
                print("@{0:^58}@".format("< Blank >"))
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"- {page} / {endpage} -"))
            print("@"+" "*58+"@")
            if page == 1:
                print("@{0:^58}@".format("[exit]"+" "*5+"[>]"))
            elif page == endpage:
                print("@{0:^58}@".format("[<]"+" "*5+"[exit]"))
            else:
                print("@{0:^58}@".format("[<]"+" "*5+"[exit]"+" "*5+"[>]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == ">" and page < endpage:
                page += 1
            elif choice == "<" and page > 1:
                page -= 1
            elif choice == "exit":
                break
    
    # exit
    @classmethod
    def exit(self):
        while True:
            self.clt()
            Picture.main()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Ends the game."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
        
            if choice == "accept":
                self.initialize()
                return False
            elif choice == "cancel":
                return True
    
    # ============== campsite ================
    
    @classmethod
    def game_start(self):
        for i in range(0, 4):
            self.clt()
            Picture.loading()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Loading"+" • "*i))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            print("Enter 》", end="")
            time.sleep(0.3)
        
        repeat = True
        
        while repeat:
            Vars.stat["health"] = Vars.stat["maxhealth"]
            Vars.stat["action"] =  10
            Vars.floor = 1
            
            self.clt()
            Picture.campsite()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("I feel at home."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[enter]"+" "*5+"[bonfire]" + " "*5 + "[shop]" + " "*5 + "[backpack]"))
            print("@{0:^58}@".format("[armory]"+" "*5+"[skill]" + " "*5 + "[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "enter":
                self.enter_tower()
            elif choice == "bonfire":
                self.bonfire()
            elif choice == "backpack":
                self.open_backpack()
            elif choice == "armory":
                self.open_armory()
            elif choice == "skill":
                self.skill_tree()
            elif choice == "shop":
                self.shop()
            elif choice == "exit":
                while True:
                    self.clt()
                    Picture.campsite()
                    Vars.stat_info("general")
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("Should I really leave?"))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    choice = self.get()
                    
                    if choice == "accept":
                        repeat = False
                        break
                    elif choice == "cancel":
                        break
    
    # bonfire
    @classmethod
    def bonfire(self):
        repeat = True
        
        while repeat:
            self.clt()
            Picture.bonfire()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("I can feel the warmth of the bonfire."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[save]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "save":
                repeat = self.save()
            elif choice == "exit":
                break
    
    @classmethod
    def save(self):
        # save data
        file = open(f"saves/{self.filename}.txt", "w")
        
        file.write("[stat]\n")
        for i in range(0, len(Vars.stat)):
            keys = list(Vars.stat.keys())
            file.write(f"{i}, {Vars.stat[keys[i]]}\n")
        
        file.write("[armory]\n")
        for i in range(0, len(Vars.armory)):
            keys = list(Vars.armory.keys())
            file.write(f"{i}, {Vars.armory[keys[i]].name}\n")
        
        file.write("[skill]\n")
        for i in range(0, len(Vars.skill)):
            keys = list(Vars.skill.keys())
            file.write(f"{i}, {Vars.skill[keys[i]]}\n")
        
        file.write("[backpack]\n")
        for item in Vars.backpack:
            file.write(f"{item.name}, {item.count}\n")
        
        file.close()
        
        self.clt()
        Picture.bonfire()
        Vars.stat_info("general")
        print("@"+" "*58+"@")
        print("@{0:^58}@".format("Saved successfully."))
        print("@"+" "*58+"@")
        print("@{0:^58}@".format("[CHECK]"))
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
        print()
        self.get()
    
    # enter tower
    @classmethod
    def enter_tower(self):
        while True:
            self.clt()
            Picture.tower_gate()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("It's the gate of the tower's garden."))
            print("@{0:^58}@".format("Should I go in?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "accept":
                self.in_tower()
                break
            elif choice == "cancel":
                break
    
    # backpack
    @classmethod
    def open_backpack(self):
        while True:
            self.update()
            
            self.clt()
            Vars.backpack_items()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[use]"+" "*5+"[discard]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "use":
                self.use_item()
            elif choice == "discard":
                self.discard_item()
            elif choice == "exit":
                break
    
    @classmethod
    def use_item(self):
        while True:
            self.update()
            
            self.clt()
            Vars.backpack_items()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Which item should I use?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "cancel":
                break
            else:
                for item in Vars.backpack:
                    if item.name == choice:
                        item.use()
                        break
    
    @classmethod
    def discard_item(self):
        while True:
            self.update()
            
            self.clt()
            Vars.backpack_items()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Which item should I discard?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "cancel":
                break
            else:
                for item in Vars.backpack:
                    if item.name == choice:
                        item.discard()
                        break
    
    # armory
    @classmethod
    def open_armory(self):
        while True:
            self.update()
            
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"<head> - {Vars.armory[0].name}"))
            print("@{0:^58}@".format(f"<top> - {Vars.armory[1].name}"))
            print("@{0:^58}@".format(f"<bottom> - {Vars.armory[2].name}"))
            print("@{0:^58}@".format(f"<boots> - {Vars.armory[3].name}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"<weapon> - {Vars.armory[4].name}"))
            print("@{0:^58}@".format(f"<accessory> - {Vars.armory[5].name}"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("armory")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[unequip]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "unequip":
                self.unequip_item()
            elif choice == "exit":
                break
    
    @classmethod
    def unequip_item(self):
        while True:
            self.update()
            
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"<head> - {Vars.armory[0].name}"))
            print("@{0:^58}@".format(f"<top> - {Vars.armory[1].name}"))
            print("@{0:^58}@".format(f"<bottom> - {Vars.armory[2].name}"))
            print("@{0:^58}@".format(f"<boots> - {Vars.armory[3].name}"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"<weapon> - {Vars.armory[4].name}"))
            print("@{0:^58}@".format(f"<accessory> - {Vars.armory[5].name}"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("armory")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Which part should I unequip?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "head":
                Vars.unequip(0)
            elif choice == "top":
                Vars.unequip(1)
            elif choice == "bottom":
                Vars.unequip(2)
            elif choice == "boots":
                Vars.unequip(3)
            elif choice == "weapon":
                Vars.unequip(4)
            elif choice == "accessory":
                Vars.unequip(5)
            elif choice == "cancel":
                break
    
    # open skill tree
    @classmethod
    def skill_tree(self):
        while True:
            self.update()
            
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            blank = 19
            i = 0
            for i in range(0, len(Skill.stat)):
                keys = list(Skill.stat.keys())
                name = keys[i]
                lv = Vars.skill[name]
                if i%2 == 0:
                    print("@  ", end="")
                    blank -= 1
                print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                if i%2 == 1:
                    print("  @")
            if i%2 == 0:
                print(" "*27+"  @")
            for i in range(0, blank):
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[lore]"+" "*5+"[learn]" + " "*5 + "[retrieve]"))
            print("@{0:^58}@".format("[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice in ("learn", "retrieve", "lore"):
                while True:
                    self.clt()
                    print("@"+"="*58+"@")
                    print("@"+" "*58+"@")
                    blank = 19
                    i = 0
                    for i in range(0, len(Skill.stat)):
                        keys = list(Skill.stat.keys())
                        name = keys[i]
                        lv = Vars.skill[name]
                        if i%2 == 0:
                            print("@  ", end="")
                            blank -= 1
                        print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                        if i%2 == 1:
                            print("  @")
                    if i%2 == 0:
                        print(" "*27+"  @")
                    for i in range(0, blank):
                        print("@"+" "*58+"@")
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    Vars.stat_info("general")
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("Which skill do I look up?"))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    name = self.get()
                    
                    if name == "cancel":
                        break
                    elif name in Skill.stat:
                        if choice == "learn":
                            self.learn(name)
                        elif choice == "retrieve":
                            self.retrieve(name)
                        elif choice == "lore":
                            self.lore(name)
                        break
            elif choice == "exit":
                break
    
    @classmethod
    def lore(self, skill):
        self.clt()
        print("@"+"="*58+"@")
        print("@"+" "*58+"@")
        blank = 19
        i = 0
        for i in range(0, len(Skill.stat)):
            keys = list(Skill.stat.keys())
            name = keys[i]
            lv = Vars.skill[name]
            if i%2 == 0:
                print("@  ", end="")
                blank -= 1
            print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
            if i%2 == 1:
                print("  @")
        if i%2 == 0:
            print(" "*27+"  @")
        for i in range(0, blank):
            print("@"+" "*58+"@")
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
        Vars.stat_info("general")
        print("@"+" "*58+"@")
        Skill.lore(skill, "skill_tree")
        print("@"+" "*58+"@")
        print("@{0:^58}@".format("[CHECK]"))
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
        print()
        self.get()
    
    @classmethod
    def learn(self, skill):
        if Vars.stat["skill"] < 1:
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            blank = 19
            i = 0
            for i in range(0, len(Skill.stat)):
                keys = list(Skill.stat.keys())
                name = keys[i]
                lv = Vars.skill[name]
                if i%2 == 0:
                    print("@  ", end="")
                    blank -= 1
                print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                if i%2 == 1:
                    print("  @")
            if i%2 == 0:
                print(" "*27+"  @")
            for i in range(0, blank):
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I don't have enough skill point."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
        elif Vars.stat["level"] < Skill.stat[skill]["lv"]:
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            blank = 19
            i = 0
            for i in range(0, len(Skill.stat)):
                keys = list(Skill.stat.keys())
                name = keys[i]
                lv = Vars.skill[name]
                if i%2 == 0:
                    print("@  ", end="")
                    blank -= 1
                print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                if i%2 == 1:
                    print("  @")
            if i%2 == 0:
                print(" "*27+"  @")
            for i in range(0, blank):
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"My level is low."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
        else:
            while True:
                self.clt()
                print("@"+"="*58+"@")
                print("@"+" "*58+"@")
                blank = 19
                i = 0
                for i in range(0, len(Skill.stat)):
                    keys = list(Skill.stat.keys())
                    name = keys[i]
                    lv = Vars.skill[name]
                    if i%2 == 0:
                        print("@  ", end="")
                        blank -= 1
                    print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                    if i%2 == 1:
                        print("  @")
                if i%2 == 0:
                    print(" "*27+"  @")
                for i in range(0, blank):
                    print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                Skill.lore(skill, "skill_tree")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Should I really learn this skill?"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                choice = self.get()
                
                if choice == "accept":
                    Vars.skill[skill] += 1
                    Vars.stat["skill"] -= 1
                    break
                elif choice == "cancel":
                    break
    
    @classmethod
    def retrieve(self, skill):
        if Vars.skill[skill] < 1:
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            blank = 19
            i = 0
            for i in range(0, len(Skill.stat)):
                keys = list(Skill.stat.keys())
                name = keys[i]
                lv = Vars.skill[name]
                if i%2 == 0:
                    print("@  ", end="")
                    blank -= 1
                print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                if i%2 == 1:
                    print("  @")
            if i%2 == 0:
                print(" "*27+"  @")
            for i in range(0, blank):
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I don't have this skill."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
        else:
            while True:
                self.clt()
                print("@"+"="*58+"@")
                print("@"+" "*58+"@")
                blank = 19
                i = 0
                for i in range(0, len(Skill.stat)):
                    keys = list(Skill.stat.keys())
                    name = keys[i]
                    lv = Vars.skill[name]
                    if i%2 == 0:
                        print("@  ", end="")
                        blank -= 1
                    print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                    if i%2 == 1:
                        print("  @")
                if i%2 == 0:
                    print(" "*27+"  @")
                for i in range(0, blank):
                    print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                Skill.lore(skill, "skill_tree")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Should I really retrieve this skill?"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                choice = self.get()
                
                if choice == "accept":
                    Vars.stat["skill"] += Vars.skill[skill]
                    Vars.skill[skill] = 0
                    break
                elif choice == "cancel":
                    break
    
    # shop
    @classmethod
    def shop(self):
        page = 1
        endpage = 3
        
        while True:
            self.clt()
            Picture.shop()
            ShopItem.show_items(page)
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("There are many items."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[buy]"+" "*5+"[sell]"+" "*5+"[backpack]"))
            if page == 1:
                print("@{0:^58}@".format("[exit]"+" "*5+"[>]"))
            elif page == endpage:
                print("@{0:^58}@".format("[<]"+" "*5+"[exit]"))
            else:
                print("@{0:^58}@".format("[<]"+" "*5+"[exit]"+" "*5+"[>]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == ">" and page < endpage:
                page += 1
            elif choice == "<" and page > 1:
                page -= 1
            elif choice == "exit":
                break
            elif choice == "backpack":
                self.open_backpack()
            elif choice == "buy":
                self.shop_buy(page)
            elif choice == "sell":
                self.shop_sell(page)
    
    @classmethod
    def shop_buy(self, page):
        while True:
            self.clt()
            Picture.shop()
            ShopItem.show_items(page)
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("What should I buy?"))
            money = 0
            for item in Vars.backpack:
                if item.name == "money":
                    money = item.count
                    break
            print("@{0:^58}@".format(f"I have {money} money."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
                    
            if choice == "cancel":
                break
            else:
                for item in ShopItem.items[page]:
                    if choice == item[0]:
                        ShopItem.buy(item, page)
                        break
    
    @classmethod
    def shop_sell(self, page):
        while True:
            self.clt()
            Vars.backpack_items()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("What should I sell?"))
            money = 0
            for item in Vars.backpack:
                if item.name == "money":
                    money = item.count
                    break
            print("@{0:^58}@".format(f"I have {money} money."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
                    
            if choice == "cancel":
                break
            else:
                for item in Vars.backpack:
                    if choice == item.name:
                        ShopItem.sell(item, page)
                        break
    
    # =============== in tower ===============
    
    @classmethod
    def in_tower(self):
        for i in range(0, 4):
            self.clt()
            Picture.enter()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Entering"+" • "*i))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            print("Enter 》", end="")
            time.sleep(0.5)
        
        restp = 2
        
        while True:
            Vars.enemy = Enemy("NONE")
            self.update()
            
            self.clt()
            Picture.in_tower(Vars.floor)
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"It's floor {Vars.floor}."))
            print("@"+" "*58+"@")
            if Vars.stat["action"] != 0 and restp > 0:
                print("@{0:^58}@".format("[explore(1ap)]"+" "*5+"[rest(1ap)]"))
            elif Vars.stat["action"] != 0 and restp == 0:
                print("@{0:^58}@".format("[explore(1ap)]"))
            elif Vars.stat["action"] == 0 or Vars.floor == len(Enemy.bosses):
                print("@{0:^58}@".format("[go forward]"+" "*5+"[go back]"))
            print("@{0:^58}@".format("[backpack]"+" "*5+"[armory]" + " "*5 + "[skill tree]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "backpack":
                self.open_backpack()
            elif choice == "armory":
                self.open_armory()
            elif choice == "skill tree":
                self.skill_tree()
            elif Vars.stat["action"] != 0:
                if choice == "explore":
                    self.explore()
                    if Vars.stat["health"] == 0:
                        # dead
                        break
                elif choice == "rest":
                    if restp > 0:
                        self.rest()
                        restp -= 1
            elif Vars.stat["action"] == 0:
                if choice == "go forward":
                    self.go_forward()
                    if Vars.stat["health"] == 0:
                        # dead
                        break
                    else:
                        # clear
                        restp = 2
                        Vars.stat["action"] = 10
                        Vars.floor += 1
                        endfloor = len(Enemy.bosses)
                        if Vars.floor == endfloor+1:
                            # clear event
                            self.clt()
                            Picture.in_tower(Vars.floor)
                            Vars.stat_info("general")
                            print("@"+" "*58+"@")
                            print("@{0:^58}@".format(f"Tower Exploration Clear!"))
                            print("@"+" "*58+"@")
                            print("@{0:^58}@".format("[CHECK]"))
                            print("@"+" "*58+"@")
                            print("@"+"="*58+"@")
                            print()
                            self.get()
                            break
                elif choice == "go back":
                    if self.go_back():
                        break
    
    # explore
    @classmethod
    def explore(self):
        for i in range(0, 4):
            self.clt()
            Picture.explore()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Exploring"+" • "*i))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            print("Enter 》", end="")
            time.sleep(0.5)
        
        event = random.randint(1, 10)
        if 1 <= event and event <= 6:
            self.event_fight()
        elif 6 <= event and event <= 10:
            self.event_treasure()
        
        Vars.stat["action"] -= 1
    
    @classmethod
    def event_fight(self):
        floor = Vars.floor
        endfloor = len(Enemy.bosses)
        action = Vars.stat["action"]
        
        if action != 0:
            species_cnt = len(Enemy.species[floor-1])
            enm = random.randint(0, species_cnt-1)
            Vars.enemy = Enemy(Enemy.species[floor-1][enm])
        else:
            if floor != endfloor:
                species_cnt = len(Enemy.bosses[floor-1])
                enm = random.randint(0, species_cnt-1)
                Vars.enemy = Enemy(Enemy.bosses[floor-1][enm])
            else:
                Vars.enemy = Enemy(Enemy.bosses[floor-1])
        
        Vars.turn = 0
        
        while True:
            self.update()
            
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"{Vars.enemy.name} blocked the road!"))
            print("@"+" "*58+"@")
            if Vars.turn == 0:
                print("@{0:^58}@".format("[roll]"+" "*5+"[end]"))
            elif Vars.turn == 1:
                print("@{0:^58}@".format("[attack]"+" "*5+"[skill]"+" "*5+"[end]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "end":
                while True:
                    self.clt()
                    Picture.enemy(Vars.enemy.name)
                    Vars.stat_info("combat")
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format(f"{Vars.enemy.name} blocked the road!"))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format(f"Should I really end my turn?"))
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    isend = self.get()
                    
                    if isend == "accept":
                        outcome = self.turn_enemy()
                        Vars.turn = 0
                        Vars.instantp = 0
                        if not(outcome):
                            return
                        break
                    elif isend == "cancel":
                        break
            
            if Vars.turn == 0:
                if choice == "roll":
                    self.roll()
            elif Vars.turn == 1:
                outcome = True
                if choice == "attack":
                    outcome = self.attack()
                elif choice == "skill":
                    outcome = self.skill()
                # end fight
                if not(outcome):
                    Vars.instantp = 0
                    break
    
    @classmethod
    def roll(self):
        reroll = False
        Vars.dice1 = random.randint(1, 6)
        Vars.dice2 = random.randint(1, 6)
        
        while True:
            if reroll:
                Vars.dice1 = random.randint(1, 6)
                Vars.dice2 = random.randint(1, 6)
            
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Dice1: {Vars.dice1}"))
            print("@{0:^58}@".format(f"Dice2: {Vars.dice2}"))
            print("@"+" "*58+"@")
            if not(reroll):
                print("@{0:^58}@".format("[accept]"+" "*5+"[reroll]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
            else:
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()
                break
            print()
            choice = self.get()
            
            if choice == "accept":
                break
            elif choice == "reroll":
                reroll = True
            
        Vars.instantp += Vars.dice1 + Vars.dice2
        Vars.turn += 1
    
    @classmethod
    def attack(self):
        while True:
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Should I use {Vars.stat['weaponp']} points to attack?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "accept":
                self.attack_enemy()
            elif choice == "cancel":
                break
            
            outcome = self.update_fight()
            if not(outcome):
                return False
        
        return True
    
    @classmethod
    def attack_enemy(self):
        if Vars.stat["weaponp"] <= Vars.instantp + Vars.storedp:
            if Vars.stat["weaponp"] <= Vars.instantp:
                Vars.instantp -= Vars.stat["weaponp"]
            else:
                Vars.storedp = Vars.storedp + Vars.instantp - Vars.stat["weaponp"]
                Vars.instantp = 0
            
            ran1 = random.randint(70, 100)
            ran2 = random.randint(70, 100)
            damage = int(ran1*(Vars.stat["damage"]/100))
            reduction = int(ran2*(Vars.enemy.stat["defense"]/100))
            reduction = int(damage*(reduction/100))
            result = damage - reduction
            Vars.enemy.stat["health"] -= result
            if Vars.enemy.stat["health"] < 0:
                Vars.enemy.stat["health"] = 0
            
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            Vars.attack_msg()
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"* {result} damage ({damage} - {reduction})"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
        else:
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I don't have that many points."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
    
    @classmethod
    def skill(self):
        while True:
            self.clt()
            print("@"+"="*58+"@")
            print("@"+" "*58+"@")
            blank = 15
            i = 0
            for i in range(0, len(Vars.skill)):
                keys = list(Vars.skill.keys())
                name = keys[i]
                lv = Vars.skill[name]
                if i%2 == 0:
                    print("@  ", end="")
                    blank -= 1
                if lv == 0:
                    print(" "*27, end="")
                else:
                    print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                if i%2 == 1:
                    print("  @")
            if len(Vars.skill) == 0:
                print("@  "+" "*27)
            if i%2 == 0:
                print(" "*27+"  @")
            for i in range(0, blank):
                print("@"+" "*58+"@")
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Which skill should I cast?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            skill = self.get()
            
            if skill == "cancel":
                return True
            elif skill in Vars.skill.keys():
                if Vars.skill[skill] != 0:
                    while True:
                        self.clt()
                        print("@"+"="*58+"@")
                        print("@"+" "*58+"@")
                        blank = 15
                        i = 0
                        for i in range(0, len(Vars.skill)):
                            keys = list(Vars.skill.keys())
                            name = keys[i]
                            lv = Vars.skill[name]
                            if i%2 == 0:
                                print("@  ", end="")
                                blank -= 1
                            if lv == 0:
                                print(" "*27)
                            else:
                                print("• {0:<25}".format(f"{name} - lv {lv}"), end="")
                            if i%2 == 1:
                                print("  @")
                        if len(Vars.skill) == 0:
                            print("@  "+" "*27)
                        if i%2 == 0:
                            print(" "*27+"  @")
                        for i in range(0, blank):
                            print("@"+" "*58+"@")
                        print("@"+" "*58+"@")
                        print("@"+"="*58+"@")
                        Vars.stat_info("combat")
                        print("@"+" "*58+"@")
                        Skill.lore(skill, "combat")
                        print("@"+" "*58+"@")
                        print("@{0:^58}@".format(f"Should I use {Skill.stat[skill]['cost']} points to cast this skill?"))
                        print("@"+" "*58+"@")
                        print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
                        print("@"+" "*58+"@")
                        print("@"+"="*58+"@")
                        print()
                        choice = self.get()
                        
                        if choice == "accept":
                            self.use_skill(skill)
                            break
                        elif choice == "cancel":
                            break
            
            outcome = self.update_fight()
            if not(outcome):
                return False
    
    @classmethod
    def use_skill(self, skill):
        if Skill.stat[skill]["cost"] <= Vars.instantp + Vars.storedp:
            if Skill.stat[skill]["cost"] <= Vars.instantp:
                Vars.instantp -= Skill.stat[skill]["cost"]
            else:
                Vars.storedp = Vars.storedp + Vars.instantp - Skill.stat[skill]["cost"]
                Vars.instantp = 0
            
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            Skill.cast(skill)
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
        else:
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I don't have that many points."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
    
    @classmethod
    def turn_enemy(self):
        # status
        if Vars.enemy.status["stun"] > 0:
            Vars.enemy.status["stun"] -= 1
            
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"{Vars.enemy.name} can't move!"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            return True
        
        # attack
        ran1 = random.randint(70, 100)
        ran2 = random.randint(70, 100)
        damage = int(ran1*(Vars.enemy.stat['damage']/100))
        reduction = int(ran2*(Vars.stat["defense"]/100))
        result = damage - reduction
        Vars.stat["health"] -= result
        if Vars.stat["health"] < 0:
            Vars.stat["health"] = 0
        
        self.clt()
        Picture.enemy(Vars.enemy.name)
        Vars.stat_info("combat")
        print("@"+" "*58+"@")
        print("@{0:^58}@".format(f"{Vars.enemy.name} attacked!"))
        print("@"+" "*58+"@")
        print("@{0:^58}@".format(f"* {result} damage ({damage} - {reduction})"))
        print("@"+" "*58+"@")
        print("@{0:^58}@".format("[CHECK]"))
        print("@"+" "*58+"@")
        print("@"+"="*58+"@")
        print()
        self.get()
        
        outcome = self.update_fight()
        if not(outcome):
            return False
        
        Vars.instantp = 0
        Vars.storedp += 1
        return True
    
    @classmethod
    def update_fight(self):
        if Vars.stat["health"] == 0:
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I lost the battle."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            return False
        elif Vars.enemy.stat["health"] == 0:
            self.clt()
            Picture.enemy(Vars.enemy.name)
            Vars.stat_info("combat")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"I won the battle!"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"+ {Vars.enemy.stat['exp']} exp"))
            loot_table = Vars.enemy.loot_table()
            Vars.add_item(Vars(loot_table[0], 1), loot_table[1])
            Vars.add_item(Vars("money", 1), loot_table[2])
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[CHECK]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            self.get()
            
            Vars.stat["exp"] += Vars.enemy.stat["exp"]
            self.update_level()
            return False
        else:
            return True
    
    @classmethod
    def event_treasure(self):
        case = random.randint(1, 3)
        
        if case == 1:
            self.event_treasure_chest()
        elif case == 2:
            self.event_treasure_puzzle()
        elif case == 3:
            self.event_treasure_sacrifice()
    
    @classmethod
    def event_treasure_chest(self):
        lock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        correct = random.randint(0, 9)
        chance = 3
        
        while True:
            lock_g = ""
            for num in lock:
                if num == -1:
                    lock_g += "X "
                else:
                    lock_g += "? "
            lock_g = lock_g.rstrip()
            
            self.clt()
            Picture.treasure("chest")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"There is a locked chest."))
            print("@{0:^58}@".format(f"Let's guess the correct number."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Chance: {chance}"))
            print("@{0:^58}@".format("0 1 2 3 4 5 6 7 8 9"))
            print("@{0:^58}@".format(lock_g))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            num = self.get()
            
            if num == "exit":
                break
            
            try:
                num = int(num)
                if num < 0 or num > 9:
                    continue
            except:
                continue
            
            chance -= 1
            
            if num < correct:
                for i in range(0, num+1):
                    lock[i] = -1
            elif num > correct:
                for i in range(num, 10):
                    lock[i] = -1
            elif num == correct:
                num += 1
                lock_g = lock_g[0:2*num-2] + "O" + lock_g[2*num-1:19]
                
                self.clt()
                Picture.treasure("chest")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("The chest has unlocked!"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Chance: {chance}"))
                print("@{0:^58}@".format("0 1 2 3 4 5 6 7 8 9"))
                print("@{0:^58}@".format(lock_g))
                print("@"+" "*58+"@")
                Loottable.loot_table(1, 1)
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()
                break
            
            if chance == 0:
                lock_g = ""
                for num in lock:
                    if num == -1:
                        lock_g += "X "
                    else:
                        lock_g += "? "
                lock_g = lock_g.rstrip()
                
                self.clt()
                Picture.treasure("chest")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("I failed to unlock the chest."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"Chance: {chance}"))
                print("@{0:^58}@".format("0 1 2 3 4 5 6 7 8 9"))
                print("@{0:^58}@".format(lock_g))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                print()
                self.get()
                break
    
    @classmethod
    def event_treasure_puzzle(self):
        power = [-1, -1, -1, -1]
        ranidx = [1, 2, 3, 4]
        random.shuffle(ranidx)
        
        while True:
            power_g = ""
            for p in power:
                if p == -1:
                    power_g += "OOO "
                elif p == 1:
                    power_g += "@@@ "
            power_g = power_g.rstrip()
            
            self.clt()
            Picture.treasure("puzzle")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"There is a puzzle."))
            print("@{0:^58}@".format(f"Let's turn it all on."))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("1   2   3   4"))
            print("@{0:^58}@".format(power_g))
            print("@{0:^58}@".format(power_g))
            print("@{0:^58}@".format(power_g))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[ENTER]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            num = self.get()
            
            if num == "exit":
                self.clt()
                Picture.treasure("puzzle")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"I failed to solve the puzzle."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("1   2   3   4"))
                print("@{0:^58}@".format(power_g))
                print("@{0:^58}@".format(power_g))
                print("@{0:^58}@".format(power_g))
                print("@"+" "*58+"@")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                self.get()
                break
            
            try:
                num = int(num)
                if num < 1 or num > 4:
                    continue
            except:
                continue
            
            if num == ranidx[0]:
                # 1, 3
                power[0] *= -1
                power[2] *= -1
            elif num == ranidx[1]:
                # 2, 3
                power[1] *= -1
                power[2] *= -1
            elif num == ranidx[2]:
                # 1, 4
                power[0] *= -1
                power[3] *= -1
            elif num == ranidx[3]:
                # 2, 3, 4
                power[1] *= -1
                power[2] *= -1
                power[3] *= -1
            
            if not(-1 in power):
                power_g = "@@@ @@@ @@@ @@@"
                
                self.clt()
                Picture.treasure("puzzle")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"The puzzle has been solved!"))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("1   2   3   4"))
                print("@{0:^58}@".format(power_g))
                print("@{0:^58}@".format(power_g))
                print("@{0:^58}@".format(power_g))
                print("@"+" "*58+"@")
                Loottable.loot_table(1, 1)
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                self.get()
                break
    
    @classmethod
    def event_treasure_sacrifice(self):
        health = Vars.stat["health"]
        amount = random.randint(int(health*(1/3)), int(health*(3/4)))
        grade = 1 + amount*0.05
        
        while True:
            self.clt()
            Picture.treasure("sacrifice")
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"There is an alter."))
            print("@{0:^58}@".format(f"Do I have to sacrifice health?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"• {amount} health"))
            print("@{0:^58}@".format(f"(Reward grade: {grade: .2f})"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[exit]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            choice = self.get()
            
            if choice == "accept":
                Vars.stat["health"] -= amount
                
                self.clt()
                Picture.treasure("sacrifice")
                Vars.stat_info("general")
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"I got some items."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"- {amount} health"))
                Loottable.loot_table(1.5, grade)
                print("@"+" "*58+"@")
                print("@{0:^58}@".format("[CHECK]"))
                print("@"+" "*58+"@")
                print("@"+"="*58+"@")
                self.get()
                break
            elif choice == "exit":
                break
    
    # rest
    @classmethod
    def rest(self):
        Vars.stat["action"] -= 1
        
        for i in range(0, 4):
            self.clt()
            Picture.rest()
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("Resting"+" • "*i))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            print("Enter 》", end="")
            
            hp_now = Vars.stat["health"]
            hp_max = Vars.stat["maxhealth"]
            hp_inc = int(hp_max * 3/16)
            if hp_now <= hp_max - hp_inc:
                Vars.stat["health"] += hp_inc
            else:
                Vars.stat["health"] = hp_max
            time.sleep(0.5)
    
    # go forward
    @classmethod
    def go_forward(self):
        while True:
            self.clt()
            Picture.in_tower(Vars.floor)
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Should I really go forward and"))
            print("@{0:^58}@".format(f"fight with the boss?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "accept":
                for i in range(0, 4):
                    self.clt()
                    Picture.boss()
                    Vars.stat_info("general")
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format(f"Moving forward"+" • "*i))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    print("Enter 》", end="")
                    time.sleep(0.5)
                self.event_fight()
                break
            elif choice == "cancel":
                break
    
    # go back
    @classmethod
    def go_back(self):
        while True:
            self.clt()
            Picture.in_tower(Vars.floor)
            Vars.stat_info("general")
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"Should I really go back?"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format("[accept]"+" "*5+"[cancel]"))
            print("@"+" "*58+"@")
            print("@"+"="*58+"@")
            print()
            choice = self.get()
            
            if choice == "accept":
                for i in range(0, 4):
                    self.clt()
                    Picture.returning()
                    Vars.stat_info("general")
                    print("@"+" "*58+"@")
                    print("@{0:^58}@".format(f"Returning"+" • "*i))
                    print("@"+" "*58+"@")
                    print("@"+"="*58+"@")
                    print()
                    print("Enter 》", end="")
                    time.sleep(0.5)
                return True
            elif choice == "cancel":
                return False