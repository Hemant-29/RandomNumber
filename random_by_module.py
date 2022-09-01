import random

random_nos = 0
total_nos = 10000
appear_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
progress, temp_progress = 0, 0


def timesAppear(i, prob_test_no=1):
    global appear_count
    # print("\ntesting probability count of ->", prob_test_no)
    if i == prob_test_no:
        appear_count[prob_test_no] += 1


def printProgress():
    global random_nos, total_nos, progress, temp_progress
    progress = (random_nos * 100) // total_nos
    if (progress - temp_progress) > 0:
        temp_progress = progress
        print("_", end="")


print("↓ 0%", " " * 93, "↓ 100%")

for i in range(total_nos):
    # the mainloop to construct the random numbers
    num = random.randint(0, 10)
    print(num, end="")  # printing the random numbers
    random_nos += 1
    # printProgress()
    for prob_test_no in range(10):
        timesAppear(num, prob_test_no)

print("\nrandom numbers generated!")


for prob_test_no in range(10):
    print(
        f"\nprobability that {prob_test_no} occurs is {appear_count[prob_test_no]/total_nos}"
    )
