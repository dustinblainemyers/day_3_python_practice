#Day 3 exercises set 2

choice = input("What exercise do you want to run ? ")



def todays_exercises(choice):
    
    if choice == "1":
        
        

        day = int(input('Day (0-6)? '))
        days_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        print(days_week[day])

    elif choice == "2":
        day = int(input('Day (0-6)? '))
        sleep = "Sleep in"
        work = "Go to work"
        if day == 0 or day == 6:
            print(sleep)
        else:
            print(work)

    elif choice == "3":
        celsius_input = float(input("Temperature in C? "))
        Fahrenheit_return = celsius_input * 1.8 + 32
        print('%.1f F' % Fahrenheit_return)
    




todays_exercises(choice)