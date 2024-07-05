# PROCESAMIENTO ETL
Los procesos se implementaron con el fin de lograr los siguientes objetivos generales y específicos así como para obtener la información requerida para el cálculo de los KPI's mencionados en la sección de README.md

## Automatización del ETL
Todas las extracciones y transformaciones se llevaron a cabo dentro de la plataforma de Google Cloud Platform, activando la función ETL_GCP.py almacenada en un bucket de Google Cloud Storage. Esta función utiliza los archivos json almacenados en un bucket independiente a los cuales aplica todas las transformaciones. Posteriormente, la función crea tablas en formato BigTable, las cuales se cargan en la consola de Big Query desde donde se pueden hacer las consultas y análisis necesarios.

A continuación se describen los procedimientos y algunos datos importantes derivados del tratamiento de cada uno de los datasets:

### Dataset: metadata_sitios
Este dataset contiene información general de los negocios de Estados Unidos que se encuentran registrados en Google Maps hasta 2018 y consiste en 11 archivos json. Estos archivos se unificaron en un solo dataframe con 3,025,011, el cual se sometió a un proceso de segmentación para obtener únicamente los registros de interés.
	 - El proceso de segmentación se llevó a cabo aplicando dos criterios: 
  
	1. Ubicación geográfica
  Respecto a la ubicación geográfica, el proceso consistió en filtrar los datos de acuerdo al par de coordenadas (latitude y longitude) de cada registro, las cuales se ubicaron dentro de los límites geográficos del condado de Los Ángeles (se tomaron los límites del sitio https://public.gis.lacounty.gov/public/rest/services/LACounty_Dynamic/Transportation/MapServer/generateKml). Estos límites geográficos se almacenaron en un archivo geojson con el cual es posible manejar funciones de análisis geográfico. Se encontraron 75,815 registros dentro del condado de Los Angeles.
  
	  2. Categoría de restaurantes
 En cuanto al criterio de categoría, se utilizó un filtro para conservar los registros que contienen la palabra "restaurant" en el campo "Category". Para lograrlo fue necesario hacer dos cosas: a) explotar el dataset en su campo "Category" pues algunos comercios contienen varias categorías en forma de lista. Una vez aplicada la función de explode, el nuevo dataset contenía 151,515 registros. b) Se eliminaron 496 registros (que representan el 0.3% del dataset). 

 - **Después de aplicar todos los procesos de segmentación, el dataset de RESTAURANTES en el CONDADO DE LOS ÁNGELES contiene 13,955 registros.**

## Dataset: reviews_California
Este dataset consiste en 18 archivos json que contienen los usuarios y sus reseñas hechas en Google Maps hasta 2018 en el Estado de California y posee 2,700,000 de registros. Estos registros no indican la categoría o el nombre de los negocios. Por eso es necesario relacionar este dataset con el de restaurantes de Los Ángeles (google_restaurants_la.json), de manera que solo queden los reviews de los establecimientos de interés. La relación se establece a partir del campo "gmap_id". Una vez que se crea la relación entre datasets, queda un total de 517,513 registros.

- Es importante mencionar que el dataset de reviews_California en su campo "text" posee 44%  de valores nulos. Es relevante debido a que en este campo se almacena la opinión que el cliente escribe sobre el restaurante. Otros campos con información nula son "pics" y "resp" con 96% y 94% de valores nulos respectivamente. El campo "resp" se refiere a la respuesta del propietario del restaurante a la reseña del cliente.

- Por otra parte, el dataset de reviews posee integridad del 100% en el resto de los campos, entre ellos son relevantes "gmap_id" (para establecer relaciones con otros dataset), "time" (timestamp de la reseña) y "rating" (calificación dada por el cliente).

- El análisis de duplicados en el campo gmap_id revela dos cosas: 1. De los 13,955 restaurantes registrados, solo 2,602 tienen información respecto a reseña y/o valoración; 2. Hay una gran disparidad en cuanto al número de reseñas para cada restaurante (máximo de 9,930 y mínimo de 10).

***Imputaciones y transformaciones***
- Se transformó el campo time (timestamp de la reseña) para proveer un formato legible (fecha y hora).
- Una vez establecida la relación entre los datasets, se imputaron los valores NULOS del campo "text"  (reseña) del dataset de reviews_California a partir de los valores del campo "avg_rating" (valoración promedio del restaurante) proveniente del dataset metadata_sitios. Los valores imputados se asignaron de acuerdo a la siguiente clasificación de las valoraciones promedio:

**rango de valoración promedio (avg_rating)** - **reseña (text)**

[1 - 2.9]  - Negativa

[3 - 3.9] - Neutra

[4 - 5] - Positiva
