# libraries
import csv
import json
from collections import defaultdict
from statistics import mean


def csvRatings():
    reader = csv.DictReader(open('movies.csv'))
    ratingsDict = defaultdict(list)
    for row in reader:
        ratingsDict[int(row['movieID'])].append(int(row['rating']))
    for key in ratingsDict:
        ratingsDict[key] = mean(ratingsDict[key])
    return ratingsDict


# Task 1
def task1():
    reader = csv.DictReader(open('movies.csv'))
    movieIDRatings = defaultdict(list)
    for row in reader:
        movieIDRatings[int(row['movieID'])].append(int(row['rating']))
    for key in movieIDRatings:
        movieIDRatings[key] = mean(movieIDRatings[key])
    filename = 'task1.csv'
    with open(filename, mode = 'w', newline='') as csvFile:
        fieldnames = ['movieID', 'avgRating']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        
        for row in sorted(movieIDRatings.keys()):
            writer.writerow({'movieID': row, 
                            'avgRating': round(movieIDRatings[row], 1)})


# Task 2
def task2():
    reader = csv.DictReader(open('movies.csv'))
    movieIDRatings = defaultdict(list)
    for row in reader:
        movieIDRatings[int(row['movieID'])].append(int(row['rating']))
    for key in movieIDRatings:
        movieIDRatings[key] = mean(movieIDRatings[key])
    filename = 'task2.csv'
    with open(filename, mode = 'w', newline='') as csvFile:
        fieldnames = ['movieID', 'avgRating']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in sorted(movieIDRatings.keys()):
            writer.writerow({'movieID': row, 
                            'avgRating': round(movieIDRatings[row], 1)})


# Task 3
def task3():
    with open('movies.json') as jsonFile:
        data = json.load(jsonFile)
        jsonStr = json.dumps(data, indent = 4)

    print(jsonStr)

def main():
    
    task1()
    task2()
    task3()


if __name__ == "__main__":
    main()