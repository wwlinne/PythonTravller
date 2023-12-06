# Author: Guohui Wan 041059351
# Date: Oct 8, 2023
# Modified Date: Oct 11, 2023
# Description: Main method for MVC pattern of travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
from travelModel import Model
from travelView import View
from travelController import Controller
'''In this class, we can test our files and easily change the file by modifying the filename.'''
def main():
    filename = "travelq.csv"
    model = Model(filename)
    controller = Controller(model)
    view = View(controller)
    view.display_menu()
'''We can call view.display_menu() to see the menu.'''
if __name__ == "__main__":
    main()
