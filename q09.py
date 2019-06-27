##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
dfaux = df0.groupby('_c1')['_c2'].apply(list)
df = pd.DataFrame()
df['_c1'] = dfaux.keys()
df['_c2'] = [elem for elem in dfaux]
df['_c2'] = [":".join(str(v) for v in sorted(elem)) for elem in df['_c2']]
df