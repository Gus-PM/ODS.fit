# Notebooks de Análisis

Esta carpeta contiene Jupyter notebooks para análisis exploratorio y documentación del proceso.

## Notebooks de Procesamiento

### 1_Manejo_Datos.ipynb
**Procesamiento de datos educativos en Google Colab** (Principal)

Este notebook construye el archivo `Datos.csv` desde los datos raw almacenados en Google Drive.
Desarrollado por el equipo ODS.fit.

### 001_procesamiento_colab.ipynb
**Versión alternativa de procesamiento en Google Colab**

Este notebook también construye el archivo `Datos.csv` desde los datos raw almacenados en Google Drive.

**Uso en Google Colab:**
1. Abre el notebook en Google Colab
2. Accede al [Google Drive compartido](https://drive.google.com/drive/folders/1TD6nWykXvYCX38hpVhopqc6mqzv3epJo?usp=drive_link)
3. Añade acceso directo a tu Drive: `Mi unidad/HackODS/datos/`
4. Monta Google Drive ejecutando la primera celda
5. Ejecuta las celdas restantes en orden

**Input:** Archivos CSV desde Google Drive (SEP - Estadística 911, INEGI)  
**Output:** `Datos.csv` (19 variables, 160 registros)

**Proceso:**
- Lectura de archivos de educación básica y media superior (2019-2025)
- Homologación de columnas entre diferentes años
- Consolidación y agregación por estado y nivel
- Cálculo de porcentajes de abandono escolar
- Cálculo de distribución de género en docentes e inscripciones

### 002_procesamiento_local.ipynb
**Versión alternativa para ejecución local (opcional)**

Notebook para trabajar localmente descargando los datos del Drive.  
Solo necesario si quieres regenerar el dataset sin usar Colab.

## Notebooks Futuros

Los siguientes notebooks se crearán conforme avance el proyecto:

- `003_analisis_exploratorio.ipynb` - EDA completo del dataset
- `004_visualizaciones_ods4.ipynb` - Visualizaciones para calidad educativa
- `005_analisis_genero.ipynb` - Análisis de brechas de género
- `006_desigualdades_regionales.ipynb` - Análisis por estado

## ¿Cuál notebook usar?

**Para generar/regenerar el dataset procesado:**
- 👉 Usa `1_Manejo_Datos.ipynb` en Google Colab (no requiere descargar 800 MB)
- Alternativa: `001_procesamiento_colab.ipynb`

**Para trabajar localmente con los datos raw descargados:**
- 👉 Usa `002_procesamiento_local.ipynb` 

**Para análisis (usando datos ya procesados):**
- 👉 Usa directamente `datos/processed/Datos.csv` (ya está en el repo)
- 👉 Crea notebooks nuevos (003, 004, etc.) para tus análisis

## Datos Raw

Los archivos CSV originales (~ 800 MB) solo existen en Google Drive:

https://drive.google.com/drive/folders/1TD6nWykXvYCX38hpVhopqc6mqzv3epJo?usp=drive_link

Contiene:
- Archivos de educación básica (2021-2025)
- Archivos de media superior (2019-2025)
- Formato: CSV con encoding latin1

No están en el repositorio. El notebook `001_procesamiento_colab.ipynb` accede directamente desde Colab.

## Uso Local

```bash
cd /path/to/ODS.fit
source .venv/bin/activate
jupyter lab
```

Abrir el notebook deseado y ejecutar las celdas en orden.

## Convenciones

- Numerar notebooks con formato 00X (001, 002, etc.)
- Incluir título, objetivo y autores al inicio
- Documentar decisiones y hallazgos importantes
- Usar rutas relativas para portabilidad
- Incluir resumen al final del notebook
