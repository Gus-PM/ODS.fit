# Scripts de Análisis

Esta carpeta contiene scripts de Python para analizar y validar los datos procesados.

## Scripts Disponibles

### analisis_exploratorio.py
**Análisis exploratorio de datos (EDA)**

Genera un reporte completo del dataset con:
- Dimensiones y cobertura del dataset
- Totales nacionales (inscripciones, docentes, egresados)
- Distribución de género en estudiantes y docentes
- Análisis por nivel educativo
- Top 5 estados con más inscripciones
- Análisis de tasas de abandono escolar

**Uso:**
```bash
source .venv/bin/activate
python scripts/analisis_exploratorio.py
```

**Input:** `datos/processed/Datos.csv`  
**Output:** Reporte en consola

### validar_datos.py
**Validación de integridad del dataset**

Verifica que el archivo `Datos.csv` cumpla con:
- Dimensiones correctas (160 filas × 19 columnas)
- Consistencia matemática (sumas, porcentajes)
- Rangos válidos en todas las variables
- Sin valores nulos en columnas críticas

**Uso:**
```bash
source .venv/bin/activate
python scripts/validar_datos.py
```

**Input:** `datos/processed/Datos.csv`  
**Output:** Reporte de validación en consola

## Uso General

```bash
cd /path/to/ODS.fit
source .venv/bin/activate
python scripts/nombre_script.py
```

## Nota sobre Procesamiento

El procesamiento de datos raw se hace en `notebooks/001_procesamiento_colab.ipynb` (Google Colab).  
Estos scripts solo analizan y validan los datos ya procesados.
