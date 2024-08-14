import random

from Variables import Vars

def loot_table(ratio, grade):
    rewards = []
    floor = Vars.floor
        
    if floor == 1:
        money_a = random.randint(2, 10)
        money_b = random.randint(5, 10)
        rewards.append(["money", money_a*money_b])
        for i in range(0, 7):
            chance = int(random.randint(1, 100)*(1-((grade-1)/10)))
            amount = random.randint(1, 100)
            if i == 0 and 1 <= chance and chance <= 50:
                if 1 <= amount and amount <= 70:
                    rewards.append(["fabric", 2])
                elif 71 <= amount and amount <= 90:
                    rewards.append(["fabric", 3])
                elif 91 <= amount and amount <= 100:
                    rewards.append(["fabric", 4])
            if i == 1 and 1 <= chance and chance <= 50:
                if 1 <= amount and amount <= 70:
                    rewards.append(["short thread", 2])
                elif 71 <= amount and amount <= 90:
                    rewards.append(["short thread", 3])
                elif 91 <= amount and amount <= 100:
                    rewards.append(["short thread", 4])
            if i == 2 and 1 <= chance and chance <= 30:
                if 1 <= amount and amount <= 70:
                    rewards.append(["normal thread", 2])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["normal thread", 3])
            if i == 3 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 70:
                    rewards.append(["long thread", 1])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["long thread", 2])
            if i == 4 and  chance and chance <= 30:
                if 1 <= amount and amount <= 70:
                    rewards.append(["leather piece", 2])
                if 71 <= amount and amount <= 100:
                    rewards.append(["leather piece", 3])
            if i == 5 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 80:
                    rewards.append(["intact leather", 1])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["intact leather", 2])
            if i == 6 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 80:
                    rewards.append(["bronze scrap", 1])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["bronze scrap", 2])
    elif floor == 2:
        money_a = random.randint(5, 10)
        money_b = random.randint(10, 15)
        rewards.append(["money", money_a*money_b])
        for i in range(0, 12):
            chance = int(random.randint(1, 100)*(1-((grade-1/10))))
            amount = random.randint(1, 100)
            if i == 0 and 1 <= chance and chance <= 35:
                if 1 <= amount and amount <= 70:
                    rewards.append(["fabric", 3])
                elif 71 <= amount and amount <= 90:
                    rewards.append(["fabric", 4])
                elif 91 <= amount and amount <= 100:
                    rewards.append(["fabric", 5])
            if i == 1 and 1 <= chance and chance <= 35:
                if 1 <= amount and amount <= 70:
                    rewards.append(["short thread", 3])
                elif 71 <= amount and amount <= 90:
                    rewards.append(["short thread", 4])
                elif 91 <= amount and amount <= 100:
                    rewards.append(["short thread", 5])
            if i == 2 and 1 <= chance and chance <= 20:
                if 1 <= amount and amount <= 70:
                    rewards.append(["normal thread", 3])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["normal thread", 4])
            if i == 3 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 70:
                    rewards.append(["long thread", 2])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["long thread", 3])
            if i == 4 and 1 <= chance and chance <= 20:
                if 1 <= amount and amount <= 80:
                    rewards.append(["leather piece", 3])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["leather piece", 4])
            if i == 5 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 80:
                    rewards.append(["intact leather", 2])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["intact leather", 3])
            if i == 6 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 80:
                    rewards.append(["bronze scrap", 2])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["bronze scrap", 3])
            if i == 7 and 1 <= chance and chance <= 5:
                if 1 <= amount and amount <= 70:
                    rewards.append(["bronze ingot", 1])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["bronze ingot", 2])
            if i == 8 and 1 <= chance and chance <= 10:
                if 1 <= amount and amount <= 70:
                    rewards.append(["steel scrap", 1])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["steel scrap", 2])
            if i == 9 and 1 <= chance and chance <= 5:
                if 1 <= amount and amount <= 80:
                    rewards.append(["steel ingot", 1])
                elif 81 <= amount and amount <= 100:
                    rewards.append(["steel ingot", 2])
            if i == 10 and 1 <= chance and chance <= 5:
                if 1 <= amount and amount <= 70:
                    rewards.append(["cast iron scrap", 1])
                elif 71 <= amount and amount <= 100:
                    rewards.append(["cast iron scrap", 2])
            if i == 11 and 1 <= chance and chance <= 2:
                if 1 <= amount and amount <= 90:
                    rewards.append(["cast iron ingot", 1])
                elif 91 <= amount and amount <= 100:
                    rewards.append(["cast iron ingot", 2])
    elif floor == 3:
        pass
    elif floor == 4:
        pass
    elif floor == 5:
        pass
    elif floor == 6:
        pass
        
    for item in rewards:
        amount = int(amount*ratio)
        if item[1] > 0:
            Vars.add_item(Vars(item[0], 1), item[1])
            print("@{0:^58}@".format(f"+ {item[0]} × {item[1]}"))