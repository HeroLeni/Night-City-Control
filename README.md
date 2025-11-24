# Night-City-Control
Descripción General

La aplicación Night City está diseñada para centralizar y optimizar el control de visitantes, el registro de misiones, la gestión de artefactos misteriosos y la administración de reportes de seguridad dentro de una metrópolis futurista con alto flujo de turistas humanos, androides y otras especies. Actualmente, las terminales locales utilizan sistemas heredados, lo que dificulta el monitoreo y la recopilación eficiente de datos. Este proyecto propone la implementación de un sistema avanzado para el registro y seguimiento, proporcionando mayor precisión y funcionalidad mediante algoritmos y estructuras modernas.
Estructura de Colecciones

El sistema emplea diferentes colecciones de datos:

    Turistas: Almacenamiento de usuarios visitantes.

    Misiones: Registro de actividades completadas por los usuarios.

    Artefactos: Inventario y seguimiento de objetos misteriosos encontrados.

    Seguridad: Colección de reportes y eventos relevantes.

Cada colección se gestiona de manera independiente, y su almacenamiento puede realizarse en archivos persistentes como CSV o bases de datos relacionales/locales según la configuración del sistema.
Funciones y Técnicas Avanzadas

La lógica interna hace uso extensivo de argumentos posicionales (args) y argumentos nombrados (kwargs) para maximizar la flexibilidad de las funciones a la hora de aceptar y procesar datos dinámicos. Adicionalmente, se implementan algoritmos recursivos en procedimientos como el conteo automatizado de visitantes recurrentes y el análisis jerárquico de reportes.
Persistencia de Datos

La persistencia se logra mediante el almacenamiento estructurado de los datos en archivos, preferentemente en formato CSV por compatibilidad y sencillez. Estos archivos pueden ser consumidos y actualizados de forma automática por el sistema para asegurar integridad y disponibilidad de la información registrada, permitiendo la consulta y modificación eficiente según los requerimientos operativos.
