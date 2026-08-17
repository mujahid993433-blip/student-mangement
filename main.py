def add():
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
