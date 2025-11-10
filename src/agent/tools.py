from src.graphql_client.client import GraphQLClient


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
