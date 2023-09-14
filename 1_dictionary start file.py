import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



#print()
#print('*****  start section 1 - print dictionary ********')
#print()


#print(phonebook)

#print(len(phonebook))

#phone=phonebook['Chris']

#print(phone)

# print()
# print('*****  end section 1 ********')
# print()


# #phonebook= {} 
# #creates an empty dictionary 

# #mydictionary = dict(m=8,n=9)
# #create a dictonary w dict function




# print()
# print('*****  start section 2 - search dictionary ********')
# print()


# name ='Chris'

# #phone = phonebook ['chris']
# #bad bc does not know lowercase c

# if name in phonebook:
#     phone = phonebook[name]
#     print(phone)
# else:
#     print(f'{name}not found in phonebook')


# print()
# print('*****  end section 2 ********')
# print()


'''

print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook ['Joe']= '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)

del phonebook['Chris']

print(phonebook)

#no append in dictionarys, just adds it if it cannot find key value pair
print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook:  #dictionaries iterate through keys by default
    #print(k)
    print(f"the key is {k} and the value is {phonebook[k]}")

for v in phonebook.values():
    print(v)
    #iterates through all values in dictionary

for phone_tuple in phonebook.items()
    print(phone_tuple)

for k,v in phonebook.items()
    print(f"the key is :{k} and the value is: {v}")
    #give them seperate objects 


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('katie', '911')
#default value (911) tells you its wrong

print(phone)

phonebook.clear()
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone = phonebook.pop("Katie", "911")
#pop takes it out of the dictionary, it pops out of the dictionary 
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#suposed to pop out a random key pair from dictionary and 

print(phonebook)
phone = phonebook.popitem()
#actually just puts out last item in the dictonary, not useful 
print(phone)
print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook)
# when you make a list of dictionary it makes a list of the KEYS of dictionary (so thier names)
print(phonebook_list)
random_key = random.choice(phonebook_list)
print(random_key)
print(phonebook[random_key])
'''

print(phonebook[random.choice(list(phonebook))])



print()
print('*****  end section 9 ********')
print()
