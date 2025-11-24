import json
import numpy as np
import os
from src.physics import calcular_intensidad
from src.plots import generar_grafica_libro

def main():
    print("Configuración...")
    with open('config/settings.json', 'r') as f:
        config = json.load(f)
    
    m = np.linspace(config['x_min'], config['x_max'], config['resolution'])
    resultados = []
    
    print("Ejecutando expresión...")
    for N in config['N_values']:
        intensidad = calcular_intensidad(m, N)
        resultados.append((N, intensidad))
    
    print("Gráficos...")
    if not os.path.exists('results'):
        os.makedirs('results')
        
    output_file = 'results/patron_difraccion.png'
    generar_grafica_libro(m, resultados, save_path=output_file)
    print("Proceso completado")

if __name__ == "__main__":
    main()
