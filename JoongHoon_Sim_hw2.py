# libraries
import csv
import json
from collections import defaultdict
from statistics import mean

# csvRatings - reads data from csv and calculates mean
def csvRatings():
    with open('movies.csv') as file:
        reader = csv.DictReader(file)
        ratingsDict = defaultdict(list)
        for row in reader:
            ratingsDict[int(row['movieID'])].append(int(row['rating']))
        for key in ratingsDict:
            ratingsDict[key] = mean(ratingsDict[key])
        return ratingsDict 


# Task 1 - writes average ratings to csv without header
def task1():
    
    movieIDRatings = csvRatings()
    
    filename = 'task1.csv'
    with open(filename, mode = 'w', newline='') as csvFile:
        fieldnames = ['movieID', 'avgRating']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        
        for row in sorted(movieIDRatings.keys()):
            writer.writerow({'movieID': row, 
                            'avgRating': round(movieIDRatings[row], 1)})


# Task 2 - writes average ratings to csv with header
def task2():
    
    movieIDRatings = csvRatings()

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

        # copy metadata only 
        dataCopy = {'metadata': data['metadata'], 'data': {}}
        print(dataCopy)
        
        

    ratingsDict = defaultdict(list)

    for row in data['data']:
        movieID = row[1]
        rating = row[2]
        ratingsDict[int(movieID)].append(int(rating))
    #print(ratingsDict)
    for key in sorted(ratingsDict):
        dataCopy['data'][key] = round(mean(ratingsDict[key]), 1)
        
    # write to file
    with open('task3.json', 'w') as fout:
        json.dump(dataCopy, fout, indent=4)
    

def main():
    
    #task1()
    #task2()
    task3()


if __name__ == "__main__":
    main()