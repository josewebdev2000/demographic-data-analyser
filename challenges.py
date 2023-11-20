# File to return the exact result expected for each challenge
from helpers import get_percentage

def challenge_1(df):
    """Return the number of people per race as Pandas Series."""

    return df["race"].value_counts()

def challenge_2(df):
    """Return the average age of men"""

    men_df = df[df["sex"] == "Male"]
    return men_df["age"].mean()

def challenge_3(df):
    """Return the percentage of people with bachelors degree"""

    bachelor_df = df[df["education"] == "Bachelors"]
    return get_percentage(len(bachelor_df), len(df))

def challenge_4(df):
    """Find people with advanced education"""

    return df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

def challenge_5(df):
    """Find people without advanced education"""

    return df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

def challenge_6(subset_df):
    """Return percentage of people that earn more than 50K"""
    rich_df = subset_df[subset_df["salary"] == ">50K"]
    return get_percentage(len(rich_df), len(subset_df))

def challenge_7(df):
    """Find the minimum number of hours worked per week."""
    return df["hours-per-week"].min()

def challenge_8(df):
    """Find percentage of people who work the minimum and earn 50K"""
    lazy_people = df[df["hours-per-week"] == challenge_7(df)]
    return challenge_6(lazy_people)

def challenge_9(df):
    """Grab country with highest percentage of people earning more than 50K along with that percentage."""

    country_pop = df["native-country"].value_counts()
    rich_pop = df[df["salary"] == ">50K"]["native-country"].value_counts()
    rich_pop_per = get_percentage(rich_pop, country_pop)

    return {
        "country": rich_pop_per.idxmax(),
        "per": rich_pop_per.max()
    }

def challenge_10(df):
    """Return the most common Indian occupation among the rich."""

    idf = df.rename(columns = {"native-country" : "country"})
    rich_indians_data = idf.query("country == 'India' and salary == '>50K'")
    return rich_indians_data["occupation"].mode().iloc[0]
