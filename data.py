import json
import csv



fieldnames = (
    "#","Name","Type 1","Type 2","Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation","Legendary",
    )

with open("./pokemon.csv",'r') as csvfile:
    with open('./poke.json','w') as jsonfile:
        next(csvfile)
        reader = csv.DictReader(csvfile, fieldnames)
        final_data = {}
        for row in reader:
            final_data[row["Name"].lower()] = {
                "Type": row["Type 1"],
                "Generation": row["Generation"],
                "Legendary": row["Legendary"],
                "Attack": row["Attack"],
                "Defense": row["Defense"],
                "Speed": row["Speed"]    
            }
        json.dump(final_data, jsonfile)
        jsonfile.write('\n')

