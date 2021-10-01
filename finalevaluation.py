

class Pet:
    def __init__(self, species, name):

        self.species=none
        self.name = ""
        spelist=['Dog','Cat','Horse','Hamster']
        if (species not in spelist):
            print("\n ERROR! THE SPECIES MUST BE FROM DOG,CAT,HORSE OR HAMSTER")


    def __str__(species,name):
        if self.name:
            return "Species of: {self.species} named {self.name}"
        else:
            return "Species of: {self.species} unnamed"

class Dog(Pet):
    def _init_(self,name,chases):
        self.chases="Cats"
        self.species= "Dog"
        self.name=""

    def _str_(species,name,chases):
        if self.name:
            return "Species of: {self.species} named {self.name} chases {self.chases} "
        else:
            return "Species of: {self.species} unnamed chases {self.chases} "

class Cat(Pet):
    def _init_(self,name,hates):
        self.hates="Dog"
        self.species= "Cat"
        self.name=""

    def _str_(species,name,chases):
        if self.name:
            return "Species of: {self.species} named {self.name} hates {self.hates} "
        else:
            return "Species of: {self.species} unnamed hates {self.hates} "

class main():
    d1 = Dog()
    d2 = Dog()
    d3 = Dog()
    d4 = Dog()
    d5 = Dog()
    c1 = Cat()
    c2 = Cat()
    c3 = Cat()

    pets= {"Dog":[d1], "Dog": [d2], "Dog": [d3],"Dog": [d4],"Dog": [d5], "Cat":[c1], "Cat":[c2], "Cat":[c3]}

    f=True
    while f:
       for "Dog" in pets:
           self.name=input("\n Enter the names of the five dogs")
           pets["Dog"].append [{self.name}]
           "
       for "Cat" in pets:
           self.name = input("\n Enter the names of the three dogs")
           pets["Cat"].append[{self.name}]

           








