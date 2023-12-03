#!/usr/bin/env python3

class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Create another instance of Person
alice = Person()
alice.walk()  # This should print "The person is walking."
