
Los procesos se implementaron con el fin de lograr los siguientes objetivos y obtener las siguientes métricas:

### Objetivo General
Desarrollar un sistema integral de análisis del mercado de restaurantes en el condado de Los Ángeles, CA, orientado a inversores del sector de restaurantes.

### Objetivos Específicos
- Caracterizar los tipos de restaurantes: Analizar el modelo de negocio, número de sucursales, distribución geográfica, entre otros aspectos relevantes.

- Identificar valoraciones y tendencias: Determinar los tipos de restaurantes que reciben las mejores y peores valoraciones de los clientes, identificando así tendencias y preferencias del mercado.
  
- Detectar zonas con mayor potencial: Evaluar las áreas con mayor potencial de desarrollo para distintos modelos de restaurantes.

- Segmentar clientes: Desarrollar un sistema de segmentación de clientes para identificar grupos según sus preferencias y comportamiento de consumo, facilitando la personalización de ofertas y estrategias de marketing.

### KPI's
#### KPI #1 - Satisfacción  del cliente
Mide el nivel de satisfacción de los clientes basándose en sus calificaciones
índice de satisfacción del cliente = (Ʃ(Calificación * Número de reseñas))/Número total de reseñas

#### KPI #2 - Sentimiento promedio de opiniones
Mide el sentimiento general de las opiniones de los clientes (positivo, negativo o neutral)
Sentimiento promedio = ƩPuntuaciones de sentimiento/Número total de opiniones

#### KPI #3 - Conversión de visitas en reseñas
El porcentaje de visitantes que dejan una reseña después de visitar el restaurante
índice de conversión = (Número de reseñas/Número total de visitantes) * 100

## Generalidades del archivo google_restaurants_la.json

-  Este dataset es el resultado de un proceso de segmentación de la base de datos original (metadata_sitios.parquet) con un total de 3,025,011 de registros.

- El proceso de segmentación se llevó a cabo aplicando dos criterios: 1. ubicación geográfica y 2. categoría de restaurantes. 
  
  - Respecto a la ubicación geográfica, el proceso consistió en filtrar los datos de acuerdo al par de coordenadas (latitude y longitude) de cada registro, las cuales se ubicaron dentro de los límites geográficos del condado de Los Ángeles (se tomaron los límites del sitio https://public.gis.lacounty.gov/public/rest/services/LACounty_Dynamic/Transportation/MapServer/generateKml). Se encontraaron 75,815 registros dentro del condado de Los Angeles.
  
  - En cuanto al criterio de categoría, se utilizó un filtro para conservar los registros que contienen la palabra "restaurant" en el campo "Category". Para lograrlo fue necesario hacer dos cosas: a) explotar el dataset en su campo "Category" pues algunos comercios contienen varias categorías en forma de lista. Una vez aplicada la función de explode, el nuevo dataset contenía 151,515 registros. b) Se eliminaron 496 registros (que representan el 0.3% del dataset). 

- **Después de aplicar todos los procesos de segmentación, el dataset de RESTAURANTES en el CONDADO DE LOS ÁNGELES contiene 13,955 registros.**

## Generalidades del archivo combined_reviews_california.parquet y gmap_reviews.json
- Se obtuvieron las reseñas o reviews del dataset combined_reviews_california.parquets, el cual originalmente posee 2,700,000 registros. Sin embargo, éste no indica la categoría o el nombre de los negocios. Por eso es necesario relacionar este dataset con el de negocios filtrado para restaurantes en Los Ángeles (google_restaurants_la.json), de manera que solo queden los reviews de los restaurantes en Los Ángeles. La relación se establece a partir del campo "gmap_id". Una vez que se crea la relación entre datasets, queda un total de 517,513 registros.

- Es importante mencionar que el dataset de reviews en su campo "text" posee 44%  de valores nulos. Es relevante debido a que en este campo se almacena la opinión que el cliente escribe sobre el restaurante. Otros campos con información nula son "pics" y "resp" con 96% y 94% de valores nulos respectivamente. El campo "resp" se refiere a la respuesta del propietario del restaurante a la reseña del cliente.

- Por otra parte, el dataset de reviews posee integridad del 100% en el resto de los campos, entre ellos son relevantes "gmap_id" (para establecer relaciones con otros dataset), "time" (timestamp de la reseña) y "rating" (calificación dada por el cliente).

- El análisis de duplicados en el campo gmap_id revela dos cosas: 1. De los 13,955 restaurantes registrados, solo 2,602 tienen información respecto a reseña y/o valoración; 2. Hay una gran disparidad en cuanto al número de reseñas para cada restaurante (máximo de 9,930 y mínimo de 10).

- Se transformó el campo time (timestamp de la reseña) para proveer un formato legible (fecha y hora).