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

El análisis se centra en la calidad educativa en México (ODS 4) a través de:

1. **Cobertura educativa:** Inscripciones totales por nivel educativo y distribución geográfica por estado

2. **Recursos docentes:** Número de docentes por nivel y ratio estudiantes por docente

3. **Resultados educativos:** Egresados por nivel educativo y análisis por estado

El dashboard también permite explorar dimensiones de género y desigualdades regionales presentes en los datos.

## Datos y Fuentes

**Justificación de la Selección de Datos**

Siguiendo las recomendaciones de mentores, hemos acotado nuestro análisis a una fuente principal de datos para mantener la narrativa clara y enfocada.

| Variable | Fuente | Licencia | Justificación |
|----------|--------|----------|---------------|
| **Datos educativos agregados** | Agregación de [SEP - Estadística 911](https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx) e [INEGI](https://www.inegi.org.mx/) | Dominio público / Libre uso con atribución | Dataset completo que incluye inscripciones, egresados y docentes, permitiendo analizar la calidad educativa por estado y nivel en México |

**Metadatos del Dataset**

Archivo Agrupado de Datos Educativos:
- Ubicación: `datos/raw/archivo_agrupado.csv` (original) → `datos/processed/archivo_agrupado_limpio.csv` (procesado)
- Fuente: Agregación de Estadística 911 (SEP) e INEGI
- Fecha de descarga: 2026-04-14
- Tamaño: 792 MB (original), 2-3 MB (procesado)
- Registros: 160 filas (32 estados × 5 niveles educativos)
- Descripción: Datos educativos agregados por estado y nivel educativo en México

Variables incluidas:
- `entidad`: Código del estado (1-32)
- `nivel`: Nivel educativo (inicial, preescolar, primaria, secundaria, media superior)
- `n_entidad`: Nombre del estado
- `insc_t`: Total de estudiantes inscritos
- `hom_t`: Total de hombres inscritos
- `muj_t`: Total de mujeres inscritas
- `egre_hom`: Egresados hombres
- `egre_muj`: Egresadas mujeres
- `egre_tot`: Total de egresados
- `docente_h`: Docentes hombres
- `docente_m`: Docentes mujeres
- `tot_doc`: Total de docentes

Proceso de limpieza: El archivo original requiere limpieza de la columna `n_entidad`. Ejecutar `python scripts/limpieza_datos.py` para generar la versión procesada.

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
├── datos/              # Datos crudos y procesados
├── scripts/            # Scripts de procesamiento
├── notebooks/          # Jupyter notebooks para análisis
├── dashboard/          # Código fuente del dashboard en Quarto
│   ├── _quarto.yml    # Configuración de Quarto
│   └── index.qmd      # Dashboard principal
├── docs/              # Archivos generados para GitHub Pages
├── README.md          # Este archivo
├── LICENSE            # Licencia CC-BY-SA-4.0
├── ai-log.md          # Registro de uso de IA
├── pyproject.toml     # Dependencias del proyecto
└── .python-version    # Versión de Python
```

## Licencia

[ODS.fit](https://github.com/Gus-PM/ODS.fit) © 2026 by [Gustavo Pérez, Vanessa Bustos, Elías Pérez](https://github.com/Gus-PM) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Contribuciones

Este proyecto fue desarrollado como parte del HackODS UNAM 2026.

## Contacto

Para más información sobre el proyecto, contacta al equipo ODS.fit.

Última actualización: Abril 2026
