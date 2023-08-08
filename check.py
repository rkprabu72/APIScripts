import pandas as pd
import mysql.connector
import os

# Set the directory where your CSV files are located
csv_directory = 'C:/Users/rkpra/Box/python/DE/callvolumes'

# Set the columns you want to read from each CSV
columns_to_read = ['Tenant',' Total Calls', ' Total Minutes', ' Agent Unique Logins']

# Create an empty DataFrame to store the data
all_data = pd.DataFrame()

# Loop through all CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # Read in only the desired columns from the CSV file
        data = pd.read_csv(os.path.join(csv_directory, filename), usecols=columns_to_read)
        
        # Add a column to the data to indicate which file it came from
        data['filename'] = os.path.splitext(filename)[0]
        df['filename'] = filename
        # Append the data to the overall DataFrame
        all_data = all_data.append(data, ignore_index=True)

# Rearrange the columns to put the filename first
all_data = all_data[['filename'] + columns_to_read]

# Save the combined data to a new CSV file
all_data.to_csv('combined_data.csv', index=False)
df