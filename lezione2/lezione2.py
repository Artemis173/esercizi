#Edwin
print ("Hello World")

# Use a variable to represent a person's name, 
# and print a message to that person. 
# Your message should be simple , such as, 
# "Hello Eric, would youl like to learn some python today?"

name: str = "Archer"

print (f"Ciao {name} ti va di imparre un po di Python insieme?")

# Use a variable to represent a person's name, 
# and then print that name person's in lowercase, uppercase, and title case

name: str = "Archer"

print (f"Ciao {name.lower()}")
print (f"Ciao {name.upper()}")
print (f"Ciao {name.title()}")

# Find a qoute from a famous person you admire. Point the qoute and the name of its author
# Your output should look a something like the following,
# includin the question mark: Alber Einstein once said, "Aperson who never made a mistake never tried anything new."

name: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""
name: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""

print (f"{name} once said, {message}")
print (f"{name} once said, {message}")

# Repeat exercise 2.5, but this time, rerpresent the fammous person's name using a variable called famous_person.
# The compose your message and represent it with a new variable called message
# Print your message

famous_person: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""

print (f"{famous_person} once said, {message}")

# Python has a removesuffix() method tht works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do

filename: str = "python_notes.txt"

print (f"Nome del file senza suffisso, {filename.removesuffix('.txt')}")

# Store the name of few of you friends in a list called names.
# Print each person's name by accessing each element in the list, one at a time.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
index = ["0", "1", "2", "3"]

print (names [0])
print (names [1])
print (names [2])
print (names [3])

# Start with the list you used in Exercise 3-1, but instead of just printing each person's name,
# print them a message to them. The text of each message should be the same,
# but each message should be personalized with the person's name.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Salve {first_name}")
print (f"Salve {second_name}")
print (f"Salve {third_name}")
print (f"Salve {fourth_name}")

# Think of your favorite mode of transportation, such as motorcycle or a car, and maake a list that stores several examples.
# Use your list to print a series of statement about these items, such as "I would like to own a honda Motorcycle"

veicoles = ["Motorcycle", "Car", "Byclycle", "Scooter"]
first_veicole = veicoles [0]
second_veicole = veicoles [1]
third_veicole = veicoles [2]
fourth_veicole = veicoles [3]

print (f"I would like to own a {first_veicole}")
print (f"I wouldn't like to own a {second_veicole}")
print (f"I own a {third_veicole}")
print (f"I own a {fourth_veicole}")

# If you could invite anyone, living or decesead, to dinner, who would you invite? 
# Make a list that includes at least three people you'd like to invite to dinner, Then use your list to print a message to each person invitin them to dinnes.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")

# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list

names.remove ("Archer")
print (names)

names = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")

# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

names.insert (0, "Ushiwaka")
names.insert (3, "Leonida")
names.append ("Quetzal")

print (names)

first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]
fifth_name = names [4]
sixth_name = names [5]
seventh_name = names [6]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")
print (f"Hello {fifth_name}, would you like to come to dinner at my place?")
print (f"Hello {sixth_name}, would you like to come to dinner at my place?")
print (f"Hello {seventh_name}, would you like to come to dinner at my place?")

print (f"Hello {names}, would you like to come to dinner at my place? We're more than before because the table is bigger")

# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program fromWorking with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner. Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print (names)

print (f"Hello {names.pop(0)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(1)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(2)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(1)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(2)}, for some problems I cant invite more than two peolpe. Sorry!")

print (names)

print (f"Hello {first_name}, you are still invited!")
print (f"Hello {second_name}, you are still invited!")

del names[0]
del names[0]

print (names)

# Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

Places = ["Babylon", "Camelot", "Avalon", "Eden", "Fuyuki"]
print (Places)

Places.sort()
print (Places)
Places.sort(reverse=True)
print (Places)
Places.reverse()
print (Places)
Places.reverse()
print (Places)
Places.sort()
print (Places)
Places.sort(reverse=True)
print (Places)

# Working with one of the programs from Exercises 3,
# use len() to print a message indicating the number of people you’re inviting to dinner.

names = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]

print (f"La lunghezza di {names} è: {len(names)}")

# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

names: list = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]
names.insert (len(names)//2, "Emiya")
print (names)

names.append ("Rin")
print (names)

print (f"Hello {names.pop(0)}, sorry see you another time")
print (f"Hello {names.pop(3)}, sorry see you another time")
del names[1]
del names[2]

print (names)
names.sort()
names.reverse()