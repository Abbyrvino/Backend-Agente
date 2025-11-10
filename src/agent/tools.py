from src.graphql_client.client import GraphQLClient
from src.reporting.generator import generar_pdf, generar_excel


def execute_graphql_query(query: str, variables: dict = None) -> dict:
    """
    A tool that allows the agent to execute a GraphQL query.

    Args:
        query (str): The GraphQL query string to execute.
                     Example for fetching specialities:
                     ```graphql
                     query GetEspecialidades {
                       especialidades {
                         id
                         nombre
                       }
                     }
                     ```
        variables (dict, optional): A dictionary of variables for the query.

    Returns:
        dict: The JSON response from the GraphQL API.
    """
    try:
        # For now, we are not handling authentication tokens.
        # We will add this capability later if needed.
        client = GraphQLClient()

        print(f"Executing GraphQL query:\n{query}")
        if variables:
            print(f"With variables: {variables}")

        result = client.execute(query, variables)

        print(f"GraphQL response: {result}")
        return result

    except Exception as e:
        print(f"Error executing GraphQL query: {e}")
        return {"error": str(e)}


def generar_pdf_tool(datos: list[dict], nombre_archivo: str = None) -> str:
    """
    A tool that allows the agent to generate a PDF report from a list of dictionaries.

    Args:
        datos (list[dict]): A list of dictionaries with the data to include in the report.
        nombre_archivo (str, optional): The name of the PDF file. If not provided, a default name will be generated.

    Returns:
        str: The path to the generated PDF file.
    """
    try:
        if nombre_archivo is None:
            # Generate a default file name with timestamp
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nombre_archivo = f"reports/reporte_{timestamp}.pdf"

        # Create reports directory if it doesn't exist
        import os

        os.makedirs("reports", exist_ok=True)

        generar_pdf(datos, nombre_archivo)
        print(f"PDF report generated: {nombre_archivo}")
        return nombre_archivo

    except Exception as e:
        print(f"Error generating PDF report: {e}")
        return {"error": str(e)}


def generar_excel_tool(datos: list[dict], nombre_archivo: str = None) -> str:
    """
    A tool that allows the agent to generate an Excel report from a list of dictionaries.

    Args:
        datos (list[dict]): A list of dictionaries with the data to include in the report.
        nombre_archivo (str, optional): The name of the Excel file. If not provided, a default name will be generated.

    Returns:
        str: The path to the generated Excel file.
    """
    try:
        if nombre_archivo is None:
            # Generate a default file name with timestamp
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nombre_archivo = f"reports/reporte_{timestamp}.xlsx"

        # Create reports directory if it doesn't exist
        import os

        os.makedirs("reports", exist_ok=True)

        generar_excel(datos, nombre_archivo)
        print(f"Excel report generated: {nombre_archivo}")
        return nombre_archivo

    except Exception as e:
        print(f"Error generating Excel report: {e}")
        return {"error": str(e)}


def get_especialidades() -> dict:
    """
    A tool that retrieves all available medical specialties from the database.

    Returns:
        dict: A list of specialties with their ID and name.
    """
    try:
        query = """
            query GetEspecialidades {
                especialidades {
                    id
                    nombre
                }
            }
        """
        return execute_graphql_query(query)
    except Exception as e:
        print(f"Error getting specialties: {e}")
        return {"error": str(e)}


