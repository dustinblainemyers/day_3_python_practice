
# first problem in python practice

choice = input("What exercise do you want to run ? ")



def todays_exercises(choice):
    
    if choice == "1":
        print("This is exercise 1 ")
        name = input('What is your name?: ')
        print('Hello, %s!' % name)
    elif choice == "2":
        print("This is exercise 2 ")
        name = (input('What is your name?: ')).upper()
    
        print('Hello, %s!' % name)
        letters_in_name = len(name)
        print("Your name has %d letters in it! Awesome ! " % letters_in_name)

    elif choice == "3":
        print("Please fill in the blanks below: ")
        print("____(name)____'s favorite subject in school is ____(subject)____.")
        name = input("What is your name? ")
        subject = input("What is your favorite subject in school? ")
        # outputs the persons name and favorite subject
        print("%s's favorite subject in school is %s." % (name, subject))




todays_exercises(choice)


    

    




    

    