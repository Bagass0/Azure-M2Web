import json
import os
import logging
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions

# Connexion à Cosmos DB via la chaîne de connexion
COSMOS_DB_ENDPOINT = "https://cosmosdbbagasso.documents.azure.com:443/"
COSMOS_DB_KEY = "7oQmgiBLPXlUAN6JTpPBoAGnVHIIJijmYrKim7WQCvEo9KCKiomzfvKlVtJIm72oqNZNvRRQ2hWAACDbZJaB3Q=="
DATABASE_NAME = 'bagasso'
CONTAINER_NAME = 'user_data'

# Initialiser le client Cosmos DB
client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing CRUD request.')

    try:
        # Si la méthode est POST, PUT, DELETE, récupère le JSON du corps
        request_json = None
        if req.method != 'GET':
            try:
                request_json = req.get_json()
                logging.info(f"Corps JSON de la requête : {request_json}")
            except ValueError:
                logging.error("Erreur : La requête ne contient pas de JSON valide")
                return func.HttpResponse("Invalid JSON", status_code=400)

        if req.method == 'GET':
            # Exécuter la requête pour obtenir tous les utilisateurs
            users = container.query_items(
                query="SELECT * FROM c",
                enable_cross_partition_query=True
            )
            return func.HttpResponse(json.dumps([user for user in users]), mimetype="application/json", status_code=200)

        elif req.method == 'POST':
            # Générer un nouvel ID utilisateur
            user_id = str(request_json.get('id'))  # Utiliser un id fourni
            user_data = request_json.get('data')

            container.create_item(body={"id": user_id, **user_data})
            return func.HttpResponse('User added!', status_code=201)

        elif req.method == 'PUT':
            user_id = str(request_json.get('id'))
            user_data = request_json.get('data')

            container.upsert_item(body={"id": user_id, **user_data})
            return func.HttpResponse('User updated!', status_code=200)

        elif req.method == 'DELETE':
            user_id = str(request_json.get('id'))

            # Vérifier si l'utilisateur existe avant de le supprimer
            user_exists = list(container.query_items(
                query="SELECT * FROM c WHERE c.id = @id",
                parameters=[{"name": "@id", "value": user_id}],
                enable_cross_partition_query=True
            ))

            if not user_exists:
                return func.HttpResponse(f"User with id {user_id} not found.", status_code=404)

            # Suppression de l'utilisateur en utilisant `id` comme partition_key
            container.delete_item(item=user_id, partition_key=user_id)
            return func.HttpResponse("User deleted!", status_code=200)

        else:
            return func.HttpResponse('Method not supported!', status_code=405)

    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Cosmos DB Error: {str(e)}")
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return func.HttpResponse(f"An unexpected error occurred: {str(e)}", status_code=500)