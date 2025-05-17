# setup.py
import sys
from cx_Freeze import setup, Executable

# Opciones para build_exe
build_exe_options = {
    # Todos los paquetes que importas “dinámicamente” o que no detecte automáticamente
    "packages": ["helpers"],

    # Archivos y carpetas que quieres copiar tal cual
    "include_files": [
        "helpers",  # copia entera la carpeta helpers
    ],

}

# Si tu app es de consola o de ventana, puedes elegir base=None o "Win32GUI"
base = None
# base = "Win32GUI"  # si no quieres la ventana de consola

setup(
    name="conversor_monedas",
    version="1.0",
    description="Mi conversor de monedas en Python",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)