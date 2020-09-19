# define function to get current date
def getdate():
    import datetime
    return datetime.datetime.now()


# define entry function
def entry(n, l, d):
    t = str(getdate())
    file_name = str(n + l) + ".txt"
    f = open(file_name, 'a')
    f.write(d + " " + t)
    f.close()


# define read function
def read(n, l):
    file_name = str(n + l) + ".txt"
    f = open(file_name, 'r')
    print(f.read())
    f.close()


# give option to choose command
cmd = input("do you wanna read or write?")

if cmd == "read":
    n = input("please enter your name!")
    l = input("log diet or exercise?")
    read(n, l)
elif cmd == "write":
    n = input("please enter your name!")
    l = input("log diet or exercise?")
    d = input("please enter data")
    entry(n, l, d)
else:
    print("please enter correct command")




'''if name == "harry" and log == "exercise":
    f = open("harryex.txt", 'a')
    t = str(getdate())
    f.write(data + " " + t)
    f.close()
elif name == "harry" and log == "diet":
    f = open("harrydiet.txt", 'a')
    t = str(getdate())
    f.write(data + " " + t)
    f.close()
elif name == "hammad" and log == "excercise":
    f = open("hammadex.txt", 'a')
    t = str(getdate())
    f.write(data + " " + t)
    f.close()
elif name == "hammad" and log == "diet":
    f = open("hammaddiet.txt", 'a')
    t = str(getdate())
    f.write(data + " " + t)
    f.close()
elif name == "hammad" and log == "diet":
    f = open("hammaddiet.txt", 'a')
    t = str(getdate())
    f.write(data + " " + t)
    f.close()'''
