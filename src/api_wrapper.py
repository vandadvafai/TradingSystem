import os
from dotenv import load_dotenv 
import simfin as sf

load_dotenv() 

# Set your API-key for downloading data.
sf.set_api_key('160f0cdb-b61d-4080-b6b1-0a41e0fe7a32')

# Set the local directory where data-files are stored.
# The directory will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Download the data from the SimFin server and load into a Pandas DataFrame.
prices_df = sf.load_shareprices(variant='daily')

# Download the data from the SimFin server and load into a Pandas DataFrame.
companies_df = sf.load_companies(market='us')

# Print the first rows of the data.
print(prices_df.head())
print(companies_df.head())