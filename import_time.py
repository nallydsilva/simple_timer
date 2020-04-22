import time

seconds = int(input("How many seconds do you want start the countdown: ?"))

for i in range(seconds):
    print("You have", str(seconds - i), "seconds remaining")
    time.sleep()

print("Your time is up !!!")
