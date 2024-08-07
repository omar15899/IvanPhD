 import pandas as pd

df = pd.read_pickle(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/df1_prueba6.pkl"
)
print(df)
df.to_excel(
    "/Users/omarkhalil/Desktop/Universidad/IvanPhD/webscrappingIvan/PreFiltering/resultados_prefiltering/df1_prueba6.xlsx"
)
