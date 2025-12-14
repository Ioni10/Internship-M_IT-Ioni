#Raport de concluzii bazat pe Analiza Strocuri SKU - Regiuni si Categorii

##Descriere
Acest proiect analizeaza distributia stocurilor de produse (SKU-uri) pe regiuni, cu accent pe:
- niveluri de **high stock**
- niveluri de **low stock**
- distributia volumelor de **categorii de produse si regiuni**

Scopul este identificarea riscurilor de stock-out si a zonelor care necesita optimizare a aprovizionarii.

---

## Regiuni analizate:

- UK-Midlands
- UK-North
- UK-Scotland
- UK-South
- UK-Wales

## Categorii analizate
- Bricks & Blocks
- Cement & Aggregates
- Drainage
- Insulation
- Paving
- Roofing
- Timber

---

## 📊 Vizualizări

### Procent SKU cu Stoc Ridicat (High Stock)
![High Stock](High-procent.png)

### Procent SKU cu Stoc Scăzut (Low Stock)
![Low Stock](Low-procent.png)

### Distribuție Regiune × Categorie (Heatmap)
![Heatmap](Heatmap.png)

---

## 🔍 Observații și concluzii

### 1. Regiunile cu cel mai mare număr de produse (High Stock)
- **UK-Midlands** și **UK-Wales** prezintă cele mai mari procente de SKU-uri aflate în high stock.
- Diferențele între regiuni sunt moderate, indicând o distribuție relativ echilibrată a stocurilor mari.

---

### 2. Regiunile cu cea mai mare pondere de Low Stock
- **UK-North** și **UK-South** au cele mai ridicate procente de produse aflate în low stock.
- Aceste regiuni reprezintă un risc operațional crescut și necesită:
  - reaprovizionare prioritară
  - revizuirea forecast-ului de cerere
  - redistribuirea stocurilor între regiuni

---

### 3. Categoriile cele mai sensibile la lipsa de stoc
(pe baza volumelor mai reduse și a variațiilor din heatmap)

- **Timber**
  - Prezintă constant valori mai mici comparativ cu alte categorii, în special în:
    - UK-North
    - UK-South
- **Insulation**
  - Volume mai scăzute în mai multe regiuni (UK-North, UK-South),
    ceea ce o face vulnerabilă în perioade de cerere crescută.
- **Cement & Aggregates**
  - Variabilitate ridicată între regiuni, cu valori semnificativ mai mici în UK-Scotland,
    sugerând un risc local de understock.

👉 **Roofing** și **Drainage** apar ca fiind cele mai stabile categorii,
având volume ridicate și consistente în majoritatea regiunilor.

---

## ⚠️ Regiuni și categorii cu risc ridicat
- **UK-North + Timber / Insulation**
- **UK-South + Timber**
- **UK-Scotland + Cement & Aggregates**

Aceste combinații ar trebui monitorizate constant pentru a preveni stock-out-urile.

---

## Concluzie generală
- Stocurile sunt relativ bine distribuite la nivel național,
  însă există **zone critice la nivel de regiune și categorie**.
- Focusul operațional ar trebui să fie pe:
  - UK-North și UK-South
  - categoriile Timber, Insulation și Cement & Aggregates
- O strategie de reaprovizionare diferențiată pe regiuni ar reduce riscul de lipsă de stoc
  și ar îmbunătăți disponibilitatea produselor.

---

## Pași următori (opțional)
- Integrarea datelor de vânzări pentru corelarea cu low stock
- Alertare automată pentru categoriile sensibile
- Optimizare stoc pe regiuni folosind demand forecasting