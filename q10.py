##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
df1 = pd.read_csv('tbl1.tsv', sep='\t')
df1.head()
dfaux = df1.groupby('_c0')['_c4'].apply(list)
df = pd.DataFrame()
df['_c0'] = dfaux.keys()
df['lista'] = [elem for elem in dfaux]
df['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in df['lista']]
df