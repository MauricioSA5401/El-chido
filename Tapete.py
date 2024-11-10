import matplotlib.pyplot as plt
import matplotlib.patches as patches

def sierpinski_carpet(ax, x, y, size, depth):
    if depth == 0:
        ax.add_patch(patches.Rectangle((x, y), size, size, edgecolor='black', facecolor='black'))
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # El cuadrado central se omite
                    
                    
                    continue
                sierpinski_carpet(ax, x + i * new_size, y + j * new_size, new_size, depth - 1)

# Parámetros iniciales
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_axis_off()

# Llamada a la función para generar el fractal
sierpinski_carpet(ax, 0, 0, 1, 4)  # Puedes cambiar el nivel de profundidad (4) para obtener más o menos detalle

# Mostrar el fractal
plt.show()
