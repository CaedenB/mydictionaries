"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons. This
information can be found in the ValueLabels file.

this is a list of dictonaries and each dictonary is a different univeristy

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"

"""  
import json
infile = open('school_data.json','r')

schools = json.load(infile)
#makes it a python object - makes it a list of dictonaries 
# if it was a json dictonary, would be a python dictonary 

conference_schools= [372, 108, 107,130]
#codes for conference schools from above 

print(len(schools))
#counts number of items in list, tells us how many schools in list 

for school in schools:
    code = school['NCAA']['NAIA conference number football (IC2020)']
    if code in conference_schools:
        grad_rate =school["Graduation rate  women (DRVGR2020)"]
        if grad_rate >=75:
            print(school["instnm"])
            print(grad_rate)


    

  


"""""
Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000




for school in schools:
    grad_rate= (school["Graduation rate  women (DRVGR2020)"])
    if grad_rate >= 75:
        print(f'University: {school["instnm"]}')
        print(f'Graduation Rate for Women: {grad_rate}')

"""