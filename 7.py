#DICTIONARIES IN PYTHON

karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}

print(karnataka_food["Mysuru"])  # Output: Mysore Pak

#Accessing Dictionary Elements
print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found

#Adding and Updating Dictionary Elements
karnataka_food["Shivamogga"] = "Kadubu"
print(karnataka_food)

karnataka_food["Bengaluru"] = "Ragi Mudde"
print(karnataka_food)

# Removing Elements from a Dictionary
mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak

del karnataka_food["Mangaluru"]

#karnataka_food.clear()

#Dictionary Methods
print(karnataka_food.keys())  # Output: dict_keys(['Bengaluru', 'Mysuru', 'Mangaluru'])
print(karnataka_food.values())  # Output: dict_values(['Bisi Bele Bath', 'Mysore Pak', 'Neer Dosa'])
print(karnataka_food.items())  # Output: dict_items([('Bengaluru', 'Bisi Bele Bath'), ('Mysuru', 'Mysore Pak'), ('Mangaluru', 'Neer Dosa')])
new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)
print(karnataka_food)  # Output: {'Bengaluru': 'Bisi Bele Bath', 'Mysuru': 'Mysore Pak', 'Mangaluru': 'Neer Dosa', 'Hubballi': 'Girmit'}    


#HOMEWORK

fruits={
    "fruit1":"apple",
    "fruit2":"banana",
    "fruit3":"orange"
}
print(fruits)
fruits["fruit4"]="grapes"
fruits["fruit1"]="mango"
fruits.pop("fruit1")
print(fruits.keys())
print(fruits.values())

details={
    "freind1":{
        "Name":"Adi",
        "Age":21,
        "City":"Vijaypura"
    },
    "freind2":{
        "Name":"Teju",
        "Age":20,
        "City":"Bengaluru"
    }
}
print(details)
print(details.get("freind2").get("City"))
print(details["freind1"][ "City"])