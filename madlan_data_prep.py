# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
import re
from datetime import datetime
# Importing the dataset
df = pd.read_csv(filedialog.askopenfilename()) 
cities = pd.read_csv(filedialog.askopenfilename())#cities4
##cities = pd.read_csv('cities4.csv')
data=df.copy()
data.tail()

def intPrice(value):
    value = str(value)
    x = re.findall('[0-9,]+',value)
    if len(x)==0:
        return None
    else:
        if x[0].isdigit()==True:
            return x[0]
        else:
            nums = x[0].split(",")
            num = nums[0]
            for i in range (1,len(nums)):
                num = num +nums[i]
            return num
        
def hebName (value):
    value = str(value)
    x = re.findall('[קראטוןםפשדגכיעלחךףזסבהנמתצץ ]+',value) #+X[קראטוןםפשדגכיעלחךףזסבהנמתצץ]:',value)
    if len(x)>1 :
        name = x[0]
        for i in range (1,len(x)):
            name = name +x[i]
        return name
    if len(x)==0:
        return None
    return x[0]

def floor (value) :
    if value == "קומת קרקע"  :
        return (0,0)
    if value == "קרקע"  :
        return (0,0)
    if value == "קומת מרתף" :
        return (-1,0)
    values=str(value).split(" ")
    if len(values) ==1:
        return (None,None)
    if values[1] == 'קרקע' :
        return (None,None)
    if len(values) ==4:
        return (values[1],values[3])
    

def getTotalFloor (value) :
    if value ==None:
        return
    return value[1]

    
def getFloor (value) :
    if value ==None:
        return
    return value[0]


def replace_time(value):
    event_time = datetime.strptime(value, '%d/%m/%Y')
    a=event_time-datetime.today()
    days=a.days
    if days<180 :
        value = "less_than_6 months"
    elif days <365 :
        value = "months_6_12" 
    else :
            value = "above_year" 
    return value

def entranceDateName (value):
    value = value.strip()
    value = value.replace("גמיש", "flexible")
    value = value.replace("מיידי", "less_than_6 months")
    value = value.replace("לא צויין","not_defined")
    value = value.strip()
    if value !="flexible" and value !="less_than_6 months" and value !="not_defined" :
        value = replace_time(value)
    
    return value

def sloveHibAir (value):
    if value in ['יש','יש מיזוג אויר','כן','יש מיזוג אוויר']:
        return "1"
    if value in ["לא","אין מיזוג אוויר","אין מיזוג אויר","אין"]:
        return "0"
    return value

def sloveHibBalcony (value):
    
#    value = str(value)
#    value = value.strip()
    if value in ['יש','יש מרפסת','כן','יש מיזוג אוויר']:
        return "1"
    if value in ["לא","אין מרפסת","אין מיזוג אויר","אין"]:
        return "0"
    return value

def sloveHibMamad (value):
    
    #value = str(value)
    #value = value.strip()
    if value in ['יש','יש ממ"ד','כן','יש ממ״ד']:
        return "1"
    if value in ["לא",'אין ממ"ד',"אין מיזוג אויר"," אין ממ״ד",'אין ממ״ד','אין']:
        return "0"
    return value

def slovehandicapFriendly (value):
    
    #value = str(value)
    #value = value.strip()
    if value in ['יש','נגיש לנכים','כן','נגיש']:
        return "1"
    if value in ["לא",'לא נגיש לנכים',"לא נגיש","אין"]:
        return "0"
    return value

def slovehasElevator (value):
    
    if value in ['יש','יש מעלית','כן','נגיש']:
        return "1"
    if value in ["לא",'אין מעלית',"לא נגיש","אין"]:
        return "0"
    return value

def slovehasParking (value):
    
    if value in ['יש','יש חנייה','כן','נגיש','יש חניה']:
        return "1"
    if value in ["לא",'אין חניה',"לא נגיש","אין"]:
        return "0"
    return value

def slovehasBars (value):
    
    if value in ['יש','יש סורגים','כן','נגיש','יש חניה']:
        return "1"
    if value in ["לא",'אין סורגים',"לא נגיש","אין"]:
        return "0"
    return value

def slovehasStorage (value):
    
    if value in ['יש','יש סורגים','כן','נגיש','יש מחסן']:
        return "1"
    if value in ["לא",'אין מחסן',"לא נגיש","אין"]:
        return "0"
    return value


