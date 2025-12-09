import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
from sympy import rotations

"""Preprocesare coloana 'region_availability' & Rename = 'region'"""

#Citim CSV.ul
df = pd.read_csv("product_master_catalog.csv")

# #Separam regiunile lipite
# df["region_availability"] = df["region_availability"].str.split(";")
# df = df.explode("region_availability")
#
# #Curatam spatii inutile
# df["region_availability"] = df["region_availability"].str.strip()
#
# #Redenumim coloana region_availability in region
# df = df.rename(columns={"region_availability": "region"})
#
# df.to_csv("product_master_catalog.csv", index=False)
#
#



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




"""Vizualizari Seaborn / Matplotlib"""
#------------------------------------------------------------------
#Bar CHART - SKU-uri per regiune:
plt.figure(figsize=(10,5))
plt.bar(total_sku_region.index, total_sku_region.values)
plt.title("Numar de SKU-uri per regiune")
plt.xlabel("Regiune")
plt.ylabel("Numar SKU")
plt.grid(axis='y', alpha=0.4)
plt.show()

#-------------------------------------------------------------------------
#Grouped bar chart - SKU.uri per regiune si category:
pivot_count.plot(kind="bar", figsize=(12,6))
plt.title("SKU-uri per regiune si categorie")
plt.xlabel("Regiune")
plt.xticks(rotation=360) #Pentru o vizualizare mai buna a Regiunilor
plt.ylabel("Numar SKU")
plt.grid(axis='y', alpha=0.4)
plt.show()

#----------------------------------------------------------------------
