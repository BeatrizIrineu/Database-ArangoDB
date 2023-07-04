from arango import ArangoClient
import json


# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "_system" database as root user.
# This returns an API wrapper for "_system" database.
sys_db = client.db("_system", username="root", password="")

# List all databases.
sys_db.databases()

# Create a new database named "universidades" if it does not exist.
# Only root user has access to it at time of its creation.
if not sys_db.has_database("univ"):
    sys_db.create_database("univ")


# Connect to "univ" database as root user.
db = client.db("univ", username="root", password="")

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

if grafo.has_vertex_collection("curso"):
    curso = grafo.vertex_collection("curso")
else:
    curso = grafo.create_vertex_collection("curso")

if grafo.has_vertex_collection("campus"):
    campus = grafo.vertex_collection("campus")
else:
    campus = grafo.create_vertex_collection("campus")

if grafo.has_vertex_collection("aluno"):
    aluno = grafo.vertex_collection("aluno")
else:
    aluno = grafo.create_vertex_collection("aluno")

if grafo.has_vertex_collection("professor"):
    professor = grafo.vertex_collection("professor")
else:
    professor = grafo.create_vertex_collection("professor")

if grafo.has_vertex_collection("grupo_extensao"):
    grupo_extensao = grafo.vertex_collection("grupo_extensao")
else:
    grupo_extensao = grafo.create_vertex_collection("grupo_extensao")

# Get the API wrapper for edge collection "teach".
if grafo.has_edge_definition("localizado"):
    localizado = grafo.edge_collection("localizado")
else:
    localizado = grafo.create_edge_definition(
        edge_collection="localizado",
        from_vertex_collections=["campus"],
        to_vertex_collections=["universidades"],
    )

# Get the API wrapper for edge collection "oferece".
if grafo.has_edge_definition("oferece"):
    oferece = grafo.edge_collection("oferece")
else:
    oferece = grafo.create_edge_definition(
        edge_collection="oferece",
        from_vertex_collections=["campus"],
        to_vertex_collections=["curso"],
    )

# Get the API wrapper for edge collection "estuda".
if grafo.has_edge_definition("estuda"):
    estuda = grafo.edge_collection("estuda")
else:
    estuda = grafo.create_edge_definition(
        edge_collection="estuda",
        from_vertex_collections=["aluno"],
        to_vertex_collections=["curso"],
    )

# Get the API wrapper for edge collection "leciona".
if grafo.has_edge_definition("leciona"):
    leciona = grafo.edge_collection("leciona")
else:
    leciona = grafo.create_edge_definition(
        edge_collection="leciona",
        from_vertex_collections=["professor"],
        to_vertex_collections=["curso"],
    )
# Get the API wrapper for edge collection "pertence".
if grafo.has_edge_definition("pertence"):
    pertence = grafo.edge_collection("pertence")
else:
    pertence = grafo.create_edge_definition(
        edge_collection="pertence",
        from_vertex_collections=["grupo_extensao"],
        to_vertex_collections=["campus"],
    )
    
# Get the API wrapper for edge collection "coordena".
if grafo.has_edge_definition("coordena"):
    coordena = grafo.edge_collection("coordena")
else:
    coordena = grafo.create_edge_definition(
        edge_collection="coordena",
        from_vertex_collections=["professor"],
        to_vertex_collections=["grupo_extensao"]
    )
# Get the API wrapper for edge collection "participa".
if grafo.has_edge_definition("participa"):
    participa = grafo.edge_collection("participa")
else:
    participa = grafo.create_edge_definition(
        edge_collection="participa",
        from_vertex_collections=["aluno"],
        to_vertex_collections=["grupo_extensao"]
    )
# Get the API wrapper for edge collection "matriculado".
if grafo.has_edge_definition("matriculado"):
    matriculado = grafo.edge_collection("matriculado")
else:
    matriculado = grafo.create_edge_definition(
        edge_collection="matriculado",
        from_vertex_collections=["aluno"],
        to_vertex_collections=["universidades"]
    )

with open("inserts\insertUnis.json") as f:
    universidades.insert_many(json.load(f))

with open("inserts\insertCampi.json") as f:
    campus.insert_many(json.load(f)) 

with open("inserts\insertCursos.json") as f:
    curso.insert_many(json.load(f))

#with open("inserts\insertAlunos.json") as f:
#    aluno.insert_many(json.load(f))

#with open("inserts\insertProfessores.json") as f:
#    aluno.insert_many(json.load(f))

with open("inserts\insertGEs.json") as f:
    grupo_extensao.insert_many(json.load(f))

with open("inserts\insertOferece.json") as f:
    oferece.insert_many(json.load(f))

with open("inserts\insertLocalizado.json") as f:
    localizado.insert_many(json.load(f))

#with open("inserts\insertEstuda.json") as f:
#    estuda.insert_many(json.load(f))

#with open("inserts\insertLeciona.json") as f:
#    leciona.insert_many(json.load(f))

with open("inserts\insertPertence.json") as f:
    pertence.insert_many(json.load(f))

#with open("inserts\insertCoordena.json") as f:
#    coordena.insert_many(json.load(f))

#with open("inserts\insertParticipa.json") as f:
#    participa.insert_many(json.load(f)) 

with open("inserts\insertMatriculado.json") as f:
    matriculado.insert_many(json.load(f)) 