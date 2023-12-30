import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dataframe_transform(file_name):
    """ 
        Load the CSV data and return 2 list of transformed and cleaned data
    """
    df = pd.read_csv(file_name) #'./data.csv'
    df_countries = df.transpose()

    # Remove header
    df_countries.columns = df_countries.iloc[0]
    df_countries = df_countries.iloc[1:]

    # replace column headers with the first row:
    df_countries.columns = df_countries.iloc[0]
    df_countries = df_countries.iloc[1:]
    return df, df_countries

def series_data(dataframe, series_name): 
    column_name = 'Series Name'
    return dataframe.loc[dataframe[column_name] == series_name]


def plot_electricity_chart(energy_data):
    """ Plot chart of data from 1990 to 2000 """
    energy_data = energy_data[['Country Name', '1990 [YR1990]', '1991 [YR1991]', '1992 [YR1992]',
           '1993 [YR1993]', '1994 [YR1994]', '1995 [YR1995]', '1996 [YR1996]',
           '1997 [YR1997]', '1998 [YR1998]', '1999 [YR1999]', '2000 [YR2000]']]

    # Melt the dataframe to create a timeseries
    df_melt = energy_data.melt(id_vars='Country Name', var_name='Year', value_name='Emissions')

    # Convert year column to actual years
    df_melt['Year'] = df_melt['Year'].str.slice(0,4)

    # Plot the timeseries
    fig, ax = plt.subplots(figsize=(10, 8))
    for country, data in df_melt.groupby('Country Name'):
        data.plot(x='Year', y='Emissions', ax=ax, label=country,  linewidth=4)

    ax.set_ylabel("Output Percentage")
    ax.set_title("Renewable electricity output (% of total electricity output)")
    ax.legend(loc='upper left', bbox_to_anchor=(1,1))

    plt.tight_layout()
    plt.show()

def plot_oil_sources(oil_data):
    """ Plot chart of data from 1990 to 2000 """
    oil_data = oil_data[['Country Name', '1990 [YR1990]', '1991 [YR1991]', '1992 [YR1992]',
           '1993 [YR1993]', '1994 [YR1994]', '1995 [YR1995]', '1996 [YR1996]',
           '1997 [YR1997]', '1998 [YR1998]', '1999 [YR1999]', '2000 [YR2000]']]

    # Melt the dataframe to create a timeseries
    df_melt = oil_data.melt(id_vars='Country Name', var_name='Year', value_name='Emissions')

    # Convert year column to actual years
    df_melt['Year'] = df_melt['Year'].str.slice(0,4)

    df_melt.head()

    # Plot the timeseries
    fig, ax = plt.subplots(figsize=(10, 8))
    for country, data in df_melt.groupby('Country Name'):
        data.plot(x='Year', y='Emissions', ax=ax, label=country,  linewidth=4)

    ax.set_ylabel("Output Percentage")
    ax.set_title("Electricity production from oil sources (% of total)")
    ax.legend(loc='upper left', bbox_to_anchor=(1,1))

    plt.tight_layout()
    return plt.show()


if __name__ == "__main__":

    # Function which takes a filename as argument, 
    # then reads a dataframe in World- bank format and returns two dataframes
    df, df_countries = dataframe_transform('./energy_data.csv')

    df_countries.head()

    energy_data = df 
    for col in energy_data.columns[4:]:
        energy_data[col] = pd.to_numeric(energy_data[col], errors='coerce')

    # Use the mean and median functions as statistical methods on the data
    mean_values = energy_data.iloc[:, 4:].mean()
    median_values = energy_data.iloc[:, 4:].median()

    # Display the results
    print('Mean values for each year:')
    print(mean_values)
    print('\nMedian values for each year:')
    print(median_values)

    # Describe the data
    df_countries.describe()

    # Plot charts
    energy_data = series_data(df, 'Renewable electricity output (% of total electricity output)')
    energy_data.head()

    plot_electricity_chart(energy_data)

    oil_data = series_data(df, 'Electricity production from oil sources (% of total)')
    plot_oil_sources(oil_data)
    
