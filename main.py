 
import pandas as pd

print("=" * 50)
print("MOBILE APP DATA CLEANING PROJECT")
print("=" * 50)

# STEP 1: Load Dataset

df = pd.read_csv("24_mobile_app_usage.csv")

print("\nSTEP 1: Dataset Loaded Successfully")

# STEP 2: Dataset Inspection

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

# STEP 3: Missing Values Analysis

print("\nSTEP 3: Missing Values Analysis")

print("\nMissing Values Count:")
print(df.isnull().sum())

print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df)) * 100)

# STEP 4: Duplicate Analysis

print("\nSTEP 4: Duplicate Analysis")

print("Total Exact Duplicate Rows:", df.duplicated().sum())

print("Duplicate Session IDs:",
      df["Session_ID"].duplicated().sum())

print("\nDuplicate Session ID Records:")

print(
    df[df["Session_ID"].duplicated(keep=False)]
    .sort_values("Session_ID")
    .to_string()
)

# STEP 5: Remove Exact Duplicate Rows

print("\nSTEP 5: Removing Exact Duplicates")

print("Before Cleaning:", df.shape)

df = df.drop_duplicates()

print("After Cleaning:", df.shape)

print("Remaining Exact Duplicates:",
      df.duplicated().sum())

# STEP 6: Handle Missing Values

print("\nSTEP 6: Handling Missing Values")

duration_median = df["Session_Duration_Mins"].median()
rating_median = df["User_Rating"].median()

print("Session Duration Median:", duration_median)
print("User Rating Median:", rating_median)

df["Session_Duration_Mins"] = (
    df["Session_Duration_Mins"].fillna(duration_median)
)

df["User_Rating"] = (
    df["User_Rating"].fillna(rating_median)
)

print("\nMissing Values After Treatment:")
print(df.isnull().sum())

# STEP 7: Data Type Correction

print("\nSTEP 7: Data Type Correction")

df["Session_Date"] = pd.to_datetime(
    df["Session_Date"], errors="coerce"
)

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nInvalid Session Dates:",
      df["Session_Date"].isnull().sum())

# STEP 8: Final Data Validation

print("\nSTEP 8: Final Data Validation")

print("Final Dataset Shape:", df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nRemaining Exact Duplicate Rows:",
      df.duplicated().sum())

print("\nRemaining Duplicate Session IDs:",
      df["Session_ID"].duplicated().sum())

# STEP 9: Export Cleaned Dataset

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

print("\nDATA CLEANING PROJECT COMPLETED")
