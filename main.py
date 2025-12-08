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





"""Metrici de baza pe regiuni"""

#Total SKU per region:
total_sku_region = df.groupby("region")["sku"].nunique()

#Media stock.urilor per SKU per region:
avg_stock_region = df.groupby(["region", "sku"])["stock_total_units"].sum().groupby("region").mean()

#Distributia pe categorie per region:
dist_categories = df.groupby(["region", "category"])["sku"].nunique()


#Crearea Tabelelor Pivot:
#Numar de SKU-uri per category per region:
pivot_count = df.pivot_table(
    index="region",
    columns="category",
    values="sku",
    aggfunc="count",
    fill_value=0
)
#print("Tabel pivot Suma stock total\n",pivot_count)
#print("-"*40)

#Suma stock_total_units (pivot = stock per category per region)
pivot_stock = df.pivot_table(
    index="region",
    columns="category",
    values="stock_total_units",
    aggfunc="sum",
    fill_value=0
)

#print("Tabel pivot Numar de SKU-uri:\n",pivot_stock)
#print("-"*40)


