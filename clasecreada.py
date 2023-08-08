# Importamos la biblioteca pandas para trabajar con DataFrames
import pandas as pd

# Definimos una clase llamada MissingValueHandler
class MissingValueHandler:
    # El método __init__ se llama cuando se crea un objeto de la clase.
    # Toma como argumento un DataFrame y lo guarda como atributo de la clase.
    def __init__(self, dataframe):
        self.dataframe = dataframe

    # Definimos un método llamado remove_missing_values
    def remove_missing_values(self, axis=0):
        # Verificamos si el valor de axis es 0 (filas) o 1 (columnas)
        if axis == 0:
            # Si axis es 0, usamos el método dropna para eliminar las filas con valores faltantes
            cleaned_df = self.dataframe.dropna()
        elif axis == 1:
            # Si axis es 1, usamos el método dropna con axis=1 para eliminar las columnas con valores faltantes
            cleaned_df = self.dataframe.dropna(axis=1)
        else:
            # Si axis no es ni 0 ni 1, lanzamos un ValueError
            raise ValueError("Invalid axis value. Use 0 for rows or 1 for columns.")
        
        # Devolvemos el DataFrame sin valores faltantes
        return cleaned_df