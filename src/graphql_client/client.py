import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GraphQLClient:
    def __init__(self, endpoint=None, token=None):
        self.endpoint = endpoint or os.getenv("GRAPHQL_ENDPOINT")
        self.token = token
        if not self.endpoint:
            raise ValueError(
                "GraphQL endpoint not provided. Please set the GRAPHQL_ENDPOINT environment variable."
            )

    def execute(self, query, variables=None):
        """
        Executes a GraphQL query.

        Args:
            query (str): The GraphQL query string.
            variables (dict, optional): A dictionary of variables for the query.

        Returns:
            dict: The JSON response from the server.

        Raises:
            Exception: If the query fails.
        """
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            response = requests.post(
                self.endpoint,
                json={"query": query, "variables": variables},
                headers=headers,
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to execute GraphQL query: {e}")
