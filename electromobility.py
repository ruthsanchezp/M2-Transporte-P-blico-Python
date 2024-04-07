import trace
import pandas as pd
import matplotlib.pyplot as plt

df_sf = pd.read_csv('transporte.csv', header=0, sep=';')

#reemplazar el -666666666.0 por ceros en el mismo dataframe
df_sf['public_transportation_pct'].replace(-666666666.0, 0, inplace=True)

#eliminar los ceros
df = df_sf.loc[(df_sf['public_transportation_pct'] != 0.0) & (df_sf['public_transportation_population'] != 0)]

print(df, "/n")

#Estadística descriptiva
Estadistica = df[['public_transportation_pct', 'public_transportation_population']].describe()
print(Estadistica)

#Dispersión
Varianza = df [['public_transportation_pct', 'public_transportation_population']].var()
print(Varianza)

#Poblacion mas grande que usa transporte publico
TranportePublicoMax= df['public_transportation_population'].max()
print("Uso transporte público Max", TranportePublicoMax)

#Poblacion mas pequeño que usa transporte publico
TranportePublicoMin= df['public_transportation_population'].min()
print("Uso transporte público Max", TranportePublicoMin)

#Porcentaje máximo del poblacion en una zona
PorcentajeMax = ['Porcentaje max', df['public_transportation_pct'].max()]
print("PorcentajeMax:", PorcentajeMax)

#Porcentaje mínimo del poblacion en una zona
PorcentajeMin = ['Porcentaje min', df['public_transportation_pct'].min()]
print("PorcentajeMin:", PorcentajeMin)

#Ventas potenciales promedio para clientes de alto uso transporte público
VPMayor10 = df[df['public_transportation_pct']>10]['public_transportation_population'].mean()
print("Ventas potenciales >%10:",VPMayor10)

#Ventas potenciales promedio para clientes de bajo uso transporte público
VPMenor10 = df[df['public_transportation_pct']<10]['public_transportation_population'].mean()
print("Ventas potenciales < 10%:",VPMenor10)

##Correlación lineal
correlacion = df.corr()
print("\n",correlacion)

df.hist(bins=30, alpha=0.5, figsize=(6, 5))
plt.show()

#GRafico de dispersión
plt.scatter(df['public_transportation_pct'], df['public_transportation_population'])
plt.show()
