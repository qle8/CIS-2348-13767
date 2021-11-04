# Student Name: Quang Le
# ID: 1768324
# Class Number: CIS-2348-13767
# Professor: Edward Ratner
import csv
import time
import copy

class InputList:

## InputList class imports ManufacturerList.csv, PriceList.csv, ServiceDatesList.csv files into data sets of manufacturer, type, damage, price, and service date

    def manufacturer():
        with open('ManufacturerList.csv', 'r') as csvfile:
            manufacturer_reader = csv.reader(csvfile, delimiter=',')
            mfr = {}
            for row in manufacturer_reader:
                mfr[row[0]] = row[1]
            return mfr

    def type():

        with open('ManufacturerList.csv', 'r') as csvfile:
            type_reader = csv.reader(csvfile, delimiter=',')
            typ = {}
            for row in type_reader:
                typ[row[0]] = row[2]
            return typ

    def damage():

        with open('ManufacturerList.csv', 'r') as csvfile:
            damaged_reader = csv.reader(csvfile, delimiter=',')
            dam = {}
            for row in damaged_reader:
                dam[row[0]] = row[3]
            return dam

    def price():

        with open('PriceList.csv', 'r') as csvfile:
            price_reader = csv.reader(csvfile, delimiter=',')
            prc = {}
            for row in price_reader:
                prc[row[0]] = row[1]
            return prc

    def service():

        with open('ServiceDatesList.csv', 'r') as csvfile:
            service_reader = csv.reader(csvfile, delimiter=',')
            svc = {}
            for row in service_reader:
                svc[row[0]] = row[1]
            return svc

class WriteOutput:

## WriteOutput class write all .csv reports

    ## This function write Full Inventory Report. It takes a comprehensive data list as parameter
    def writeFullInv(full_list):
        ## Because list is already sorted by manufacturer, we can output it directly to FullInventory.csv
        with open('FullInventory.csv', 'w', newline='') as scvFullInv:
            full_inv = csv.writer(scvFullInv)
            full_inv.writerows(full_list)

    ## This function write Full Inventory Report. It takes a comprehensive data list and type list as parameter
    def writeTypeInv(full_list, type_list):
        sorted_list = sorted(full_list, key=lambda k: k[0])

        # This block of code is to find unique types of items in inventory, to be used later to name item files
        types_list = []
        for rowUnq in type_list:
            types_list.append(type_list[rowUnq])
        unique_types = set(types_list)

        # This block of code reformat the list to NOT include type
        # In python, an object can't be copied with Assignment. However, using 'copy' module, it is possible to make a deep copy of the list as 2D.
        duplicatelist1 = copy.deepcopy(sorted_list)
        for rowDup in duplicatelist1:
            rowDup.pop(2)

        # This block of code write Inventory
        for rowInv in unique_types:
            invFmt = rowInv.strip().capitalize()
            with open('{}Inventory.csv'.format(invFmt), 'w', newline='') as scvfl:
                grades_writer = csv.writer(scvfl)
                # To know if an item belongs to its respective inventory file, its type needs to be checked
                # As a copy of list early before remove the types, original list will be used to check
                counter = 0
                for rowCounter in sorted_list:
                    if sorted_list[counter][2] == rowInv:
                        grades_writer.writerow(duplicatelist1[counter])
                    counter += 1

    ## This function write Past Service Dates Inventory Report. It takes a comprehensive data list as parameter
    def writePastDateInv(full_list):
        # Time module is imported to work with time-related inputs
        # This line sort the list by time
        sorted_list = sorted(full_list, key=lambda k: time.strptime(k[4], "%m/%d/%Y"))

        # This block of code determine if sorted_list has any items past service date. If it is, that item won't be imported to servicelist
        today = time.localtime()
        servicelist = []
        for rowSort in sorted_list:
            date_format = time.strptime(rowSort[4], "%m/%d/%Y")
            if date_format < today:
                servicelist.append(rowSort)

        # Write to file
        with open('PastServiceDateInventory.csv', 'w', newline='') as scvflx:
            serviceWriter = csv.writer(scvflx)
            serviceWriter.writerows(servicelist)

    ## This function write Damaged Inventory Report. It takes a comprehensive data list as parameter
    def writeDmgInv(full_list):
        sorted_list = sorted(full_list, key=lambda k: int(k[3]), reverse=True)

        # This block of code determine if sorted_list has any damaged item. If it is, it wont be imported to damagedList
        damaged_list = []
        for rowDam in sorted_list:
            if rowDam[5] == "damaged":
                damaged_list.append(rowDam)

        # This block code remove the 'damaged' tag from the list
        # For posterity, damaged_list is a copy, and only damaged_copy is edited
        damaged_copy = copy.deepcopy(damaged_list)
        for rowCop in damaged_copy:
            rowCop.pop(5)

        # Write to file
        with open('DamagedInventory.csv', 'w', newline='') as scvflq:
            dmgWriter = csv.writer(scvflq)
            dmgWriter.writerows(damaged_copy)


