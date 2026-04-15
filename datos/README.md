# Datos del Proyecto ODS.fit

Esta carpeta contiene los datos utilizados para el análisis.

## Estructura

```
datos/
├── raw/                              # Datos sin procesar (originales)
│   └── archivo_agrupado.csv         # 792 MB - Dataset original
├── processed/                        # Datos procesados y limpios
│   └── archivo_agrupado_limpio.csv  # ~2-3 MB - Dataset limpio (se genera)
└── README.md                         # Este archivo
```

## Dataset Principal

### archivo_agrupado.csv
- **Ubicación:** `raw/archivo_agrupado.csv`
- **Fuente:** Agregación de Estadística 911 (SEP) e INEGI
- **Fecha de descarga:** 2026-04-14
- **Tamaño:** 792 MB (original) → ~2-3 MB (procesado)
- **Registros:** 160 filas (32 estados × 5 niveles educativos)
- **Licencia:** Dominio público (SEP) / Libre uso con atribución (INEGI)
- **Descripción:** Datos educativos agregados por estado y nivel educativo en México

**Variables incluidas:**
| Variable | Tipo | Descripción |
|----------|------|-------------|
| entidad | int | Código del estado (1-32) |
| nivel | str | Nivel educativo (inicial, preescolar, primaria, secundaria, media superior) |
| n_entidad | str | Nombre del estado |
| insc_t | int | Total de estudiantes inscritos |
| hom_t | int | Total de hombres inscritos |
| muj_t | int | Total de mujeres inscritas |
| egre_hom | int | Egresados hombres |
| egre_muj | int | Egresadas mujeres |
| egre_tot | int | Total de egresados |
| docente_h | int | Docentes hombres |
| docente_m | int | Docentes mujeres |
| tot_doc | int | Total de docentes |

**Problema conocido:** La columna `n_entidad` en el archivo original tiene valores repetidos millones de veces, aumentando el tamaño del archivo innecesariamente.

**Solución:** Ejecutar el script de limpieza:
```bash
python scripts/limpieza_datos.py
```

Este script:
1. Lee el archivo original de `raw/`
2. Corrige la columna `n_entidad` con los nombres correctos de los estados
3. Guarda el archivo limpio en `processed/archivo_agrupado_limpio.csv`

## Instrucciones

1. Los archivos grandes en `raw/` NO se suben al repositorio (protegidos por `.gitignore`)
2. Los archivos procesados en `processed/` SÍ se suben (son pequeños)
3. Para trabajar con los datos, usar siempre la versión de `processed/`
4. Documentar cualquier transformación adicional en el script correspondiente
