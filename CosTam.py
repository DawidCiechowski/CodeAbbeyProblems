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

#Coding problem 'Triangles'

def problem13(a, b, c):
    if((a+b) > c):
        return 1
    else:
        return 0

#Coding problem 'Weighted sum of digits'

def problem14(number):
    result = 0
    stringified = str(number)
    for i in range (len(stringified)):

        result += ((i+1) * int(stringified[i]))

    return result

#Coding problem 'Average of an array'

def problem15(list = []):
    average  = 0

    for i in list:
        average += i

    return average/len(list)

#Coding problem 'Dice roll'
import math
def problem16(n):
    return math.floor(n * 6) + 1


#Coding problem 'Array Checksum'

def problem17(list = []):
    result = 0

    #Changes have been made to this problem, to complement problem 25 in which it was reused.
    for i in range(len(list) - 1):
        result += list[i]
        result *= 113 

    return result % 10000007

#Coding problem 'Reverse String'

def problem18(string):
    return string[::-1]

    
#Coding problem 'Array Counters'

def problem19(list = []):
    results = []

    for i in range(len(list)):
        counter = 0

        for j in list:
            if j == i:
                counter += 1
        
        if(counter > 0):
            results.append(counter)


    return results

#Coding problem 'Collatz Sequence'

def problem20(start):

    counter = 0
    while(start != 1):
        if(start % 2 == 0):
            start = start / 2
            counter += 1
        else:
            start = 3 * start + 1
            counter += 1

    return counter

#Coding problem 'Modulo and time difference'

def problem21(day1, hour1, min1, sec1, day2, hour2, min2, sec2):
    dayDiff = day2-day1
    hourDiff = hour2 - hour1
    minDiff = min2 - min1
    secDiff = sec2 - sec1

    if(dayDiff < 1):
        dayDiff = 31 + dayDiff

    if(hourDiff < 0):
        hourDiff = 24 + hourDiff

    if(minDiff < 0):
        minDiff = 60 + minDiff

    if(secDiff < 0):
        secDiff = 60 + secDiff

    return dayDiff, hourDiff, minDiff, secDiff 

#Coding problem 'Modular Calculator'

def problem22(initial, signs = [], numbers = []):
    final = initial
    for i in range(len(signs) - 1):
        if signs[i] == "*":
            final *= numbers[i]
        else:
            final += numbers[i]
    
    return final % numbers[len(numbers) - 1]

#Coding problem 'Greatest common divisor'

def problem23(a, b):
    gcd = 0
    for i in range(min(a, b) - 1):
        if((a % (i+1)) == 0 and (b % (i+1)) == 0):
            gcd = i + 1

    lcm = a * b / gcd

    return gcd, int(lcm)
    
#Coding problem 'Sort with Indexes'

def problem24(list = []):
    indexes = {}
    counter = 1
    result = []

    for i in list:
        indexes[i] = counter
        counter += 1

    list = sort_list(list)


    result = pair_results(indexes, list)

    return result

def sort_list(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]: 
                list[j], list[j+1] = list[j+1], list[j] 

    return list

def pair_results(ind, arr):
    result = []
    for val in arr:
        for key in ind:
            if(key == val):
                result.append(ind[val])

    return result

#Coding problem 'Square Root'

def problem25(x , n):
    r = 1
    d = x / r
    for i in range(n):
        d = x/r
        r = (r+d) / 2
    return r

#Coding problem 'Bubble in Array'

def problem26(list = []):
    return bubble_sort_list(list)
    
def bubble_sort_list(list):
    swaps = 0
    for j in range(len(list) - 0 - 2):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swaps += 1
    
    return swaps, problem17(list)


#Coding problem 'Palindromes'

def problem27(string):
    palindrome = ""
    for i in string:
        if(i.isalpha()):
            palindrome += i.lower()

    return palindrome == palindrome[::-1]

#Coding problem 'Rotate String'

def problem28(n, string):
    return string[n:] + string[:n]

d = ["+", "*", "+", "*", "*", "+", "%"]
a = [3, 7, 10, 2, 3, 1, 11]
b = [424, 12, 22]
c = [1, 4, 3, 2, 6, 5, -1]

print(problem28(-6, "verycomplexnumber"))

