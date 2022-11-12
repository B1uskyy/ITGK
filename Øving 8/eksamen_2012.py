# 2 a)

# def summerOlympics(firstYear, lastYear):

#     year = 1944

#     years = []

#     olympic_years = []

#     for _ in range(20):
#         olympic_years.append(year + 4)
#         year = year + 4

#     for år in olympic_years:
#         if firstYear <= år and lastYear >= år:
#             years.append(år)

#     return years


# print(summerOlympics(1999, 2012))


# 2 b)

import random
from datetime import datetime


def current_date():
    yyyy = int(datetime.today().strftime('%Y'))
    mm = int(datetime.today().strftime('%m'))
    dd = int(datetime.today().strftime('%d'))
    return yyyy, mm, dd


def findAge(bYear, bMonth, bDay):
    today = current_date()

    year, month, day = today[0], today[1], today[2]

    years = (year - bYear)

    if month < bMonth:
        years = years - 1

    elif month == bMonth:
        if bDay > day:
            years = years - 1

    return years


# print(findAge(2002, 11, 10))

def printAgeDiff(table):

    for element in table:

        person = element[0:2]
        birthday = element[2:5]

        year = birthday[0]
        month = birthday[1]
        date = birthday[2]

        ages = findAge(year, month, date)


printAgeDiff(table=[['Justin', 'Bieber', 1994, 3, 1],
                    ['Donald', 'Duck', 1934, 8, 1],
                    ['George', 'Clooney', 1961, 5, 6],
                    ['Eddie', 'Murphy', 1961, 4, 3]])

# 4a


def cold_days(templist):

    days = 0

    for temp in templist:
        if temp < 0:
            days += 1
    return days


days = cold_days([1, -5, 3, 0, -6, -3, 15, 0])

# 4b


def cap_data(A, min_value, max_value):
    result = []

    for temp in A:
        if temp > min_value and temp < max_value:
            result.append(temp)

        elif temp < min_value:
            result.append(min_value)

        else:
            result.append(max_value)

    return result


A = [-70, 30, 0, 90, 23, -12, 95, 12]
result = cap_data(A, -50, 50)

# print(result)

# 4d


# 4c


def generate_testdata(N, min_value, max_value):

    randtall = random.sample(range(min_value, max_value), N)

    return randtall


result = generate_testdata(10, -5, 10)

# print(result)


temp = [1, 5, 3]
rain = [0, 30, 120]
humidity = [30, 50, 65]
wind = [3, 5, 7]


def create_db(temp, rain, hunidity, wind):

    database = {}
    day = 1

    for i in range(len(temp)):
        database[day] = temp[i], rain[i], hunidity[i], wind[i]
        day += 1

    return database


weather = create_db(temp, rain, humidity, wind)

# print(weather)


# 4e

def print_db(weather):

    print("Day | Temp | Rain | Humidity | Wind")
    print("====+======+======+==========+======")

    # .rjust()

    for day, values in weather.items():
        # print(day)
        temp = values[0]
        rain = values[1]
        humidity = values[2]
        wind = values[3]

        print(str(day).rjust(4), str(temp).rjust(6), str(rain).rjust(
            6), str(humidity).rjust(10), str(wind).rjust(6))


print_db(weather)
