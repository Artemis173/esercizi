
# Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# - Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
  # For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# - Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
  # The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence,
  # such as I really love pizza!

Pizzas = ["Focaccia e Crudo", "Margherita", "Diavola"]
print("Le mie pizze preferite sono: ")
for pizza in Pizzas:
    print(pizza)

print("\nLe mie pizze preferite sono: ")
for pizza in Pizzas:
    if pizza == "Focaccia e Crudo":
        print("Mi piace la FOcaccia con Crudo")

    elif pizza == "Margherita":
        print("Non posso mangiare la Margherita")

    else:
        print("Non posso mangiare la Diavola")
print("\nMi piaciono davvero poche pizze!")


# Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# - Modify your program to print a statement about each animal, such as A dog would make a great pet.
# - Add a line at the end of your program, stating what these animals have in common. 
  # You could print a sentence, such as Any of these animals would make a great pet!

Animal = ["Iguana", "Lucertola", "Serpente"]
print("Animali con carattertistiche simili sono: ")
for animal in Animal:
    print(animal)
for animal in Animal:
    if animal == "Lucertola":
        print("Molto liberi e facili da accudire")

    elif animal == "Iguana":
        print("Da accudire con cura e dedizione")

    else:
        print("Diffficile da accudire come animale ma molto affascianante")
print("\nMi piaciono davvero gli animali a sangue freddo")

# Use a for loop to print the numbers from 1 to 20, inclusive.

x: int = 1
while (x<20):
    print(x)
    x += 1

# Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

x: int = 1
while (x<1000000):
    # print(x)
    x += 1

# Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

x: int = 1
num = []
while (x<1000000):
    # print(x)
    x += 1
    num.append (x)
print(min(num), max(num), sum(num))

# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_number = list(range(1, 20, 2))
for number in odd_number:
    print(number)

# Make a list of the multiple of the nuumber 3, from 3 to 30.
# Use a for loop to print the number in your list

x: int = 0
num: list = [number for number in range(3,31) if number%3==0]
for i in num:
    print(f"{i}",end=" ")
print("")

# A number raised to the third power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is,
# the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

print([num ** 3 for num in range (1, 11)])

# Use a list comprehension to generate a list of the first 10 cubes.

num: list = ([num**3 for num in range (1,11)])
print(num)

# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# - Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# - Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# - Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

Personaggi: list = ["Gilgamesh", "Enkidu", "Ushiwakamaru", "Gorgone", "Semiranide", "Leonida", "Saber", "Archer"]
x = slice(3)
y = slice(3, 5)
z = slice(5, 8)
print(Personaggi[x])
print(Personaggi[y])
print(Personaggi[z])

# Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 
print("\nIs car == 'maserati'? I predict False.")
print(car == 'maserati')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 
print("\nIs car == 'toyota'? I predict False.")
print(car == 'toyota')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 
print("\nIs car == 'ferrari'? I predict False.")
print(car == 'ferrari')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 
print("\nIs car == 'opel'? I predict False.")
print(car == 'opel')

# You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them

# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = "green"
green = 5

if alien_color == "green":
    print("Il giocatore ha totalizato 5 punti!")

elif alien_color == "yellow":
    print(" Il giocatore ha totalizzato 10 punti!")

else:
    print("Il giocatore ha totalizzato 15 punti!")

alien_color = "yellow"
yellow = 10

if alien_color == "green":
    print("Il giocatore ha totalizato 5 punti!")

elif alien_color == "yellow":
    print(" Il giocatore ha totalizzato 10 punti!")

else:
    print("Il giocatore ha totalizzato 15 punti!")


# -------

age: int = 21

if age < 2:
    print("Baby\n")
elif age < 4:
    print("Toddler\n")
elif age < 13:
    print("Kid\n")
elif age < 20:
    print("Teenager\n")
elif age < 65:
    print("Adult\n")
else:
    print("Elder")

# -------  