import csv
import pandas as pd
import re

column_list=['Name', 'type', 'date added', 'expiration']
refrigerator_list = pd.read_csv("food.csv", usecols= column_list)
count = 0
#######print(refrigerator_list)
new_refrigerator_list = pd.read_csv("food.csv", usecols= column_list)
for row in refrigerator_list.count(axis = "columns"):
    count +=1




def add_items():
    add = input("Would you like to add items to the fridge? (Y/N)")
    if add == "Y":
        item = input("What is the name of the item you would like to add?")
        type1 = input("What type of item is this? (dairy, meat, fruit, vegetable)")
        date_added = input("What date was this added on?(ex. 15-Dec)")
        expiration_date = input("What date does this expire on?(ex. 15-Dec)")
        item_name = [item]
        item_type = [type1]
        item_date = [date_added]
        item_expiration = [expiration_date]
        new_item = pd.DataFrame({
            'Name':item_name,
            'type':item_type,
            'date added':item_date,
            'expiration':item_expiration})
        global new_refrigerator_list
        new_refrigerator_list = new_item.append(refrigerator_list, ignore_index = True)
        print(new_refrigerator_list)
    else:
        return
        

def remove_items():
    count1 = -1
    remove = input("Would you like to remove items? (Y/N)")
    if remove == "Y":
        print(new_refrigerator_list['Name'])
        remove_items = input("What items would you like to remove?")
        # for row in range(1,count):
        #     name = refrigerator_list.iloc[row,0]
        #     for item in name:
        #         if remove_items == item:
        #             are_you_sure = input("Are you sure you want to remove ", remove_items,"?")
        #         else:
        #             pass

        # for row in range(count):
        for item in new_refrigerator_list['Name']:
            count1 += 1
            if item == remove_items:
                print("Are you sure you want to remove", remove_items,"? (Y/N)")
                are_you_sure = input()
                if are_you_sure == 'Y' or 'y':
                    row_to_remove= new_refrigerator_list.loc[[count1]]
                    print(row_to_remove)
                    #updated_refrigerator_list = new_refrigerator_list.drop(new_refrigerator_list.loc[count1], axis = 0, inplace = True)
                    updated_refrigerator_list = new_refrigerator_list.drop([0,count1])
                    print(updated_refrigerator_list)
                    




def __main__():
    add_items()
    remove_items()
if __name__ == __main__():
    __main__()