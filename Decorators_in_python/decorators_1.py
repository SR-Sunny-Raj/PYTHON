def dec1(func):
    def execnow():
        print("Executing now...")
        func()
        print("Executed")
    return execnow


# Either write @dec1 here or write sunny = dec1(sunny) below
# @dec1
def sunny():
    print("Sunny is a good boy")


sunny = dec1(sunny)


sunny()
