# Librerias
from fpdf import FPDF
from xarray import align
WHITH=210
HIGHT=297
from datetime import datetime
from os import remove

# Textos
textoInicio='La UEFA Champion League es un torneo de fútbol continental que se juega en la UEFA (Union des Associations Européennes de Football). La primera edicion de esta competencia fue en 1956 bajo el nombre Copa de Europa, en 1993 cambio a su nombre actual Champions League. Desde esa edicon hasta la actualidad se ha jugado anualmente teniendo 22 campeones distintos; el equipo con mas titulos es el Real Madrid, seguido de AC Milan, Liverpool y Bayern Munich.'
textoInicio2='En la edicion 2021-22 de la UEFA Champion League participaron 32 equipos. La final se jugo en el estadio Stade de France en la ciudad de Paris, el dia 28 de mayo de 2022, donde se enfrentaron Liverpool y Real Madrid. El ganador fue el Real Madrid, y con esto consiguio su 14 copa de Europa.'
textoInicio3='Este reporte incluye estadisticas sobre el desempeño del jugador en la UEFA Champion League. Para poder comparar de forma objetiva a los jugadores en la mayoria de los datos se presentan en diferentes formatos: cantidad, cantidad por partidos jugados y por minutos jugados. Adicional a esto cada jugador solo es compara con otros de su misma posicion; finalmente se comprara con el resto de jugadores en su posicion y mismo equipo para poder determinar la relevancia que tuvo en su equipo.'
textoLiga='Los datos para realizar este reporte se obtivieron de la siguiente '
textoComparacion0=''
textoComparacion1=''

# Funciones principales

def footer(pdf):
    pdf.image('media/img/lateral.png',x=WHITH-15,y=0,w=15,h=HIGHT)
    pdf.image('media/img/footer.png',x=0,y=HIGHT-15,w=210,h=15)
    pdf.set_xy(WHITH-15,280)
    pdf.set_font('Arial', size=10)
    pdf.set_text_color(241,250,238)
    pdf.cell(15,15,str(pdf.page_no()-1),0,0,'C')
    pdf.add_page()
    pdf.set_font('Arial', size=9)
    pdf.set_text_color(0,0,0)
    return pdf

def titulo(Titulo, pdf):
    pdf.set_font('Arial','B', size=20)
    pdf.set_text_color(69, 123, 157)
    pdf.multi_cell(0,10,txt=Titulo,align='L')
    pdf.cell(0,8,ln=1)
    pdf.set_font('Arial', size=12)
    pdf.set_text_color(0,0,0)
    return pdf

def texto(texto,ancho,separacion,ln,pdf):
    pdf.set_font('Arial', size=12)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(ancho,5,txt=texto,align='J')
    pdf.cell(0,separacion,ln=ln)
    return pdf

def portada(pdf,jugador,posicion,club):
    pdf.add_page()
    pdf.set_font('Times', size=28)
    pdf.set_text_color(2,48,71)
    pdf.image('media/img/portada.png',x=0,y=0,w=210,h=70)
    pdf.set_xy(0,70)
    fecha=datetime.today().strftime("%d/%m/%Y")
    pdf.multi_cell(0,20,txt=f'Analisis de UEFA Champion League 2021-22\nJugador: {jugador}\nPosicion: {posicion}\nEquipo: {club}\n\nFecha de reporte: {fecha}',align='C')
    pdf.set_right_margin(20)
    return pdf

def introduccion(pdf):
    pdf.add_page()
    pdf=titulo('Introducción',pdf)
    pdf=texto(textoInicio,0,3,1,pdf)
    pdf=texto(textoInicio2,0,5,1,pdf)
    pdf=texto(textoInicio3,0,3,1,pdf)
    pdf.cell(121,4,textoLiga,ln=0)
    pdf.set_font('Arial', size=12,style='UI')
    pdf.set_text_color(1, 79, 134)
    pdf.cell(13.5,4,'página.',link='https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league',ln=0)
    pdf=footer(pdf)
    return pdf

def pag_partidos(pdf):
    pdf=titulo('Participacion en partidos',pdf)
    pdf.image('media/plots/partidos_minutos.png',x=10,y=25,w=185)
    #remove('media/plots/partidos_minutos.png')
    pdf.cell(0,59,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=footer(pdf)
    return pdf 

def pag_goles(pdf):
    pdf=titulo('Distrubucion de goles',pdf)
    pdf.image('media/plots/goles.png',x=-20,y=18,w=210)
    #remove('media/plots/goles.png')
    pdf.cell(0,135,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=footer(pdf)
    return pdf

def pag_comparacion0(pdf):
    pdf=titulo('Comparacion con jugadores',pdf)
    pdf=texto(textoComparacion1,0,3,1,pdf)
    pdf=footer(pdf)
    pdf=titulo('Comparacion con jugadores de la misma posicion',pdf)
    pdf.image('media/plots/comparacion0.png',x=10,y=25,w=180)
    #remove('media/plots/comparacion0.png')
    pdf.cell(0,115,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=footer(pdf)
    pdf=titulo('Comparacion con jugadores de la misma posicion y equipo',pdf)
    pdf.image('media/plots/comparacion1.png',x=10,y=32,w=180)
    #remove('media/plots/comparacion1.png')
    pdf.cell(0,112,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=footer(pdf)
    return pdf

def pag_comparacion1(pdf):
    pdf=titulo('Comparacion con jugadores',pdf)
    pdf=texto(textoComparacion1,0,3,1,pdf)
    pdf=footer(pdf)
    pdf=titulo('Comparacion con jugadores de la misma posicion',pdf)
    pdf.image('media/plots/comparacion0.png',x=10,y=25,w=180)
    #remove('media/plots/comparacion0.png')
    pdf.cell(0,97,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=texto(textoInicio,0,3,1,pdf)
    pdf=footer(pdf)
    pdf=titulo('Comparacion con jugadores de la misma posicion y equipo',pdf)
    pdf.image('media/plots/comparacion1.png',x=10,y=32,w=180)
    #remove('media/plots/comparacion1.png')
    pdf.cell(0,94,ln=1) # Por si se quiere agregar texto despues de la grafica
    pdf=texto(textoInicio,0,3,1,pdf)
    pdf=footer(pdf)
    return pdf