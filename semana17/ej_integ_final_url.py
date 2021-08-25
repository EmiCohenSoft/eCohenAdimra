# EMILIANO COHEN
# 24/08/2021. CURSO INTRO. PROG. ADIMRA 2021
# ej_final_semana_17
# https://github.com/EmiCohenSoft/eCohenAdimra

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

URL_LISTA_PROD = (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR_PROD}10?token={PRDTO_TOKEN}")
URL_LISTA_PEDIDO = (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR_PEDIDO}10?token={PRDTO_TOKEN}")

MSN_URL = os.getenv("TELEG_URL")
MSN_TOKEN = os.getenv("TELEG_TOKEN")
MSN_ENDPOINT = os.getenv("TELEG_ENDPOINT_MSN")
MSN_ID_ADIMRA = os.getenv("TELEG_ID_ADIMRA")
MSN_ID_ECOHEN = os.getenv("TELEG_ID_ECOHEN")

# URL_MSN = f'{MSN_URL}{MSN_TOKEN}/{MSN_ENDPOINT}?chat_id={MSN_ID_ADIMRA}&text='
URL_MSN = f'{MSN_URL}{MSN_TOKEN}/{MSN_ENDPOINT}?chat_id={MSN_ID_ECOHEN}&text='


# FUNCIONES

# Esta función consulta el servidor, trae la lista de productos, lo convierte a formato json,
# y por medio de un ciclo lo muestra como lista con nombre, stock y precio

# ¡¡¡¡¡¡¡¡SEGURO HAY UNA FORMA CORRECTA DE HACER ESTE CICLADO SIN EL EXCEPT!! ¿CUAL SERÁ?

def consulta_prdto(url_consulta):
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
        except: pass
    else:
        print ("Consulta de productos insatisfactoria")
        pass
    return recup_prod

# Se selecciona el id de producto, y si es correcto, la función muestra el nombre, sino te lleva arriba.
# Se escribe la cantidad y a continuación se valida el inventario. 
def seleccion_pdtos(url_seleccion):
    consulta = req.get(url_seleccion)
    lista_pdto = consulta.json()

    stock_validado = False
    while not(stock_validado):
        try:
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
            print('\t\t'"Error al seleccionar el producto")
    return dicc_pedido


# Se postea el reqerimiento y el servidor devuelve un mensaje con el número de pedido
def envio_pedido(url_pedido,matr_pedido):
    try:
        pedido = req.post(url_pedido,matr_pedido)
        if(pedido.status_code == 200):
            recup_pedido = pedido.json()
            # print(recup_pedido)

            print(recup_pedido["mensaje"],"con N°",recup_pedido["codigo"])
        else:
            print("No se logro establecer la conexión")
    except: 
        print("No se pudo carga el pedido")


# Se consulta por número de pedido, se verifica si existe, y si valida, se envía el detalle en un msn a Telegram
# Si no se conecta a Telegram comunica el error.
def envio_msn(url_msn,url_seleccion):
    numero_pedido = 0
    
    while(True):
        numero_pedido = input('\n' f'Indique el número del pedido a consultar '
                                    'o presione asterisco para salir''\n')
        if (numero_pedido == "*"):
            print("Consulta finalizada"'\n')
            break
        else:
            try:
                URL_PEDIDO= (f"{PRDTO_URL}:{PRDTO_PUERTO}/{PRDTO_DIR_PEDIDO}{numero_pedido}?token={PRDTO_TOKEN}")
                consulta_prdto = req.get(url_seleccion)
                consulta_pedido = req.get(URL_PEDIDO)
                
                if(consulta_pedido.status_code == 200 and consulta_prdto.status_code == 200):
                    
                    recup_pedido = consulta_pedido.json()
                    prdto_pedido = consulta_prdto.json()

                    id_prdto_pedido = recup_pedido["productos"]["id"]
                    cant_pedido = recup_pedido["productos"]["cantidad"]

                    nombre_prod_pedido = prdto_pedido["productos"][int(id_prdto_pedido)]["nombre"]

                    msn_telegram = ('\n'f'Pedido de Emiliano Cohen, N°: {numero_pedido}''\n'f'Prod: {nombre_prod_pedido}''\n'
                    f'Cant.: {cant_pedido}''\n')
                    print(msn_telegram)
                                        
                    msn_pedido = (f'{url_msn}{msn_telegram}')
                    
                    envio_msn = req.get(msn_pedido)
                    if(envio_msn.status_code == 200):
                        print("Confirmación de pedido enviado")
                    else:
                        print("Error de envío del detalle del pedido")

                else:
                    print("Pedido inexistente")
            except: 
                print("No hay pedido con ese número")


# Luego revisar el listado de productos, se puede salir con asterisco, o consultar un pedido. 
def main(): 
    prod_disp = consulta_prdto(URL_LISTA_PROD)

    while(True):
        nuevo_pedido = input('\n' f'Presione asterisco para cancelar el pedido '
        'o cualquier tecla para solicitar un producto''\n')
        if (nuevo_pedido == "*"):
            print("Pedido concluído")
            break
        else:
            pedido_json = seleccion_pdtos(URL_LISTA_PROD)
            sube_pedido = envio_pedido(URL_LISTA_PEDIDO,pedido_json)

    envio_ms_teleg = envio_msn(URL_MSN,URL_LISTA_PROD)
    
    
# BLOQUE CENTRAL
if (__name__ == "__main__"):
	main()