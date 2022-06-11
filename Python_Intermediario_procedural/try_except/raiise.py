#Usando raise

def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print("Log: ", error)
        raise


try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)