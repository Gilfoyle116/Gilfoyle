import pandas as pd

# 1. Create Data Structures
# 1.1 Create DataFrame from a dictionary (similar to an Excel sheet)
data = {
    'Name': ["Gilfoyle", "Indus", "Alex", "Andrew"],
    'Age': [21, 19, 18, 18],
    'Score': [100, 95, 90, 90]
}
df = pd.DataFrame(data)

# 1.2 Create Series (similar to an indexed 1D array)
# Pass a list and define custom index
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# 2. Data Inspection and Attributes (similar to numpy's shape/ndim)
# Shape (rows, columns)
print("df shape:", df.shape)
# Column names
print("df columns:", df.columns)
# Row index
print("df index:", df.index)
# View first 2 rows (default is 5)
print("First two rows:\n", df.head(2))
# Quick view of descriptive statistics (mean, std, etc.)
print("Descriptive statistics:\n", df.describe())  # Fixed: changed descrive to describe

# 3. Indexing, Slicing, and Filtering
# Extract a single column (returns Series)
names = df['Name']
# Extract multiple columns (using double brackets)
subset = df[['Name', 'Age']]

# loc (locate by label/name)
# Extract 'Name' column at row index 1
val_loc = df.loc[1, 'Name']

# iloc (locate by integer position, similar to numpy indexing)
val_iloc = df.iloc[0, 1]

# Boolean indexing / Conditional filtering (extract rows where Age > 30)
mask_df = df[df['Age'] > 30]

# 4. Data Manipulation and Operations
# Add a new column
df['Is_Adult'] = df['Age'] >= 18
# Math operations on a column (add 5 to all scores)
df['Score_Plus'] = df['Score'] + 5
# Statistical calculations
mean_age = df['Age'].mean()
max_score = df['Score'].max()

# 5. Data Concatenation and Merging
# 5.1 Vertical concatenation (similar to numpy concatenate axis=0)
df2 = pd.DataFrame({'Name': ['Eve'], 'Age': [22], 'Score':[88.0]})
df_concat_v = pd.concat([df, df2], ignore_index=True)

# 5.2 Horizontal merge (similar to SQL JOIN, matching on a common column)
df_info = pd.DataFrame({'Name': ['Gilfoyle', 'Indus'], 'City': ['Beijing', 'Guangzhou']}) # Fixed: separated names
# Left merge based on the 'Name' column
df_merged = pd.merge(df, df_info, on='Name', how='left')