# Diseño y Desarrollo de API REST en un Sistema Bancario

En un sistema bancario, se requiere desarrollar una API REST que gestione las transacciones de los clientes. La API debe permitir la creación, lectura, actualización y eliminación de transacciones. Además, debe garantizar la idempotencia de las operaciones y manejar adecuadamente los errores y excepciones. Los actores involucrados son el cliente, el sistema de gestión de transacciones y el sistema de auditoría. La API debe operar con una latencia máxima de 200ms y una tasa de procesamiento de 1000 transacciones por segundo.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | api-rest-fastapi |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del Modelo de Transacciones

**Objetivo:** Definir el modelo de datos para las transacciones y establecer las relaciones con otros componentes del sistema.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los atributos necesarios para una transacción (ID, monto, fecha, descripción, estado).
- Definir las relaciones entre las transacciones y otros componentes del sistema (cliente, cuenta).
- Establecer las restricciones y validaciones necesarias para las transacciones (monto positivo, fecha válida).

**Entregable:** Modelo de datos para transacciones con relaciones y restricciones definidas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los tipos de datos adecuados para cada atributo.
- Piensa en las validaciones necesarias para garantizar la integridad de los datos.

</details>

### Fase 2: Implementación de la API REST

**Objetivo:** Implementar la API REST para gestionar las transacciones, garantizando la idempotencia y manejando los errores y excepciones.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Crear las rutas necesarias para crear, leer, actualizar y eliminar transacciones.
- Implementar la idempotencia en las operaciones de la API.
- Manejar adecuadamente los errores y excepciones, proporcionando respuestas adecuadas al cliente.

**Entregable:** API REST funcional con rutas para CRUD de transacciones, idempotencia implementada y manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza claves de idempotencia para garantizar la unicidad de las operaciones.
- Considera los diferentes tipos de errores y excepciones que pueden ocurrir y cómo manejarlos.

</details>

### Fase 3: Optimización y Pruebas de la API

**Objetivo:** Optimizar el rendimiento de la API y realizar pruebas exhaustivas para garantizar su funcionamiento correcto.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar y optimizar las consultas y operaciones más costosas en términos de rendimiento.
- Realizar pruebas unitarias y de integración para verificar el funcionamiento correcto de la API.
- Generar carga de prueba para evaluar el rendimiento y la escalabilidad de la API.

**Entregable:** API REST optimizada y pruebas exhaustivas realizadas.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza herramientas de profiling para identificar las operaciones más costosas.
- Considera diferentes escenarios de prueba para verificar el comportamiento de la API en situaciones límite.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuáles son sus principales características?
- **paraQueSirve**: ¿Para qué sirve la API REST en el contexto del sistema bancario?
- **comoSeUsa**: ¿Cómo se utiliza la API REST para gestionar las transacciones en el sistema bancario?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al utilizar la API REST y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño y desarrollo de la API REST en términos de rendimiento, escalabilidad y manejo de errores?

## Criterios de Evaluacion

- Definición correcta del modelo de datos para transacciones.
- Implementación de la API REST con rutas para CRUD de transacciones.
- Garantía de idempotencia en las operaciones de la API.
- Manejo adecuado de errores y excepciones en la API.
- Optimización del rendimiento de la API y realización de pruebas exhaustivas.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