def citiesNameB (value):
    value = value.strip()
    value = value.replace("-", " ")
    value = value.replace("ישראל","")
    value = value.replace("קריית ביאליק","קרית ביאליק")
    value = value.replace("תל אביב-יפו","תל אביב")
    value = value.replace("תל אביב  יפו","תל אביב")

    value = value.strip()
    return value

def merge (data,cities):
    cities['שם']=cities['שם'].apply(citiesNameB)
    merged_df = pd.merge(data, cities, left_on='City', right_on='שם', how='left')
    return merged_df


def typeCategory (value):
    value = value.strip()
    value = value.replace("דו משפחתי", "קוטג")
    value = value.replace("קוטג'", "קוטג")
    value = value.replace("בניין","דירה")
    value = value.replace("פנטהאוז","דירת גג")
    value = value.replace("מיני פנטהאוז","דירת גג")
    value = value.replace("מיני דירת גג","דירת גג")
    value = value.replace("קוטג' טורי","קוטג")
    value = value.replace("קוטג טורי","קוטג")
    value = value.replace("טריפלקס","דופלקס")
    return value

def onlyNumber(value):
    value=str(value)
    x = re.findall('[0-9.]+' ,value)
    if len(x)==0:
        return '0'
    return x[0]

def citiesName (value):
    value = value.strip()
    value = value.replace("-", " ")
    value = value.replace("ישראל","")
    
    value = value.replace("נהרייה","נהריה")
    value = value.strip()
    return value

def cleanData (data,cities):
    data=data.copy()
    data['City']=data.City.apply(citiesName)
    data['price']=data.price.apply(intPrice)
    data=data.dropna(subset=['price'])
    data.price = pd.to_numeric(data.price,downcast="integer")
    data.Street=data.Street.apply(hebName)
    data.city_area=data.city_area.apply(hebName)
    data['description ']=data['description '].apply(hebName)
    data['floor'] = data['floor_out_of'].apply(floor)
    data['total_floors']=data.floor.apply(getTotalFloor)
    data['floor']=data.floor.apply(getFloor)
    data['entranceDate ']=data['entranceDate '].apply(entranceDateName)
    data['hasAirCondition '] = data['hasAirCondition '].apply(sloveHibAir)
    data['hasAirCondition '] = data['hasAirCondition '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasBalcony '] = data['hasBalcony '].apply(sloveHibBalcony)
    data['hasBalcony '] = data['hasBalcony '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasMamad '] = data['hasMamad '].apply(sloveHibMamad)
    data['hasMamad '] = data['hasMamad '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['handicapFriendly '] = data['handicapFriendly '].apply(slovehandicapFriendly)
    data['handicapFriendly '] = data['handicapFriendly '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasElevator '] = data['hasElevator '].apply(slovehasElevator)
    data['hasElevator '] = data['hasElevator '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasParking '] = data['hasParking '].apply(slovehasParking)
    data['hasParking '] = data['hasParking '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasBars '] = data['hasBars '].apply(slovehasBars)
    data['hasBars '] = data['hasBars '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    data['hasStorage '] = data['hasStorage '].apply(slovehasStorage)
    data['hasStorage '] = data['hasStorage '].replace({'TRUE': "1", 'FALSE': "0" ,'no':"0",'yes':"1"})
    for i in ['נחלה','אחר','דירת נופש','מגרש']:
        data=data.drop(data[(data['type'] ==i)].index, inplace=False)
    data['type'] = data['type'].apply(typeCategory)
    data=data.drop(columns=['Unnamed: 23'])
    data['room_number']=data['room_number'].apply(onlyNumber)
    data['num_of_images']=data['num_of_images'].apply(onlyNumber)
    data['Area']=data['Area'].apply(onlyNumber)
    numValue=['num_of_images','price','Area','hasElevator ',
       'hasParking ', 'hasBars ', 'hasStorage ',
       'hasAirCondition ', 'hasBalcony ', 'hasMamad ','room_number', 'handicapFriendly ','floor', 'total_floors']
    for i in range(0,len(numValue)):
        data[numValue[i]] = pd.to_numeric(data[numValue[i]],downcast="integer")
        data[numValue[i]] = data[numValue[i]].fillna(data[numValue[i]].median())
    merged_df=merge (data,cities)
    return merged_df
