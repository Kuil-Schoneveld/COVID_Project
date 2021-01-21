import csv
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace, BNode

rivm_data = list(csv.reader(open("COVID-19_aantallen_gemeente_cumulatief.csv")))

print(*rivm_data[-100:], sep="\n")

rivm_dataframe = pd.read_csv("COVID-19_aantallen_gemeente_cumulatief.csv", sep=";", quotechar='"')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
rivm_dataframe['Municipality_name'] = rivm_dataframe['Municipality_name'].str.replace(" ","_")

print(rivm_dataframe[-100:], sep="\n")

