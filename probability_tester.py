import os
import random_no as ran


random_nos = 0
total_nos = 100000  # <--enter the total no. of random numbers required
appear_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
progress, temp_progress = 0, 0


def clearScreen():
    # function to clear the terminal screen
    print("\033c")


def timesAppear(i, prob_test_no=1):
    # funtion that tells how many times a random no. was generated
    # "i" is the current no., "prob_test_no" is no. whose probability is being counted
    global appear_count
    # print("\ntesting probability count of ->", prob_test_no)
    if i == prob_test_no:
        appear_count[prob_test_no] += 1


def printProgress():
    # This function draw a progress bar.
    global random_nos, total_nos, progress, temp_progress
    progress = (random_nos * 100) // total_nos
    if (progress - temp_progress) > 0:
        clearScreen()
        temp_progress = progress
        if progress < 50:
            print(
                "[",
                progress * "-",
                (50 - progress) * " ",
                progress,
                "%",
                (50) * " ",
                "]",
                sep="",
            )
        elif progress >= 50:
            print(
                "[",
                50 * "-",
                progress,
                "%",
                (progress - 50) * "-",
                (99 - progress) * " ",
                "]",
                sep="",
            )


while random_nos != (total_nos):

    a = ran.random()  # a stores the value of current random no
    # printProgress()  #if you want the progress bar
    for prob_test_no in range(10):
        timesAppear(a, prob_test_no)
    if a != None:
        print(a, end="")  # printing the random numbers
        random_nos += 1
    else:
        pass

for prob_test_no in range(10):
    print(
        f"\nprobability that {prob_test_no} occurs is {appear_count[prob_test_no]/total_nos}"
    )
print(f"\n{random_nos} Random numbers were generated")
