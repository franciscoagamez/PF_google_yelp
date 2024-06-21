# ANÁLISIS EXPLORATORIO DE LOS DATOS PRELIMINAR 

El análisis exploratorio para la primera fase del proyecto consistió en la inspección del contenido de las bases de datos de manera superficial, con el objetivo de entender la información de la cual se dispone. La información que deriva de este primer análisis es una de las bases para el diseño de los objetivos generales del proyecto, es por ello que esta primera exploración es sumamente relevante. En este documento se describe de manera resumida las características básicas de las bases de datos así como los principales hallazgos encontrados a partir de la aplicación de estadística descriptiva y se organiza en tres secciones:

- 1. Producto Interno Bruto en las regiones de Estados Unidos
- 2.  Bases de datos de comercios (Yelp y Google Maps)
- 3. Análisis de rubros

 ## 1._ Producto Interno Bruto en las regiones de Estados Unidos
   
## 2._ Bases de datos de comercios (Yelp y Google Maps)
### YELP
#### Generalidades
   El dataset de Yelp consiste en 5 archivos en diferentes formatos (pkl, json y parquet) que contienen información respecto a los negocios (nombre, rubro, ubicación, calificación promerido, entre otros), reseñas de los clientes  (comentarios, tips, valoraciones, entre otros), información del perfil de los clientes (antiguedad, número de fans, utilidad de sus reseñas, entre otros) y los check-in de los clientes a los negocios.

   #### Integridad
   Cuenta con una integridad alta puesto que cuenta con datos en prácticamente todos los campos de los archivos que la componen, por cual se considera una fuente de información bastante confiable. Respecto a valores repetidos que puedan generar resultados erróneos, tampoco se identificaron atributos que pudieran generar conflictos.


   ### Análisis y hallazgos
   Yelp posee una base de datos bien nutrida respecto a los registros que los clientes hacen sobre los negocios que visitan. Por ejemplo, se posee una base de datos de casu 7 millones de reseñas para el periodo de 2005 a 2022, en las cuales se especifica además de la opinión del cliente, fehca de la reseña, la valoración en número de estrellas y la evaluación de otros clientes sobre dicha opinión ("useful", "cool", "funny"). Se observa que la mayoría de las valoraciones son altas (4 estrellas o más) y que el mayor número de registros se llevaron a cabo de 2014 a 2021, con un máximo entre 2018 y 2019.
   *VALORACIONES POR AÑO*
   *GRAFICA Valoraciones_anio_Yelp_ARIEL.png*

   *NÚMERO DE VALORACIONES POR ESTRELLAS*
   *GRAIFCA Valoraciones_estrellas_Yelp_ARIEL.png*

   Además de las reseñas, Yelp cuenta con un dataset de poco más de 900 mil consejos ("tips") que los usuarios ofrecen a futuros clientes que visiten los establecimientos. En esta base de datos encontramos comentarios en los que prevalecen de manera general palabras como Place, Deliciou, Love, Grear Food, Amazing,Awesome, Best, Great Service. Es interesante cómo al segmentar esta base de datos, por ejemplo para comentarios con más de 20 palabras y valoración de 5 estrellas, la predominancia cambia a las palabras Place, Food, Great, Good, Order, One, Go, Love. Por otra parte, se identifican patrones en la frecuencia de Tips que los clientes ofrecen, los cuales varían en función de un usario a otro (por ejemplo, hay usuarios que tienden a escribir más Tips que otros) y al año.

   *NUBE DE PALABRAS RESPECTO A LOS TIPS DE LOS CLIENTES*
   *Nube_palabras_Tip_completos_Yelp_ARIEL.png*

   *NUBE DE PALABRAS RESPECTO A TIPS CON FRASES DE MÁS DE 20 PALABRAS VALORACIÓN DE 5 ESTRELLAS*
   *Nube_palabras_Tip_rate5_Yelp_ARIEL.png*
   
   *NÚMERO DE TIPS POR AÑO Y USUARIO*
   *Tips_Usuarios_Anio_Yelp_ARIEL.png*

   Respecto a los negocios, Yelp permite conocer cuáles categorías (rubros) y negocios han sido más o menos valorados, por ejemplo, se observa que Starbucks es la empresa con más valoraciones, mientras que la categoría o rubro más valorada es  "Beauty & Spas, Nail Salons"; en ambos casos se identifican patrones de frecuencias similares en los que hay dos o tres negocios/categorías con mayor frecuencia y el resto desciende progresivamente.

   *NEGOCIOS MÁS RESEÑADOS*
   *Negocios_resenados_Yelp_ARIEL.png*

   *CATEGORÍAS O RUBROS MÁS RESEÑADOS*
   *Categorias_Mas_Resenadas_Yelp_ARIEL.png*
   
   Un aspecto importante es la localización de los establecimientos que forman parte de la base de datos de Yelp. Al respecto se observa que cuenta con información de sitios particulares de Estados Unidos (incluso de una ciudad de Canadá), por lo cual, no se tiene una distribución espacial amplia. Pennsylvania (PA) es el estado con más registros seguido por Florida, mientras que la ciudad con más reseñas es Philadephia seguida por Tucson.
   
   *ESTADOS CON MAYOR NÚMERO DE RESEÑAS*
   *Negocios_Estados_Yelp_ARIEL.png*

   *CIUDADES CON MAYOR NÚMERO DE RESEÑAS*
   *Ciudades_Mas_Negocios_Yelp_ARIEL.png*

   *MAPA DE CALOR (DENSIDAD) DE NEGOCIOS CON RESEÑAS*
   *Mapa_Dataset_Yelp.png*

   ### GOOGLE MAPS
   #### Generalidades
   La base de datos de Google Maps posee dos grupos de archivos (todos en formato json) los cuales describen datos generales de los establecimientos  así como reseñas de los mismos. De estos datos se puede obtener información rica en cuanto a la distribución espacial y frecuencia de los negocios y sus rubros.
   
   #### Integridad
   El grupo de archivos que describe a los negocios posee una integridad parcial, dado que tiene un nivel de completud alto para la localización de los establecimientos, sin embargo, carece de gran parte de la información descriptiva de los mismos (precios, horario de apertura, descripción, entre otros). La parte que refiere a las reseñas presenta una situación similar, en la que prácticamente carece de datos para los campos de texto aunque si se encuentra completa para las valoraciones cuantitativas (rating) y fechas. 

   ### Análisis y hallazgos
   

3. ## Análisis de rubros

