import ssl
from ucimlrepo import fetch_ucirepo

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Fetch dataset
try:
    mice_protein_expression = fetch_ucirepo(id=342)

    # Data (as pandas DataFrames)
    X = mice_protein_expression.data.features.copy()
    y = mice_protein_expression.data.targets.copy()

    # Metadata
    print(mice_protein_expression.metadata)

    # Variable information
    print(mice_protein_expression.variables)
except Exception as e:
    print(f"An error occurred: {e}")
