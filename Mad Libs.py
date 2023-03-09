import random


print("Hello, my friend.")
answer = input("Do you got couple minutes to check my project?(yes/no):  ")
answers = ["Yes", "yes", "No", "no"]

while answer != str(answers[0]) and answer != str(answers[1]):
    print("Ok, another time...")
    answer = input("You are free now?(yes/no):  ")

a = random.randrange(1, 4)
print("Ok, great, lets begin!")
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

    print("It was about", Number, Measure_of_time, "ago when I arrived at the hospital in a ", Mode_of_Transportation,
          ". The hospital is a/an ", Adjective, " place, there are a lot of ", Adjective2, Noun,
          "here. There are nurses here who have ", Color, Part_of_the_Body,
          ". If someone wants to come into my room I told them that they have to", Verb,
          " first. I’ve decorated my room with ", Number2, Noun2,
          ". Today I talked to a doctor and they were wearing a ", Noun3, " on their", Part_of_the_Body_2,
          ". I heard that all doctors", Verb, Noun4, " every day for breakfast. The most ", Adjective3,
          " thing about being in the hospital is the ", Silly_Word, Noun, "!")
elif a == 2:
    Name = input("input Proper Noun (Person’s Name):  ")
    Noun = input("input noun:  ")
    Feeling = input("input Adjective (Feeling):  ")
    Verb = input("input verb:  ")
    Feeling2 = input("input Adjective (Feeling):  ")
    Animal = input("input animal:  ")
    Verb2 = input("input Verb2:  ")
    Color = input("input color:  ")
    Verb_ing = input("input Verb (ending in ing):  ")
    Ad_ly = input("input Adverb (ending in ly):  ")
    Number = input("input number:  ")
    Measure_of_Time = input("input Measure of Time:  ")
    Silly_Word = input("Silly Word:  ")
    Noun2 = input("input noun2:  ")
    print("This weekend I am going camping with ", Name, ". I packed my lantern, sleeping bag, and ", Noun, ". I am so ", Feeling, " to ", Verb, " in a tent. I am ", Feeling2, " we might see a(n)", Animal, "I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and ", Verb2, ". I have heard that the ", Color,  "lake is great for", Verb_ing, " . Then we will ", Ad_ly,  "hike through the forest for ", Number, Measure_of_Time, ". If I see a ", Color, Animal, " while hiking, I am going to bring it home as a pet! At night we will tell ", Number, Silly_Word, " stories and roast ", Noun2, " around the campfire!!")
else:
    Name = input("input Proper Noun (Person’s Name):  ")
    Adjective = input("input Adjective:  ")
    Color = input("input color:  ")
    Animal = input("input animal:   ")
    Place = input("input place:  ")
    Adjective2 = input("input Adjective2:  ")
    Magical_Creature = input("input Magical_Creature_(Plural):  ")
    Adjective3 = input("input Adjective3:  ")
    Magical_Creature_2 = input("input Magical_Creature_(Plural)2:  ")
    Room_in_a_House = input("input Room in House:  ")
    Noun = input("input noun:  ")
    Noun2 = input("input noun2:  ")
    Noun3 = input("input Noun(Plural):  ")
    Adjective4 = input("input Adjective4:  ")
    Noun4 = input("input Noun(Plural):  ")
    Number = input("input number:  ")
    Measure_of_Time = input("input Measure of Time:  ")
    Verb = input("Verb (ending in ing):  ")
    Adjective5 = input("input Adjective5:  ")
    Noun5 = input("input noun5:  ")
    print("Dear", Name, ", I am writing to you from a ", Adjective, " castle in an enchanted forest. I found myself here one day after going for a ride on a ", Color,  Animal, " in ", Place, ", . There are ", Adjective2, Magical_Creature, " and ", Adjective3, Magical_Creature_2, " here! In the ", Room_in_a_House, ",  there is a pool full of ", Noun, ". I fall asleep each night on a ", Noun2, " of ", Noun3, " and dream of ", Adjective4,  Noun4, ". It feels as though I have lived here for", Number, Measure_of_Time, ". I hope one day you can visit, although the only way to get here now is", Verb, " on a ", Adjective5, Noun5, "!!")
