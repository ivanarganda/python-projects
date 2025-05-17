# Proyecto de Automatización en Python

Este repositorio contiene diferentes proyectos y ejercicios organizados por nivel de dificultad: **básico**, **intermedio** y **avanzado**. El enfoque principal está en la automatización utilizando Python, con ejemplos prácticos y utilidades para el aprendizaje progresivo.

## Requisitos Previos

1. **Python 3.12 o superior**: Asegúrate de tener Python instalado en tu sistema.
2. **Entorno Virtual**: Para mantener las dependencias aisladas del sistema.

### Configuración del Entorno Virtual

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Unix/MacOS:**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

## Estructura del Proyecto

### Niveles de Dificultad

- **`/basico`**  
  Ejercicios y scripts introductorios de Python. Incluye proyectos como:
  - **adivinar_numero/**: Juego interactivo para adivinar un número aleatorio.
  - **calculadora/**: Calculadora básica de operaciones aritméticas.
  - **conversor_monedas_o_temperatura/**: Conversor interactivo de monedas (USD/EUR) y temperaturas (Celsius/Fahrenheit).

- **`/intermedio`**  
  Proyectos para practicar estructuras de datos, manejo de archivos y módulos personalizados. *(Actualmente en desarrollo)*

- **`/avanzado/automatizacion`**  
  Sistema de automatización avanzado con Python, incluyendo menús configurables, utilidades y generación de ejecutables.

### Componentes Principales

```
/basico/
├── adivinar_numero/
│   ├── main.py
│   ├── README.md
│   ├── setup.py
│   └── helpers/
├── calculadora/
│   ├── main.py
│   ├── README.md
│   ├── setup.py
│   └── helpers/
├── conversor_monedas_o_temperatura/
│   ├── main.py
│   ├── README.md
│   └── helpers/
│
/intermedio/
│   └── (en desarrollo)
/avanzado/automatizacion/
├── main.py
├── menu.json
├── dispatches_menu.json
├── setup.py
├── helpers/
├── keyboard_shortcuts/
└── build/
```

## Inicio Rápido

1. Clona el repositorio.
2. Activa el entorno virtual.
3. Instala dependencias (si aplica):
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el proyecto que desees, por ejemplo:
   ```bash
   python basico/adivinar_numero/main.py
   python basico/calculadora/main.py
   python basico/conversor_monedas_o_temperatura/main.py
   python avanzado/automatizacion/main.py
   ```

## Compilación

Para generar ejecutables (por ejemplo, en la carpeta de automatización o calculadora):

```bash
python setup.py build
```

Los archivos compilados se encontrarán en `/build/exe.win-amd64-3.12/` dentro del proyecto correspondiente.

## Contribución

1. Haz fork del repositorio.
2. Crea una rama feature (`git checkout -b feature/NuevaFuncionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/NuevaFuncionalidad`).
5. Crea un Pull Request.

---

Para más información, consulta los README específicos de cada módulo o carpeta.