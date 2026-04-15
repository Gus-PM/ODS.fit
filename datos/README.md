# Datos del Proyecto ODS.fit

Esta carpeta contiene los datos procesados utilizados para el análisis.

## Estructura

```
datos/
├── processed/                        # Datos procesados y limpios
│   └── Datos.csv                    # 50 KB - Dataset final
├── RESUMEN_EJECUTIVO.md             # Análisis del dataset
└── README.md                         # Este archivo
```

Los datos raw NO están en el repositorio (son ~800 MB).

## Dataset Principal

### Datos.csv
- **Ubicación:** `processed/Datos.csv`
- **Fuente:** Agregación de Estadística 911 (SEP) e INEGI  
- **Fecha de obtención:** 2026-04-14
- **Tamaño:** 162 líneas (161 registros + 1 encabezado)
- **Registros:** 160 observaciones (32 estados × 5 niveles educativos)
- **Licencia:** Dominio público (SEP) / Libre uso con atribución (INEGI)
- **Descripción:** Datos educativos agregados por estado y nivel en México, incluyendo inscripciones, egresados, docentes y porcentajes de abandono escolar

**Variables incluidas (19 total):**

| # | Variable | Tipo | Descripción |
|---|----------|------|-------------|
| 1 | entidad | int | Código numérico del estado (1-32) |
| 2 | n_entidad | str | Nombre del estado |
| 3 | nivel | str | Nivel educativo: inicial, preescolar, primaria, secundaria, media superior |
| 4 | insc_t | int | Total de estudiantes inscritos |
| 5 | hom_t | int | Hombres inscritos |
| 6 | muj_t | int | Mujeres inscritas |
| 7 | egre_hom | int | Egresados hombres |
| 8 | egre_muj | int | Egresadas mujeres |
| 9 | egre_tot | int | Total de egresados |
| 10 | docente_h | int | Docentes hombres |
| 11 | docente_m | int | Docentes mujeres |
| 12 | tot_doc | int | Total de docentes |
| 13 | porc_aban_hom | float | Porcentaje de abandono escolar - hombres (0-1) |
| 14 | porc_aban_muj | float | Porcentaje de abandono escolar - mujeres (0-1) |
| 15 | porc_aban_tot | float | Porcentaje de abandono escolar - total (0-1) |
| 16 | porc_doc_hom | float | Porcentaje de docentes hombres (0-1) |
| 17 | porc_doc_muj | float | Porcentaje de docentes mujeres (0-1) |
| 18 | porc_ins_hom | float | Porcentaje de inscripciones hombres (0-1) |
| 19 | porc_insc_muj | float | Porcentaje de inscripciones mujeres (0-1) |

**Notas importantes:**
- Los porcentajes están expresados como decimales (ej: 0.75 = 75%)
- Valor de 1.0 en `porc_aban_*` indica que no hay datos de abandono para ese nivel
- Los niveles inicial y preescolar no tienen datos de egresados (aparecen como 0)
- Los nombres de estados están en minúsculas

## Datos Raw

Los archivos CSV originales NO están en el repositorio por su tamaño (~800 MB).

**Los datos raw solo existen en Google Drive:**  
https://drive.google.com/drive/folders/1TD6nWykXvYCX38hpVhopqc6mqzv3epJo?usp=drive_link

**Para regenerar el dataset procesado:**
1. Abre `notebooks/001_procesamiento_colab.ipynb` en Google Colab
2. Añade acceso directo al Drive compartido en tu Google Drive
3. Ejecuta el notebook completo
4. Descarga el `Datos.csv` generado y guárdalo en `datos/processed/`

**Nota:** No es necesario regenerar los datos a menos que se actualicen las fuentes originales. El archivo `Datos.csv` ya procesado está en el repositorio.

## Uso de los Datos

Para trabajar con los datos:

1. **Análisis y visualizaciones:** Usa directamente `datos/processed/Datos.csv` (ya está en el repositorio)

2. **Exploración rápida:** Ejecuta `python scripts/analisis_exploratorio.py` para ver estadísticas

3. **Validación:** Ejecuta `python scripts/validar_datos.py` para verificar integridad

4. **Regenerar dataset:** Solo si es necesario, usa `notebooks/001_procesamiento_colab.ipynb` en Google Colab

## Notas Importantes

- Los datos raw (~800 MB) NO están ni estarán en el repositorio
- Los datos procesados (50 KB) SÍ están versionados en Git
- El archivo `Datos.csv` es el único necesario para análisis y dashboard
- La fuente original está siempre disponible en Google Drive para auditoría
