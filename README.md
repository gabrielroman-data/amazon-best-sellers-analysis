🎯 Descripción del Proyecto

**Exploración del Top 50 de Libros Bestsellers de Amazon (2009-2019).**

Este proyecto utiliza la librería **Pandas** de Python para realizar un Análisis Exploratorio de Datos (EDA) sobre un dataset que contiene 550 registros de los libros más vendidos de Amazon entre 2009 y 2019.

El análisis se centra en investigar y responder las siguientes preguntas:

* **Rendimiento de Autores:** ¿Quiénes son los autores con más apariciones en la lista de *bestsellers*?
* **Tendencias de Precios:** ¿Cómo se distribuyen los precios de los libros más vendidos?
* **Comparativa de Género:** ¿Qué género (Ficción o No Ficción) tiene un rating promedio más alto?

---

## Archivos Principales
* `main.py`: script principal de Python que realiza la limpieza, el análisis y genera los archivos de resultados.
* `bestsellers.csv`: dataset original utilizado para el análisis.

## Resultados del Análisis
Los siguientes archivos son generados por `main.py` después de la limpieza y análisis de datos:
* `data_clean.csv`: Versión limpia del dataset, lista para el análisis.
* `avg_rating_by_genre.csv`: Tabla con el promedio de puntaje (ratings) por género.
* `top_authors`: Tabla con el top 5 de autores con más apariciones en la lista de *bestsellers*.

## Cómo Ejecutar
1.  **Clonar el repositorio:**
    ```bash
    git clone [la_url_de_tu_repositorio]
    ```
2.  **Instalar dependencias:**
    Asegúrate de tener Python y **Pandas** instalados. Puedes instalar Pandas con pip:
    ```bash
    pip install pandas
    ```
3.  **Ejecutar el script principal:**
    ```bash
    python main.py
    ```