#Day 3 exercises set 2

choice = input("What exercise do you want to run ? ")




    
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
    celsius_input = int(input("Temperature in C? "))
    Fahrenheit_return = celsius_input * 1.8 + 32
    print('%.1f F' % Fahrenheit_return)
elif choice == "4":
    bill_amount = float(input('Total bill amount? '))
    
        
    #user selects level of service from 1 being bad , 2 being fair, and 3 being good.
    user_input = input('Level of service? (Choose 1 for bad, 2 for fair, and 3 for good) ')
    number_to_split = int(input('Enter the number of people to split the bill between (enter 1 if it is just you) :'))

    if user_input == "1":
        #bad service level
        tip_amount = bill_amount * .1
        
    elif user_input == "2":
        # fair service level
        tip_amount = bill_amount * .15

    elif user_input == "3":
        # good service level
        tip_percentage = .2
        tip_amount = bill_amount * .2

    else: print("You did not enter a valid selection. Please run the program again")

    total = (bill_amount + tip_amount) / number_to_split
    print('Total amount per person: ${:.2f}'.format(total))
    print('Your tip is  : ${:.2f}'.format(tip_amount))
        


        
        
    


    




