# libraries
import csv
from collections import defaultdict
from statistics import mean


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

def main():
    print("hello")
    task1()
    task2()


if __name__ == "__main__":
    main()