# ANÁLISIS EXPLORATORIO DE LOS DATOS PRELIMINAR

El análisis exploratorio para la primera fase del proyecto consistió en la inspección del contenido de las bases de datos de manera superficial, con el objetivo de entender la información de la cual se dispone. La información que deriva de este primer análisis es una de las bases para el diseño de los objetivos generales del proyecto, es por ello que esta primera exploración es sumamente relevante. En este documento se describe de manera resumida las características básicas de las bases de datos así como los principales hallazgos encontrados a partir de la aplicación de estadística descriptiva y se organiza en dos secciones: 1. Producto Interno Bruto en las regiones de Estados Unidos y 2. Bases de datos de comercios (Yelp y Google Maps).

  
 ## 1. Producto Interno Bruto en las regiones de Estados Unidos

El Producto Interno Bruto o GDP por sus siglas en inglés es un índice ampliamente utilizado para caracterizar el estado de la economía a diferentes escalas geográficas. En el contexto de este proyecto, el GDP es de gran utilidad para conocer el nivel de productividad de las distintas zonas de Estados Unidos, de manera que esto se puede traducir en sitios donde puede ser mejor invertir en ciertos rubros dependiendo de los objetivos de un potencial inversionista. Con lo anterior en mente, se obtuvo una base de datos de GDP de Estados Unidos, sus regiones, estados y condados para el periodo de 2001 a 2018. Estos datos se normalizaron a nivel nacional, de manera que se obtuvo el cambio anual de GDP de cada estado, en relación al resto del país. Esta es una manera de conocer la productividad RELATIVA de los estados. Es interesante notar que, aunque el GDP de un estado de manera independiente muestre crecimiento, si se compara con el GDP del resto de los estados (es decir, su valor normalizado) puede ser que su tendencia sea negativa.

De esta manera, se identificó al estado de California como el que ha mostrado crecimiento de su GDP de manera constante durante el periodo analizado y por ello se considera un sitio apropiado para invertir.

  

*PRODUCTO INTERNO BRUTO (GDP) DEL ESTADO DE CALIFORNIA*

![California_normalizado](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/California.png)

  
  

*PRODUCTO INTERNO BRUTO (GDP) NORMALIZADO DEL ESTADO DE CALIFORNIA*

![California_normalizado](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/California_normalizado.png)

  

## 2. Bases de datos de comercios (Yelp y Google Maps)


> ## YELP

  

#### Generalidades

  

El dataset de Yelp consiste en 5 archivos en diferentes formatos (pkl, json y parquet) que contienen información respecto a los negocios (nombre, rubro, ubicación, calificación promerido, entre otros), reseñas de los clientes (comentarios, tips, valoraciones, entre otros), información del perfil de los clientes (antiguedad, número de fans, utilidad de sus reseñas, entre otros) y los check-in de los clientes a los negocios.

  

#### Integridad

  

Cuenta con una integridad alta puesto que cuenta con datos en prácticamente todos los campos de los archivos que la componen, por cual se considera una fuente de información bastante confiable. Respecto a valores repetidos que puedan generar resultados erróneos, tampoco se identificaron atributos que pudieran generar conflictos.

  

  

### Análisis y hallazgos

  

Yelp posee una base de datos bien nutrida respecto a los registros que los clientes hacen sobre los negocios que visitan. Por ejemplo, se posee una base de datos de casu 7 millones de reseñas para el periodo de 2005 a 2022, en las cuales se especifica además de la opinión del cliente, fehca de la reseña, la valoración en número de estrellas y la evaluación de otros clientes sobre dicha opinión ("useful", "cool", "funny"). Se observa que la mayoría de las valoraciones son altas (4 estrellas o más) y que el mayor número de registros se llevaron a cabo de 2014 a 2021, con un máximo entre 2018 y 2019.

  

*VALORACIONES POR AÑO*

  

![Valoraciones-anio-Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/6e692ae3d85e57f73fdaad9f83035b4e2c039450/Imagenes/Valoraciones_estrellas_Yelp_ARIEL.png)

  

*NÚMERO DE VALORACIONES POR ESTRELLAS*

  

![Valoraciones-anio-Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Valoraciones_estrellas_Yelp_ARIEL.png)

  
  