class DataDict:

    # This function generate a data dictionary from lists. Takes manufacturer list, type list, price list, service date list, and damage status list as parameters, respectively
    def generateDataDict(manufacturer, type, price, service, damage):
        ## Goal: Using all the available informations from these list to generate a comprehensive dictionary of inventory
        ## Dictionary format: {(item_id_1: [manufacturer_1, type_1, price_1, service_date_1, damage_status_1]), (item_id_2: [etc.])]

        # This block of code List all item ids as keys, using item ids from manufacturer
        u = manufacturer.keys()
        list_keys = []
        for row1 in u:
            list_keys.append(row1)

        comprehensive_data_dict = {}
        for row2 in list_keys:
            comprehensive_data_dict[row2] = [manufacturer[row2], type[row2], price[row2], service[row2], damage[row2]]
        return comprehensive_data_dict

    # This function generate a sorted list. Takes data dictionary generated by DataDict.generateDataDict as parameter
    def dictToSortedList(data_dict):
        ## After obtaining data dictionary, it will be converted to a sorted list (since dictionary is unsorted)
        ## The first list will be a comprehensive list of all data in data dictionary, sorted by manufacturer
        ## Each sorted list thereafter will be based off this list, and will be re-sorted depending of on the required output contents

        # sort_tuple format: [(item_id_1, [manufacturer_1, type_1, price_1, service_date_1, damage_status_1]), (item_id_2, [manufacturer_2, ...])]
        sort_tuple = sorted(data_dict.items(), key=lambda k: k[1][0])

        # This block of codes changes the sortlist from a list of tuples to a list of lists, to make it easier to edit and output to .csv files
        # sort_list format: [[item_id_1, manufacturer_1, type_1, price_1, service_date_1, damage_status_1], [item_id_2, manufacturer_2, ...]]
        sort_list = []
        list_counter = 0
        for row_sort in sort_tuple:
            temp_list = []
            temp_list.append(row_sort[0])
            temp_list.append(row_sort[1][0])
            temp_list.append(row_sort[1][1])
            temp_list.append(row_sort[1][2])
            temp_list.append(row_sort[1][3])
            temp_list.append(row_sort[1][4])
            sort_list.append(temp_list)
            list_counter += 1

        return sort_list



## The main code process will run from here
if __name__ == "__main__":

    # Receive all inputs files into lists
    a = InputList.manufacturer()
    b = InputList.type()
    c = InputList.price()
    d = InputList.service()
    e = InputList.damage()

    ## DataDict class is used to generate full dictionary and sort it into a list
    data_dict = DataDict.generateDataDict(a, b, c, d, e)
    n = DataDict.dictToSortedList(data_dict)

    ## Call WriteInventory class to write reports
    WriteOutput.writeFullInv(n)
    WriteOutput.writeTypeInv(n, b)
    WriteOutput.writePastDateInv(n)
    WriteOutput.writeDmgInv(n)

