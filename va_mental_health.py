#program converts json to csv file that's readable in excel
#if val is % then converted to a floating val with two decimals of accuracy then back to str
#if val number with commas -> remove commas from the number
# csv should have header from the keys in the json file


import json 
import csv

def read_json():
    with open('station-data.json', 'r') as json_file:
        data = json.load(json_file)
        for record in data:
            if record.get('ValueType') == 'Percent':
                modify_value = round(float(record.get('Value').replace('%',''))/100, 2)
                record['Value'] = str(modify_value)
  
            if record.get('ValueType') == 'Number':
                record['Value'] = record['Value'].replace(',', '')
        return data
        

def create_csv():
    json_data = read_json()
    headers = json_data[0].keys()
    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for record in json_data:
            rec = [val for val in record.values()]
            writer.writerow(rec)

def main():
    create_csv()







if __name__ == "__main__":
    main()