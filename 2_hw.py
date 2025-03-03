def task_1() -> None:
    """return: None"""
    var_int = 35
    var_float = 5.14
    var_str = "panda"
    var_list = [1, 2, 3, 4, 5]
    var_bool = True

    print(f"Тип переменной var_int: {type(var_int)}")
    print(f"Тип переменной var_float: {type(var_float)}")
    print(f"Тип переменной var_str: {type(var_str)}")
    print(f"Тип переменной var_list: {type(var_list)}")
    print(f"Тип переменной var_bool: {type(var_bool)}")

task_1()



def task_2(a=[1,2,3,5,8,13,21]) -> list:
    return a[0:3]

print (task_2())
#последовательность Фибоначчи


def task_3(number: int) -> int:
    return number ** 2

print(task_3(6))


