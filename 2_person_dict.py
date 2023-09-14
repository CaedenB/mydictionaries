person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child

print(person["children"][1])
children=person['children']

print(type(children))


# print out the name of the cat
pets = person['pets']

print(type(pets))
#dictionary

print(pets['cat']) #cat is the key of the pets dictionary 

cat_name = person['pets'] ['cat']
print(cat_name)


# use a loop to print out the names of each child

for child in person['children']:
    print(child)
    #this is a list
    #child represents each item in the list

# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for k,v in person['pets'].items():
    #this is a dictonary so k represents the key and v represents the object
    print(f"The type of pet is: {k} and the name of the pet is: {v}")
        