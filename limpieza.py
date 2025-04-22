import pandas as pd

#CARGA Y VISUALIZACION DE DATASET
# Cargar el archivo (ajusta el nombre si es diferente)
df = pd.read_csv("Asignaci_n_de_dosis_de_vacuna_contra_COVID-19_20250418.csv")

# Ver las primeras filas
#print(df.head())

# Ver información general del dataset
#print(df.info())

# Reemplazar espacios vacíos por NaN si los hubiera
#df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)

#LIMPIEZA DE VALORES NULOS

print(df[df.isnull().any(axis=1)])


# Verificar valores nulos
#print(df.isnull().sum())

# Eliminar filas con nulos en las columnas clave
df = df.dropna(subset=[
    'Cod_Territorio',
    'Nom_Territorio',
    'Laboratorio_Vacuna',
    'Cantidad',
    'Uso_vacuna'
])

print(df.isnull().sum())



#df['Fecha_Resolucion'] = pd.to_datetime(df['Fecha_Resolucion'], errors='coerce')
#df['fecha_corte'] = pd.to_datetime(df['fecha_corte'], errors='coerce')



#df = df.dropna(subset=['Cod_Territorio', 'Nom_Territorio', 'Laboratorio_Vacuna', 'Cantidad', 'Uso_vacuna'])



#df = df.rename(columns={
#    'Nom_Territorio': 'Territorio',
#    'Laboratorio_Vacuna': 'Laboratorio',
#    'Uso_vacuna': 'Uso',
#    'Modificacion Res 2270-2022': 'Modificacion_Res_2270'
#})




#print(df['Territorio'].unique())
#print(df['Laboratorio'].unique())
#print(df['Uso'].unique())



#guardar dataset
df.to_csv("vacunacion_covid_limpio.csv", index=False)
