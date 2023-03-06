import random

print("Hello, my friend.")
a = random.randrange(1, 4)
print(a)
if a == 1:
    Number = input("input a number:  ")
    Measure_of_time = input("input Measure of time:  ")
    Mode_of_Transportation = input("input Mode of Transportation:  ")
    Adjective = input("input Adjective:  ")
    Adjective2 = input("input Adjective2:  ")
    Noun = input("input noun:  ")
    Color = input("input Color:  ")
    Part_of_the_Body = input("input Part of the Body:  ")
    Verb = input("Verb:  ")
    Number2 = input("Number2:  ")
    Noun2 = input("Noun2:  ")
    Noun3 = input("Noun3:  ")
    Part_of_the_Body_2 = input("Part of the Body 2:  ")
    Noun4 = input("Noun4:  ")
    Adjective3 = input("Adjective3:  ")
    Silly_Word = input("Silly Word:  ")

    print("It was about", Number, Measure_of_time, "ago when I arrived at the hospital in a ", Mode_of_Transportation, ". The hospital is a/an ", Adjective, " place, there are a lot of ", Adjective2, Noun, "here. There are nurses here who have ", Color, Part_of_the_Body, ". If someone wants to come into my room I told them that they have to", Verb, " first. I’ve decorated my room with ", Number2, Noun2, ". Today I talked to a doctor and they were wearing a ", Noun3,  ") on their", Part_of_the_Body_2, ". I heard that all doctors", Verb, Noun4, " every day for breakfast. The most ", Adjective3, " thing about being in the hospital is the ", Silly_Word, Noun, "!")
elif a == 2:
    
    print("This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!")
else:
    print("jjjj")