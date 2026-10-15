import json
go_go = "yes"
while go_go == "yes":

    try:
        star_level = int(input("what level is the charater you want to level up?"))
        with open(f"level_{star_level}_character.json", "r") as file:
            level = int(input("how many level?, num"))
            data = json.load(file)
            data["level"] = data["level"] + 1*level
            data["armor_class"] = data["armor_class"] + 1*level
            for n in range(level):
                attribute = input("what attribute to increase?")
                data["attributes"][attribute] = data["attributes"][attribute] + 1
                skills = input("what skill to add?")
                data["skills"].append(skills)
                go = input("you what to add a weapon y/n ")
                if go == "y":
                    weapon = input("add what weapon?")
                    data["weapons"].append(weapon)
            with open(f"level_{data['level']}_character.json", "w") as file:
                json.dump(data, file, indent=4)
            print("invalid input")
            go_go = "no"
    except FileNotFoundError:
        try:
            go1= input("that character doesn't exist, do you want to create one? y/n")
            if go1 == "y":
                level = int(input("what level is the charater you want to make?")) -1
                with open(f"level_1_character.json", "r") as file:
                    data = json.load(file)
                    data["level"] = data["level"] + 1 * level
                    data["armor_class"] = data["armor_class"] + 1 * level
                    for n in range(level):
                        attribute = input("what attribute to increase?")
                        data["attributes"][attribute] = data["attributes"][attribute] + 1
                        skills = input("what skill to add?")
                        data["skills"].append(skills)
                        go = input("you what to add a weapon y/n ")
                        if go == "y":
                            weapon = input("add what weapon? ")
                            data["weapons"].append(weapon)
                with open(f"level_{data['level']}_character.json", "w") as file:
                    json.dump(data, file, indent=4)
                go_go = "no"
        except (ValueError, NameError, KeyError):
            print("invalid input")

    except (ValueError, NameError, KeyError):
        print("invalid input")
