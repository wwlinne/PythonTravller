# Author: Guohui Wan 041059351
# Date: Oct 8, 2023
# Modified Date: Nov 28, 2023
# Description: Controller for travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
class Controller:
    def __init__(self, model):
        self.model = model
    '''This function will reload the date in the memory'''    
    def reload_data(self):
        self.model.reload_data()
    '''This funtion is used to save into a new CSV file'''
    def persist_data(self, new_filename):
        self.model.persist_data(new_filename)
    '''To display one record or all records'''
    def display_one_record(self):
        self.model.display_one_record()
    def display_all_records(self):
        self.model.display_all_records()
    '''This function is used to accept the user input, and then we call the create_record() method in Model, then we can update the data in memory.'''
    def create_and_store_record(self):
        '''We use try block to handle the exceptions for the float numbers'''
        ref_number = input("Enter Ref Number(String): ")
        title = input("Enter Title(String): ")
        purpose = input("Enter Purpose(String): ")
        start_date = input("Enter Start Date(String): ")
        end_date = input("Enter End Date(String): ")
        try:
            aircraft = float(input("Enter Aircraft(Number): "))
            other_transport = float(input("Enter Other Transport(Number): "))
            lodging = float(input("Enter Lodging(Number): "))
            meals = float(input("Enter Meals(Number): "))
            other_expenses = float(input("Enter Other Expenses(Number): "))
            total = float(input("Enter Total: "))
        except ValueError:
            print("Invalid input for numeric fields(Aircraft-Total). Please enter numeric values.")
            return

        self.model.create_record(
            ref_number, title, purpose, start_date, end_date, aircraft, other_transport, lodging, meals, other_expenses, total
        )
        print("Record created and stored successfully.")
    '''This function is used to accept the user input to edit the selected record and update it into the memory.'''
    def edit_selected_record(self):
        index = int(input("Enter the index of the record you want to edit: "))
        if 0 <= index < len(self.model.records):
            new_values = {}
            record = self.model.records[index]
            '''This can make sure user edit in the correct order.'''
            attributes_to_edit = ['Ref_Number', 'Title', 'Purpose', 'Start_Date', 'End_Date', 'Aircraft', 'Other_Transport', 'Lodging', 'Meals', 'Other_Expenses', 'Total']
            
            for attribute in attributes_to_edit:
                new_value = input(f"Enter new value for {attribute}(Use Correct Format): ")
                new_values[attribute] = new_value

            self.model.edit_record(index, new_values)
            print("Record edited successfully.")
        else:
            print("Invalid index.")
    '''This function is used to delete the selected index of record and update the data in memory.'''
    def delete_selected_record(self):
        index = int(input("Enter the index of the record you want to delete: "))
        if 0 <= index < len(self.model.records):
            self.model.delete_record(index)
            print("Record deleted successfully.")
        else:
            print("Invalid index.")
    '''Modified at Nov 28 Created by Guohui Wan 041059351'''
    '''This function is used to accept the input of the date and then use input as the search criteria.'''    
    def display_record_based_on_search(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        total_str = input("Enter total fee:")
        total = float(total_str)
        criteria = {'Start_Date': start_date, 'End_Date': end_date, 'Total': total}
        self.model.search_and_display_records(criteria)
       
