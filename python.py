print ('Hello World!');
a=10
b=0
try:
    print("This is outer try block")
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Division by 0")
    finally:
        print("inside inner finally block")
except Exception:
    print("general exception")
finally:
    print("inside oter finally block")