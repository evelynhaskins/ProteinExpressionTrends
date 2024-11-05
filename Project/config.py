from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

# Column names for numeric columns
numeric_columns = [...]  # List of numeric column names

# Initialize LabelEncoder and StandardScaler
label_encoder = LabelEncoder()
scaler = StandardScaler()
numeric_columns = X.select_dtypes(include='number').columns
group_columns = ['Genotype', 'Treatment', 'Behavior']