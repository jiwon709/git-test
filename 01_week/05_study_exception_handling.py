try:
    arr = [1, 2]
    print(arr[3])
    4 / 0
except IndexError as e:
    print("IndexError 발생!", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError 발생!", e)
except (IndexError, ZeroDivisionError) as e:
    print("Index Of ZeroDivision Error 발생!", e)
