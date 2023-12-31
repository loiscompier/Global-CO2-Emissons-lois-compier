# -*- coding: utf-8 -*-
"""Kopie van Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17qqj422qMDHJfT4pbgC2znq6V_cvuzn7
"""

import pandas as pd
from google.colab import files

# Upload het CSV-bestand
#uploaded = files.upload()

# Lees het geüploade CSV-bestand
filename = 'co2_emissions.csv'
total_table = pd.read_csv(filename, header=[0, ])  # Lees met MultiIndex kolommen

print (total_table)


only_country = total_table.loc[3:]

print(only_country)

#Graph 1: CO2 of the bigger countries

df = pd.DataFrame(only_country)
#print (df)

# Automatisch selecteer de laatste kolom
laatste_kolom = df.columns[-1]

most_co2 = only_country.sort_values(by=laatste_kolom, ascending = False)

# Selecteer de hoogste 5 waarden
vijf_most_co2 = most_co2.head(5)

print (vijf_most_co2)

import numpy as np
import matplotlib.pyplot as plt



# Selecteer alleen de middelste kolommen
selected_columns = vijf_most_co2.iloc[:, 1:-1]
# Selecteer de kopregels van de geselecteerde kolommen
selected_headers = selected_columns.columns
# dit zijn de jaren die op de x-as komen


for index, row in vijf_most_co2.iterrows():
    country_name = row['Country']
    emissions = row[selected_headers ]  # Select emissions data for the years

    plt.plot(selected_headers , emissions, marker='o', label=country_name)


# Set labels and title
plt.xlabel('Years')
plt.ylabel('Fossil CO2 Emissions (Mt CO2)')
plt.title('Fossil CO2 Emissions of the Top 5 CO2 Producers')

# Set x-axis ticks to the selected years
#plt.xticks(selected_headers )

# Add a legend
plt.legend()

# Show the plot
plt.show()

# Graph 2: worst and best changers

print(only_country)
basis_df = pd.DataFrame(only_country)


basis_df['Basis_index'] = 100
# Selecteer alleen de middelste kolommen
selected_columns2 = vijf_most_co2.iloc[:, 1:]
# Selecteer de kopregels van de geselecteerde kolommen
selected_headers2 = selected_columns2.columns


# Filter out countries with emissions less than 5 Mt in 1990
basis_df = basis_df[basis_df['1990'] >= 5]

# Bereken de indices voor elk jaar en voeg de kolommen toe
for jaar in selected_headers2[1:]:  # Sla het eerste jaar over, omdat de basisindex al 100 is
    index_kolom_naam = f'{jaar}_index'  # Maak de kolomnaam voor de index
    basis_kolom = basis_df['1990']  # De basiswaarde is de waarde van 1990
    index_waarden = (basis_df[jaar] / basis_kolom) * 100
    basis_df[index_kolom_naam] = index_waarden

print(basis_df)

basis_df

laatste_kolom = df.columns[-1]
# Sorteer basis_df op basis van de laatste kolom
basis_df_sorted = basis_df.sort_values(by=laatste_kolom)



basis_df_sorted_index = basis_df_sorted.loc[:,"Basis_index": ]


# Voeg de "Country" kolom toe aan basis_df_sorted_index
country_column = basis_df_sorted[["Country"]]
basis_df_sorted_index = pd.concat([country_column, basis_df_sorted_index], axis=1)
print(basis_df_sorted_index)

top_three = basis_df_sorted_index.head(3)
bottom_three = basis_df_sorted_index.tail(3)

# Concatenate the top_three and bottom_three DataFrames
combined_df = pd.concat([top_three, bottom_three])

# Display the combined DataFrame
print(combined_df)

# Set the years you want to plot
selected_columns3 = combined_df.iloc[:, 1:]
selected_headers3 = selected_columns3.columns
selected_years = selected_headers3.tolist()

# Plotting
plt.figure()

for index, country_df in combined_df.iterrows():
    country_name = country_df['Country']
    emissions = country_df[selected_headers3]

    # Remove the '_index' suffix from each year
    selected_years_without_index = [year.replace('_index', '') for year in selected_years]

    # Plot the emissions data for the current country, using Basis_index as y-axis
    plt.plot(selected_years_without_index, emissions['Basis_index'], marker='o', label=country_name)

plt.title('Relative Change in CO2 Emissions (1990 as 100%)')
plt.xlabel('Year')
plt.ylabel('Relative CO2 Emissions (%)')
plt.legend()
plt.grid(True)

plt.show()

# Set the years you want to plot
selected_columns3 = combined_df.iloc[:, 1:]
selected_headers3 = selected_columns3.columns
selected_years = selected_headers3.tolist()

# Remove the '_index' suffix from year values
#selected_years = [year.replace('_index', '') for year in selected_years]
#combined_df= [year.replace('_index', '') for year in combined_df]

# Plotting
plt.figure()

for index, country_df in combined_df.iterrows():
    country_name = country_df['Country']
    emissions = country_df[selected_years]
    selected_years_without_index = [year.replace('_index', '') for year in selected_years]

    plt.plot(selected_years_without_index , emissions, marker='o', label=country_name)

plt.title('Relative Change in CO2 Emissions (1990 as 100%)')
plt.xlabel('Year')
plt.ylabel('Relative CO2 Emissions (%)')
plt.legend()
plt.grid(True)