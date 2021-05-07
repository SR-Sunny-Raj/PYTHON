import time
i = 0
initial = time.time()
print("Initial time -: ", initial)
print("In while loop")
while(i < 45):
    print(i)
    i += 1

print("After while loop -: ", time.time()-initial)
initial2 = time.time()

print("In for loop")
for j in range(45):
    print(j)
print("After for loop -: ", time.time()-initial2)

print(time.asctime(time.localtime(time.time())))
time.sleep(3)
print("Bye")
