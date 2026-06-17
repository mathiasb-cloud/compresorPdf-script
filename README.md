# Optimizador de PDF Avanzado (Ghostscript)

## 📌 Descripción
Script automatizado en Python diseñado para reducir drásticamente el tamaño de archivos PDF sin depender de herramientas en la nube. Utiliza **Ghostscript** como motor de procesamiento y ofrece un control granular sobre la resolución (DPI), lo que permite realizar ajustes finos para alcanzar tamaños de archivo específicos (por ejemplo, para cumplir con límites de subida en plataformas web).

## 🚀 Características
- **Control Manual de DPI:** Ajusta la resolución de salida (ej. 72, 100, 150 DPI) para encontrar el equilibrio exacto entre calidad visual y peso en Megabytes.
- **Detección Multiplataforma:** Asigna automáticamente los comandos de Ghostscript correspondientes según el sistema operativo (Windows, macOS o Linux).
- **Cero Dependencias de Python:** Escrito utilizando únicamente la biblioteca estándar de Python (`os`, `subprocess`). No requiere `pip install`.
- **Protección de Archivos Originales:** Diseñado para generar nuevos archivos de salida seguros.

---

## 🛠️ Requisitos Previos

Para que el script funcione, es estrictamente necesario tener instalado **Python 3** y **Ghostscript** en tu sistema.

### Instalación de Ghostscript:
- **macOS (con Homebrew):**
  ```bash
  brew install ghostscript
Windows:
Descarga el instalador desde la página oficial o usa winget:

DOS
winget install ArtifexSoftware.Ghostscript
Linux (Ubuntu/Debian):

Bash
sudo apt-get update
sudo apt-get install ghostscript
⚙️ Configuración y Uso
Clona o descarga este repositorio.

Prepara tu espacio de trabajo: Coloca el archivo PDF que deseas comprimir en la misma carpeta donde se encuentra el script comprimir.py.

Configura el script: Abre comprimir.py en tu editor de código favorito y modifica la sección de ejecución principal al final del archivo:

Python
if __name__ == "__main__":
    # IMPORTANTE: Los nombres deben ser DIFERENTES
    archivo_entrada = "tu_archivo_original.pdf"
    archivo_salida = "tu_archivo_comprimido.pdf"

    # Ajusta este valor para controlar el peso final
    resolucion_dpi = 100 

    comprimir_pdf_avanzado(archivo_entrada, archivo_salida, dpi=resolucion_dpi)
Ejecuta el script desde tu terminal:
Abre la terminal en la carpeta del proyecto y ejecuta:

En macOS / Linux:

Bash
python3 comprimir.py
En Windows:

DOS
python comprimir.py
⚠️ Notas Importantes y Solución de Problemas
Archivos de 0 Bytes: Asegúrate de que archivo_entrada y archivo_salida tengan nombres diferentes. Si usas exactamente el mismo nombre para ambos, Ghostscript vaciará tu archivo original antes de procesarlo, dejándolo en 0.00 MB.

Ajuste Fino de Tamaño: Los compresores de PDF no permiten fijar un peso exacto de salida (ej. "39 MB"). Para llegar a un peso objetivo, realiza pruebas modificando la variable resolucion_dpi. Si el archivo final pesa demasiado, baja el valor (ej. a 90 o 85). Si pesa muy poco y pierde calidad, súbelo (ej. a 120 o 150).
