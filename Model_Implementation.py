import random

#Useful as there is an edge case when there is only 1 truck or 1 landfill
#Syntax for nested tuples does not work with only 1 tuple
x = int(input('Enter number of trucks : '))
y = int(input('Enter number of landfills : '))
print()

#Input format for trucks: ((waste_amount1, truck_capacity1), (waste_amount2, truck_capacity2), ...)
#Input format for landfills: ((landfill_name1, daily_quota1), (landfill_name2, daily_quota2), ...)

a = eval(input('Amount of dry waste and capacity of each truck : '))
b = eval(input('Name and daily quota of each landfill : '))
print()

if x == 1 :
  a = (a, )

if y == 1 :
  b = (b, )

#Trucks sorted according to their capacities
trucks_sorted = sorted(a, key = lambda x : x[1], reverse = True)

#Landfills sorted according to their daily quotas
landfills_sorted = sorted(b, key = lambda x : x[1], reverse = True)

#All items to be layed out and separated at the recycling plant
recycling_plant = []

#List of all items
items = [
    'cardboard', 'paper', 'newspaper', 'magazine', 'cardboard box', 'pizza box', 'notebook', 'printer paper', 'office paper', 'wrapping paper',
    'plastic bottle', 'water bottle', 'soda bottle', 'milk jug', 'detergent bottle', 'shampoo bottle', 'plastic container', 'plastic jar', 'plastic tub', 'plastic cup',
    'aluminum can', 'soda can', 'beer can', 'tin can', 'metal can', 'steel can', 'aluminum foil', 'metal lid', 'metal tray', 'metal container',
    'glass bottle', 'wine bottle', 'beer bottle', 'mason jar', 'glass jar', 'glass container', 'glass cup', 'glass vase', 'glass bowl', 'glass plate',
    'cardboard tube', 'paper bag', 'kraft paper', 'egg carton', 'cereal box', 'shipping box', 'paper envelope', 'paper plate', 'paper cup', 'recycling bin',
    'styrofoam', 'plastic bag', 'bubble wrap', 'ceramic mug', 'broken glass', 'dirty paper', 'greasy pizza box', 'used tissue', 'napkin', 'paper towel',
    'food waste', 'banana peel', 'apple core', 'eggshell', 'coffee grounds', 'food scraps', 'dirty container', 'contaminated plastic', 'wet paper', 'stained cardboard',
    'rubber band', 'plastic straw', 'plastic utensil', 'plastic wrap', 'plastic packaging', 'disposable glove', 'wire', 'broken electronics', 'cigarette butt', 'light bulb',
    'ceramic plate', 'porcelain cup', 'mirror', 'window glass', 'drinking glass', 'crystal', 'pyrex', 'ceramic tile', 'porcelain figurine', 'ceramic bowl',
    'medical waste', 'diaper', 'sanitary pad', 'cotton swab', 'makeup wipe', 'dirty rag', 'leather', 'fabric scrap', 'wax paper', 'plastic toy'
  ]


#List of recyclable items
recyclable = [
    'cardboard', 'paper', 'newspaper', 'magazine', 'cardboard box', 'pizza box', 'notebook', 'printer paper', 'office paper', 'wrapping paper',
    'plastic bottle', 'water bottle', 'soda bottle', 'milk jug', 'detergent bottle', 'shampoo bottle', 'plastic container', 'plastic jar', 'plastic tub', 'plastic cup',
    'aluminum can', 'soda can', 'beer can', 'tin can', 'metal can', 'steel can', 'aluminum foil', 'metal lid', 'metal tray', 'metal container',
    'glass bottle', 'wine bottle', 'beer bottle', 'mason jar', 'glass jar', 'glass container', 'glass cup', 'glass vase', 'glass bowl', 'glass plate',
    'cardboard tube', 'paper bag', 'kraft paper', 'egg carton', 'cereal box', 'shipping box', 'paper envelope', 'paper plate', 'paper cup', 'recycling bin'
  ]


#Items to be recycled after segregation
to_be_recycled = []

landfill = []

#List of non - recyclable
non_recyclable = []
for i in items :
  if i not in recyclable :
    non_recyclable.append(i)

#List of maximum capacities for optimal deposition
#For example you have a truck with a capacity of 40 and a landfill with a daily quota of 50,
#the truck should carry 40 waste there and vice versa if the capacity of the truck is 50
#and the daily quota is 40, we want the optimized space to be 40
optimized_space = []

#List of amounts of trash to be dumped
to_be_dumped = []

sum = 0

#Unpacking trucks and landfills
dry_waste, capacity = zip(*trucks_sorted)
name, daily_quota = zip(*landfills_sorted)

