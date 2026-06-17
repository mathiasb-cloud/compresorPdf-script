"""
Herramienta de Compresión de PDF
Descripción: Reduce el tamaño de archivos PDF utilizando Ghostscript.
"""

__version__ = "1.1.0"
__status__ = "Producción"

import subprocess
import os

def comprimir_pdf(ruta_entrada, ruta_salida, nivel_calidad="/screen"):
    """
    Niveles de calidad:
    - /screen   : Máxima compresión (ideal para enviar por correo).
    - /ebook    : Compresión media (mejor calidad visual).
    - /printer  : Baja compresión (alta calidad).
    """
    if not os.path.exists(ruta_entrada):
        print(f"[Error] El archivo '{ruta_entrada}' no existe.")
        return False

    comando_gs = "gswin64c" if os.name == 'nt' else "gs"

    argumentos = [
        comando_gs,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={nivel_calidad}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={ruta_salida}",
        ruta_entrada
    ]

    try:
        print(f"[{__version__}] Comprimiendo: '{ruta_entrada}'...")
        subprocess.run(argumentos, check=True)
        
        tamano_original = os.path.getsize(ruta_entrada) / (1024 * 1024)
        tamano_final = os.path.getsize(ruta_salida) / (1024 * 1024)
        ahorro = 100 - ((tamano_final / tamano_original) * 100)
        
        print(f"[Éxito] Archivo guardado como '{ruta_salida}'")
        print(f" > Tamaño original : {tamano_original:.2f} MB")
        print(f" > Tamaño final    : {tamano_final:.2f} MB")
        print(f" > Reducción       : {ahorro:.2f}%\n")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"[Error] Fallo en Ghostscript: {e}")
        return False
    except FileNotFoundError:
        print("[Error] Ghostscript no encontrado. Asegúrate de instalarlo y agregarlo al PATH.")
        return False

# ==========================================
# Bloque de ejecución principal
# ==========================================
if __name__ == "__main__":
    # Nombres de tus archivos
    archivo_entrada = "documento.pdf"
    archivo_salida = "documento_comprimido.pdf"
    
    # Ejecutamos la función
    comprimir_pdf(archivo_entrada, archivo_salida, nivel_calidad="/screen")