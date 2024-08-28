# Compresión de Imágenes con SVD: Interactividad y Visualización

¿Alguna vez te has preguntado cómo funcionan los algoritmos de compresión de imágenes? ,es un tema fascinante que combina matemáticas y tecnología. 

El código implementa un algoritmo de compresión de imágenes a color utilizando SVD, permitiendo:

1.	Compresión por canales: Procesa cada canal de color (R, G, B) de manera independiente.
2.	Visualización: Muestra los resultados de la compresión de forma clara y atractiva.
3.	Interactividad: Permite ajustar el nivel de compresión en tiempo real o visualizar comparaciones estáticas.

Opción 1: Función Interactiva
La función imagen_comprimida_interactiva() ofrece una experiencia dinámica:
•	Control en tiempo real: Utiliza un slider para ajustar el número de componentes en la compresión.
•	Visualización instantánea: Muestra la imagen comprimida y actualiza el error de reconstrucción a medida que cambias los componentes.
•	Aprendizaje práctico: Ideal para entender cómo la compresión afecta la calidad de la imagen de manera intuitiva.

¿Por qué es interesante?

1.	Aplicación práctica de álgebra lineal: Muestra cómo se utilizan conceptos matemáticos en el procesamiento de imágenes.
2.	Balance entre calidad y tamaño: Permite explorar el compromiso entre la calidad de la imagen y su tamaño comprimido.
3.	Interacción intuitiva: Hace que el aprendizaje sea más atractivo y accesible.

Opción 2: Función No Interactiva

La función graficas_ima_compri_color() proporciona una visualización estática:

•	Comparación lado a lado: Muestra la imagen original junto a cinco versiones comprimidas con diferentes niveles de componentes.
•	Análisis visual: Permite observar cómo la calidad de la imagen se degrada a medida que se reduce el número de componentes.
•	Error de reconstrucción: Cada imagen comprimida incluye su error de reconstrucción, lo que facilita la evaluación de la calidad.

¿Por qué es fascinante?

1.	Gradiente de compresión: Observa cómo la imagen se vuelve menos detallada pero aún reconocible incluso con solo 10 componentes.
2.	Cuantificación del error: Proporciona una medida numérica del error para cada nivel de compresión.
3.	Estudio de características importantes: Revela qué elementos de una imagen son más "esenciales" según el algoritmo SVD.


Ambas funciones ofrecen perspectivas únicas sobre la compresión de imágenes.
La opción interactiva es perfecta para una exploración práctica y dinámica, mientras que la opción no interactiva permite un análisis comparativo claro y directo.
Ya sea que elijas experimentar con la interactividad o prefieras la visualización estática, ¡te animo a probar el código y descubrir el poder de la compresión de imágenes utilizando SVD! 
¿Listo para sumergirte en el mundo de la compresión de imágenes? 

## Acceso al Código

Puedes acceder al código completo para la compresión de imágenes utilizando SVD aquí:

[Ver Código de Compresión de Imágenes con SVD](compresion.py)

## Cómo Usar

1. Asegúrate de tener Python instalado en tu sistema.
2. Copia el código del enlace anterior en un archivo .py en tu computadora.
3. Ejecuta el archivo Python.
