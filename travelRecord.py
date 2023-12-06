# Author: Guohui Wan 041059351
# Date: Nov 9, 2023
# Description: Model for travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
from record import Record
class TravelRecord(Record):
    '''This is the sub-classed record object, we changed the record format here.'''
    def __init__(self, Ref_Number, Title, Purpose, Start_Date, 
                 End_Date, Aircraft, Other_Transport, Lodging, Meals, Other_Expenses, Total):
        super().__init__(Ref_Number)
        self.Title = Title
        self.Purpose = Purpose
        self.Start_Date = Start_Date
        self.End_Date = End_Date
        self.Aircraft = float(Aircraft) if Aircraft else None
        self.Other_Transport = float(Other_Transport) if Other_Transport else None
        self.Lodging = float(Lodging) if Lodging else None
        self.Meals = float(Meals) if Meals else None
        self.Other_Expenses = float(Other_Expenses) if Other_Expenses else None
        self.Total = float(Total) if Total else None
    def display_record(self):
        return f"Ref_Number: {self.Ref_Number}, Title: {self.Title}, Purpose: {self.Purpose}, Start_Date: {self.Start_Date}, End_Date: {self.End_Date}, Aircraft: {self.Aircraft}, Other_Transport: {self.Other_Transport}, Lodging: {self.Lodging}, Meals: {self.Meals}, Other_Expenses: {self.Other_Expenses}, Total: {self.Total}"
