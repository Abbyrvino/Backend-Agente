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
