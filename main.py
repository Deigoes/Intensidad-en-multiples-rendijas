import json
import numpy as np
import os
from src.physics import calcular_intensidad
from src.plots import generar_grafica_estetizada 

def cargar_configuracion():
    """Lee el archivo JSON de configuración."""
    ruta_config = os.path.join('config', 'settings.json')
    with open(ruta_config, 'r') as f:
        return json.load(f)

def main():
    # 1. CARGAR CONFIGURACIÓN
    print("Leyendo configuración...")
    try:
        config = cargar_configuracion()
    except FileNotFoundError:
        print("¡ERROR! No encuentro el archivo config/settings.json")
        print("Asegúrate de haber creado la carpeta 'config' y el archivo 'settings.json'.")
        return

    delta_max = config['delta_max']
    resolucion = config['resolucion']
    n_valores = config['n_values']
    output_name = config['output_filename']

    # 2. PREPARACIÓN DE DATOS
    delta = np.linspace(-delta_max * np.pi, delta_max * np.pi, resolucion)
    
    resultados = []
    
    print(f"Calculando para N = {n_valores}...")
    for N in n_valores:
        y = calcular_intensidad(delta, N)
        resultados.append((N, y))
    
    # 3. VISUALIZACIÓN
    if not os.path.exists('results'):
        os.makedirs('results')
    
    ruta_salida = os.path.join('results', output_name)
    print(f"Generando gráfica en {ruta_salida}...")
    
    generar_grafica_estetizada(delta, resultados, delta_max, save_path=ruta_salida)
    
    print("¡Proceso terminado con éxito!")

if __name__ == "__main__":
    main()
    