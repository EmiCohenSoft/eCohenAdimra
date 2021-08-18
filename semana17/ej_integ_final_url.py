# LIBRERIAS
import requests as req
import os
from dotenv.main import load_dotenv
load_dotenv()

# DEFINICIONES

PRDTO_URL = os.getenv("ITEC_URL")
PRDTO_PUERTO = os.getenv("ITEC_PUERTO")
PRDTO_DIR = os.getenv("ITEC_DIR")
PRDTO_TOKEN = os.getenv("ITEC_TOKEN")

URL_LISTA = (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR}?token={PRDTO_TOKEN}")
 

# FUNCIONES

def consultaProd(urlConsulta):
    consulta = req.get(urlConsulta)
    if(consulta.status_code == 200):
        recupProd = consulta.json()
        return recupProd
        # print(recupProd["productos"])
    else:
        print ("Consulta no lograda")
        pass


def main(): 
    prodDisp = consultaProd(URL_LISTA)

    if(prodDisp):
        listaProd = prodDisp["productos"]
        print(listaProd)
        
    else:
        print("Error")






# BLOQUE CENTRAL
if (__name__ == "__main__"):
	main()