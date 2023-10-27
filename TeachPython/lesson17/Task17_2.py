def deco(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        func(*args, **kwargs)
        lst = []
        for v in kwargs.values():

            if type(v) == str:
                lst.append(v.upper())
        for i in args:
            if type(i) == str:
                lst.append(i.upper())
        return lst
    return wrapper
@deco
def create_to_list(*args, **kwargs):
    pass
print(create_to_list('первый', 'второй', 3, 4, fifth = 'пятый', six = 6))