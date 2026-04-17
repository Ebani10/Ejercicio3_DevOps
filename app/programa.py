"""
import os

# 1. Configurar rutas (usando el truco del directorio actual)
dir_actual = os.path.dirname(__file__)
ruta_entrada = os.path.join(dir_actual, 'lista.txt')
ruta_salida = os.path.join(dir_actual, 'organizado.txt')

try:
    # 2. Leer y filtrar
    with open(ruta_entrada, 'r', encoding='utf-8') as entrada:
        lineas = entrada.readlines()
    
    # Supongamos que filtramos líneas que contienen la palabra "IMPORTANTE"
    # O líneas que no estén vacías. Aquí puedes poner tu lógica.
    datos_filtrados = [linea for linea in lineas if "FILTRO" in linea.upper()]

    # 3. Escribir en el nuevo archivo
    with open(ruta_salida, 'w', encoding='utf-8') as salida:
        for item in datos_filtrados:
            salida.write(item)
            
    print(f"¡Proceso terminado! Se creó '{ruta_salida}' con los datos filtrados.")

except FileNotFoundError:
    print("Error: No se encontró el archivo lista.txt")
    """

import os
import sys
from datetime import datetime

def procesar_datos():
    # --- CONFIGURACIÓN DE RUTAS ---
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_entrada = os.path.join(dir_actual, 'lista.txt')
    archivo_salida = os.path.join(dir_actual, 'resultados.txt')
    archivo_log = os.path.join(dir_actual, 'backup.log')


    # Si pasas un argumento al ejecutar, lo toma. Si no, usa "V1.0" por defecto.
    version_cambio = sys.argv[1] if len(sys.argv) > 1 else os.getenv('APP_VERSION', 'V1.0-auto')
   
    try:
        # A. LEER INFORMACIÓN
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        # B. PROCESAR / FILTRAR (Ejemplo: filtrar líneas que no estén vacías y tengan más de 3 caracteres)
        # Aquí puedes cambiar la condición por lo que necesites
        datos_filtrados = [l.strip() for l in lineas if len(l.strip()) > 3]
        total_procesados = len(datos_filtrados)

        # C. GENERAR ARCHIVO CON RESULTADOS
        with open(archivo_salida, 'w', encoding='utf-8') as f_out:
            for dato in datos_filtrados:
                f_out.write(f"{dato}\n")

        # D. REGISTRO DE ACTIVIDAD (LOG)
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Formato del log: Fecha | Archivo | Resultado | Versión
        mensaje_log = (f"[{fecha_hora}] Archivo: {os.path.basename(archivo_entrada)} | "
                       f"Resultado: Se filtraron {total_procesados} datos | "
                       f"Versión: {version_cambio}\n")

        with open(archivo_log, 'a', encoding='utf-8') as f_log:
            f_log.write(mensaje_log)

        print(f"--- Proceso Completado ---")
        print(f"Se filtraron {total_procesados} datos.")
        print(f"Actividad registrada en backup.log")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {archivo_entrada}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    procesar_datos()