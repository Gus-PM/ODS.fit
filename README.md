# ODS.fit

Dashboard interactivo en Quarto para el seguimiento de los Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030 de la ONU, enfocado en la educación en México.

## Equipo

**Nombre del equipo:** ODS.fit

**Integrantes:**
- Vanessa Leonor Bustos Manríquez
- Gustavo Alberto Pérez Mendoza
- Elías Pérez Saldaña

## ODS Elegido

**ODS 4 - Educación de calidad**

El análisis también puede explorar conexiones con otros ODS como igualdad de género (ODS 5) y reducción de desigualdades (ODS 10).

## Descripción del Proyecto

**Pregunta Central:** ¿Cuál es el estado de la calidad educativa en México?

**Motivación:** Contribuir al alcance de los objetivos 2030 en la calidad de la educación, analizando el contexto actual en México a través de indicadores clave como inscripciones, docentes y egresados por estado y nivel educativo.

**Objetivo:** Visualizar y analizar las condiciones educativas en México para identificar áreas de oportunidad y desafíos en el cumplimiento del ODS 4 (Educación de calidad).

## Narrativa del Dashboard

El análisis se centra en la calidad educativa en México (ODS 4) utilizando datos de 177.8 millones de inscripciones en 32 estados:

1. **Cobertura educativa:** 
   - 5 niveles: inicial, preescolar, primaria, secundaria y media superior
   - Distribución geográfica por los 32 estados de México
   - Análisis de paridad de género en inscripciones (50.1% hombres, 49.9% mujeres)

2. **Recursos docentes:** 
   - 8.6 millones de docentes en el sistema educativo nacional
   - Ratio estudiantes/docente por nivel (varía de 13 a 25)
   - Distribución de género en docentes (66.5% mujeres, 33.5% hombres)

3. **Abandono escolar:**
   - Tasas de abandono en secundaria (69%) y media superior (73%)
   - Análisis de brechas de género (hombres 71.9%, mujeres 70.2%)
   - Identificación de desafíos críticos para el cumplimiento del ODS 4

4. **Desigualdades regionales:**
   - Comparativa entre estados
   - Concentración de matrícula en grandes estados
   - Brechas en acceso y calidad educativa

Ver análisis detallado en `datos/RESUMEN_EJECUTIVO.md`

## Datos y Fuentes

**Justificación de la Selección de Datos**

Siguiendo las recomendaciones de mentores, hemos acotado nuestro análisis a una fuente principal de datos para mantener la narrativa clara y enfocada.

| Variable | Fuente | Licencia | Justificación |
|----------|--------|----------|---------------|
| **Datos educativos Formato 911** | [SEP - Formato 911](https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx) | Dominio público | Sistema oficial de estadísticas del Sistema Educativo Nacional, permite analizar inscripciones, egresados, docentes y abandono escolar por estado y nivel educativo |

**Metadatos del Dataset**

Datos educativos de México (Formato 911 - SEP):
- Ubicación: `datos/processed/Datos.csv`
- Fuente: Formato 911 - Secretaría de Educación Pública (SEP)
- Fecha de obtención: 2026-04-14
- Registros: 160 observaciones (32 estados × 5 niveles educativos)
- Variables: 19 columnas con datos del Sistema Educativo Nacional
- Descripción: Estadísticas oficiales por estado y nivel: inscripciones, egresados, docentes y tasas de permanencia escolar

Variables principales:
- Identificación: entidad (código 1-32), n_entidad (nombre), nivel (inicial, preescolar, primaria, secundaria, media superior)
- Inscripciones: insc_t (total), hom_t (hombres), muj_t (mujeres)
- Egresados: egre_tot (total), egre_hom (hombres), egre_muj (mujeres)
- Docentes: tot_doc (total), docente_h (hombres), docente_m (mujeres)
- Tasas de abandono: porc_aban_tot, porc_aban_hom, porc_aban_muj (0-1)
- Porcentajes calculados: porc_ins_hom, porc_insc_muj, porc_doc_hom, porc_doc_muj

**Datos raw:** Los archivos CSV originales del Formato 911 (~800 MB) solo existen en [Google Drive](https://drive.google.com/drive/folders/1TD6nWykXvYCX38hpVhopqc6mqzv3epJo?usp=drive_link). No están en el repositorio por su tamaño.

Ver documentación completa en `datos/README.md` y análisis en `datos/RESUMEN_EJECUTIVO.md`

## Tecnologías Utilizadas

- Python 3.13+
- uv (gestor de paquetes y entornos virtuales)
- Quarto (generación del dashboard interactivo)
- Pandas (análisis y manipulación de datos)
- Plotly (visualizaciones interactivas)
- Matplotlib/Seaborn (visualizaciones estáticas)
- Jupyter (notebooks para análisis exploratorio)

## Instalación y Uso

**Requisitos previos:**
- Python 3.10 o superior
- uv
- Quarto CLI

**Instalación:**

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/ODS.fit.git
cd ODS.fit
```

2. Crear el entorno virtual e instalar dependencias con uv:
```bash
uv sync
```

3. Activar el entorno:
```bash
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate  # En Windows
```

**Generar el dashboard:**

```bash
cd dashboard
quarto render
```

El dashboard estará disponible en `docs/index.html`

## Estructura del Proyecto

```
ODS.fit/
├── datos/                          # Datos procesados
│   ├── processed/
│   │   └── Datos.csv              # Dataset final (50 KB)
│   ├── RESUMEN_EJECUTIVO.md       # Análisis del dataset
│   └── README.md                   # Documentación de datos
├── scripts/                        # Scripts de análisis
│   ├── analisis_exploratorio.py   # EDA del dataset
│   ├── validar_datos.py           # Validación de integridad
│   └── README.md
├── notebooks/                      # Jupyter notebooks
│   ├── 001_procesamiento_colab.ipynb  # Procesa datos desde Drive
│   ├── 002_procesamiento_local.ipynb  # Versión local (opcional)
│   └── README.md
├── dashboard/                      # Dashboard en Quarto
│   ├── _quarto.yml                # Configuración de Quarto
│   └── index.qmd                  # Dashboard principal
├── docs/                          # Archivos generados para GitHub Pages
├── README.md                      # Este archivo
├── LICENSE                        # Licencia CC-BY-SA-4.0
├── ai-log.md                      # Registro de uso de IA
├── pyproject.toml                 # Dependencias del proyecto
└── .python-version                # Versión de Python

Nota: Los datos raw (~800 MB) no están en el repo, solo en Google Drive.
```

## Licencia

[ODS.fit](https://github.com/Gus-PM/ODS.fit) © 2026 by [Gustavo Pérez, Vanessa Bustos, Elías Pérez](https://github.com/Gus-PM) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Contribuciones

Este proyecto fue desarrollado como parte del HackODS UNAM 2026.

## Contacto

Para más información sobre el proyecto, contacta al equipo ODS.fit.

Última actualización: Abril 2026
