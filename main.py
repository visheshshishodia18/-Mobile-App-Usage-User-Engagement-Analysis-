
import pandas as pd
import numpy as np

print("Mobile App Analysis Project")
print("Python libraries imported successfully!")


# Load mobile app dataset

df = pd.read_csv("24_mobile_app_usage.csv")

print("\nDataset loaded successfully!")

# Display first 5 records
print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
# STEP 7: Missing Values Analysis

print("\nMissing Values Count:")

print(df.isnull().sum())

print("\nMissing Values Percentage:")

print((df.isnull().sum() / len(df)) * 100)
# STEP 8: Duplicate Analysis

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Session IDs:")
print(df["Session_ID"].duplicated().sum())

print("\nDuplicate Session ID Records:")
print(df[df["Session_ID"].duplicated(keep=False)])
print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Session ID Count:")
print(df["Session_ID"].duplicated().sum())

print("\nUnique Session IDs:")
print(df["Session_ID"].nunique())
# STEP 9: Investigate Duplicate Records

duplicate_data = df[
    df["Session_ID"].duplicated(keep=False)
]

print("\nDuplicate Session Records:")
print(duplicate_data.sort_values("Session_ID").to_string())

print("\nExact Duplicate Rows:")
print(df[df.duplicated(keep=False)].shape[0])


# STEP 10: Remove Exact Duplicate Rows

print("\nBefore Cleaning:", df.shape)

df = df.drop_duplicates()

print("\nAfter Cleaning:", df.shape)

print("\nRemaining Duplicate Rows:")
print(df.duplicated().sum())

print("\nRemaining Duplicate Session IDs:")
print(df["Session_ID"].duplicated().sum())


# STEP 11: Calculate Median

print("\nBefore Filling Missing Values:")
print(df.isnull().sum())

duration_median = df["Session_Duration_Mins"].median()
rating_median = df["User_Rating"].median()

print("\nSession Duration Median:", duration_median)
print("User Rating Median:", rating_median)


# STEP 12: Fill Missing Values

df["Session_Duration_Mins"] = df["Session_Duration_Mins"].fillna(duration_median)

df["User_Rating"] = df["User_Rating"].fillna(rating_median)

print("\nAfter Filling Missing Values:")

print(df.isnull().sum())


# STEP 13: DateTime Conversion

df["Session_Date"] = pd.to_datetime(df["Session_Date"])

# Extract Month, Weekday and Hour

df["Month"] = df["Session_Date"].dt.month
df["Weekday"] = df["Session_Date"].dt.day_name()
df["Hour"] = df["Session_Date"].dt.hour

print("\nDateTime Conversion:")
print(df[["Session_Date", "Month", "Weekday", "Hour"]].head())

print("\nUpdated Data Types:")
print(df.dtypes)


# STEP 14: Most Used App Features

feature_usage = df["Feature_Used"].value_counts()

print("\nMost Used App Features:")
print(feature_usage.head(10))


# STEP 15: Device Type Analysis

device_analysis = df.groupby("Device_Type")[
    "Session_Duration_Mins"
].mean()

print("\nAverage Session Duration by Device:")
print(device_analysis)

df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved successfully!")

# STEP 16: 

cleaned_df = pd.read_csv("cleaned_data.csv")

print("Cleaned Dataset Shape:", cleaned_df.shape)

print("\nMissing Values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate Rows:")
print(cleaned_df.duplicated().sum())


import matplotlib.pyplot as plt
import seaborn as sns

feature_counts = cleaned_df["Feature_Used"].value_counts()

plt.figure(figsize=(10, 5))
sns.barplot(x=feature_counts.index, y=feature_counts.values)

plt.title("Most Used App Features")
plt.xlabel("App Features")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)

plt.tight_layout()
#plt.show()

device_duration = cleaned_df.groupby(
    "Device_Type"
)["Session_Duration_Mins"].mean()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=device_duration.index,
    y=device_duration.values
)

plt.title("Average Session Duration by Device")
plt.xlabel("Device Type")
plt.ylabel("Average Duration (Minutes)")

plt.tight_layout()
#plt.show()

rating_counts = cleaned_df["User_Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=rating_counts.index,
    y=rating_counts.values
)

plt.title("User Rating Distribution")
plt.xlabel("User Rating")
plt.ylabel("Number of Users")

plt.tight_layout()
#plt.show()


monthly_usage = cleaned_df["Month"].value_counts().sort_index()

plt.figure(figsize=(10, 5))

sns.barplot(
    x=monthly_usage.index,
    y=monthly_usage.values
)

plt.title("Monthly App Usage")
plt.xlabel("Month")
plt.ylabel("Number of Sessions")

plt.tight_layout()
#plt.show()


print("Now showing Weekday Graph")


weekday_usage = cleaned_df["Weekday"].value_counts()

plt.figure(figsize=(9, 5))

sns.barplot(
    x=weekday_usage.index,
    y=weekday_usage.values
)

plt.title("App Usage by Weekday")
plt.xlabel("Day")
plt.ylabel("Number of Sessions")
plt.xticks(rotation=45)

plt.tight_layout()
print("WEEKDAY GRAPH IS RUNNING")



plt.show()

print("WEEKDAY CODE STARTED")

print(cleaned_df["Weekday"].value_counts())

print("WEEKDAY CODE FINISHED")

print("\n--- PROJECT INSIGHTS ---")

print("Most Used Feature:",
      cleaned_df["Feature_Used"].value_counts().idxmax())

print("Most Active Weekday:",
      cleaned_df["Weekday"].value_counts().idxmax())

print("Average Session Duration:",
      round(cleaned_df["Session_Duration_Mins"].mean(), 2))

print("Average User Rating:",
      round(cleaned_df["User_Rating"].mean(), 2))
