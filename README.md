# Personal-UCL-21-22-

Primer proyecto de data science 

Análisis de la UCL 2021-2022. Datos obtenidos de: https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league?select=goals.csv Incluye 8 archivos

El proyecto de análisis UCL 2021-22 lo realicé con la intención de practicar los conocimientos adquiridos sobre análisis de datos y gráficas utilizando pandas y matplotlib. 

## Objetivos
- Responder preguntas que todos los aficionados de fútbol se realizan al término de una temporada como ¿Quién es el máximo goleador de la competencia?, o ¿Quién es el máximo asistidor?, hay datos más específicos por ejemplo ¿Cuál es la posición y equipo que más goles anota?
- Brindar una forma fácil de comparar el rendimiento de un jugador en específico de la forma más objetiva posible y al mismo tiempo poder generar reportes fáciles de compartir con esta información.

## Estructura
Este proyecto cuenta con 2 archivos fuente y 1 auxilear. Para cumplir el primer objetivo está el cuaderno data_ analysis, mientras que para el segundo objetivo está el cuaderno reportes. 


Para lograr el correcto funcionamiento de los programas no es necesario instalar ningún programa, se puede ejecutar desde internet. No se debe eliminar ni cambiar de nombre ninguna carpeta, después de realizar los reportes la sub carpeta media/plots estará vacia, ya que es una carpeta temporal. Todos los reportes generados se almacenan en la carpeta reportes. 

## Estado del proyecto y errores
Por el momento este proyecto está terminado, en un futuro planeo mejorar la creación de los reportes para poder incluir una interpretación o texto complementario a las gráficas, adicionalmente quiero agregar una página final que resuma toda la información y califique el desempeño del jugador. Otra opcion que quiero implementar es poder realizar comparaciones entre 2 jugadores en especifico.

Problemas detectados:
- Algunos jugadores tienen el mismo nombre. Solucionado en su mayoría, se solicita un identificador al usuario
- Algunos jugadores que cambiaron de equipo están registrados dos veces. Solucionado, se eliminan ambos registros
- Los datos de regates no son correctos en todos los casos. No se puede solucionar, es un error de los datos originales
- El nombre de algunos equipos está incompleto. Va a ser solucionado en un futuro
