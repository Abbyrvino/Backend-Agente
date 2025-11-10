# Backend del Agente Inteligente para Reportes Médicos

Este proyecto contiene el backend para un agente inteligente capaz de generar reportes médicos a partir de una base de datos consultada a través de GraphQL.

## Configuración

Antes de ejecutar el proyecto, necesitas configurar las variables de entorno.

1.  **Crear el archivo `.env`:**
    Copia el archivo `example.env` y renómbralo a `.env`.

2.  **Configurar las variables:**
    Abre el archivo `.env` y añade tus claves y endpoints correspondientes:
    -   `GRAPHQL_ENDPOINT`: La URL de tu API de GraphQL.
    -   `GOOGLE_API_KEY`: Tu clave de API para Google Generative AI.

## Ejecución

Para poner en marcha el servidor, sigue estos pasos desde la terminal en la raíz del proyecto:

1.  **Activar el entorno virtual:**

    ```bash
    .venv\Scripts\activate
    ```

2.  **Iniciar el servidor con Uvicorn:**

    ```bash
    uvicorn app:app --reload
    ```

    -   `app`: Se refiere al archivo `app.py`.
    -   `app`: Se refiere al objeto `app = FastAPI()` dentro de ese archivo.
    -   `--reload`: Hace que el servidor se reinicie automáticamente cada vez que detecta un cambio en el código.

    El servidor estará disponible en `http://127.0.0.1:8000`.

## API para el Frontend

El frontend debe comunicarse con los siguientes endpoints:

### 1. Endpoint Principal (para interactuar con el agente)

-   **URL:** `http://127.0.0.1:8000/ask_agent/`
-   **Método HTTP:** `POST`
-   **Cuerpo de la solicitud (Body):** Debe ser un JSON con la siguiente estructura:
    ```json
    {
        "prompt": "Aquí va la pregunta del usuario en lenguaje natural"
    }
    ```
    **Ejemplo:**
    ```json
    {
        "prompt": "Quiero un listado de todas las especialidades médicas"
    }
    ```

### 2. Endpoint Raíz (para verificar que el servidor está funcionando)

-   **URL:** `http://127.0.0.1:8000/`
-   **Método HTTP:** `GET`
-   **Respuesta:** Devuelve un mensaje de bienvenida.
