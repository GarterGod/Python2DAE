import functions

choice=1
try:
    while choice>0:
        print("Read = 1")
        print("Write = 2")
        print("Clear = 3")
        choice=int(input("Selection: "))
        print()
        if choice==1:
            functions.read()
            print()
        elif choice==2:
            functions.write()
            print()
        else:
            functions.clear()
            print()

except:
    print("Error")
finally:
    print()
    print("Done")