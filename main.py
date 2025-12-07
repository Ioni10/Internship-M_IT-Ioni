import pandas as pd

"""Preprocesare coloana 'region_availability' & Rename = 'region'"""

#Citim CSV.ul
df = pd.read_csv("product_master_catalog.csv")

#Separam regiunile lipite
df["region_availability"] = df["region_availability"].str.split(";")
df = df.explode("region_availability")

#Curatam spatii inutile
df["region_availability"] = df["region_availability"].str.strip()

#Redenumim coloana region_availability in region
df = df.rename(columns={"region_availability": "region"})

df.to_csv("product_master_catalog.csv", index=False)