from classes import DoubleLinkedList
from functions import *

if __name__ == '__main__':
    history = DoubleLinkedList()
    #add_test_data(history)
    curr_page = history.head
    print("Browser History")
    if history.size>0:
        print(f"Current history size {history.size}")
        print("First page:")
        print_page(curr_page.data)
        em_fl = 0

    else:
        print("History is empty")
        em_fl = 1

    print("Choose one of the options:")
    print("1. Move forward")
    print("2. Move backward")
    print("3. Clear history ")
    print("4. Find by domain")
    print("5. Watch history for period of time")
    print("6. Import history from file")
    print("7. Add test data")
    print("0. Quit")
    i=-1

    while i!=0:

        try:
            i = int(input("Your option: "))

        except:
            print("Invalid input")
            print("Please enter a valid option")

        if i>7:
            print("Invalid input")
            print("Please enter a valid option")

        if i==1:
            curr_page=move_forward(curr_page,history)

        if i==2:
            curr_page = move_backward(curr_page, history)

        if i==3:
            clear_history(history)
            em_fl=1

        if i==4:
            find_by_domain(history)

        if i==5:
            find_by_time_period(history)

        if i==6:
            add_data_from_file(history)
            if em_fl==1:
                curr_page = history.head
                em_fl=0

        if i==7:
            add_test_data(history)
            if em_fl==1:
                curr_page = history.head
                em_fl=0
            print("Test data was successfully added!")
            print(f"Current history size {history.size}")