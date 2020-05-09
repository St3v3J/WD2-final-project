# Solution by Raphael Assa, SmartNinja instructor from Belgium

# first we need to put our given data into a suitable data-structure
# in this case we use dictionaries to map human properties to their respective dna-sequence
hair = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
face = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eyes = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

# map each person to a list of properties describing the person at hand...
# mind that the order of properties in the list is important
people = {"eva" : ["female", "white", "blonde", "blue", "oval"],
          "larisa" : ["female", "white", "brown", "brown", "oval"],
          "matej" : ["male", "white", "black", "blue", "oval"],
          "miha" : ["male", "white", "brown", "green", "square"]}

# read the dna file
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

person = []  # will represent our suspect...

#  now we check properties in the same order
for i in gender:  # check all genders, i.e. male & female
    #  now check the gender[i] is a substring of dna,
    #  i.e. does dna contain gender[i]...
    if gender[i] in dna:  # if the current gender is present in the dna
        print(i)
        person.append(i)  # add this property to our suspect
for i in race:  # check all races...
    if race[i] in dna:  # same idea as gender, only 1 race will match
        print(i)
        person.append(i)
for i in hair:
    if hair[i] in dna:
        print(i)
        person.append(i)
for i in eyes:
    if eyes[i] in dna:
        print(i)
        person.append(i)
for i in face:
    if face[i] in dna:
        print(i)
        person.append(i)

# now we have a description of our suspect,
# so now check who corresponds to this description...
for p in people:
    if people[p] == person:
        print("The person we're looking for is %s" % p.upper())
        break
    # Solution by Raphael Assa, SmartNinja instructor from Belgium

    # map each person to a list of DNA sequences describing the properties of the person at hand...
    # since everybody is white, we can technically leave "race" out
    # but for demonstration purposes we'll simply keep it...
people = {"eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

# read the dna file
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

# simply check if all properties of a person appear in the DNA string
# as soon as one of the person's properties doesn't appear in the DNA string,
# we know that this person is innocent...
# only the real perpetrator's will have all his/her properties in the DNA string
for person in people:
    suspect = True
    for prop in people[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect is True:
        print("{} is our perpetrator!".format(person.upper()))

#           smartninja course example
# characteristics = {
#     'hair': {
#         'black': 'CCAGCAATCGC',
#         'brown': 'GCCAGTGCCG',
#         'blonde': 'TTAGCTATCGC'
#     },
#     'face': {
#         'square': 'GCCACGG',
#         'round': 'ACCACAA',
#         'oval': 'AGGCCTCA'
#     },
#     'eyes': {
#         'blue': 'TTGTGGTGGC',
#         'green': 'GGGAGGTGGC',
#         'brown': 'AAGTAGTGAC'
#     },
#     'gender': {
#         'female': 'TGAAGGACCTTC',
#         'male': 'TGCAGGAACTTC'
#     },
#     'race': {
#         'white': 'AAAACCTCA',
#         'black': 'CGACTACAG',
#         'asian': 'CGCGGGCCG'
#     }
# }
#
# suspects = {
#     'Eva': {
#         'hair': 'blonde',
#         'face': 'oval',
#         'eyes': 'blue',
#         'gender': 'female',
#         'race': 'white'
#     },
#     'Larisa': {
#         'hair': 'brown',
#         'face': 'oval',
#         'eyes': 'brown',
#         'gender': 'female',
#         'race': 'white'
#     },
#     'Matej': {
#         'hair': 'black',
#         'face': 'oval',
#         'eyes': 'blue',
#         'gender': 'male',
#         'race': 'white'
#     },
#     'Miha': {
#         'hair': 'brown',
#         'face': 'square',
#         'eyes': 'green',
#         'gender': 'male',
#         'race': 'white'
#     }
# }
#
# # read the dna file
# with open("dna.txt", "r") as dna_file:
#     dna = dna_file.read()
#
# suspect = {}
#
# # iteritems() function will iterate through the characteristics data
# for key, value in characteristics.items():
#     for characteristic, sequence in value.items():
#         if dna.find(sequence) != -1:
#             suspect[key] = characteristic
#             break
#
# name = ''
#
# for n, value in suspects.items():
#     current_name = ''
#
#     for k, v in value.items():
#         if suspect[k] == v:
#             current_name = n
#         else:
#             current_name = ''
#             break
#
#     if current_name:
#         name = current_name
#         break
#
# print("The person who ate the ice cream is {0}.".format(name))

