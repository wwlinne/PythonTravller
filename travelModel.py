# Author: Guohui Wan 041059351
# Date: Nov 9, 2023
# Modified Date: Nov 28, 2023
# Description: Model for travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
#!/Library/Frameworks/Python.framework/Versions/3.11 Python
import csv
from travelRecord import TravelRecord
class Model:
    def __init__(self, filename):
        self.filename = filename
        self.records = self._read_travel_records(filename, 100)
    #program by Guohui Wan 041059351 wan00038 
    def _read_travel_records(self, filename, num):
        records = []
        try:
            with open(filename, 'r') as file:
                travelR = csv.reader(file)
                columnInfo = False
                for col in travelR:
                    if not columnInfo:
                        columnInfo = True
                        continue
                    if len(records) >= num:
                        break
                    record = TravelRecord(
                        col[0],   # ref_number
                        col[2],   # title_en
                        col[5],   # purpose_en
                        col[7],   # start_date
                        col[8],   # end_date
                        col[11],   # airfare
                        col[12],   # other_transport
                        col[13],   # lodging
                        col[14],   # meals
                        col[15],   # other_expenses
                        col[16]   # total
                )
                    records.append(record)
        except FileNotFoundError:
            print("File not found")
            raise
        except Exception as e:
            print(f"Something wrong: {e}")
        return records
    '''This function is used to reload the data into the memory'''
    def reload_data(self):
        self.records = self._read_travel_records(self.filename, 100)
        print("Data reloaded successfully.")
    #program by Guohui Wan 041059351 wan00038
    '''This function is used to write the in memory data into a new CSV file'''
    def persist_data(self, new_filename):
        try:
            with open(new_filename, 'w', newline = '') as file:
                travelW = csv.writer(file, delimiter=',')
                travelW.writerow(['Ref_Number', 'Title', 'Purpose', 
                                  'Start_Date', 'End_Date', 'Aircraft', 
                                  'Other_Transport', 'Lodging', 'Meals', 'Other_Expenses', 'Total'])
                for record in self.records:
                    travelW.writerow([record.Ref_Number, record.Title, 
                                      record.Purpose, record.Start_Date, record.End_Date, 
                                      record.Aircraft, record.Other_Transport, record.Lodging, 
                                      record.Meals, record.Other_Expenses, record.Total])
            print("Data saved successfully to:", new_filename)
        except Exception as e:
            print(f"Error writing to file: {e}")
    '''These two functions is used to display one record or all records'''
    '''Nov 09 modified for RA3 '''
    def display_one_record(self):
        index = int(input("Enter the index of the record you want to display: "))
        if 0 <= index < len(self.records):
            print(self.records[index].display_record())
        else:
            print("Invalid index.")
    def display_all_records(self):
        for index, record in enumerate(self.records):
                    print(record.display_record())
                    if (index + 1) % 10 == 0:
                        print("Guohui Wan #041059351 wan00038")
    '''This function is used to create a new record and store it in the memory'''
    def create_record(self, ref_number, title, purpose, start_date, end_date, aircraft, other_transport, lodging, meals, other_expenses, total):
        record = TravelRecord(
            ref_number, title, purpose, start_date, end_date, aircraft, other_transport, lodging, meals, other_expenses, total
        )
        self.records.append(record)
    '''This function is used to edit the selected index of record'''
    def edit_record(self, index, new_values):
        if 0 <= index < len(self.records):
            record = self.records[index]
            for key, value in new_values.items():
                setattr(record, key, value)
        else:
            print("Invalid index.")
    '''This function is used to delete the selected index of record'''
    def delete_record(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]
        else:
            print("Invalid index.")
    '''Modified at Nov 28 Created by GuohuiWan #041059351'''
    '''This function is used to search and display the record, the criteria is we set to find the match record'''
    '''getattr() can help us to find the attribute value of the record object''' 
    '''we use == to test if the attribute of record we found is equal to the values after applying the criteria'''
    '''If it is true, then we have found the match record. else is false.'''
    def search_and_display_records(self, criteria):
        found_record = False
        for index, record in enumerate(self.records):
            match = all(getattr(record, attribute) == value for attribute, value in criteria.items())
            if match:
                print(self.records[index].display_record())
                found_record = True
        if not found_record:
            print("No matching records found.")
    
  
            
    
