import time

seconds = int(input("How many seconds do you want to countdown from ?"))

for i in range(seconds):
    print(str(seconds - i), "seconds remaining")
    time.sleep(1)

print("Your time is up !!!")
