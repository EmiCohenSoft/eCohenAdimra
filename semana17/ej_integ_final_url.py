# LIBRERIAS
import requests as req
import os
from dotenv.main import load_dotenv
load_dotenv()

# DEFINICIONES

PRDTO_URL = os.getenv("ITEC_URL")
PRDTO_PUERTO = os.getenv("ITEC_PUERTO")
PRDTO_DIR_PROD = os.getenv("ITEC_DIR_PROD")
PRDTO_DIR_PEDIDO = os.getenv("ITEC_DIR_PEDIDO")
PRDTO_TOKEN = os.getenv("ITEC_TOKEN")

URL_LISTA_PROD = (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR_PROD}?token={PRDTO_TOKEN}")
URL_LISTA_PEDIDO = (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR_PEDIDO}?token={PRDTO_TOKEN}")
 

# FUNCIONES

def consulta_prod(url_consulta):
    consulta = req.get(url_consulta)
    if(consulta.status_code == 200):
        recup_prod = consulta.json()
        # print(recup_prod["productos"])
        
        indice_producto = 0
        limite_producto = recup_prod["productos"][indice_producto]
        try:
            print(f'Prdto.id    Descripción')
            while (limite_producto is not None):
                lista_id_nombre = recup_prod["productos"][indice_producto]["nombre"]
                print(f'{indice_producto:<12}{lista_id_nombre}')
                indice_producto +=1
        except: pass
        return recup_prod

    else:
        print ("Consulta de productos insatisfactoria")
        pass


def carga_pedido(url_pedido):
    pedido = req.post(url_pedido,{"id":"8","cantidad":5})
    if(pedido.status_code == 200):
        recup_pedido = pedido.json()
        print(recup_pedido["mensaje"],"con N°",recup_pedido["codigo"])
        # return recup_pedido
    else:
        print("sin pedido")


def main(): 
    prod_disp = consulta_prod(URL_LISTA_PROD)

    if(prod_disp):
        lista_prod = prod_disp["productos"]
        # print(lista_prod)
        
    else:
        print("Error")

    sube_pedido = carga_pedido(URL_LISTA_PEDIDO)

    # if(sube_pedido):







# BLOQUE CENTRAL
if (__name__ == "__main__"):
	main()