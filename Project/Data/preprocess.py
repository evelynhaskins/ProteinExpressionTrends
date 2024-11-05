from Project.raw_data import X

#CHECKING FOR NA
nan_counts = X.isnull().sum()

# Output the count of NaN values for each feature
print("Count of NaN values in each feature:")
print(nan_counts[nan_counts > 0])  # Display only features with NaN values

# Optionally, check the total count of NaNs
total_nan = X.isnull().sum().sum()
print(f"\nTotal number of NaN values in the dataset: {total_nan}")

#FILLING IN NA WITH MEAN
numeric_columns = X.select_dtypes(include='number').columns

# Grouping columns based on categorical variables in 'y'
group_columns = ['Genotype', 'Treatment', 'Behavior']

# Fill NaN values with group mean
for column in numeric_columns:
    X[column] = X.groupby(group_columns)[column].transform(lambda x: x.fillna(x.mean()))

# Verify that NaNs are replaced
print(X.isnull().sum())

# Step 4: Verify that NaNs are replaced
print(X.isnull().sum())

total_nan_new = X.isnull().sum().sum()
print(f"\nTotal number of NaN values in the dataset: {total_nan_new}")