def get_especialidad_por_id(especialidad_id: str) -> dict:
    """
    A tool that retrieves a specific medical specialty by its ID.

    Args:
        especialidad_id (str): The ID of the specialty to retrieve.

    Returns:
        dict: The specialty information with ID and name.
    """
    try:
        query = """
            query GetEspecialidad($id: ID!) {
                especialidad(id: $id) {
                    id
                    nombre
                }
            }
        """
        variables = {"id": especialidad_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting specialty by ID: {e}")
        return {"error": str(e)}


def get_usuarios() -> dict:
    """
    A tool that retrieves all users in the system with their basic information.

    Returns:
        dict: A list of users with ID, username, email, and roles.
    """
    try:
        query = """
            query GetUsuarios {
                usuarios {
                    id
                    username
                    email
                    roles {
                        id
                        nombre
                    }
                }
            }
        """
        return execute_graphql_query(query)
    except Exception as e:
        print(f"Error getting users: {e}")
        return {"error": str(e)}


def get_medicos() -> dict:
    """
    A tool that retrieves all doctors/medicos in the system.

    Returns:
        dict: A list of doctors with their information and specialties.
    """
    try:
        query = """
            query GetMedicos {
                medicos {
                    id
                    username
                    email
                    especialidades {
                        id
                        nombre
                    }
                }
            }
        """
        return execute_graphql_query(query)
    except Exception as e:
        print(f"Error getting doctors: {e}")
        return {"error": str(e)}


def get_usuarios_por_especialidad(especialidad_id: str) -> dict:
    """
    A tool that retrieves users (doctors) associated with a specific specialty.

    Args:
        especialidad_id (str): The ID of the specialty to filter by.

    Returns:
        dict: A list of users with their specialty information.
    """
    try:
        query = """
            query GetUsuariosPorEspecialidad($especialidadId: ID!) {
                usuariosPorEspecialidad(especialidadId: $especialidadId) {
                    usuarioId
                    usuario
                    especialidad
                    turno
                    horario
                    dia
                    fecha
                    horarioId
                    disponibilidad
                }
            }
        """
        variables = {"especialidadId": especialidad_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting users by specialty: {e}")
        return {"error": str(e)}


def get_citas() -> dict:
    """
    A tool that retrieves all appointments in the system.

    Returns:
        dict: A list of appointments with patient, doctor, and schedule information.
    """
    try:
        query = """
            query GetCitas {
                citas {
                    id
                    usuario {
                        username
                    }
                    medico {
                        username
                    }
                    especialidad {
                        nombre
                    }
                    horario
                    fecha
                    nombreUsuarioLogeado
                }
            }
        """
        return execute_graphql_query(query)
    except Exception as e:
        print(f"Error getting appointments: {e}")
        return {"error": str(e)}


def get_citas_por_usuario(usuario_id: str) -> dict:
    """
    A tool that retrieves all appointments for a specific user/patient.

    Args:
        usuario_id (str): The ID of the user/patient.

    Returns:
        dict: A list of appointments for the specified user.
    """
    try:
        query = """
            query GetCitasPorUsuario($usuarioId: ID!) {
                citasPorUsuario(usuarioId: $usuarioId) {
                    id
                    usuario {
                        username
                    }
                    medico {
                        username
                    }
                    especialidad {
                        nombre
                    }
                    horario
                    fecha
                    nombreUsuarioLogeado
                }
            }
        """
        variables = {"usuarioId": usuario_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting appointments by user: {e}")
        return {"error": str(e)}


def get_citas_por_medico(medico_id: str) -> dict:
    """
    A tool that retrieves all appointments for a specific doctor.

    Args:
        medico_id (str): The ID of the doctor.

    Returns:
        dict: A list of appointments for the specified doctor.
    """
    try:
        query = """
            query GetCitasPorMedico($medicoId: ID!) {
                citasPorMedico(medicoId: $medicoId) {
                    id
                    usuario {
                        username
                    }
                    medico {
                        username
                    }
                    especialidad {
                        nombre
                    }
                    horario
                    fecha
                    nombreUsuarioLogeado
                }
            }
        """
        variables = {"medicoId": medico_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting appointments by doctor: {e}")
        return {"error": str(e)}


def get_diagnosticos_por_paciente(paciente_id: str) -> dict:
    """
    A tool that retrieves all diagnoses for a specific patient.

    Args:
        paciente_id (str): The ID of the patient.

    Returns:
        dict: A list of diagnoses for the specified patient.
    """
    try:
        query = """
            query GetDiagnosticosPorPaciente($pacienteId: ID!) {
                diagnosticosPorPaciente(pacienteId: $pacienteId) {
                    id
                    descripcion
                    tratamiento
                    fecha
                    nombreMedico
                    nombrePaciente
                    especialidad
                }
            }
        """
        variables = {"pacienteId": paciente_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting diagnoses by patient: {e}")
        return {"error": str(e)}


def get_triajes_por_paciente(paciente_id: str) -> dict:
    """
    A tool that retrieves all triage records for a specific patient.

    Args:
        paciente_id (str): The ID of the patient.

    Returns:
        dict: A list of triage records for the specified patient.
    """
    try:
        query = """
            query GetTriajesPorPaciente($pacienteId: ID!) {
                triajesPorPaciente(pacienteId: $pacienteId) {
                    id
                    paciente {
                        username
                    }
                    enfermera {
                        username
                    }
                    temperatura
                    peso
                    estatura
                    frecuenciaCardiaca
                    frecuenciaRespiratoria
                    saturacionOxigeno
                    alergias
                    enfermedadesCronicas
                    motivoConsulta
                    fecha
                }
            }
        """
        variables = {"pacienteId": paciente_id}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting triages by patient: {e}")
        return {"error": str(e)}


def get_horarios_disponibles(especialidad_id: str, fecha: str) -> dict:
    """
    A tool that retrieves available schedules for a specific specialty and date.

    Args:
        especialidad_id (str): The ID of the specialty.
        fecha (str): The date in YYYY-MM-DD format.

    Returns:
        dict: A list of available schedules for the specified specialty and date.
    """
    try:
        query = """
            query GetHorariosDisponibles($especialidadId: ID!, $fecha: Date!) {
                horariosDisponibles(especialidadId: $especialidadId, fecha: $fecha) {
                    id
                    fecha
                    horaInicio
                    horaFin
                    disponible
                    especialidad {
                        nombre
                    }
                    turno {
                        nombre
                    }
                    dia {
                        nombre
                    }
                }
            }
        """
        variables = {"especialidadId": especialidad_id, "fecha": fecha}
        return execute_graphql_query(query, variables)
    except Exception as e:
        print(f"Error getting available schedules: {e}")
        return {"error": str(e)}
