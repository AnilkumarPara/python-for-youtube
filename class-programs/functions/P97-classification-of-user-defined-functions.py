# 1. Function with No Arguments and No Return Value
def display_greetings():
    print("Hello!")


display_greetings()


# 2. Function with Arguments and No Return Value
def greetings(name):
    print(f"Hello {name}")


greetings('Anil')
# 3. Function with No Arguments and a Return Value
import datetime


def current_date():
    return datetime.date.today()


today_date = current_date()
print(today_date)


# 4. Function with Arguments and a Return Value
def add(a, b):
    return a + b


print(add(2, 3))
