import csv
import pandas as pd
import re
import datetime

column_list=['Name', 'type', 'date added', 'expiration']
refrigerator_list = pd.read_csv("food.csv", usecols= column_list)
count = 0
new_refrigerator_list = pd.read_csv("food.csv", usecols= column_list)
for row in refrigerator_list.count(axis = "columns"):
    count +=1




def add_items():
    add = input("Would you like to add items to the fridge? (Y/N)")
    if add == "Y":
        item = input("What is the name of the item you would like to add?")
        type1 = input("What type of item is this? (dairy, meat, fruit, vegetable)")
        date_added = input("What date was this added on?(ex. mm/dd/yyyy)")
        expiration_date = input("What date does this expire on?(ex. mm/dd/yyyy)")
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
        for item in new_refrigerator_list['Name']:
            count1 += 1
            if item == remove_items:
                print("Are you sure you want to remove", remove_items,"? (Y/N)")
                are_you_sure = input()
                if are_you_sure == 'Y' or 'y':
                    row_to_remove= new_refrigerator_list.loc[[count1]]
                    print(row_to_remove)
                   
                    updated_refrigerator_list = new_refrigerator_list.drop([0,count1])
                    print(updated_refrigerator_list)

#########someone needs to do time in fridge so it uses the added date of each item in the dataframe   
# make time_passed a global variable                  
def time_in_fridge():
    today = datetime.datetime.now()
    ex_date = re.compile(r"(\d{1,2})\/(\d{1,2})\/(\d{4})")
    ex_month = ex_date.group(1)
    ex_day = ex_date.group(2)
    ex_year = ex.date.group(3)
    time_passed = (today - datetime.datetime(ex_year, ex_month, ex_days)).days
    
    for item in updated_refrigerator_list():
        return time_passed




def smell_time_passed():
    if time_passed/7 <= 1:
        smell = 0
    elif 2 >= (time_passed/7) > 1:
        smell = 2
    elif 3 >= (time_passed/7) > 2:
        smell = 4
    elif 4 >= (time_passed/7) > 3:
        smell = 6
    elif 5 >= (time_passed/7) > 4:
        smell = 8
    elif 6 >= (time_passed/7) > 5:
        smell = 10

    return smell



def smell():
    smell == 0
    total_fruit_smell = 0
    total_dairy_smell = 0
    total_meat_smell = 0
    total_vegetable_smell = 0 
    fcount = 0
    dcount = 0
    mcount = 0
    vcount = 0
    for item in new_refrigerator_list['type']:
        if item == 'fruit':
            count +=1
            total_fruit_smell += smell_time_passed()
    fruit = total_fruit_smell / fcount
    for item in new_refrigerator_list['type']:
        if item == 'dairy':
            count +=1
            total_dairy_smell += smell_time_passed()   
    dairy = total_dairy_smell / dcount   
    for item in new_refrigerator_list['type']:
        if item == 'meat':
            count +=1
            total_meat_smell += smell_time_passed()   
    meat = total_meat_smell / dcount  
    for item in new_refrigerator_list['type']:
        if item == 'vegetable':
            count +=1
            total_vegetable_smell += smell_time_passed()   
    vegetable = total_vegetable_smell / dcount

    TOTAL_FRIDGE_SMELL = (fruit+dairy+meat+vegetable)/4
    print(TOTAL_FRIDGE_SMELL)

def save_to_file():
    updated_refrigerator_list.to_csv("Final_Refrigerator_List.csv")


def __main__():
    add_items()
    remove_items()
    time_in_fridge()
    smell()
    save_to_file()

if __name__ == __main__():
    __main__()