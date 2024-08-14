import random
from Variables import Vars

class Skill:
    # class variables
    stat = {
        "slash":{
                    "atk": 0,
                    "cost": 0,
                    "lv": 1
                    },
        "smite":{
                    "atk": 0,
                    "stun": 0,
                    "cost": 0,
                    "lv": 3
                    }
        }
    
    # =============== other func ===============
    @classmethod
    # asjust skill stat
    def adjust(self):
        lv = Vars.skill
        
        for skill in self.stat.keys():
            if skill == "slash":
                self.stat[skill]["atk"] = 2 + lv[skill]
                self.stat[skill]["cost"] = 6
            elif skill == "smite":
                self.stat[skill]["atk"] = 2 + lv[skill]
                self.stat[skill]["stun"] = 1 + int(lv[skill]/10)
                self.stat[skill]["cost"] = 8
    
    # =============== func ===============
    @classmethod
    # show skill lore
    def lore(self, name, mode):
        pstat = Vars.stat
        plv = Vars.skill
        sstat = self.stat
        
        # combat lore
        if mode == "combat":
            if name == "slash":
                print("@{0:^58}@".format(f"< Slash >"))
                print("@{0:^58}@".format(f"Slash the enemy deeply."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"ATK: {pstat['damage']}+{sstat['slash']['atk']}   COST: {sstat['slash']['cost']}"))
            elif name == "smite":
                print("@{0:^58}@".format(f"< Smite >"))
                print("@{0:^58}@".format(f"Hit the head of enemy."))
                print("@{0:^58}@".format(f"Stun enemy for some turn."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"ATK: {sstat['smite']['atk']}   STUN: {sstat['smite']['stun']}   COST: {sstat['smite']['cost']}"))
        # skill tree lore
        elif mode == "skill_tree":
            if name == "slash":
                print("@{0:^58}@".format(f"< Slash >"))
                print("@{0:^58}@".format(f"Slash the enemy deeply."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"ATK: {pstat['damage']}+{sstat['slash']['atk']}   COST: {sstat['slash']['cost']}"))
                print("@{0:^58}@".format(f"LIMIT LV: {sstat['slash']['lv']}   LV: {plv['slash']}"))
            elif name == "smite":
                print("@{0:^58}@".format(f"< Smite >"))
                print("@{0:^58}@".format(f"Hit the head of enemy."))
                print("@{0:^58}@".format(f"Stun enemy for some turn."))
                print("@"+" "*58+"@")
                print("@{0:^58}@".format(f"ATK: {sstat['smite']['atk']}   STUN: {sstat['smite']['stun']}   COST: {sstat['smite']['cost']}"))
                print("@{0:^58}@".format(f"LIMIT LV: {sstat['smite']['lv']}   LV: {plv['smite']}"))
    
    @classmethod
    # cast skill
    def cast(self, name):
        if name == "slash":
            # slash
            ran1 = random.randint(70, 100)
            ran2 = random.randint(70, 100)
            damage = int(ran1*((self.stat["slash"]["atk"]+Vars.stat["damage"])/100))
            reduction = int(ran2*(Vars.enemy.stat["defense"]/100))
            reduction = int(damage*(reduction/100))
            result = damage - reduction
            Vars.enemy.stat["health"] -= result
            if Vars.stat["health"] < 0:
                Vars.stat["health"] = 0
            
            print("@{0:^58}@".format(f"I slashed {Vars.enemy.name} deeply!"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"* {result} damage ({damage} - {reduction})"))
        elif name == "smite":
            # smite
            ran1 = random.randint(70, 100)
            ran2 = random.randint(70, 100)
            damage = int(ran1*self.stat["smite"]["atk"]/100)
            reduction = int(ran2*(Vars.enemy.stat["defense"]/100))
            reduction = int(damage*(reduction/100))
            result = damage - reduction
            Vars.enemy.stat["health"] -= result
            if Vars.stat["health"] < 0:
                Vars.stat["health"] = 0
            
            stun = self.stat["smite"]["stun"]
            Vars.enemy.status["stun"] = stun
            
            print("@{0:^58}@".format(f"I hit hard head of {Vars.enemy.name}!"))
            print("@"+" "*58+"@")
            print("@{0:^58}@".format(f"* {result} damage ({damage} - {reduction})"))
            print("@{0:^58}@".format(f"* {stun} turn stun"))
        
        if Vars.enemy.stat["health"] < 0:
                Vars.enemy.stat["health"] = 0