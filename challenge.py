from datetime import datetime


def finish_date(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        now_time = datetime.now()
        print('Finish the program: ', now_time.strftime('%d/%m/%Y - %H:%M:%S'))
    return wrapper
        


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
