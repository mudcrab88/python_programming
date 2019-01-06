def interact():
    print("Hello stream world") # print выводит в sys.stdout
    while True:
        try:
            reply = input("Enter a number>") # input читает из sys.stdin
        except EOFError:
            break # исключение при встрече символа eof
        else: # входные данные в виде строки
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print("Bye")
if __name__ == "__main__":
    interact() # если выполняется, а не импортируется