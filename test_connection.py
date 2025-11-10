from src.graphql_client.client import GraphQLClient


def test_graphql_connection():
    """
    Tests the connection to the GraphQL API by fetching a list of specialities.
    """
    print("Attempting to connect to the GraphQL API...")

    try:
        # Initialize the client
        client = GraphQLClient()

        # Define the query to fetch specialities
        query = """
            query GetEspecialidades {
                especialidades {
                    id
                    nombre
                }
            }
        """

        # Execute the query
        result = client.execute(query)

        # Check for errors in the response
        if "errors" in result:
            print("GraphQL query returned errors:")
            for error in result["errors"]:
                print(f"- {error['message']}")
            return

        # Check if data is present
        if "data" in result and "especialidades" in result["data"]:
            print("Successfully connected to the GraphQL API!")
            print("Available specialities:")
            for especialidad in result["data"]["especialidades"]:
                print(f"- ID: {especialidad['id']}, Name: {especialidad['nombre']}")
        else:
            print(
                "Query executed, but no 'especialidades' data was found in the response."
            )
            print("Response:", result)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the following:")
        print("1. Is the GraphQL server running?")
        print("2. Is the `GRAPHQL_ENDPOINT` in your .env file set correctly?")


if __name__ == "__main__":
    test_graphql_connection()
