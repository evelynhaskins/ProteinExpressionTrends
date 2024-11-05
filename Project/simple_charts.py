import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Project.Data.raw_data import X, y

data = pd.concat([X, y], axis=1)

# Simple comparison charts for general understanding, function adding in class type

def plot_mean_protein_expression(data, class_types=['t-CS-s', 't-CS-m']):
    # Filter data based on specified class types
    filtered_data = data[data['class'].isin(class_types)]

    # Select only the numerical columns (protein expression levels)
    numerical_data = filtered_data.select_dtypes(include=['float64', 'int64'])

    # Add the class column back to the numerical data for grouping
    numerical_data['class'] = filtered_data['class'].values

    # Calculate the mean of each protein for the two groups
    mean_values = numerical_data.groupby('class').mean().T  # Transpose to have proteins as rows

    # Reset index for plotting
    mean_values.reset_index(inplace=True)
    mean_values.rename(columns={'index': 'Protein'}, inplace=True)

    # Plotting
    plt.figure(figsize=(15, 7))
    sns.barplot(data=mean_values.melt(id_vars='Protein', var_name='Class', value_name='Mean Expression'),
                x='Protein', y='Mean Expression', hue='Class')

    # Adding titles and labels
    plt.title(f'Mean Protein Expression Levels for {class_types[0]} vs {class_types[1]}')
    plt.xticks(rotation=90)
    plt.ylabel('Mean Expression Level')
    plt.xlabel('Protein')
    plt.legend(title='Class')
    plt.tight_layout()

    # Show the plot
    plt.show()

plot_mean_protein_expression(data, class_types=['t-CS-s', 't-CS-m'])
plot_mean_protein_expression(data, class_types=['t-CS-s', 'c-CS-s'])
plot_mean_protein_expression(data, class_types=['t-CS-m', 'c-CS-m'])

def plot_mean_protein_expression(data, class_types=['c-CS-s', 'c-SC-s', 't-CS-s', 't-SC-s']):
    # Mapping for more descriptive class labels
    label_mapping = {
        'c-CS-s': 'Control (Learn)',
        'c-SC-s': 'Control (No Learn)',
        't-CS-s': 'Trisomy (Learn)',
        't-SC-s': 'Trisomy (No Learn)'
    }

    # Filter data based on specified class types and apply label mapping
    filtered_data = data[data['class'].isin(class_types)].copy()
    filtered_data['class'] = filtered_data['class'].map(label_mapping)

    # Select only the numerical columns (protein expression levels)
    numerical_data = filtered_data.select_dtypes(include=['float64', 'int64'])

    # Add the mapped class column back to the numerical data for grouping
    numerical_data['class'] = filtered_data['class'].values

    # Calculate the mean of each protein for the specified groups
    mean_values = numerical_data.groupby('class').mean().T  # Transpose to have proteins as rows

    # Reset index for plotting
    mean_values.reset_index(inplace=True)
    mean_values.rename(columns={'index': 'Protein'}, inplace=True)

    # Plotting
    plt.figure(figsize=(15, 7))
    sns.barplot(
        data=mean_values.melt(id_vars='Protein', var_name='Class', value_name='Mean Expression'),
        x='Protein', y='Mean Expression', hue='Class'
    )

    # Adding titles and labels
    plt.title(f"Mean Protein Expression Levels for {' vs '.join(label_mapping[ct] for ct in class_types)}")
    plt.xticks(rotation=90)
    plt.ylabel('Mean Expression Level')
    plt.xlabel('Protein')
    plt.legend(title='Class')
    plt.tight_layout()

    # Show the plot
    plt.show()


# Example usage for saline classes
plot_mean_protein_expression(data, class_types=['c-CS-s', 'c-SC-s', 't-CS-s', 't-SC-s'])