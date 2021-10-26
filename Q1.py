# Question #1a

# contain logics of leap year, no of days in month and occurences
from datetime import date


def getSunday(startyear, endyear):
    # count the no of Sunday match
    count = 0
    # count year | endyear+1 since counter starts from 0
    for year in range(startyear, endyear+1):
        # count month
        for month in range(1, 13):
            # match date = sunday
            if date(year, month, 1).weekday() == 6:
                # add to no of count
                count += 1
    return count


print("Question 1a:")
print("No of Sundays that fell on the first of the month within the period is " +
      str(getSunday(1901, 2000)) + "\n")


# Question #1b

no = 100
result = 0
fac = 1

# factorials for loop
for i in range(no, 1, -1):
    fac = fac * i
# using repr() to convert values into "string"
facStr = repr(fac)
# get the length
length = len(facStr)
# looping in digits length
for i in range(length):
    # adding all the digits by i in [array]
    result = result + int(facStr[i])

print("Question 1b:")
print("Factorial of " + str(no) + " is " + str(fac) + "\n")
print("Sum of all the digits are ", str(result) + "\n")
