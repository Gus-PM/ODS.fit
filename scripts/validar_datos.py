"""
Script de validación del dataset Datos.csv
Verifica integridad y consistencia de los datos procesados
"""

import pandas as pd
import sys

def validar_estructura(df):
    """Valida la estructura del dataset"""
    print("1. VALIDACIÓN DE ESTRUCTURA")
    print("-" * 60)
    
    # Verificar dimensiones esperadas
    assert df.shape == (160, 19), f"Dimensiones incorrectas: {df.shape}, esperado (160, 19)"
    print(f"   ✓ Dimensiones correctas: {df.shape}")
    
    # Verificar columnas esperadas
    columnas_esperadas = [
        'entidad', 'n_entidad', 'nivel', 'insc_t', 'hom_t', 'muj_t',
        'egre_hom', 'egre_muj', 'egre_tot', 'docente_h', 'docente_m', 'tot_doc',
        'porc_aban_hom', 'porc_aban_muj', 'porc_aban_tot',
        'porc_doc_hom', 'porc_doc_muj', 'porc_ins_hom', 'porc_insc_muj'
    ]
    assert list(df.columns) == columnas_esperadas, "Columnas no coinciden"
    print(f"   ✓ 19 columnas presentes y en orden correcto")
    
    # Verificar estados y niveles
    assert df['entidad'].nunique() == 32, "No hay 32 estados"
    print(f"   ✓ 32 estados únicos")
    
    assert df['nivel'].nunique() == 5, "No hay 5 niveles educativos"
    print(f"   ✓ 5 niveles educativos")
    
    print()

def validar_consistencia(df):
    """Valida consistencia interna de los datos"""
    print("2. VALIDACIÓN DE CONSISTENCIA")
    print("-" * 60)
    
    # Verificar que no hay valores nulos críticos
    columnas_criticas = ['entidad', 'n_entidad', 'nivel', 'insc_t', 'tot_doc']
    nulos = df[columnas_criticas].isnull().sum().sum()
    assert nulos == 0, f"Hay {nulos} valores nulos en columnas críticas"
    print(f"   ✓ Sin valores nulos en columnas críticas")
    
    # Verificar que inscripciones = hombres + mujeres
    diferencia = abs(df['insc_t'] - (df['hom_t'] + df['muj_t']))
    assert diferencia.max() < 1, "Inscripciones no suman correctamente"
    print(f"   ✓ insc_t = hom_t + muj_t")
    
    # Verificar que docentes = docentes_h + docentes_m
    diferencia_doc = abs(df['tot_doc'] - (df['docente_h'] + df['docente_m']))
    assert diferencia_doc.max() < 1, "Docentes no suman correctamente"
    print(f"   ✓ tot_doc = docente_h + docente_m")
    
    # Verificar que porcentajes de inscripción suman ~1
    suma_porc = df['porc_ins_hom'] + df['porc_insc_muj']
    assert (suma_porc - 1.0).abs().max() < 0.01, "Porcentajes de inscripción no suman 1"
    print(f"   ✓ Porcentajes de inscripción suman ~100%")
    
    # Verificar que porcentajes de docentes suman ~1
    suma_doc = df['porc_doc_hom'] + df['porc_doc_muj']
    assert (suma_doc - 1.0).abs().max() < 0.01, "Porcentajes de docentes no suman 1"
    print(f"   ✓ Porcentajes de docentes suman ~100%")
    
    print()

def validar_rangos(df):
    """Valida que los valores estén en rangos lógicos"""
    print("3. VALIDACIÓN DE RANGOS")
    print("-" * 60)
    
    # Porcentajes deben estar entre 0 y 1
    columnas_porcentaje = [col for col in df.columns if col.startswith('porc_')]
    for col in columnas_porcentaje:
        assert df[col].min() >= 0, f"{col} tiene valores negativos"
        assert df[col].max() <= 1, f"{col} tiene valores > 1"
    print(f"   ✓ Todos los porcentajes están entre 0 y 1")
    
    # Valores numéricos no negativos
    columnas_numericas = ['insc_t', 'hom_t', 'muj_t', 'egre_tot', 'tot_doc']
    for col in columnas_numericas:
        assert df[col].min() >= 0, f"{col} tiene valores negativos"
    print(f"   ✓ No hay valores negativos en columnas numéricas")
    
    # Entidades deben estar entre 1 y 32
    assert df['entidad'].min() == 1, "Entidad mínima debe ser 1"
    assert df['entidad'].max() == 32, "Entidad máxima debe ser 32"
    print(f"   ✓ Códigos de entidad en rango 1-32")
    
    print()

def mostrar_resumen(df):
    """Muestra un resumen del dataset"""
    print("4. RESUMEN DEL DATASET")
    print("-" * 60)
    
    print(f"Total nacional:")
    print(f"   - Inscripciones: {df['insc_t'].sum():,}")
    print(f"   - Docentes: {df['tot_doc'].sum():,}")
    print(f"   - Egresados: {df['egre_tot'].sum():,}")
    print(f"   - Ratio estudiantes/docente: {df['insc_t'].sum() / df['tot_doc'].sum():.1f}:1")
    
    print(f"\nDistribución de género:")
    print(f"   - Estudiantes H/M: {df['hom_t'].sum():,} / {df['muj_t'].sum():,}")
    print(f"   - Docentes H/M: {df['docente_h'].sum():,} / {df['docente_m'].sum():,}")
    
    print()

if __name__ == "__main__":
    try:
        print("="*60)
        print("VALIDACIÓN DE DATOS - ODS.fit")
        print("="*60)
        print()
        
        # Cargar datos
        df = pd.read_csv('datos/processed/Datos.csv')
        print(f"✓ Archivo cargado exitosamente\n")
        
        # Ejecutar validaciones
        validar_estructura(df)
        validar_consistencia(df)
        validar_rangos(df)
        mostrar_resumen(df)
        
        print("="*60)
        print("✓ TODAS LAS VALIDACIONES PASARON EXITOSAMENTE")
        print("="*60)
        print("\nEl dataset está listo para usar en el dashboard.")
        
    except AssertionError as e:
        print(f"\n✗ ERROR DE VALIDACIÓN: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"\n✗ ERROR: No se encontró el archivo datos/processed/Datos.csv")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR INESPERADO: {e}")
        sys.exit(1)