if len(a) == x :
    if len(b) == y :

        #Code for generating random items equal to the amount of trash for each truck
        for i in trucks_sorted :
            c = i[0]
            d = []
            e = []
            def summation(list) :           #Our own summation function to find the quantity of waste
              s = 0                                         #We needed to make it as using the sum function on an empty list gives the output as None
              for i in list :                             #Which is problematic as we're using it for comparison
                s = s + i                                   #because we need the sum of an empty list to output a 0
              return s
            while summation(d) != c :                    #Continues using the summation function until values sum to dry waste quantity
                if summation(d) < c :
                    d.append(random.randint(1, int(c)))   #Basically creates random quantities for an undecided item so that it equals to dry waste
                else :
                    d.pop()
            for i in range(len(d)) :
                e.append(items[random.randint(0, len(items) - 1)]) #Chooses a random item from the list of items
            f = tuple(zip(e, d))
            recycling_plant.append(f)       #Appends the name and quantity of waste into a list recycling_plant

        #Code for separating items into recyclable and non - recyclable (to be sent to landfills)
        for i in range(len(recycling_plant)) :
            part = []
            for j in range(len(recycling_plant[i])) :
                if recycling_plant[i][j][0] in recyclable :       #Main part that checks if the item is recyclable or not
                    to_be_recycled.append(recycling_plant[i][j])  #If recyclable, append to list to_be_recycled
                else :
                  part.append(recycling_plant[i][j])
            landfill.append(tuple(part))                          #If nonrecyclable gets appended to list landfill

        print('Items sent for recycling -', tuple(to_be_recycled))  #Print statement that prints the recycled waste
        print()

        #Calculating total waste going to landfills
        for i in landfill :
            for j in i :
              sum = sum + j[1]            #Finds the total amount of unrecyclable waste

        #First if - else statement is for deciding the correct number of iterations
        #because we need the correct amount of iterations for example if there are 4 trucks and 5 landfills,
        #we need 4 iterations
        if len(trucks_sorted) < len(landfills_sorted) :
            for i in range(len(trucks_sorted)) :
                if trucks_sorted[i][1] > landfills_sorted[i][1] :      #Checks which is larger: capacity of trucks or capacity of landfill
                    optimized_space.append(landfills_sorted[i][1])     #Accordingly adds that capacity to optimised_space
                    if optimized_space[i] <= sum :                     #Generally capacity less than total waste to be dumped
                        to_be_dumped.append(optimized_space[i])        #So capacity added to list to_be_dumped
                        sum = sum - optimized_space[i]                 #Total waste reduces as some is being sent to landfill in current truck
                    elif sum == 0 :
                        break                                          #As soon as no more waste, stop the optimisation
                    else :
                        to_be_dumped.append(sum)                      #If capacity for waste greater than total remaining waste then obviously can
                        sum = 0                                       #send to landfill. sets total waste to 0
                else :
                    optimized_space.append(trucks_sorted[i][1])       #REMAINING BLOCK OF CODE SAME JUST FOR DIFFERENT IF-ELSE CONDITIONS
                    if optimized_space[i] <= sum :
                        to_be_dumped.append(optimized_space[i])
                        sum = sum - optimized_space[i]
                    elif sum == 0 :
                        break
                    else :
                        to_be_dumped.append(sum)
                        sum = 0
        else :
            for i in range(len(landfills_sorted)) :
                if trucks_sorted[i][1] > landfills_sorted[i][1] :
                    optimized_space.append(landfills_sorted[i][1])
                    if optimized_space[i] <= sum :
                        to_be_dumped.append(optimized_space[i])
                        sum = sum - optimized_space[i]
                    elif sum == 0 :
                        break
                    else :
                        to_be_dumped.append(sum)
                        sum = 0
                else :
                    optimized_space.append(trucks_sorted[i][1])
                    if optimized_space[i] <= sum :
                        to_be_dumped.append(optimized_space[i])
                        sum = sum - optimized_space[i]
                    elif sum == 0 :
                        break
                    else :
                        to_be_dumped.append(sum)
                        sum = 0



        #Output format - (name, amount of waste, capacity of truck sent there)
        print('Concise info -', tuple(zip(name[:len(to_be_dumped)], to_be_dumped, capacity[:len(to_be_dumped)]))) #Splicing done as the length of to_be_dumped will always be the list with the smallest length
        print()                                                                                                                                                                                                       #this is because optimized_space is the backbone and its length is the same as the number of  iterations
        print('Detailed info -')                                                                                                                                                                          #for example if we have 3 trucks with optimized spaces 40, 50 and 60 and the amount of trash is 70
        print()                                                                                                                                                                                                        #then to_be_dumped is [40, 30] and there's no need to print the rest as there's no trash to be sent there
        for i in range(len(to_be_dumped)) :
            print('Name of landfill -', name[i])                        #Prints the information of waste distribution:
            print('Daily quota of landfill -', daily_quota[i])          #The landfill name, the quota of landfill and the capacity of truck
            print('Capacity of truck sent to landfill -', capacity[i])
            temp1 = []
            temp2 = []
            while summation(temp1) != to_be_dumped[i] :
                if summation(temp1) < to_be_dumped[i] :
                    temp1.append(random.randint(1, int(c)))            #Code that randomly generates non - recyclable items and their amounts, same as before
                else:
                    temp1.pop()
            for i in range(len(temp1)) :
                temp2.append(non_recyclable[random.randint(0, len(non_recyclable) - 1)])
            stuff = tuple(zip(temp2, temp1))
            print('Items sent to the landfill -', stuff)                #Displays the unrecyclable items in the form of a tuple
            print()
    else :
        print('Wrong number of landfills entered.')
else :
    print('Wrong number of trucks entered.')