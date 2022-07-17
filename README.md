# Personal-UCL-21-22-

Primer proyecto de data science
Analisis de la UCL 2021-2022.
Datos obtenidos de: https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league?select=goals.csv
Incluye 8 archivos

El proyecto de analisis UCL 2021-22 lo realice con la intencion de practicar los conocimientos adquiridos sobre analisis de datos y graficas utilizando pandas y matplotlib. Busca cumplir dos objetivos: 
1) Responder preguntas que todos los aficionados de futbal se realizan al termino de una temporada como ¿Quien es el maximo goleador de la competencia? o ¿Quien es el máximo asistidor? hay datos mas especificos por ejemplo ¿Cual es la posicion y equipo que mas goles anota? 
2) Brindar una forma facil de comparar el rendimiento de un jugador en especifico de la forma mas objetiva posible y al mismo tiempo poder generar reportes faciles de compartir con esta informacion.

Este proyecto cuenta con 2 archivos fuente y 1 principal. Para cumplir el primer objetivo esta el cuaderno data_ analysis, mientras que para el segundo objetivo esta el cuaderno reportes. 

Para lograr el correcto funcionamiento de los programas no es necesario instalar ningun programa, se puede ejecutar desde internet. No se debe eliminar ni cambiar de nombre ninguna carpeta, despues de realizar los reportes la subcarpeta media/plots estara vacia ya que es una carpeta temporal. Todos los reortes generados se almacenan en la carpeta reportes.

Por el momento este proyecto esta terminada, en un futuro planeo mejorar la creacion de los reportes para poder incluir una interpretacion o texto complementario a las graficas, adicionalmente quiero agregar una pagina final que resuma toda la informacion y califique el desempeño del jugador.

Problemas detectados:
- Algunos jugadores tienen el mismo nombre. Solucionado en su mayoria, se solicita un identificador al usuario
- Algunos jugadores que cambiaron de equipo estan registrados dos veces. Solucionado, se eliminan ambos registros
- Los datos de regates no son correctos en todos los casos. No se puede solucionar es un error de los datos originales
- El nombre de algunos equipos esta incompleto. Va a ser solucionado en un futuro
