name = "Devin"
Subject = "Treehouse loves {}".format(name)

""" Methods for changing lists """

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.append(11)
print(my_list)

my_list = [1,2,3]
my_list.extend([4,5,6])
print(my_list)

my_list.remove(5)
print(my_list)

list('hello')
print(list)

""" Turning a list() into a String """
flavors = ['chocolate', 'mint','strawberry']
print(','.join(flavors))

print("My favorite flavors are: {}".format(", ".join(flavors)))


""" This is how you split() items """
available = "banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(';')
print(sundaes)

alpha = 'abcde'
print(alpha.index('a'))
print('abcde'.index('a'))
print(alpha.index('cd'))

""" This is how you find the index """
""" Turns the string alpha into the list alpha_list """
alpha_list = list(alpha)
print(alpha_list)
print(alpha_list.index('b'))

print(alpha[0])
print(alpha_list[2])

print(alpha)

"""Deleting from a list """
trash = 99
del trash
alpha_list = list('abcde')
del alpha_list[2]
print(alpha_list)

"""
Deleting from a String:
1.) Turn the string into a list
2.) delete from the list
3.) turn the list back into a String
"""
letters = "abcdefg"
letters_list = list(letters)
print(letters_list)
del(letters_list[6])
print(letters_list)
newletters = (' '.join(letters_list))
print(newletters)



""" Splitting String into a list, that seperates by the ";"
format a string to connect to the sundaes variable once it has been joined
as a string. """
available = "banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(';')
menu = "Our available flavors are: {}.".format(", ".join(sundaes))
print(menu)

""" Using "in" with an "if" statement to search for the item in list,
then prints a statement based on the results """
days_open = ['monday', 'tuesday', 'wednesday', 'thursday']
today = 'tuesday'
if today in days_open:
    print("Come on in!")
else:
    print("Sorry, we're closed")

""" Most python developers prefer the method of "not in" """
if today not in days_open:
    print("sorry we're closed")





""" breaks out of loop if "name == 'QUIT'" """
names = ['Ken', 'Amy', 'Devin', 'QUIT', 'Mark']
for name in names:
    if name == 'QUIT':
        break
    print(name)


""" skipping an element in a for loop """
for name in names:
    if name == "QUIT":
        continue
    print(name)






""" converting user input string into integer """
age = int(input("What's your age? "))



""" FUNCTIONS() """

def hows_the_parrot():
    print("He's pining for the fjords")


hows_the_parrot()


""" FUNCTION TAKING AN ARGUMENT """

def lumberjack(name, action):
    if name.lower() =='god':
        print("Leave God out of this")
    else:
        print("{} {} all day!".format(name, action))


""" calling a function while passing user input as the argument """

lumberjack(input("What is the name? "), input("What do they do? "))
    

""" ?????????????????? """






""" EXCEPTIONS """

""" CATCHING ERROR CODES FOR USERS """

try:
    count = int(input("Give me a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("nuuuuuumber....", count, "!")



 

""" PYTHON COLLECTIONS """
a_list = [1, 2, 3]
a_list.append([4,5])
print(a_list)










      
