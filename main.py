def add():
    try :
        roll = int(input("enter the roll number of the student"))
    except : ValueError:
        print ("enter only number")
    name = input("enter the name of the student")
    try: 
        age  = int(input ("enter the age of the student"))
    except : ValueError :
        print("enter number only")
    father_name = input ("enter your father name please")

    pass
def search():
    pass
def delete():
    pass
def update():
    pass
try:
    n = int(input("enter the number for your choice"))
except ValueError:
    print("enter the number")
if n == 1:
    add()
elif n == 2:
    search()
elif n == 3:
    delete()
elif n== 4:
    update()
else:
    print("wrong choice")

