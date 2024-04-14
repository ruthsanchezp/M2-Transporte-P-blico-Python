# Análisis de Correlación entre Uso del Transporte Público y Ventas de Scooters

En este proyecto de análisis de datos, se utiliza el conjunto de datos del Censo de los Estados Unidos sobre el uso del transporte público por código postal para analizar si existe alguna correlación entre el nivel de uso del transporte público y las ventas de scooters en una zona postal determinada. El objetivo es proporcionar recomendaciones al equipo de marketing de la empresa "Electromobility Plus" para realizar campañas focalizadas por zona postal.

## Conjunto de Datos
El conjunto de datos utilizado se encuentra en el archivo CSV llamado `public_transportation_statistics_by_zip_code.csv`. Contiene tres columnas:
- `zip_code`: Código postal de cinco dígitos de los Estados Unidos.
- `public_transportation_pct`: Porcentaje de la población en una zona postal que utiliza el transporte público para ir al trabajo.
- `public_transportation_population`: Número bruto de personas en una zona postal que utilizan el transporte para ir al trabajo.

## Proceso de Análisis
El análisis se realiza en varias etapas:
1. **Preprocesamiento de Datos:**
   - Se copian los datos del transporte público en un DataFrame.
   - Se encuentran los porcentajes máximo y mínimo, y se eliminan los valores por debajo de 0.
2. **Cálculo de Ventas Potenciales:**
   - Se calcula el promedio de ventas potenciales para clientes que viven en zonas de alto transporte público (> 10%) y en zonas de bajo uso del transporte público (≤ 10%).
3. **Visualización de Datos:**
   - Se lee y grafica un histograma de la distribución de los datos.
4. **Estimación de Ventas por Código Postal:**
   - Se agrupan los potenciales clientes en función del uso del transporte público por código postal y se estima el número promedio de ventas.
   - Se crea un diagrama de dispersión para comprender la relación entre el uso del transporte público y las ventas.
5. **Recomendaciones:**
   - Basado en el análisis, se proporcionan recomendaciones al equipo de marketing sobre las oportunidades de ventas.

## Resultados y Recomendaciones
Con base en el análisis realizado, se pueden proporcionar recomendaciones al equipo de marketing sobre las oportunidades de ventas. Estas recomendaciones pueden incluir estrategias para dirigir campañas de marketing a áreas específicas con alto uso de transporte público, identificar posibles clientes potenciales en función de la ubicación y la disponibilidad de scooters, entre otros aspectos relevantes.

Este análisis proporciona información valiosa que puede ayudar al equipo de marketing a tomar decisiones más informadas y efectivas para promover las ventas de scooters en diferentes áreas geográficas.
