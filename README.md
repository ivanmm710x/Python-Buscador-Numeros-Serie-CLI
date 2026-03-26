# 🔍 Buscador Automático de Patrones (File System Scanner)

Aplicación de terminal (CLI) desarrollada en Python diseñada para automatizar el análisis masivo de archivos de texto dentro de estructuras de carpetas anidadas. El script rastrea el sistema de archivos local y extrae información específica (números de serie) que coincida con un patrón predefinido, ignorando el "ruido" o texto basura.

## 🧰 Inventario de Habilidades Técnicas Aplicadas

Este proyecto simula un entorno real de extracción de datos, poniendo a prueba el rendimiento de lectura de disco (I/O) y el procesamiento de cadenas. No utiliza librerías de terceros, apoyándose 100% en la biblioteca estándar de Python:

### 1. Manipulación del Sistema de Archivos (I/O)
* **`os` y `pathlib`:** Uso de `os.walk()` para recorrer de forma recursiva árboles de directorios (carpetas y subcarpetas).
* Lectura eficiente de archivos de texto en modo lectura (`'r'`), extrayendo el contenido dinámicamente.

### 2. Procesamiento de Texto y RegEx
* **`re` (Expresiones Regulares):** Implementación del patrón de búsqueda `r'N\D{3}-\d{5}'` para validar y extraer cadenas que cumplan estrictamente la regla matemática: la letra 'N', seguida de 3 caracteres no numéricos, un guion, y exactamente 5 dígitos.
* Uso de `.group()` para desempaquetar los objetos *Match* y limpiar los datos extraídos.

### 3. Benchmarking y Control de Datos
* **`time` y `math`:** Medición precisa del tiempo de ejecución del script (desde que empieza a escanear hasta que imprime la tabla) para monitorizar el rendimiento y el coste computacional.
* **`datetime`:** Etiquetado temporal de los informes de búsqueda.

---

## ⚙️ Cómo ejecutarlo

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener una carpeta con archivos de texto para escanear y actualiza la variable `ruta` en el script principal con la ruta absoluta de tu directorio.
3. Ejecuta el archivo desde tu terminal:
   ```bash
   python buscador.py
