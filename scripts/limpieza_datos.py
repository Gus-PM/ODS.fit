"""
Script para limpiar el archivo_agrupado.csv
Corrige el problema de repetición en la columna n_entidad
"""

import csv
import sys

def limpiar_csv(archivo_entrada, archivo_salida):
    """
    Limpia el archivo CSV corrigiendo la columna n_entidad
    
    Args:
        archivo_entrada: Path del archivo CSV a limpiar
        archivo_salida: Path donde guardar el archivo limpio
    """
    # Aumentar límite de campo CSV
    csv.field_size_limit(10000000)
    
    # Mapeo de códigos de entidad a nombres
    ENTIDADES = {
        1: 'Aguascalientes',
        2: 'Baja California',
        3: 'Baja California Sur',
        4: 'Campeche',
        5: 'Coahuila',
        6: 'Colima',
        7: 'Chiapas',
        8: 'Chihuahua',
        9: 'Ciudad de México',
        10: 'Durango',
        11: 'Guanajuato',
        12: 'Guerrero',
        13: 'Hidalgo',
        14: 'Jalisco',
        15: 'México',
        16: 'Michoacán',
        17: 'Morelos',
        18: 'Nayarit',
        19: 'Nuevo León',
        20: 'Oaxaca',
        21: 'Puebla',
        22: 'Querétaro',
        23: 'Quintana Roo',
        24: 'San Luis Potosí',
        25: 'Sinaloa',
        26: 'Sonora',
        27: 'Tabasco',
        28: 'Tamaulipas',
        29: 'Tlaxcala',
        30: 'Veracruz',
        31: 'Yucatán',
        32: 'Zacatecas'
    }
    
    filas_procesadas = 0
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f_in, \
             open(archivo_salida, 'w', encoding='utf-8', newline='') as f_out:
            
            reader = csv.reader(f_in)
            writer = csv.writer(f_out)
            
            # Escribir encabezado
            header = next(reader)
            writer.writerow(header)
            print(f"Columnas: {header}")
            
            # Procesar cada fila
            for i, row in enumerate(reader, 1):
                if len(row) >= 12:
                    # Corregir el nombre de la entidad
                    codigo_entidad = int(row[0])
                    row[2] = ENTIDADES.get(codigo_entidad, f'Desconocida_{codigo_entidad}')
                    
                    writer.writerow(row)
                    filas_procesadas += 1
                    
                    if i % 20 == 0:
                        print(f"Procesadas {i} filas...", end='\r')
                else:
                    print(f"\nAdvertencia: Fila {i} tiene {len(row)} columnas, esperadas 12")
            
            print(f"\n✓ Proceso completado: {filas_procesadas} filas procesadas")
            print(f"✓ Archivo limpio guardado en: {archivo_salida}")
            
    except Exception as e:
        print(f"✗ Error al procesar archivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    archivo_entrada = "archivo_agrupado.csv"
    archivo_salida = "datos/processed/archivo_agrupado_limpio.csv"
    
    print("=== Limpieza de datos educativos ===")
    print(f"Entrada: {archivo_entrada}")
    print(f"Salida: {archivo_salida}\n")
    
    limpiar_csv(archivo_entrada, archivo_salida)
