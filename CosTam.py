#Coding problem 'Sum "A+B"

def problem1(a, b):
    return a+b

#Coding problem 'Sum in Loop'

def problem2(list = []):
    result = 0
    for i in range(len(list)):
        result += list[i]

    return result

#Coding problem 'Sums in Loop'

def problem3(list1 = [], list2 = []):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])

    return results

#Coding problem 'Minimum of Two'

def problem3(list1 = [], list2 = []):
    results = []

    for i in range(len(list1)):
        if(list1[i] >= list2[i]):
            results.append(list2[i])
        else:
            results.append(list1[i])

    return results

#Coding problem 'Minimum of three'

def problem4(list1 = [], list2 = [], list3 = []):
    results = []
    for i in range(len(list1)):
        results.append(min(list1[i], list2[i], list3[i]))

    return results

#Coding problem 'Maxiumum of Array'

def problem5(list = []):
    minimum = float("inf")
    maximum = -1

    for i in range(len(list)):
        minimum = min(minimum, list[i])
        maximum = max(maximum, list[i])

    return minimum, maximum


#Coding problem 'Rounding'

def problem6(a, b):
    result = int(round((a/b), 0))

    return result

#Coding problem 'Fahrenheit to Celcius'

def problem7(temps = []):
    conversions = []

    for i in range(len(temps)):
        conversions.append((temps[i] - 32) * 5/9)

    return conversions

#Coding problem 'Vowel Count'

def problem8(sentence):
    vowels = 0
    for i in sentence:
        if(i == 'a' or i == 'e' or i == 'u' or i == 'i' or i == 'y' or i == 'o'):
            vowels += 1

    return vowels

#Coding problem 'Sum of digits'

def problem9(a, b, c):
    result = a * b + c
    final = 0
    
    for i in str(result):
        final += int(i)

    return final

#Coding problem 'Median of Three'

import statistics

def problem10(list = []):
    return statistics.median(list)

#Coding problem 'Arithmetic Progression'

def problem11(a, b, c):
    result = 0

    for i in range(c):
        result += a + ((i) * b)

    return result

#Coding problem 'Body Mass Index'

def problem12(weight, height):
    BMI = weight / (height ** 2)
    result = ["Underweight", "Normal weight", "Overweight", "Obesity"]

    if BMI < 18.5:
        return result[0]
    elif BMI >= 18.5 and BMI < 25:
        return result[1]
    elif BMI >= 25 and BMI < 30:
        return result[2]
    else:
        return result[3]



a = [12, 23, 42]
b = [424, 12, 22]
c = [4, 15, 17]

print(problem12(55, 1.58))