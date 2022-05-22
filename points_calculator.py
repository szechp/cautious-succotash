from datetime import datetime, date
import argparse
import pandas as pd


# define functions
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


def prepare_df(i_df):
    """wrapper function: prepares the df for further use: changes type from
    the "Annual amount" column from string to float, adds an empty "Points" column
    and adds and calculates an "Age" column.
    Args:
        i_df (pandas.core.frame.DataFrame): a pandas df that will be edited in place
    """
    # change type from str to float
    i_df["Annual amount"] = i_df["Annual amount"].str.replace(",", ".").apply(float)
    # add Points column
    i_df["Points"] = 0.0
    # add age column
    i_df['Age'] = i_df['Date of birth'].apply(calculate_age)


def calculate_points(i_df):
    """calculates the Points for a df according to a pre defined point scheme

    Args:
        i_df (pandas.core.frame.DataFrame): a pandas dataframe
    """
    for index, row in i_df.iterrows():
        if row["Annual amount"] >= 300 and row["Age"] >= 50:
            i_df.loc[index, "Points"] += 3
        if row["Annual amount"] >= 300 and row["Age"] >= 30:
            i_df.loc[index, "Points"] += 1.5
        if row["Annual amount"] >= 150 and row["Age"] >= 50:
            i_df.loc[index, "Points"] += 2
        if row["Annual amount"] >= 150 and row["Age"] >= 30:
            i_df.loc[index, "Points"] += 1
        if row["Annual amount"] >= 120 and row["Age"] >= 50:
            i_df.loc[index, "Points"] += 1
        if row["Annual amount"] >= 120 and row["Age"] >= 30:
            i_df.loc[index, "Points"] += 0.5


def main():
    """pulling it all together"""
    # get arguments from cl
    parser = argparse.ArgumentParser(description="Points calculator for fundraising")
    parser.add_argument("flag", type=str, help='specify directory or run tests')
    parser.add_argument("--fundraiser", required = False, type = int, help="specify one single fundraiser to get the Points from")
    argument = parser.parse_args()

    if argument.flag == "test":
        print("run test")

    elif argument.fundraiser:
        df=pd.read_csv(argument.flag, sep = ";")
        subset = df.loc[df["Fundraiser ID"] == argument.fundraiser]
        if subset.empty:
            raise Exception("Fundraiser ID doesn't exist")
        prepare_df(df)
        calculate_points(df)
        pd.set_option("display.max_rows", None, "display.max_columns", None) #to show all entries
        print(df.sort_values(by=["Points"], ascending=False))

    else:
        df=pd.read_csv(argument.flag, sep = ";")
        prepare_df(df)
        calculate_points(df)
        pd.set_option("display.max_rows", None, "display.max_columns", None) #to show all entries
        print(df.sort_values(by=["Points"], ascending=False))


if __name__ == "__main__":
    main()