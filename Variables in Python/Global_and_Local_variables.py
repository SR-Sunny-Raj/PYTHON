def sunny():
    x = 5

    def raj():
        global x
        x = 10
    print("before calling raj() x = ", x)
    raj()
    print("after calling raj() x = ", x)


sunny()
print("Global variable x = ", x)
