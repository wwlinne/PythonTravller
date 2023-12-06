# Author: Guohui Wan 041059351
# Date: Oct 8, 2023
# Modified Date: Nov 28, 2023
# Description: View for travel records.
# Datasource: https://open.canada.ca/data/en/dataset/009f9a49-c2d9-4d29-a6d4-1a228da335ce/resource/8282db2a-878f-475c-af10-ad56aa8fa72c
# OpenLicense: https://open.canada.ca/en/open-government-licence-canada
class View:
    def __init__(self, controller):
        self.controller = controller
    '''In this function, we create a decision structure to handle the options chosen by users.'''         
    def display_menu(self):
         while True:
            print("\nOptions:")
            print("1. Reload Data")
            print("2. Persist Data")
            print("3. Display One Record")
            print("4. Display All Records")
            print("5. Create a New Record")
            print("6. Edit a Selected Record")
            print("7. Delete a Selected Record")
            print("8. Search and Display record")
            print("9. Quit")
            print("Program by Guohui Wan #041059351 wan00038")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.controller.reload_data()
            elif choice == "2":
                new_filename = input("Enter the new filename to save data(e.g. test.csv): ")
                self.controller.persist_data(new_filename)
            elif choice == "3":
                self.controller.display_one_record()
            elif choice == "4":
                self.controller.display_all_records()
            elif choice == "5":
                self.controller.create_and_store_record()
            elif choice == "6":
                self.controller.edit_selected_record()
            elif choice == "7":
                self.controller.delete_selected_record()
            elif choice == "8":
                self.controller.display_record_based_on_search()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please try again.")

