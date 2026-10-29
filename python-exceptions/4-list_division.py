#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        division = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError
            division = a / b
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(division)
    return result
