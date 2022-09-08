# import dask
import dask
import dask.dataframe as dd

# read in watson_healthcare data
ddf = dd.read_csv('watson_healthcare_modified.csv')

# print the first 5 rows
print(ddf.head())