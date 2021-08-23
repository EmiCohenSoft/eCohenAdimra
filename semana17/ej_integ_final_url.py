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
    consulta_lista = req.get(url_consulta)
    if(consulta_lista.status_code == 200):
        recup_prod = consulta_lista.json()
        
        indice_producto = 0
        limite_producto = recup_prod["productos"][indice_producto]
        try:
            print('\n' f'Pdto.\tPrecio($)\tStock\tDescripción')
            while (limite_producto is not None):
                lista_nombres = recup_prod["productos"][indice_producto]["nombre"]
                lista_precio = float(recup_prod["productos"][indice_producto]["precio"])
                lista_stock = recup_prod["productos"][indice_producto]["stock"]
                print(f'{indice_producto}\t{lista_precio:7.2f}\t\t{lista_stock:>5}\t{lista_nombres}')
                indice_producto +=1
        except: print()
        pass
    else:
        print ("Consulta de productos insatisfactoria")
        pass
    return recup_prod


def seleccion_pdtos(url_seleccion):
    consulta = req.get(url_seleccion)
    lista_pdto = consulta.json()

    stock_validado = False
    while not(stock_validado):
        try:
            print()
            id_pdto = input('Códido de pdto.: ')
            nombre_pdto = lista_pdto["productos"][int(id_pdto)]["nombre"]
            cant_pdto = int(lista_pdto["productos"][int(id_pdto)]["stock"])
            print('\t\t'f'Hay {cant_pdto} unid. disponibles de {nombre_pdto}\n')
            cant_req = int(input("Cant. requerida: "))
            if(cant_req > cant_pdto):
                stock_validado = False
                print('\t\t'f'Solo hay {cant_pdto} unidades en stock.')
            else:
                stock_validado = True
                dicc_pedido = {"id":id_pdto,"cantidad":cant_req}
                break
        except:
            print("Error al seleccionar el producto")
    return dicc_pedido


def envio_pedido(url_pedido,matr_pedido):
    try:
        # pedido = req.post(url_pedido,{"id":"8","cantidad":5})
        pedido = req.post(url_pedido,matr_pedido)
        if(pedido.status_code == 200):
            recup_pedido = pedido.json()
            print(recup_pedido["mensaje"],"con N°",recup_pedido["codigo"])
            # return recup_pedido
        else:
            print("No se logro establecer la conexión")
    except: 
        print("No se pudo carga el pedido")


def main(): 
    prod_disp = consulta_prod(URL_LISTA_PROD)

    while(True):
        nuevo_pedido = input('\n' f'Presione ENTER para cargar nuevo pedido o asterisco para finalizar''\n')
        if (nuevo_pedido == "*"):
            break
        else:
            pedido_json = seleccion_pdtos(URL_LISTA_PROD)
            sube_pedido = envio_pedido(URL_LISTA_PEDIDO,pedido_json)


# BLOQUE CENTRAL
if (__name__ == "__main__"):
	main()