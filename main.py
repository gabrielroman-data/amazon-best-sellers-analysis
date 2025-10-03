import pandas as pd # Importo la librería pandas para el manejo y análisis de datos.

# Cargo mi dataset original de bestsellers.
df = pd.read_csv('bestsellers.csv')
print("\n-----------------------------------------------------------------------------------------------------------------------------")

# Muestro las primeras 5 filas del dataset para una inspección inicial.
print("First 5 rows of the dataset:")
print(df.head())
print("\n-----------------------------------------------------------------------------------------------------------------------------")

# Obtengo la forma del dataset (número de filas y columnas).
print("Shape of the dataset (rows, columns):")
print(df.shape)
print("\n-----------------------------------------------------------------------------------------------------------------------------")

# Muestro los nombres de todas las columnas.
print("Column names:")
print(df.columns)
print("\n-----------------------------------------------------------------------------------------------------------------------------")

# Obtengo estadísticas de resumen para las columnas numéricas.
print("Summary statistics of the dataset:")
print(df.describe())

# Elimino filas duplicadas exactas. Modifico el DataFrame directamente (inplace=True).
df.drop_duplicates(inplace=True)

# Renombro columnas para hacerlas más claras y fáciles de usar.
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

print("\n-----------------------------------------------------------------------------------------------------------------------------")
# Vuelvo a mostrar el 'head' para ver los nombres de columnas actualizados.
print("First 5 rows of the dataset new head:")
print(df.head())

# Convierto la columna 'Price' a tipo flotante (decimal) para asegurar operaciones numéricas correctas.
df["Price"] = df["Price"].astype(float)
print("\n-----------------------------------------------------------------------------------------------------------------------------")

# Reviso los tipos de datos de las columnas después de la conversión.
df.info()
print("\n----------------------------------------------------------------")

# Obtengo una visión de qué autores tienen la mayor cantidad de libros en la lista de Bestsellers.
print("Top Authors by Number of Bestsellers:")
# Cuento la frecuencia de cada autor.
author_counts = df['Author'].value_counts()
print(author_counts)
print("\n----------------------------------------------------------------")

# Calculo el rating promedio para cada género en el dataset.
# Agrupo los datos por "Genre" y calculo el promedio de la columna "Rating".
print("Average Rating by Genre:")
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Exporto el conteo del top 5 de autores más vendidos a un archivo CSV.
author_counts.head(5).to_csv("top_authors.csv")

# Exporto el rating promedio por género a un archivo CSV.
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

# Finalmente, exporto el dataset limpio y transformado a un nuevo archivo CSV.
df.to_csv("bestsellers_cleaned.csv", index=False);