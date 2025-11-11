from activity1 import act1
from activity2 import act2
from activity3 import act3
from activity4 import act4
from activity5 import act5
from activity6 import act6
from activity7 import act7
from activity8 import act8
from activity9 import act9
from activity10 import act10
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14
from activity15 import act15
from activity16 import act16
from activity17 import act17
from activity18 import act18
from activity19 import act19
from activity20 import act20
from activity21 import act21
# from activity22 import act22

def activity_menu():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("___________________________________________________________________________________________") 
        print("|             Prelims  Menu:                 |                                            |") 
        print("|                                            |                                            |") 
        print("|             1.Activity 1                   |             16.Activity 16                 |") 
        print("|             2.Activity 2                   |             17.Activity 17                 |") 
        print("|             3.Activity 3                   |             18.Activity 18                 |") 
        print("|             4.Activity 4                   |             19.Activity 19                 |") 
        print("|             5.Activity 5                   |             20.Activity 20                 |") 
        print("|             6.Activity 6                   |             21.Activity 21                 |")  
        print("|             7.Activity 7                   |             22.Activity 22                 |") 
        print("|             8.Activity 8                   |             23.Activity 23                 |") 
        print("|             9.Activity 9                   |             19.Activity 19                 |") 
        print("|             10.Activity 10                 |             20.Activity 20                 |") 
        print("|             11.Activity 11                 |             21.Activity 21                 |") 
        print("|             12.Activity 12                 |             22.Activity 22                 |") 
        print("|             13.Activity 13                 |             23.Activity 23                 |") 
        print("|             14.Activity 14                 |             0.Back to Main Menu            |") 
        print("|             15.Activity 15                 |                                            |") 
        print("|____________________________________________|____________________________________________|") 
        activity_number = int(input("Enter the activity number: "))
        if activity_number == 0:
            print("\n\nReturning to Main Menu.")
            display_zero()
            break
        elif activity_number <= 100:
            if activity_number == 1:
                act1()
                display_exit()
            elif activity_number == 2:
                act2()
                display_exit()
            elif activity_number == 3:
                act3()
                display_exit()
            elif activity_number == 4:
                act4()
                display_exit()
            elif activity_number == 5:
                act5()
                display_exit()
            elif activity_number == 6:
                act6()
                display_exit()
            elif activity_number == 7:
                act7()
                display_exit()
            elif activity_number == 8:
                act8()
                display_exit()
            elif activity_number == 9:
                act9()
                display_exit()
            elif activity_number == 10:
                act10()
                display_exit()
            elif activity_number == 11:
                act11()
                display_exit()
            elif activity_number == 12:
                act12()
                display_exit()
            elif activity_number == 13:
                act13()
                display_exit()
            elif activity_number == 14:
                act14()
                display_exit()
            elif activity_number == 15:
                act15()
                display_exit()
            elif activity_number == 16:
                act16()
                display_exit()
            elif activity_number == 17:
                act17()
                display_exit()
            elif activity_number == 18:
                act18()
                display_exit()
            elif activity_number == 19:
                act19()
                display_exit()
            elif activity_number == 20:
                act20()
                display_exit()
            elif activity_number == 21:
                act21()
                display_exit()

import time
def  timer_exit(open, delay): 
    try: 
        for line in open: 
            print("\r", end="") 
            for c in line: 
                print(c, end="", flush=True) 
                time.sleep(delay / 1000.0) 
            time.sleep(delay * 15 / 1000.0) 
    except KeyboardInterrupt: 
        pass 
def display_enter(): 
    name = input("Enter name: ").title() 
    open = [ 
        f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n         Giving Access to {name.capitalize()}", 
        f"         Hello, {name.capitalize()}           ", 
        "         Welcome to Finals Compilation         ",
        "         Generated by Roberto Guevarra Jr.                           ", 
        "         Please wait a few seconds                            ", 
        "                                                        ", 
    ] 
    delay = 40 
    timer_exit(open, delay) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return name
display_enter()

def exiting(out, go):
    try:
        for x in out:
            print("\r", end="")
            for i in x:
                print(i, end="", flush=True)
                time.sleep(go / 1000)
            time.sleep(go * 15 / 1000)
    except KeyboardInterrupt:
        pass


def display_activities(): 
    sure = [ 
        "\n\n",
        "Option in Activity show in 3 seconds", 
        "3..................................................", 
        "2..................................................", 
        "1..................................................", 
        "                                                   ", 
    ] 
    hi = 30
    exiting(sure, hi) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def display_exit(): 
    sure = [ 
        "\n\n\nYou want to exit?", 
        "Goodbye!                       ", 
        "Program exiting in 3 seconds", 
        "3...........................", 
        "2...........................", 
        "1...........................", 
        "                            ", 
    ] 
    hi = 30 
    exiting(sure, hi) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def display_zero(): 
    sure = [ 
        "Exiting in 3 seconds", 
        "3............................", 
        "2............................", 
        "1............................", 
        "                            ", 
    ] 
    hi = 30
    exiting(sure, hi) 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def main():
    while True:
        print(" ____________________________________________")         
        print("|                Choose here                 |") 
        print("|____________________________________________|") 
        print("|                 Main Menu:                 |") 
        print("|                                            |") 
        print("|                 1.Activity                 |") 
        print("|                 2.Code Challange           |") 
        print("|                 3.Exam                     |") 
        print("|                 0.Exit                     |") 
        print("|____________________________________________|") 
        choice = int(input("Enter your choice: "))
        if choice == 0:
            display_exit()
            break
        elif choice == 1:
            display_activities()
            activity_menu()
        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")      
main()