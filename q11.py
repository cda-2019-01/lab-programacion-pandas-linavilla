##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
df2 = pd.read_csv('tbl2.tsv', sep='\t')
df2.head()
df2['_c5'] = df2['_c5a'] + ":" + df2['_c5b'].astype('str')
dfaux = df2.groupby('_c0')['_c5'].apply(list)
df = pd.DataFrame()
df['_c0'] = dfaux.keys()
df['lista'] = [elem for elem in dfaux]
df['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in df['lista']]
df
