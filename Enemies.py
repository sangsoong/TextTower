import random

class Enemy:
    # class var
    species = [
        ["Wushroom", "Rat"], # f1: forest
        ["Bat", "Slime"], # f2: dungeon
        ["Spike Fish", "Seafolks"], # f3: sewer
        ["Haunted Armors", "Haunted Weapons"], # f4: armor depot
        ["Corrupted Book", "Librarian"], # f5: library
        ["Believer", "Ascetic"], # f6: ritual area
        ["Lifeguard", "Court Wizard"] # f7: top of towet
        ]
    
    bosses = [
        ["Tumbler", "Giant Rat"], # f1
        ["Skeleton Knight", "The Undead"], # f2
        ["Decaying Lump", "Mossy Golem"], # f3
        ["Headless Knight"], # f4
        ["Clerk"], # f5
        ["Chief Priest", "Summoned Thing"], # f6
        "Past Emperor" # f7
        ]
    
    # instance var
    name = ""
    stat = {"maxhealth":0,
        "health":0,
        "damage":0,
        "defense":0,
        "exp":0}
    
    status = {
        "stun": 0
    }
    
    # =============== mobs ===============
    def __init__(self, name):
        self.name = name
        
        if name == "Wushroom":
            self.stat = {"maxhealth":15,
                "health":15,
                "damage":6,
                "defense":20,
                "exp":5}
        elif name == "Rat":
            self.stat = {"maxhealth":10,
                "health":10,
                "damage":8,
                "defense":20,
                "exp":5}
        elif name == "Tumbler":
            self.stat = {"maxhealth":30,
                "health":30,
                "damage":9,
                "defense":50,
                "exp":50}
        elif name == "Giant Rat":
            self.stat = {"maxhealth":25,
                "health":25,
                "damage":12,
                "defense":25,
                "exp":50}
        elif name == "Bat":
            self.stat = {"maxhealth":9,
                "health":9,
                "damage":15,
                "defense":10,
                "exp":10}
        elif name == "Slime":
            self.stat = {"maxhealth":15,
                "health":15,
                "damage":8,
                "defense":30,
                "exp":10}
        elif name == "Skeleton Knight":
            self.stat = {"maxhealth":40,
                "health":40,
                "damage":15,
                "defense":40,
                "exp":80}
        elif name == "The Undead":
            self.stat = {"maxhealth":45,
                "health":45,
                "damage":12,
                "defense":30,
                "exp":80}
        elif name == "Spike Fish":
            self.stat = {"maxhealth":15,
                "health":15,
                "damage":18,
                "defense":20,
                "exp":15}
        elif name == "Seafolks":
            self.stat = {"maxhealth":20,
                "health":20,
                "damage":14,
                "defense":30,
                "exp":15}
        elif name == "Decaying Lump":
            self.stat = {"maxhealth":60,
                "health":60,
                "damage":15,
                "defense":40,
                "exp":120}
        elif name == "Mossy Golem":
            self.stat = {"maxhealth":50,
                "health":50,
                "damage":20,
                "defense":50,
                "exp":120}
        elif name == "Haunted Armors":
            self.stat = {"maxhealth":30,
                "health":30,
                "damage":15,
                "defense":30,
                "exp":20}
        elif name == "Haunted Weapons":
            self.stat = {"maxhealth":25,
                "health":25,
                "damage":20,
                "defense":10,
                "exp":20}
        elif name == "Headless Knight":
            self.stat = {"maxhealth":60,
                "health":60,
                "damage":30,
                "defense":40,
                "exp":170}
        elif name == "Corrupted Book":
            self.stat = {"maxhealth":25,
                "health":25,
                "damage":30,
                "defense":20,
                "exp":25}
        elif name == "Librarian":
            self.stat = {"maxhealth":30,
                "health":30,
                "damage":25,
                "defense":30,
                "exp":25}
        elif name == "Clerk":
            self.stat = {"maxhealth":80,
                "health":80,
                "damage":30,
                "defense":20,
                "exp":200}
        elif name == "Believer":
            self.stat = {"maxhealth":35,
                "health":35,
                "damage":30,
                "defense":20,
                "exp":30}
        elif name == "Ascetic":
            self.stat = {"maxhealth":50,
                "health":50,
                "damage":20,
                "defense":50,
                "exp":30}
        elif name == "Chief Priest":
            self.stat = {"maxhealth":80,
                "health":80,
                "damage":30,
                "defense":20,
                "exp":250}
        elif name == "Summoned Thing":
            self.stat = {"maxhealth":100,
                "health":100,
                "damage":35,
                "defense":30,
                "exp":250}
        elif name == "Lifeguard":
            self.stat = {"maxhealth":60,
                "health":60,
                "damage":35,
                "defense":40,
                "exp":50}
        elif name == "Court Wizard":
            self.stat = {"maxhealth":40,
                "health":40,
                "damage":45,
                "defense":30,
                "exp":50}
        elif name == "Past Emperor":
            self.stat = {"maxhealth":200,
                "health":200,
                "damage":50,
                "defense":70,
                "exp":500}
    
    # =============== func ===============
    def loot_table(self):
        n = self.name
        chance = random.randint(1, 10)
        item = ""
        amount = 0
        money = 0
        
        if n == "Wushroom":
            item = "wushroom piece"
            if 1 <= chance and chance <= 3:
                amount = random.randint(1, 1)
            elif 4 <= chance and chance <= 10:
                amount = random.randint(2, 4)
            money = 10
        elif n == "Rat":
            item = "rat tail"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 1)
            money = 10
        elif n == "Tumbler":
            item = "log fragment"
            if 1 <= chance and chance <= 6:
                amount = random.randint(1, 2)
            elif 7 <= chance and chance <= 10:
                amount = random.randint(3, 4)
            money = 50
        elif n == "Giant Rat":
            item = "big rat foot"
            if 1 <= chance and chance <= 5:
                amount = random.randint(1, 2)
            elif 6 <= chance and chance <= 10:
                amount = random.randint(3, 4)
            money = 50
        elif n == "Bat":
            item = "bat wing"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 2)
            money = 15
        elif n == "Slime":
            item = "mucus"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 15
        elif n == "Skeleton Knight":
            item = "thick bone"
            if 1 <= chance and chance <= 6:
                amount = random.randint(1, 2)
            elif 7 <= chance and chance <= 9:
                amount = random.randint(3, 5)
            elif 10 <= chance and chance <= 10:
                amount = random.randint(6, 8)
            money = 100
        elif n == "The Undead":
            item = "corrupted meat"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 100
        elif n == "Spike Fish":
            item = "spike"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 20
        elif n == "Seafolks":
            item = "rusty scrap"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 20
        elif n == "Decaying Lump":
            item = "filth"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 150
        elif n == "Mossy Golem":
            item = "golem core"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 2)
            money = 150
        elif n == "Haunted Armors":
            item = "broken armor"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 25
        elif n == "Haunted Weapons":
            item = "broken weapon"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 25
        elif n == "Headless Knight":
            item = "dark core"
            if 1 <= chance and chance <= 8:
                amount = random.randint(1, 1)
            elif 9 <= chance and chance <= 10:
                amount = random.randint(2, 2)
            money = 200
        elif n == "Corrupted Book":
            item = "paper"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 30
        elif n == "Librarian":
            item = "burnt book"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 30
        elif n == "Clerk":
            item = "broken clock"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 1)
            money = 250
        elif n == "Believer":
            item = "torn hood"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 35
        elif n == "Ascetic":
            item = "shakle"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 35
        elif n == "Chief Priest":
            item = "priest's book"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 300
        elif n == "Summoned Thing":
            item = "something"
            if 1 <= chance and chance <= 7:
                amount = random.randint(1, 2)
            elif 8 <= chance and chance <= 10:
                amount = random.randint(3, 5)
            money = 300
        elif n == "Lifeguard":
            item = "seal"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 1)
            money = 50
        elif n == "Court Wizard":
            item = "medal"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 1)
            money = 50
        elif n == "Past Emperor":
            item = "crown"
            if 1 <= chance and chance <= 10:
                amount = random.randint(1, 1)
            money = 500
        
        print("@{0:^58}@".format(f"+ {item} × {amount}"))
        print("@{0:^58}@".format(f"+ money × {money}"))
        
        return [item, amount, money]