import time
import base64
import re
from classes import BrowserHistory

def add_test_data(history): #Добавление тестовых данных
    test_data = [
        {"url": "https://google.com", "time": time.time() - 3600, "bookmark": False},
        {"url": "https://github.com", "time": time.time() - 7200, "bookmark": True},
        {"url": "https://stackoverflow.com", "time": time.time() - 10800, "bookmark": False},
        {"url": "https://youtube.com", "time": time.time() - 15000, "bookmark": False},
        {"url": "https://reddit.com", "time": time.time() - 20000, "bookmark": True},
        {"url": "https://python.org", "time": time.time() - 28000, "bookmark": False},
        {"url": "https://habr.com", "time": time.time() - 35000, "bookmark": False},
        {"url": "https://djangoproject.com", "time": time.time() - 42000, "bookmark": True},
        {"url": "https://pypi.org", "time": time.time() - 50000, "bookmark": False},
        {"url": "https://docker.com", "time": time.time() - 60000, "bookmark": False},
        {"url": "https://kubernetes.io", "time": time.time() - 72000, "bookmark": True},
        {"url": "https://postgresql.org", "time": time.time() - 85000, "bookmark": False},
        {"url": "https://mongodb.com", "time": time.time() - 95000, "bookmark": False},
        {"url": "https://reactjs.org", "time": time.time() - 110000, "bookmark": True},
        {"url": "https://vuejs.org", "time": time.time() - 125000, "bookmark": False},
        {"url": "https://angular.io", "time": time.time() - 140000, "bookmark": False},
        {"url": "https://typescriptlang.org", "time": time.time() - 160000, "bookmark": True},
        {"url": "https://nodejs.org", "time": time.time() - 180000, "bookmark": False},
        {"url": "https://npmjs.com", "time": time.time() - 200000, "bookmark": False},
        {"url": "https://yarnpkg.com", "time": time.time() - 220000, "bookmark": True},
        {"url": "https://webpack.js.org", "time": time.time() - 245000, "bookmark": False},
        {"url": "https://babeljs.io", "time": time.time() - 270000, "bookmark": False},
        {"url": "https://eslint.org", "time": time.time() - 295000, "bookmark": True},
        {"url": "https://prettier.io", "time": time.time() - 320000, "bookmark": False},
        {"url": "https://jestjs.io", "time": time.time() - 350000, "bookmark": False},
        {"url": "https://cypress.io", "time": time.time() - 380000, "bookmark": True},
        {"url": "https://storybook.js.org", "time": time.time() - 410000, "bookmark": False},
        {"url": "https://figma.com", "time": time.time() - 450000, "bookmark": False},
        {"url": "https://notion.so", "time": time.time() - 500000, "bookmark": True},
        {"url": "https://trello.com", "time": time.time() - 560000, "bookmark": False}
    ]
    for i in test_data:
        page=BrowserHistory()
        page.url=i["url"]
        page.visit_time=i["time"]
        page.bookmark=i["bookmark"]
        history.insert_at_end(page)

    return history

def print_page(page): #Вывод одной страницы истории
    print(f" URL: {page.url}")
    print(f" Visit time: {time.ctime(float(page.visit_time))}")
    print(f" Bookmark: {page.bookmark}")


def get_valid_time_range(): #Корректное получение временного периода
    while True:
        try:
            pattern = r'^\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}$'

            start_input = input("Start time (dd.mm.yyyy hh:mm:ss): ").strip()

            if not re.match(pattern, start_input):
                print("Invalid start time format")
                continue

            end_input = input("End time (dd.mm.yyyy hh:mm:ss): ").strip()

            if not re.match(pattern, end_input):
                print("Invalid end time format")
                continue

            start_struct = time.strptime(start_input, "%d.%m.%Y %H:%M:%S")
            end_struct = time.strptime(end_input, "%d.%m.%Y %H:%M:%S")

            start_timestamp = time.mktime(start_struct)
            end_timestamp = time.mktime(end_struct)

            if start_timestamp > end_timestamp:
                print("Start time cannot be after end time")
                continue

            return start_timestamp, end_timestamp

        except:
            print("Invalid time format")

def move_forward(curr_page, history): #Движение вперед по истории
    if history.size == 0:
        print("History is empty")
    else:
        if curr_page.next != None:
            print("Current page is")
            curr_page = curr_page.next
            print_page(curr_page.data)
        else:
            print("It's already last element")
    return curr_page

def move_backward(curr_page, history): #Движение назад по истории
    if history.size == 0:
        print("History is empty")
    else:
        if curr_page.prev != None:
            print("Current page is")
            curr_page = curr_page.prev
            print_page(curr_page.data)
        else:
            print("It's already first element")
    return curr_page

def clear_history(history) : #Очситка истории
    for i in range(history.size):
        history.delete_at_end()
    print(f"Current history size {history.size}")
    print("Now history is empty!")

def find_by_domain(history): #Поиск по домену
    if history.size == 0:
        print("History is empty")
    else:
        curr_page_f = history.head
        domain = str(input("Enter the domain of the page(or part of it): "))
        fl = 0
        cnt = 0
        for i1 in range(history.size):

            if domain in curr_page_f.data.url:
                fl = 1
                cnt += 1
                print(
                    f" URL: {curr_page_f.data.url} Visit time:{time.ctime(float(curr_page_f.data.visit_time))} Bookmark:{curr_page_f.data.bookmark}")
            if curr_page_f.next != None:
                curr_page_f = curr_page_f.next
            else:
                break
        if fl == 0:
            print("No such domain in history")
        else:
            print(f"{cnt} pages found for this domain")

def find_by_time_period(history): #Поиск по временному периоду
    if history.size == 0:
        print("History is empty")
    else:
        start_ts, end_ts = get_valid_time_range()

        curr_page_f = history.head
        fl = 0
        cnt = 0
        while curr_page_f:
            if start_ts <= float(curr_page_f.data.visit_time) <= end_ts:
                fl = 1
                cnt += 1
                print(
                    f" URL: {curr_page_f.data.url} Visit time:{time.ctime(float(curr_page_f.data.visit_time))} Bookmark:{curr_page_f.data.bookmark}")
            curr_page_f = curr_page_f.next

        if fl == 0:
            print("No browser history found for this time period")
        else:
            print(f"{cnt} pages found for this time period")

def add_data_from_file(history): #Добавление данных из файла
    try:
        f = open("data.b64", "r", encoding="utf-8")
        b64_string = f.read()
        decoded_data = base64.b64decode(b64_string).decode('utf-8').split("\r\n")
        for i in decoded_data:
            i = i.split()
            page = BrowserHistory()
            page.url = i[0]
            page.visit_time = i[1]
            page.bookmark = i[2]
            history.insert_at_end(page)
        print("Data from file was successfully added!")
        print(f"Current history size {history.size}")
    except:
        print("Cannot open the file")








