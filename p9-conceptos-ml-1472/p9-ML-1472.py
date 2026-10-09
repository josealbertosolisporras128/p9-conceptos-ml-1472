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

print("jose solis nc 1472 NL 52")