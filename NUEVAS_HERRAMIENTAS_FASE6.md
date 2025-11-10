# Documentación: Nuevas Herramientas del Agente - Fase 6

## Descripción General

La Fase 6 ha expandido significativamente las capacidades del agente inteligente mediante la implementación de **herramientas específicas de alto nivel**. Estas herramientas permiten al agente realizar consultas complejas de manera más eficiente y confiable, en lugar de construir consultas GraphQL manualmente.

## Nuevas Herramientas Implementadas

### 1. Herramientas de Especialidades

#### `get_especialidades()`

-   **Propósito**: Obtiene todas las especialidades médicas disponibles
-   **Retorna**: Lista completa de especialidades con ID y nombre
-   **Ejemplo de uso**: "Muéstrame todas las especialidades disponibles"

#### `get_especialidad_por_id(especialidad_id: str)`

-   **Propósito**: Obtiene información específica de una especialidad
-   **Parámetros**:
    -   `especialidad_id`: ID de la especialidad a consultar
-   **Retorna**: Información detallada de la especialidad especificada
-   **Ejemplo de uso**: "¿Qué información hay sobre la especialidad con ID 1?"

### 2. Herramientas de Usuarios y Médicos

#### `get_usuarios()`

-   **Propósito**: Obtiene todos los usuarios del sistema
-   **Retorna**: Lista de usuarios con ID, username, email y roles
-   **Ejemplo de uso**: "Lista todos los usuarios del sistema"

#### `get_medicos()`

-   **Propósito**: Obtiene todos los médicos registrados
-   **Retorna**: Lista de médicos con sus especialidades asociadas
-   **Ejemplo de uso**: "Muestra todos los médicos disponibles"

#### `get_usuarios_por_especialidad(especialidad_id: str)`

-   **Propósito**: Obtiene médicos filtrados por especialidad específica
-   **Parámetros**:
    -   `especialidad_id`: ID de la especialidad para filtrar
-   **Retorna**: Lista de usuarios con información de especialidad, turno, horario y disponibilidad
-   **Ejemplo de uso**: "¿Qué médicos hay disponibles en cardiología?"

### 3. Herramientas de Citas

#### `get_citas()`

-   **Propósito**: Obtiene todas las citas del sistema
-   **Retorna**: Lista completa de citas con información de paciente, médico y especialidad
-   **Ejemplo de uso**: "Muestra todas las citas programadas"

#### `get_citas_por_usuario(usuario_id: str)`

-   **Propósito**: Obtiene citas de un paciente específico
-   **Parámetros**:
    -   `usuario_id`: ID del paciente
-   **Retorna**: Lista de citas del usuario especificado
-   **Ejemplo de uso**: "¿Qué citas tiene el paciente con ID 1?"

#### `get_citas_por_medico(medico_id: str)`

-   **Propósito**: Obtiene citas de un médico específico
-   **Parámetros**:
    -   `medico_id`: ID del médico
-   **Retorna**: Lista de citas del médico especificado
-   **Ejemplo de uso**: "Muestra las citas del Dr. García"

### 4. Herramientas Médicas

#### `get_diagnosticos_por_paciente(paciente_id: str)`

-   **Propósito**: Obtiene todos los diagnósticos de un paciente
-   **Parámetros**:
    -   `paciente_id`: ID del paciente
-   **Retorna**: Lista de diagnósticos con descripción, tratamiento, fecha y médico
-   **Ejemplo de uso**: "¿Qué diagnósticos tiene el paciente Juan Pérez?"

#### `get_triajes_por_paciente(paciente_id: str)`

-   **Propósito**: Obtiene todos los triajes de un paciente
-   **Parámetros**:
    -   `paciente_id`: ID del paciente
-   **Retorna**: Lista de triajes con signos vitales, alergias y motivo de consulta
-   **Ejemplo de uso**: "Muestra los triajes del paciente ID 1"

#### `get_horarios_disponibles(especialidad_id: str, fecha: str)`

-   **Propósito**: Obtiene horarios disponibles para una especialidad y fecha específica
-   **Parámetros**:
    -   `especialidad_id`: ID de la especialidad
    -   `fecha`: Fecha en formato YYYY-MM-DD
-   **Retorna**: Lista de horarios disponibles con información de turno y día
-   **Ejemplo de uso**: "¿Qué horarios hay disponibles en cardiología para el 2025-11-10?"

## Casos de Uso Mejorados

Con estas nuevas herramientas, el agente puede manejar consultas mucho más complejas de manera eficiente:

### Ejemplo 1: Reporte de Especialidades

-   **Consulta**: "Genera un reporte en PDF de todas las especialidades médicas"
-   **Proceso**: El agente usa `get_especialidades()` → procesa los datos → genera PDF

### Ejemplo 2: Disponibilidad Médica

-   **Consulta**: "¿Qué médicos de cardiología están disponibles mañana?"
-   **Proceso**: El agente usa `get_usuarios_por_especialidad()` con ID de cardiología

### Ejemplo 3: Historial de Paciente

-   **Consulta**: "Muestra el historial completo del paciente Juan Pérez"
-   **Proceso**: El agente usa `get_diagnosticos_por_paciente()` y `get_triajes_por_paciente()`

## Beneficios de la Fase 6

1. **Mayor Confiabilidad**: Las herramientas específicas reducen errores de sintaxis
2. **Mejor Rendimiento**: Consultas optimizadas y predefinidas
3. **Facilidad de Uso**: El agente puede entender y ejecutar consultas complejas automáticamente
4. **Mantenibilidad**: Código más limpio y fácil de mantener
5. **Escalabilidad**: Fácil agregar nuevas herramientas específicas

## Estado de Implementación

✅ **Completado**: Todas las herramientas están implementadas y probadas
✅ **Integrado**: Registradas en el agente principal
✅ **Funcionando**: Pruebas exitosas confirman operatividad
✅ **Documentado**: Esta documentación proporciona guía completa

## Pruebas Realizadas

Las pruebas automatizadas confirmaron que:

-   Todas las herramientas se ejecutan sin errores
-   Las consultas GraphQL se generan correctamente
-   El agente puede usar estas herramientas automáticamente
-   Los datos se retornan en el formato esperado
-   La integración con el agente principal es exitosa

## Próximos Pasos

Con la Fase 6 completada, el agente ahora cuenta con herramientas específicas de alto nivel que le permiten:

1. Realizar consultas complejas de manera más confiable
2. Generar reportes más precisos y específicos
3. Responder a preguntas médicas con mayor contexto
4. Proporcionar información más detallada y estructurada

La Fase 6 ha sentado las bases para un agente médico mucho más capable y eficiente, listo para manejar casos de uso reales en el entorno clínico.
