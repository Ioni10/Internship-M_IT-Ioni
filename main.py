import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


"""Preprocesare coloana 'region_availability' & Rename = 'region'"""

#Citim CSV.ul
df = pd.read_csv("product_master_catalog.csv")

# # #Separam regiunile lipite
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


#===========================================================================

"""Metrici de baza pe regiuni"""

#Total SKU per region:
total_sku_region = df.groupby("region")["sku"].nunique()

#Media stock.urilor per SKU per region:
avg_stock_region = df.groupby(["region", "sku"])["stock_total_units"].sum().groupby("region").mean()

#Distributia pe categorie per region:
dist_categories = df.groupby(["region", "category"])["sku"].nunique()

#-------------------------------------------------------------------------
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
#------------------------------------------------------------------------
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
#=========================================================================



"""Vizualizari Seaborn / Matplotlib"""
#-------------------------------------------------------------------------

#Bar CHART - SKU-uri per regiune:
plt.figure(figsize=(11,6)) #Setam o marime pentru figura noastra
plt.bar(total_sku_region.index, total_sku_region.values) #alegem genul de plot si ce plotam
plt.title("Numar de SKU-uri per regiune") #titlul graficului nostru
plt.xlabel("Regiune", rotation=0, color="blue") #eticheta caracteristica pentru regiuni
plt.ylabel("Numar SKU",rotation=0, labelpad=30, color="red")
plt.grid(axis='y', alpha=0.4) #Vrem sa fie trasat frumos ----- sa intelegem mai bine
plt.savefig("figura-Bar1.png")
plt.show()
#-------------------------------------------------------------------------

#Grouped bar chart - SKU.uri per regiune si category:
pivot_count.plot(kind="bar",stacked=True, figsize=(13,6))
plt.title("SKU-uri per regiune si categorie")
plt.xlabel("Regiune", color="red")
plt.xticks(rotation=0) #Pentru o vizualizare mai buna a Regiunilor
plt.ylabel("Numar SKU",rotation=0, labelpad=30,color="blue")
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()
plt.grid(axis='y', alpha=0.4)
plt.savefig("Bar-color-sku.png")
plt.show()
#----------------------------------------------------------------------

#Heatmap Pivot stock_total:
plt.figure(figsize=(14,6))
sns.heatmap(data=pivot_stock, annot=True, fmt=".0f", cmap="Blues")
plt.title("Heatmap Region x Category")
plt.xlabel("Category", color="Red")
plt.xticks(rotation=5)
plt.ylabel("Region",rotation=0, labelpad=20, color="Blue")
plt.yticks(rotation=0)
plt.savefig("Heatmap.png")
plt.show()
##--------------------------------------------------------------------

##BoxPlot Stock_total_units per categorie:
plt.figure(figsize=(15,5))
sns.boxplot(data=df, x="stock_total_units", y="category")
plt.title("Boxplot Variatia Stocurilor:")
plt.xlabel("Stock Total")
plt.ylabel("Category")
plt.savefig("Boxplot.png")
plt.show()
#==========================================================================

"""
 Analiza pe "Stock Risk"
 """


#Definim criterii:
#----------------------------------------------------------------------
#Low-stock-sku:
low_stock = df[df["stock_total_units"] < 20] #punem conditia
sku_low_stock = low_stock["sku"].nunique() #ii spunem ce vrem sa aflam

#----------------------------------------------------------------------
#High-stock-sku:
high_stock = df[df["stock_total_units"] > 500] #conditia pt high
sku_high_stock = high_stock["sku"].nunique()

#--------------------------------------------------------------------

#Calculam per regiune procentul:
#--------------------------------------------------------------------
#Low:
sku_low_region = low_stock.groupby("region")["sku"].nunique()
#procent:
procent_low = (sku_low_region/ total_sku_region) * 100
#-------------------------------------------------------------------------
#high:
sku_high_region = high_stock.groupby("region")["sku"].nunique()
#procent:
procent_high = (sku_high_region / total_sku_region) * 100
#--------------------------------------------------------------------------



#Vizualizare Low procent
#--------------------------------------------------------------------------
plt.figure(figsize=(11, 6))
procent_low.plot(kind="bar", title="Percent SKU Low Stock", color="blue")
plt.ylabel("Percent SKU",rotation=0, labelpad=40)
plt.xlabel("Region")
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.savefig("Low-procent.png")
plt.show()
#-------------------------------------------------------------------------
#Vizualizare High procent:
plt.figure(figsize=(11, 6))
procent_high.plot(kind="bar", title="Percent SKU High Stock", color="red")
plt.ylabel("Percent SKU",rotation=0, labelpad=40)
plt.xlabel("Region")
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.savefig("High-procent.png")
plt.show()
#========================================================================