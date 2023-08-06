# Written by @NotScottt on Github
import datetime


def getTime():
    current_date = datetime.datetime.now()
    if len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 1:
        current_time = f"0{current_date.hour}:0{current_date.minute}"
    elif len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 2:
        current_time = f"0{current_date.hour}:{current_date.minute}"
    elif len(str(current_date.hour)) == 2 and len(str(current_date.minute)) == 1:
        current_time = f"{current_date.hour}:0{current_date.minute}"
    else:
        current_time = f"{current_date.hour}:{current_date.minute}"
    
    return current_time


def getFullDate():
    current_date = datetime.datetime.now()
    if len(str(current_date.day)) == 1 and len(str(current_date.month)) == 1:
        full_Date = (f"0{current_date.day}.0{current_date.month}.{current_date.year}")
    elif len(str(current_date.day)) == 1 and len(str(current_date.month)) == 2:
        full_Date = (f"0{current_date.day}.{current_date.month}.{current_date.year}")
    elif len(str(current_date.day)) == 2 and len(str(current_date.month)) == 1:
        full_Date = (f"{current_date.day}.0{current_date.month}.{current_date.year}")
    else:
        full_Date = (f"{current_date.day}.{current_date.month}.{current_date.year}")
    
    return full_Date

def printTime():
    current_date = datetime.datetime.now()
    if len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 1:
        current_time = f"0{current_date.hour}:0{current_date.minute}"
    elif len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 2:
        current_time = f"0{current_date.hour}:{current_date.minute}"
    elif len(str(current_date.hour)) == 2 and len(str(current_date.minute)) == 1:
        current_time = f"{current_date.hour}:0{current_date.minute}"
    else:
        current_time = f"{current_date.hour}:{current_date.minute}"
    
    print(current_time)


def printFullDate():
    current_date = datetime.datetime.now()
    if len(str(current_date.day)) == 1 and len(str(current_date.month)) == 1:
        full_Date = (f"0{current_date.day}.0{current_date.month}.{current_date.year}")
    elif len(str(current_date.day)) == 1 and len(str(current_date.month)) == 2:
        full_Date = (f"0{current_date.day}.{current_date.month}.{current_date.year}")
    elif len(str(current_date.day)) == 2 and len(str(current_date.month)) == 1:
        full_Date = (f"{current_date.day}.0{current_date.month}.{current_date.year}")
    else:
        full_Date = (f"{current_date.day}.{current_date.month}.{current_date.year}")
    
    print(full_Date)