import json
with open("level_1_character.json", "r") as file:
    data = json.load(file)
    data["level"] = data["level"] + 1
    data["armor_class"] = data["armor_class"] + 1
    data["attributes"]["strength"] = data["attributes"]["strength"] + 2
    data["attributes"]["constitution"] = data["attributes"]["constitution"] + 1
    data["skills"].append("Survival")
    data["weapons"].append("Silver Dagger")
    
    print(data)
