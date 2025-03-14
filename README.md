# Funciones de Activación y sus Derivadas

Este proyecto implementa y grafica las funciones de activación **Sigmoid, ReLU y TanH**, junto con sus respectivas derivadas. Estas funciones son esenciales en redes neuronales para introducir no linealidad y permitir el aprendizaje de patrones complejos.

## 📌 Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install numpy matplotlib
🚀 Ejecución
Para ejecutar el script y visualizar las gráficas, simplemente corre:

bash
Copiar
Editar
python main.py
📂 Estructura del Proyecto
css
Copiar
Editar
project/
│── src/
│   │── sigmoid.py
│   │── relu.py
│   │── tanh.py
│── main.py
│── README.md
📊 Descripción del Código
main.py:

Importa las funciones de activación y sus derivadas desde la carpeta src/.
Genera un conjunto de valores en el rango [-5, 5].
Grafica las funciones Sigmoid, ReLU y TanH junto con sus derivadas.
Muestra todas las gráficas en una figura de Matplotlib.
src/sigmoid.py:

Implementa la función sigmoid(x) y su derivada sigmoid_derivative(x).
src/relu.py:

Implementa la función relu(x) y su derivada relu_derivative(x).
src/tanh.py:

Implementa la función tanh(x) y su derivada tanh_derivative(x).
📷 Ejemplo de Salida
El script generará una figura con seis gráficos mostrando cada función y su derivada:

Sigmoid y su derivada
ReLU y su derivada
TanH y su derivada
📌 Notas
Asegúrate de que la carpeta src/ contenga correctamente los archivos de las funciones de activación.
Si usas un entorno virtual, activa el entorno antes de ejecutar el código.
