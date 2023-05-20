# A few ways to do string concatenation
#name = "Peanut Butter"

#print("Hello, my name is " + name)
#print("Hello, my name is {}".format(name))
#print(f"Hello, my name is {name}")

# In this project I will use f strings.

adj = input("Adjective: ")
verb1 = input("Verb: ")
noun = input("Noun: ")
animal = input("Animal: ")
verb2 = input("Verb: ")

#madlib example usung cocatenation.
madlib = f"""Computer progrmming makes me very {adj}! 
First thing in the morning, I can't wait to {verb1}
out of bed. Grab my {noun}. Eat breakfast like a(n) {animal}. 
Then hop on my PC to begin {verb2}ing out code!"""

#print the finished madlib.
print(madlib)
