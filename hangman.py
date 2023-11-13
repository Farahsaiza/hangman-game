def lenword(mot):  #this function checks the size of the entered word

    L=len(mot)
    if L>=4 and L<=25 :
        return True
    else:
        return False
    

print("Welcome to Hangman game  ^_____^:")  #it's a short introduction to the game where the user knows the rules and how it works
print("Hangman is a game consisting of finding a word by guessing which letters make it up.")
print("the rules of the game are simple:")
print("First of all choose a word")

choice=str(input("if you play with your freind and you want to enter a word , please write *Yes* if you don't, write *No*"))

while choice.lower() !="yes" and  choice.lower() !="no": #the user must unswer yes or no, if he didn't  this question will repeat until he answer a right answer
     choice=str(input("plese answer the question")) 


if choice.lower() == "yes" :  # that means that the user wants to enter a word by his choice
    word=str(input("enter a word: "))

    while lenword(word)== False: #that means that the word entered bythe user dosn't respect the lenght condition of the word
        print("the word entered is invalid")
        word=str(input("please enter another capital word and its letters between 4 and 25: "))
        lenword(word)

else:
    print("we will give you a random word") # that means that the user wants a random word
    print("Please choose which level do you want")
    level=str(input("choose one: Easy, Medium or Hard:  "))
    L=level.lower()

    if L == "easy":
        category=str(input("please choose one of these categories: Animals,Fruits,vegetables,color,country,food,clothes: "))
        x=category.lower()

        while x!="animal" and x!="animals" and x!="food" and x!="color" and x!="colors" and x!="clothe" and x!="contry" and x!="fruit" and x!="clothes" and x!="contries" and x!="fruits" and x!="vegetable" and x!="vagetables":
            print("this category dosn't exist")
            category=str(input("enter another category: "))
            x=category.lower()


        if x == "animals" or x == "animal" :
            Animals = {"SHEEP", "CHIKEN","SNAKE","ELEPHANT", "RABBIT","CAMEL"}
            word=list(Animals).pop()

        elif x == "fruits" or  x == "fruit":
            Fruits = {"BANANA", "APPLE","ANANAS","WATERMELON ", "PEACH","BLACKBERRY"}
            word=list(Fruits).pop()

        elif x == "vegetables" or  x == "vegetable":
            vegetables = {"CARROT", "BEETROOT","BROCCOLI","CUCUMBER", "ONION","PUMPKIN"}
            word=list(vegetables).pop()

        elif x == "colors" or  x == "color":
            Colors = {"PURPLE", "GREEN","WHITE","BLACK" , "YELLOW","BROWN"}
            word=list(Colors).pop()

        elif x == "country" or  x == "countries":
            country = {"GERMANY", "FRANCE","MORROCO","INDIA", "TURKEY","UKRAIN"}
            word=list(country).pop()

        elif x == "food" :
            Food = {"BREAD", "SANDWICH","HAMBURGER","SAUSAGE", "DONUT","PIZZA"}
            word=list(Food).pop()

        elif x == "clothes" or  x == "clothe":
            Clothes = {"SWEATER", "SHIRT","DRESS","SUIT", "GLOVES","JEANS"}
            word=list(Clothes).pop()
        else:
            print("sorry! we can't find this category,  please enter it again")
    
    elif L== "medium":
        Medium= {"KNIGHT", "TEMPERATURE","INGREDIENT","RHYTHM", "GRAVITY","FRIENDSCHIP"}
        word=list(Medium).pop()
    
    elif  L== "hard":
        Hard= {"LABORATORY", "CONSCIENCE","DICTIONARY","ACCIDENTALLY", "HOMOGENEOUS","EXPONENTIALLY"}
        word=list(Hard).pop()

L=len(word)

T=[]
for i in range (L):
    T.append("*")
    
print(T)

i=0
chance=0


while i<=L:
    

    C=str(input("enter a letter: "))
    cmaj=C.upper()
    print(cmaj)


    while cmaj in  T:  #that means if th lettre is already entred and it was right the user can't enter the same letter
         print("you have already  enter this letter ")
         C=str(input("enter again  a letter: "))
         cmaj=C.upper()


        
 
    occ=word.count(cmaj)  

    if occ==0 :  #that means that the letter is not found in the word
          print("unfortunately this letter is not in the word")
          print("Don't worry you still have",4-chance,"other chances lef")
          
          chance=chance+1

    else:
        print("congratulation.this letter exist!!")
        for j in range  (L): 
            if word[j]==cmaj:
                T[j]=cmaj
                print(T)
    
    i=i+1
    if  chance==5:
        print("unfortunately you lost all the chances")
       
        break
    
com=0
for j in range (L):
    if T[j]==word[j]:
        com=com+1

if com==L:
    print("congratulation! you win")
    print(T)
    print("the word is: ",word)
            
else:
     print("sorry you lost the game!")
     print("you didn't guess the word.")
     print("the word is: ",word)

       

        

    
    
        

    





     
        
        
        
        
        
        



