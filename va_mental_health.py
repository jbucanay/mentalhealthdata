#program converts json to csv file that's readable in excel
#if val is % then converted to a floating val with two decimals of accuracy then back to str
#if val number with commas -> remove commas from the number
# csv should have header from the keys in the json file

import json 
import csv

def read_json():
    fl = open('station-data.json', 'r')
    data = json.load(fl)
    print(data[0])
    print(data[1])

def create_csv():
    pass

def main():
    read_json()







if __name__ == "__main__":
    main()