# Author: Guohui Wan 041059351
# Date: Nov 9, 2023
# Description: Model for travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
class Record:
    '''This is the super class object we have created for managing travel records.'''
    def __init__(self, Ref_Number):
        self.Ref_Number = Ref_Number 
        
    '''display_record is the funtion used to print travel record object'''
    def display_record(self):
        return f"Ref_Number: {self.Ref_Number}"
