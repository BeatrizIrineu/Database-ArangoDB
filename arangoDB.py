from arango import ArangoClient, AQLQueryKillError

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "_system" database as root user.
# This returns an API wrapper for "_system" database.
sys_db = client.db("_system", username="root", password="")

# List all databases.
sys_db.databases()

# Create a new database named "universidades" if it does not exist.
# Only root user has access to it at time of its creation.
if not sys_db.has_database("universidade"):
    sys_db.create_database("universidade")


# Connect to "test" database as root user.
db = client.db("universidade", username="root", password="")

# Create a new graph named "universidades" if it does not already exist.
# This returns an API wrapper for "universidades" graph.
if db.has_graph("universidades"):
    grafo = db.graph("universidades")
else:
    grafo = db.create_graph("universidades")

# Create a new vertex collection named "universidades" if it does not exist.
# This returns an API wrapper for "universidades" vertex collection.
if grafo.has_vertex_collection("universidades"):
    universidades = grafo.vertex_collection("universidades")
else:
    universidades = grafo.create_vertex_collection("universidades")

if grafo.has_vertex_collection("predio"):
    predio = grafo.vertex_collection("predio")
else:
    predio = grafo.create_vertex_collection("predio")

# Get the API wrapper for edge collection "teach".
if grafo.has_edge_definition("localizado"):
    localizado = grafo.edge_collection("localizado")
else:
    localizado = grafo.create_edge_definition(
        edge_collection="localizado",
        from_vertex_collections=["predio"],
        to_vertex_collections=["universidades"],
    )


universidades.insert_many(
    [
        {"_key": "UNIFESP", "name": "UNIFESP"},
        {"_key": "UNIP", "name": "UNIP"},
        {"_key": "UNIVAP", "name": "UNIVAP"},
        {"_key": "USP", "name": "USP"},
        {"_key": "UNICAMP", "name": "UNICAMP"},
    ]
)
predio.insert_many(
    [
        {"_key": "Medicina", "name": "Medicina", "numero": "1"},
        {"_key": "Engenharia", "name": "Engenharia", "numero": "2"},
        {"_key": "Letras", "name": "Letras", "numero": "1"},
        {"_key": "Matematica", "name": "Matematica", "numero": "3"},
        {"_key": "Musica", "name": "Musica", "numero": "2"},
    ]
)

localizado.insert_many(
    [{"_key": "UNIFESP-Medicina", "_from": "predio/Medicina", "_to": "universidades/UNIFESP"},
     {"_key": "UNIP-Engenharia", "_from": "predio/Engenharia", "_to": "universidades/UNIP"},
     {"_key": "UNIVAP-Letras", "_from": "predio/Letras", "_to": "universidades/UNIVAP"},
     {"_key": "USP-Matematica", "_from": "predio/Matematica", "_to": "universidades/USP"},
     {"_key": "UNICAMP-Musica", "_from": "predio/Musica", "_to": "universidades/UNICAMP"}]
)
