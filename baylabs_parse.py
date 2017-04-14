#!/usr/bin/python3
from random import randint
from os.path import isfile


def create_file():
    with open('patients.csv', 'w') as f:
        for x in range(100):
            year = randint(1990, 2017)
            exam_id = randint(0, 10)
            patient_id = randint(0,99)
            entry = '{:02d},{:02d},{:04d}\n'.format(exam_id,
                                                    patient_id,
                                                    year )
            f.write(entry)
        

def parse_patients():
    year = dict()
    counter = 1
    duplicates = set()
    with open('./patients.csv', 'r') as f:
        for line in f:
            date = line.split(',')[2]
            patient_id = line.split(',')[1]

            if date not in year or patient_id not in duplicates:
                year[date] = counter
                duplicates.add(patient_id)
            else:
                year[date] += counter

    print(year.values())


if __name__=='__main__':
    if isfile('./patients.csv'):
        print("file exists")
    else:
         create_file()
    parse_patients()
