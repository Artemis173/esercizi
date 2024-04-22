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


#