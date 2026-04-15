"""
Análisis exploratorio del dataset de educación en México
"""

import pandas as pd
import numpy as np

def cargar_datos():
    """Carga el dataset desde la carpeta processed"""
    return pd.read_csv('datos/processed/Datos.csv')

def resumen_general(df):
    """Genera un resumen general del dataset"""
    print("="*60)
    print("ANÁLISIS EXPLORATORIO - DATOS EDUCATIVOS MÉXICO")
    print("="*60)
    
    print(f"\n📊 Dimensiones del dataset:")
    print(f"   - Filas: {len(df)}")
    print(f"   - Columnas: {len(df.columns)}")
    print(f"   - Estados: {df['entidad'].nunique()}")
    print(f"   - Niveles educativos: {df['nivel'].nunique()}")
    
    print(f"\n📚 Niveles educativos:")
    for nivel in sorted(df['nivel'].unique()):
        count = len(df[df['nivel'] == nivel])
        print(f"   - {nivel.capitalize()}: {count} estados")
    
    print(f"\n👥 Totales nacionales:")
    print(f"   - Inscripciones totales: {df['insc_t'].sum():,}")
    print(f"   - Total docentes: {df['tot_doc'].sum():,}")
    print(f"   - Egresados totales: {df['egre_tot'].sum():,}")
    
    print(f"\n⚖️ Distribución de género en inscripciones:")
    total_hombres = df['hom_t'].sum()
    total_mujeres = df['muj_t'].sum()
    total = total_hombres + total_mujeres
    print(f"   - Hombres: {total_hombres:,} ({total_hombres/total*100:.1f}%)")
    print(f"   - Mujeres: {total_mujeres:,} ({total_mujeres/total*100:.1f}%)")
    
    print(f"\n👨‍🏫 Distribución de género en docentes:")
    total_doc_h = df['docente_h'].sum()
    total_doc_m = df['docente_m'].sum()
    total_doc = total_doc_h + total_doc_m
    print(f"   - Hombres: {total_doc_h:,} ({total_doc_h/total_doc*100:.1f}%)")
    print(f"   - Mujeres: {total_doc_m:,} ({total_doc_m/total_doc*100:.1f}%)")

def analisis_por_nivel(df):
    """Análisis agrupado por nivel educativo"""
    print(f"\n{'='*60}")
    print("ANÁLISIS POR NIVEL EDUCATIVO")
    print("="*60)
    
    por_nivel = df.groupby('nivel').agg({
        'insc_t': 'sum',
        'tot_doc': 'sum',
        'egre_tot': 'sum'
    }).sort_values('insc_t', ascending=False)
    
    print(f"\n{'Nivel':<20} {'Inscripciones':>15} {'Docentes':>12} {'Egresados':>12}")
    print("-"*60)
    for nivel, row in por_nivel.iterrows():
        ratio = row['insc_t'] / row['tot_doc'] if row['tot_doc'] > 0 else 0
        print(f"{nivel.capitalize():<20} {int(row['insc_t']):>15,} {int(row['tot_doc']):>12,} {int(row['egre_tot']):>12,}")

def top_estados(df):
    """Top 5 estados por inscripciones"""
    print(f"\n{'='*60}")
    print("TOP 5 ESTADOS CON MÁS INSCRIPCIONES")
    print("="*60 + "\n")
    
    por_estado = df.groupby('n_entidad')['insc_t'].sum().sort_values(ascending=False).head(5)
    
    for i, (estado, insc) in enumerate(por_estado.items(), 1):
        print(f"{i}. {estado.title()}: {insc:,} estudiantes")

def analisis_abandono(df):
    """Análisis de tasas de abandono escolar"""
    print(f"\n{'='*60}")
    print("ANÁLISIS DE ABANDONO ESCOLAR")
    print("="*60)
    
    # Filtrar solo registros con datos válidos de abandono (< 1.0)
    df_abandono = df[df['porc_aban_tot'] < 1.0].copy()
    
    if len(df_abandono) > 0:
        print(f"\nPromedio de abandono escolar por nivel (solo secundaria y media superior):")
        aban_nivel = df_abandono.groupby('nivel')['porc_aban_tot'].mean() * 100
        for nivel, tasa in aban_nivel.sort_values(ascending=False).items():
            print(f"   - {nivel.capitalize()}: {tasa:.1f}%")
        
        print(f"\nBrechas de género en abandono:")
        print(f"   - Promedio hombres: {df_abandono['porc_aban_hom'].mean()*100:.1f}%")
        print(f"   - Promedio mujeres: {df_abandono['porc_aban_muj'].mean()*100:.1f}%")
    else:
        print("\nNo hay datos de abandono disponibles para análisis.")

if __name__ == "__main__":
    df = cargar_datos()
    resumen_general(df)
    analisis_por_nivel(df)
    top_estados(df)
    analisis_abandono(df)
    
    print(f"\n{'='*60}")
    print("Análisis completado ✓")
    print("="*60 + "\n")