Además de las reseñas, Yelp cuenta con un dataset de poco más de 900 mil consejos ("tips") que los usuarios ofrecen a futuros clientes que visiten los establecimientos. En esta base de datos encontramos comentarios en los que prevalecen de manera general palabras como Place, Deliciou, Love, Grear Food, Amazing,Awesome, Best, Great Service. Es interesante cómo al segmentar esta base de datos, por ejemplo para comentarios con más de 20 palabras y valoración de 5 estrellas, la predominancia cambia a las palabras Place, Food, Great, Good, Order, One, Go, Love. Por otra parte, se identifican patrones en la frecuencia de Tips que los clientes ofrecen, los cuales varían en función de un usario a otro (por ejemplo, hay usuarios que tienden a escribir más Tips que otros) y al año.

  

*NUBE DE PALABRAS RESPECTO A LOS TIPS DE LOS CLIENTES*

  

![Nube_palabras_Tip_completos_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Nube_palabras_Tip_completos_Yelp_ARIEL.png)

  

*NUBE DE PALABRAS RESPECTO A TIPS CON FRASES DE MÁS DE 20 PALABRAS VALORACIÓN DE 5 ESTRELLAS*

  

![Nube_palabras_Tip_rate5_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Nube_palabras_Tip_rate5_Yelp_ARIEL.png)

  

*NÚMERO DE TIPS POR AÑO Y USUARIO*

  

![Tips_Usuarios_Anio_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Tips_Usuarios_Anio_Yelp_ARIEL.png)

  

Respecto a los negocios, Yelp permite conocer cuáles categorías (rubros) y negocios han sido más o menos valorados, por ejemplo, se observa que Starbucks es la empresa con más valoraciones, mientras que la categoría o rubro más valorada es "Beauty & Spas, Nail Salons"; en ambos casos se identifican patrones de frecuencias similares en los que hay dos o tres negocios/categorías con mayor frecuencia y el resto desciende progresivamente.

  

*NEGOCIOS MÁS RESEÑADOS*

  

![Negocios_resenados_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Negocios_resenados_Yelp_ARIEL.png)

  

*CATEGORÍAS O RUBROS MÁS RESEÑADOS*

  

![Categorias_Mas_Resenadas_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Categorias_Mas_Resenadas_Yelp_ARIEL.png)

  

Un aspecto importante es la localización de los establecimientos que forman parte de la base de datos de Yelp. Al respecto se observa que cuenta con información de sitios particulares de Estados Unidos (incluso de una ciudad de Canadá), por lo cual, no se tiene una distribución espacial amplia. Pennsylvania (PA) es el estado con más registros seguido por Florida, mientras que la ciudad con más reseñas es Philadephia seguida por Tucson.

  

*ESTADOS CON MAYOR NÚMERO DE RESEÑAS*

  

![Negocios_Estados_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Negocios_Estados_Yelp_ARIEL.png)

  

*CIUDADES CON MAYOR NÚMERO DE RESEÑAS*

  

![Ciudades_Mas_Negocios_Yelp_ARIEL](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Ciudades_Mas_Negocios_Yelp_ARIEL.png)

  

*MAPA DE CALOR (DENSIDAD) DE NEGOCIOS CON RESEÑAS*

  

![Mapa_Dataset_Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Mapa_Dataset_Yelp.png)

  
  

Respecto a la distribución de frecuencias categorías o rubros, se observa que pocos rubros poseen una cantidad grande de negocios y por otra parte, la mayoría de los rubros poseen pocos negocios. Esto se infiere gracias a un análisis de outliers.

  

*CATEGORÍAS CONSIDERADAS COMO OUTLIERS*

  

![Categorias_outliers_Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Categorias_outliers_Yelp.png)

  

Las categorías o rubros más frecuentes son "Restaurants", "Food", "Shopping", "Home Services", "Beauty & Spas", "Night life", "Church", "Healht & Medical", "Local Services", "Bars" y "Automotive.

  

*CATEGORÍAS MÁS FRECUENTES*

  

![Categorias_frecuentes_Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Categorias_frecuentes_Yelp.png)

  

Dentro de cada categoría se exploraron los principales negocios en función de su frecuencia. Se identificó un patrón similar en todas las categorías, el cual se caracteriza por una frecuencia muy alta de uno o dos negocios o empresas en comparación del resto. Este comportamiento se puede interpretar como una característica que distingue a los tipos o modelos de negocio en función del su número de sucursales.

  

