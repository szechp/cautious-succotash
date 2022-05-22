from ast import parse
from email import parser
import pandas as pd
from datetime import datetime, date
import argparse



#import file as df and clean
df=pd.read_csv("donations.csv", sep = ";")
df["Annual amount"] = df["Annual amount"].str.replace(",", ".").apply(float)
df["points"] = 0.0

#functions

def calculate_age(i_birtday) -> int:
    """this function takes a birthday and calculates the current age
    of a person

    Args:
        i_birtday (str): a birthdate in the format %Y-%m-%d

    Returns:
        int: returns the age in relation to today
    """    
    birthday = datetime.strptime(i_birtday, "%Y-%m-%d").date()
    today = date.today()
    return today.year - birthday.year - ((today.month, 
                                      today.day) < (birthday.month, 
                                                    birthday.day))
    
df['Age'] = df['Date of birth'].apply(calculate_age)

def calculate_points(i_df):
    """calculates the points for a df according to a pre defined point scheme

    Args:
        i_df (pandas.core.frame.DataFrame): a pandas dataframe
    """    
    for index, row in i_df.iterrows():
        if row["Annual amount"] >= 300 and row["Age"] >= 50:
            df.loc[index, "points"] += 3
        if row["Annual amount"] >= 300 and row["Age"] >= 30:
            df.loc[index, "points"] += 1.5
        if row["Annual amount"] >= 150 and row["Age"] >= 50:
            df.loc[index, "points"] += 2
        if row["Annual amount"] >= 150 and row["Age"] >= 30:
            df.loc[index, "points"] += 1
        if row["Annual amount"] >= 120 and row["Age"] >= 50:
            df.loc[index, "points"] += 1
        if row["Annual amount"] >= 120 and row["Age"] >= 30:
            df.loc[index, "points"] += 0.5

### main

""" parser = argparse.ArgumentParser(description="Points calculator for fundraising")
parser.add_argument("--test", required = False, default = True, help="run the tests")
parser.add_argument()
parser.add_argument("--fundraiser", required = False, default = "", help="specify one single fundraiser to get the points from")

argument = parser.parse_args()
status = False """

if __name__ == "__main__":
    if argument.test:
        