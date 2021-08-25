# EMILIANO COHEN
# 14/08/2021. CURSO INTRO. PROG. ADIMRA 2021
# ej_integracion_semana_10
# https://github.com/EmiCohenSoft/eCohenAdimra

# LIBRERIAS
import requests as req
import time


# DEFINICION DE CONSTANTES
RUTA_API_COVID = "http://api.covid19api.com/summary"


# DEFINICION DE VARIABLES


# DEFINICION DE FUNCIONES
def consultaCovid(link):
    respuesta = req.get(link)
    return respuesta.json()

def formateoFecha(fechaAFormatear):
    formatoDeSalida = "%Y-%m-%dT%H:%M:%S.%fZ"
    fechaAConvertir = time.strptime(fechaAFormatear,formatoDeSalida)
    fechaFormateada = f'{fechaAConvertir.tm_mday}/{fechaAConvertir.tm_mon:0>2d}/{fechaAConvertir.tm_year}'
    horaFormateada = f'{fechaAConvertir.tm_hour}:{fechaAConvertir.tm_min}'
    return fechaFormateada, horaFormateada

def main():
    infoCovid = consultaCovid(RUTA_API_COVID)
    
    if(infoCovid):

        infoCovidGlobalConfirm = infoCovid["Global"]["TotalConfirmed"]
        infoCovidGlobalRecup = infoCovid["Global"]["TotalRecovered"]
        #infoCovidGlobalRecup = int(500)

        InfoCovidArg = infoCovid["Countries"][6]

        InfoCovidPais = InfoCovidArg["Country"]
        InfoCovidCodPais = InfoCovidArg["CountryCode"]
        InfoCovidNuevosConf = InfoCovidArg["NewConfirmed"]
        InfoCovidTotalConf = InfoCovidArg["TotalConfirmed"]
        InfoCovidNuevasMuertes = InfoCovidArg["NewDeaths"]
        InfoCovidTotalMuertes = InfoCovidArg["TotalDeaths"]
        InfoCovidNuevosRecup = InfoCovidArg["NewRecovered"]
        InfoCovidTotalRecup = InfoCovidArg["TotalRecovered"]
        InfoCovidFecha = InfoCovidArg["Date"]
        #print(InfoCovidFecha)

        fechaActualizacion, horaActualizacion =  formateoFecha(InfoCovidFecha)
        actualizacion = f'el día {fechaActualizacion} a la hora {horaActualizacion}'
        #print(actualizacion)

        InfoCovidArgActual = {
        "País":InfoCovidPais,
        "Código":InfoCovidCodPais,
        "Nuevos casos confirmados":InfoCovidNuevosConf,
        "Total de casos confirmados":InfoCovidTotalConf,
        "Nuevas muertes":InfoCovidNuevasMuertes,
        "Total de muertes":InfoCovidTotalMuertes,
        "Recuperdos del día":InfoCovidNuevosRecup,
        "Total de recuperados":InfoCovidTotalRecup
        }

        print("\n"
            f'Información sobre casos Covid en {InfoCovidArgActual["País"]}, actualizada {actualizacion}' "\n"
            f'      Nuevos casos confirmados: {InfoCovidArgActual["Nuevos casos confirmados"]}' "\n"
            f'      Total de casos confirmados: {InfoCovidArgActual["Total de casos confirmados"]:,}' "\n"
            f'      Nuevas muertes: {InfoCovidArgActual["Nuevas muertes"]}' "\n"
            f'      Total de muertes: {InfoCovidArgActual["Total de muertes"]:,}' "\n"
            f'      Nuevos recuperados: {InfoCovidArgActual["Recuperdos del día"]}' "\n"
            f'      Total de recuperados: {InfoCovidArgActual["Total de recuperados"]:,}' "\n"
            f'      '"\n"
            f'      Total global de casos confirmados: {infoCovidGlobalConfirm:,}' "\n"
            f'      Total global de casos recuperados: {infoCovidGlobalRecup}' "\n"
            f'      ')
        
        porcentajeConfirmArg = InfoCovidTotalConf/infoCovidGlobalConfirm
        
        print(f'      Participación argentina de casos Covid en el mundo: {porcentajeConfirmArg:0.2%}')

        if(infoCovidGlobalRecup == 0):
            print("      El porcentaje de recuperados argentinos en el mundo es indeterminado")
            pass
        else:
            porcentajeRecupArg = InfoCovidTotalRecup/infoCovidGlobalRecup
            print(f'      El porcentaje de recuperados argentinos del global mundial es {porcentajeRecupArg:0.2%}'"\n"
            f'     ')

        archivoInforme = open("Informe_Covid_Argenina.json", "w")
        archivoInforme.write(str(InfoCovidArgActual))
        archivoInforme.close

        print(f'\n      Se ha creado el archivo Informe_Covid_Argenina.json')

        print(f'\n INFORME FINALIZADO\n ')

# BLOQUE CENTRAL
if (__name__ == "__main__"):
	main()