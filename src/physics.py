    delta = m * 2 * np.pi
    
def calcular_intensidad_normalizada(delta, N):
    
    #Calcula la intensidad relativa I/I0 para una red de difracción de N rendijas.
    
    N = float(N)

    numerador = np.sin(N * delta / 2)

    # Se agrega un epsilon muy pequeño para mantener la coherencia de la operación y no dividir entre '0'
    epsilon = 1e-10
    denominador = np.sin(delta / 2) + epsilon

    # Fórmula de la intensidad
    intensidad = (numerador / denominador)**2

    # Normalización de la expresión
    intensidad_norm = intensidad / (N**2)

    return intensidad_norm
