import matplotlib.pyplot as plt
import numpy as np

def generar_grafica_estetizada(delta, resultados, x_max, save_path=None):
    """
    Genera la gráfica con el estilo visual avanzado solicitado.
    
    delta: Array del eje X (radianes)
    resultados: Lista de tuplas (N, y_intensidad)
    delta_max: Valor límite (ej. 2.5) para posicionar textos y ejes.
    """
    n_graficas = len(resultados)
    
    # Configuración mejorada de gráficas apiladas
    fig, axs = plt.subplots(n_graficas, 1, figsize=(10, 14), sharex=True)
    plt.subplots_adjust(hspace=0.3)  # Espacio más ajustado

    for i, (N, y) in enumerate(resultados):
        ax = axs[i]

        # Pintar la línea negra sólida con mejor grosor
        ax.plot(delta, y, 'k', linewidth=1.5)

        # --- CONFIGURACIÓN ESTÉTICA (Copiada de tu snippet) ---
        ax.set_ylim(0, 1.15) # Un poco más de aire para el texto
        ax.set_yticks([])
        
        # Líneas de guía en y=1 para referencia
        ax.axhline(y=1.0, color='red', alpha=0.3, linestyle=':', linewidth=0.8)
        
        # Líneas verticales en los órdenes de interferencia (-2, -1, 0, 1, 2)
        tick_m_values = [-2, -1, 0, 1, 2]
        for m in tick_m_values:
            ax.axvline(x=m * 2 * np.pi, color='gray', alpha=0.2, linestyle='-', linewidth=0.5)

        # Etiquetas personalizadas con lógica de color
        if N >= 50: # Asumimos 50 o más como "muy grande"
            label_text = "N muy grande"
            color_text = 'red'
        else:
            label_text = f"N = {N}"
            color_text = 'black'

        # Texto posicionado con bbox (caja redondeada)
        ax.text(x_max * np.pi + 0.2, 0.85, label_text, 
                fontsize=11, fontweight='bold', color=color_text,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))

        # Configuración de ticks del eje X
        # Convertimos los enteros -2, -1... a radianes para saber DONDE poner el tick
        ax.set_xticks([m_val * 2 * np.pi for m_val in tick_m_values])
        
        # Solo mostrar labels numéricos en el último subplot
        if i == n_graficas - 1:
            ax.set_xlabel(r'$m = \frac{a \sin \theta}{\lambda}$', fontsize=13, labelpad=10)
            ax.set_xticklabels([str(m_val) for m_val in tick_m_values])
        else:
            ax.tick_params(labelbottom=False) # Ocultar números
        
        # Grid sutil
        ax.grid(True, alpha=0.1, axis='x')
        
        # Marcar el borde de cada subplot (Spines)
        for spine in ax.spines.values():
            spine.set_edgecolor('gray')
            spine.set_alpha(0.3)

    # Título general
    fig.suptitle('Patrón de Interferencia de Múltiples Rendijas', 
                 fontsize=14, y=0.92, fontweight='bold')

    # Guardar o mostrar
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfica guardada en: {save_path}")
    else:
        plt.show()
