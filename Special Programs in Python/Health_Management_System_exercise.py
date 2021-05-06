def getdate():
    import datetime
    return datetime.datetime.now()


def writeread(d, var):
    if(d != "1" and d != "2"):
        print("Please provide a valid input")
        start()
    a = input(
        f"Whose data you want to {var} ?\n1. Sunny\n2. Harry\n3. Rohan\n")
    if(a != "1" and a != "2" and a != "3"):
        print("Please provide a valid input")
        writeread(d, var)
    x = input(f"Which data you want to {var} ?\n1. Diet\n2. Exercise\n")
    if(x != "1" and x != "2"):
        print("Please provide a valid input")
        writeread(d, var)
    dic = {"11": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\sd.txt", "12": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\se.txt", "21": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\hd.txt",
           "22": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\he.txt", "31": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\rd.txt", "32": "E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\re.txt"}
    if(d == "1"):
        f = open(dic[a+x], "a")
        f.write(str(getdate())+"\n")
        f.write("Enter data -: "+input()+"\n")
        print("Data added successfully")
        ch = input("Do you want to add some more data (Y|N) ? ")
        if ch == "y" or ch == "Y":
            writeread("1", "write")
        else:
            f.close()
            exit()
    elif(d == "2"):
        f = open(dic[a+x], "r")
        print("\nData in the file -: \n"+f.read())
        ch = input("Do you want to read some more data (Y|N) ? ")
        if ch == "y" or ch == "Y":
            writeread("2", "read")
        else:
            f.close()
            exit()


def start():
    d = input(("What do you want ?\n1. Write data\n2. Retrieve data\n"))
    if d == "1":
        var = "write"
    elif d == "2":
        var = "read"
    else:
        var = ""
    writeread(d, var)


start()
