import pandas as pd
print(pd.__version__) # Output: 1.5.2

# jose solis nc 1472 NL 52
# codigo para leer
import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos = {
    'distancia_km': [5.1, 2.9, 4.0, 1.4, 6.3],
    'trafico_nivel': [3, 2, 1, 3, 2],
    'edad_repartidor': [40, 27, 33, 22, 45],
    'tiempo_entrega_min': [48, 24, 28, 14, 58]
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

# codigo de practicas de pandas 31-60

# 31. Dataset original de referencia

# 52.
datos22 = {
    'distancia_km': [5.1, 2.9, 4.0, 1.4, 6.3],
    'trafico_nivel': [3, 2, 1, 3, 2],
    'edad_repartidor': [40, 27, 33, 22, 45],
    'tiempo_entrega_min': [48, 24, 28, 14, 58]
}

print("-------HOSIPTAL--------")
# CASO 3 HOSIPTAL
import pandas as pd

# 1. Dataset de ejemplo del hospital
datos_hospital = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 23, 60, 35, 50],
    'nivel_glucosa': [140, 85, 200, 110, 160],
    'presion_arterial': [80, 70, 90, 75, 85],
    'indice_masa_corporal': [28.5, 22.0, 33.1, 24.5, 30.2],
    'diagnostico_diabetes': [1, 0, 1, 0, 1] # 1: Sí, 0: No
}

df_hospital = pd.DataFrame(datos_hospital)

# 2. Eliminación de columna irrelevante (id_paciente)
# Usamos .drop() para excluir id_paciente y el diagnostico (que es la salida)
X = df_hospital.drop(columns=['id_paciente', 'diagnostico_diabetes'])

# 3. Definición del Target
y = df_hospital['diagnostico_diabetes']

# Mostrar resultados
print("--- FEATURES (X) ---")
print(X.head())

print("\n--- TARGET (y) ---")
print(y.head())
print("jose solis nc 1472 NL 52")