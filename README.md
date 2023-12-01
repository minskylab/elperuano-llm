# Sistema de Extracción y Procesamiento de Datos

Este sistema está diseñado para extraer, procesar y analizar las normas del diario 'El Peruano', utilizando tecnologías de almacenamiento en la nube y capacidades de inteligencia artificial proporcionadas por OpenAI(*).

## Arquitectura

La arquitectura del sistema incluye los siguientes componentes:

- **El Peruano**: Fuente de datos externa.
- **VDB (Vector Database con Qdrant)**: Motor de búsqueda vectorial para manejar datos de alta dimensionalidad.
- **OpenAI**: Utilizado para procesar datos y generar resúmenes automatizados.
- **Open API**: Interfaz para interactuar con el sistema creado con el fin de ejecutar las consultas necesarias.
- **S3(Amazon Simple Storage Service)**: Servicio de almacenamiento para datos procesados y resultados de análisis.

## Procesos

- **Long-pooling**: Mantenemos una conexión persistente con el servidor, permitiendo la recepción de datos actualizados en tiempo real o hasta  hasta que el servidor tiene nueva información para enviar.
- **Scraping**: Proceso de extracción de las normas respectivas del sitio web del diario 'El Peruano'.
- **Homologación**: Normalización de datos extraídos para cumplir con estándares determinados previamente.
- **Segmentación y Modelado**: Organización de datos en segmentos y aplicación de modelos según se necesite para que los documentos luego sean leídos y analizados.
- **Summarization**: Utilización de OpenAI para crear resúmenes, responder o interpretar los datos procesados según una petición por medio de algún evento lanzado.
## API Endpoints

- `GET /posts?start_date=...`: Buscar normas/publicaciones a partir de una fecha dada.
- `GET /posts?query=...`: Buscar normas/publicaciones utilizando criterios de consulta.
- `PUT /posts?update=...`: Actualizar normas/publicaciones con nueva información(*).

(*)Puntos por consultar