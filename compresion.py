import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from skimage import data

def sse_score(X, X_hat):
    return np.sum((X - X_hat)**2)

def svm(X):    
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    S = np.diag(s)
    return U, S, Vt

def reconstruction(U, S, Vt):
    return np.dot(U, np.dot(S, Vt))

def image_compression_color(A, n_comp):
    """
    Función que recibe una imagen A a color, devuelve la imagen comprimida y el error de reconstrucción
    """
    # Separar los canales de color
    R, G, B = A[:,:,0], A[:,:,1], A[:,:,2]
    
    # Comprimir cada canal
    R_hat, sse_R = image_compression(R, n_comp)
    G_hat, sse_G = image_compression(G, n_comp)
    B_hat, sse_B = image_compression(B, n_comp)
    
    # Reconstruir la imagen a color
    A_hat = np.dstack((R_hat, G_hat, B_hat))
    
    # Calcular el error total
    sse = sse_R + sse_G + sse_B
    
    return A_hat, sse

def image_compression(A, n_comp):
    U, S, Vt = svm(A)
    
    S_reducida = S[:n_comp,:n_comp]
    U_reducida = U[:,:n_comp]
    Vt_reducida = Vt[:n_comp,:]

    A_hat = reconstruction(U_reducida, S_reducida, Vt_reducida)

    sse = sse_score(A, A_hat)
    
    return A_hat, sse

def graficas_ima_compri_color(comp1=200, comp2=100, comp3=50, comp4=25, comp5=10):
    """
    Muestra las imágenes resultantes de aplicar el algoritmo de 
    Singular Value Decomposition para comprimir una imagen a color, con sus valores de error.
    Recibe 5 valores que por defecto son (200,  100, 50, 25, 10)
    Usamos la imagen "astronaut" de scikit-image.
    """    
    componentes = [comp1, comp2, comp3, comp4, comp5]
    imagen = data.astronaut()
    #imagen = np.array(Image.open(ruta_imagen))
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 20))
    fig.suptitle('IMÁGENES A COLOR\n Vs: Valores singulares\n E: Error de reconstrucción')
    axes = axes.ravel()
    
    axes[0].imshow(imagen)
    axes[0].set_title("Imagen Original")
    
    for plot, comp in zip(range(1,6), componentes):
        imagen_hat, sse = image_compression_color(imagen, n_comp=comp)
        axes[plot].imshow(imagen_hat.astype(np.uint8))
        axes[plot].set_title(f"Vs: {comp} \n E: {sse:.1e}")
    
    plt.tight_layout()
    plt.show()

def imagen_comprimida_interactiva():
    imagen = data.astronaut()
    #imagen = np.array(Image.open(ruta_imagen))
    fig, (ax_imagen, ax_slider) = plt.subplots(nrows=2, figsize=(10, 12), 
                                               gridspec_kw={'height_ratios': [20, 1]})
    plt.subplots_adjust(bottom=0.2)
    
    ax_imagen.set_title("Imagen Comprimida")
    imagen_plot = ax_imagen.imshow(imagen)
    
    ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
    slider = Slider(ax_slider, 'Componentes', 1, 400, valinit=400, valstep=1)
    
    def actualizar(val):
        n_comp = int(slider.val)
        imagen_hat, sse = image_compression_color(imagen, n_comp=n_comp)
        imagen_plot.set_data(imagen_hat.astype(np.uint8))
        ax_imagen.set_title(f"Imagen Comprimida (Componentes: {n_comp}, Error: {sse:.1e})")
        fig.canvas.draw_idle()
    
    slider.on_changed(actualizar)
    
    plt.show()

# Uso de la función interactiva
imagen_comprimida_interactiva()

# Si quieres usar la función no interactiva, descomenta la siguiente línea:
#graficas_ima_compri_color()