*PRINCIPALES EMPRESAS POR RUBRO*

  

![Empresas_frecuentes_Yelp](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Empresas_frecuentes_Yelp.png)

  
  
#
> ### GOOGLE MAPS

  

#### Generalidades

  

La base de datos de Google Maps posee dos grupos de archivos (todos en formato json) los cuales describen datos generales de los establecimientos así como reseñas de los mismos. De estos datos se puede obtener información rica en cuanto a la distribución espacial y frecuencia de los negocios y sus rubros.

  

#### Integridad

  

El grupo de archivos que describe a los negocios posee una integridad parcial, dado que tiene un nivel de completud alto para la localización de los establecimientos, sin embargo, carece de gran parte de la información descriptiva de los mismos (precios, horario de apertura, descripción, entre otros). La parte que refiere a las reseñas presenta una situación similar, en la que prácticamente carece de datos para los campos de texto aunque sí se encuentra completa para las valoraciones cuantitativas (rating) y fechas.

  

### Análisis y hallazgos

  

La sección descriptiva de establecimientos posee más de 3 millones de registros de la cual se analizó principalmente la frecuencia de los negocios, su localización y categorización por rubros. Respecto a la frecuencia de los rubros se observa mediante una representación gráfica de outliers que al igual que en la base de datos de Yelp, existe una amplia variedad de frecuencias, en las cuales las más altas están muy por encima de la mayoría y son dominadas por unas cuantas categorías.

*CATEGORÍAS O RUBROS CONSIDERADOS OUTLIERS*

![Categorias_outliers_GM](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Categorias_outliers_GM.png)

  

Las categorías o rubros más frecuentes son "Restaurant", "Auto repair shop", "Gas station", "Service establishment", "Beauty Salon", "Convenient store", "Church", "Hair salon", "Nail salon" y "ATM".

  

*CATEGORÍAS MÁS FRECUENTES*

![Categorias_frecuentes_GM](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Categorias_frecuentes_GM.png)

  

Respecto a la frecuencia de empresas por rubro, se encontró el mismo patrón identificado en la base de datos de Yelp. Es decir, una o dos empresas poseen frecuencias muy altas en comparación con el resto.

*PRINCIPALES EMPRESAS POR RUBRO*

![Empresas_frecuentes_GM](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Empresas_frecuentes_GM.png)

  

En el caso de la base de datos de Google Maps se realizó un análisis más profundo en cuanto a la distribución de frecuencias. Particularmente para el rubro de restaurantes, ya que se trata de la categoría que presenta mayor robustez tanto en las bases de datos de Yelp como en Google Maps (en esta última, con un registro de 97,257 restaurantes). Este análisis consistió en la exploración de restaurantes que se pudieran considerar outliers en función del número de sucursales; sin embargo, el análisis convencional (cuartiles y definión de umbral) no arrojó resultados claros. Esto último se debe a que la mayoría de los restaurantes poseen una sola sucursal, lo cual genera que el rango intercuartil sea igual a 0. Por lo tanto, para obtener una caracterización formal de la distribución de frecuencias, se procedió a hacer una categorización por quiebres (método de Jenks). Esta clasificación de frecuencias indica que, en efecto, la mayoría de los restaurantes (cerca de 70 mil) solo consta de una sucursa, y en el caso contrario, solo 3 empresas poseen más de 600 sucursales. Este dato, nos brinda información importante para la toma de decisiones en cuanto al modelo de negocio que se pretenda desarrollar, por ejemplo, el de las grandes cadenas como Subway o McDonalds, o bien, restaurantes de corte local.

  

*CLASIFICACIÓN DE RESTAURANTES EN FUNCIÓN DEL NÚMERO DE SUCURSALES QUE POSEE*

![Frecuencias_Restaurantes_sucursales_GM](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Frecuencias_Restaurantes_sucursales_GM.png)

A diferencia de la base de datos de Yelp, Google Maps posee una rica distribución espacial de las empresas. Los registros se localizan tanto en territorio continental de Estados Unidos como fuera de él.

  

*MAPA DE CALOR (DENSIDAD) DE EMPRESAS*

![Mapa_Dataset_GM](https://github.com/franciscoagamez/PF_google_yelp/blob/main/Imagenes/Mapa_Dataset_GM.png)