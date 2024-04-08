Caso de aplicación

El gerente en “Electromobility Plus” les dice que el área de marketing ha decidido que
quiere hacer una serie de campañas para ayudar a promover las ventas de scooters. Ustedes
como equipo de análisis de datos deben utilizar los datos del Censo de los Estados Unidos
sobre el uso del transporte público por código postal. El propósito es analizar si el nivel de
uso del transporte público tiene alguna correlación con las ventas de la empresa de scooter
mencionada anteriormente, en una zona postal determinada, de tal manera que el equipo
de marketing pueda realizar una campaña focalizada por zona postal.

Aplicación:

Después de leer el caso, use el archivo CSV con el conjunto de datos de transporte público
por código postal:
public_transportation_statistics_by_zip_code.csv

1. Este conjunto de datos tiene tres columnas:
• zip_code: Este es el código postal de cinco dígitos de los Estados Unidos que se
utiliza para identificar la región.
• public_transportation_pct: Este es el porcentaje de la población en una zona
postal que ha sido identificado como usuarios del transporte público para ir al
trabajo.
• public_transportation_population: Este es el número bruto de personas en una
zona postal que utilizan el transporte para ir al trabajo.
3. Copie el conjunto de datos de transporte público en un DataFrame.
4. Encuentre los porcentajes máximo y mínimo en estos datos. Los valores por debajo
de 0, lo más probable que indique datos faltantes.
5. Calcule las ventas potenciales promedio para clientes que viven en zonas de alto
transporte público (más del 10%), así como en las zonas de bajo uso del transporte
público (menor o igual al 10%).
6. Lea los datos en Pandas y grafique un histograma de la distribución para producir un
histograma.
7. Agrupe a los potenciales clientes en función del uso del transporte público por
código postal y estime el número promedio de ventas, además, cree un diagrama
de dispersión para comprender mejor la relación entre el uso del transporte público
y las potenciales ventas. Exporte estos datos a un archivo Excel.
8. Con base en este análisis, ¿Qué recomendaciones le daría al equipo de marketing de
la empresa al considerar oportunidades de ventas?
