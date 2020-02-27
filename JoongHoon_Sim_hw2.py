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


# Task 3 - writes average ratings to json
def task3():
    with open('movies.json') as jsonFile:
        data = json.load(jsonFile)

        # json to write to file
        dataCopy = {'metadata': {
                        'info': {
                            'author': 'Joong Hoon Sim',
                            'organization': 'USC', 
                            'creation_date': '2/24/2020'
                        },
                        'columns': {
                            'movieID': 'movie id for the movies', 
                            'avg_rating': 'average rating given to the movies'
                        }
                        }, 
                    'data':[]}
        
    ratingsDict = defaultdict(list)

    for row in data['data']:
        movieID = row[1]
        rating = row[2]
        ratingsDict[int(movieID)].append(int(rating))
    
    for key in sorted(ratingsDict):
        avgRating = round(mean(ratingsDict[key]), 1)
        dataCopy['data'].append([key, avgRating])
        
    # write to file
    with open('task3.json', 'w') as fout:
        json.dump(dataCopy, fout, indent=4)
    
# Task 4 - converts task3.json to csv format
def task4():
    with open('task3.json') as fin:
        data = json.load(fin)

    # dictionaries for each section
    infoDict = data['metadata']['info']
    colDict = data['metadata']['columns']
    dataDict = data['data']

    # build header from dictionaries
    header = ','.join(infoDict.keys()) + '\n' + ','.join(infoDict.values()) +'\n\n'
    header += ','.join(colDict.keys())+'\n'
    


    with open('task4.csv', mode = 'w', newline='') as fout:
        fieldnames = ['movieID', 'avg_rating']
        writer = csv.writer(fout)
        fout.write(header)

        for row in dataDict:
            writer.writerow(row)
            

def main():
    
    #task1()
    #task2()
    #task3()
    task4()

if __name__ == "__main__":
    main()