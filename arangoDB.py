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
if not sys_db.has_database("univ"):
    sys_db.create_database("univ")


# Connect to "test" database as root user.
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


universidades.insert_many(
    [
        {"_key": "UNIFESP"},
        {"_key": "UNIP"},
        {"_key": "UNIVAP"},
        {"_key": "USP"},
        {"_key": "UNICAMP"},
    ]
)
campus.insert_many(
    [
        {"_key": "SJC", "name": "UNIFESP", "telefone": "1234-1234"},
        {"_key": "Diadema", "name": "UNIP", "telefone": "1111-1111"},
        {"_key": "Santos", "name": "UNIVAP", "telefone": "4321-1234"},
        {"_key": "Campinas", "name": "USP", "telefone": "1234-4321"},
        {"_key": "SP", "name": "UNICAMP", "telefone": "4321-4321"},
    ]
)
curso.insert_many(
    [
        {"_key": "Medicina"},
        {"_key": "Engenharia"},
        {"_key": "Letras"},
        {"_key": "Matematica"},
        {"_key": "Musica"},
    ]
)
aluno.insert_many(
    [
        {"_key": "Maria", "cpf": "123.456.782-87", "ra": "12-3456"},
        {"_key": "Joao", "cpf": "823.456.234-87", "ra": "11-2456"},
        {"_key": "Felipe", "cpf": "765.456.782-87", "ra": "15-3256"},
        {"_key": "Mateus", "cpf": "153.466.712-87", "ra": "10-3156"},
        {"_key": "Marina", "cpf": "283.385.782-87", "ra": "11-2356"},
        {"_key": "Ana", "cpf": "103.456.782-17", "ra": "22-3469"},
        {"_key": "Roberto", "cpf": "707.456.782-87", "ra": "10-1236"},
        {"_key": "Maycon", "cpf": "612.456.782-87", "ra": "11-2436"},
        {"_key": "Victor", "cpf": "552.456.782-87", "ra": "18-7646"}
    ]
)

professor.insert_many(
    [
        {"_key": "Arnaldo", "cpf": "123.456.789-00"},
        {"_key": "Gomes", "cpf": "333.333.729-10"},
        {"_key": "Quiles", "cpf": "122.345.789-00"},
        {"_key": "Amanda", "cpf": "111.222.789-00"},
        {"_key": "Musa", "cpf": "113.436.939-00"},
    ]
)


grupo_extensao.insert_many(
    [
        {"_key": "Forgers"},
        {"_key": "Atletica"},
        {"_key": "Mao3D"},
        {"_key": "Tor"},
        {"_key": "Pandas"},
    ]
)

oferece.insert_many(
    [{"_key": "SJC-Medicina", "_from": "campus/SJC", "_to": "curso/Medicina"},
     {"_key": "Diadema-Engenharia", "_from": "campus/Diadema", "_to": "curso/Engenharia"},
     {"_key": "Santos-Letras", "_from": "campus/Santos", "_to": "curso/Letras"},
     {"_key": "Campinas-Matematica", "_from": "campus/Campinas", "_to": "curso/Matematica"},
     {"_key": "SP-Musica", "_from": "campus/SP", "_to": "curso/Musica"}]
)

localizado.insert_many(
    [{"_key": "UNIFESP-SJC", "_from": "campus/SJC", "_to": "universidades/UNIFESP"},
     {"_key": "UNIP-Diadema", "_from": "campus/Diadema", "_to": "universidades/UNIP"},
     {"_key": "UNIVAP-Santos", "_from": "campus/Santos", "_to": "universidades/UNIVAP"},
     {"_key": "USP-Campinas", "_from": "campus/Campinas", "_to": "universidades/USP"},
     {"_key": "UNICAMP-SP", "_from": "campus/SP", "_to": "universidades/UNICAMP"}]
)

estuda.insert_many(
    [{"_key": "Maria-Medicina", "_from": "aluno/Maria", "_to": "curso/Medicina"},
     {"_key": "Joao-Medicina", "_from": "aluno/Joao", "_to": "curso/Medicina"},
     {"_key": "Felipe-Matematica", "_from": "aluno/Felipe", "_to": "curso/Matematica"},
     {"_key": "Mateus-Engenharia", "_from": "aluno/Mateus", "_to": "curso/Engenharia"},
     {"_key": "Marina-Letras", "_from": "aluno/Marina", "_to": "curso/Letras"},
     {"_key": "Ana-Musica", "_from": "aluno/Ana", "_to": "curso/Musica"},
     {"_key": "Roberto-Musica", "_from": "aluno/Roberto", "_to": "curso/Musica"},
     {"_key": "Maycon-Letras", "_from": "aluno/Maycon", "_to": "curso/Letras"},
     {"_key": "Victor-Engenharia", "_from": "aluno/Victor", "_to": "curso/Engenharia"}]
)


leciona.insert_many(
    [{"_key": "Arnaldo-Medicina", "_from": "professor/Arnaldo", "_to": "curso/Medicina"},
     {"_key": "Gomes-Engenharia", "_from": "professor/Gomes", "_to": "curso/Engenharia"},
     {"_key": "Quiles-Letras", "_from": "professor/Quiles", "_to": "curso/Letras"},
     {"_key": "Amanda-Matematica", "_from": "professor/Amanda", "_to": "curso/Matematica"},
     {"_key": "Musa-Musica", "_from": "professor/Musa", "_to": "curso/Musica"}]
)


pertence.insert_many(
    [
        {"_key": "Forgers-SJC", "_from": "grupo_extensao/Forgers", "_to": "campus/SJC"},
        {"_key": "Atletica-Diadema", "_from": "grupo_extensao/Atletica","_to": "campus/Diadema"},
        {"_key": "Mao3D-Santos", "_from": "grupo_extensao/Mao3D","_to": "campus/Santos"},
        {"_key": "Tor-Campinas", "_from": "grupo_extensao/Tor","_to": "campus/Campinas"},
        {"_key": "Pandas-SP", "_from": "grupo_extensao/Pandas","_to": "campus/SP"},
    ]
)

coordena.insert_many(
    [{"_key": "Arnaldo-Forgers", "_from": "professor/Arnaldo", "_to": "grupo_extensao/Forgers"},
     {"_key": "Gomes-Atletica", "_from": "professor/Gomes", "_to": "grupo_extensao/Atletica"},
     {"_key": "Quiles-Mao3D", "_from": "professor/Quiles", "_to": "grupo_extensao/Mao3D"},
     {"_key": "Amanda-Tor", "_from": "professor/Amanda", "_to": "grupo_extensao/Tor"},
     {"_key": "Musa-Pandas", "_from": "professor/Musa", "_to": "grupo_extensao/Pandas"}]
)

participa.insert_many(
    [{"_key": "Maria-Forgers", "_from": "aluno/Maria", "_to": "grupo_extensao/Forgers"},
     {"_key": "Joao-Forgers", "_from": "aluno/Joao", "_to": "grupo_extensao/Forgers"},
     {"_key": "Felipe-Tor", "_from": "aluno/Felipe", "_to": "grupo_extensao/Tor"},
     {"_key": "Mateus-Atletica", "_from": "aluno/Mateus", "_to": "grupo_extensao/Atletica"},
     {"_key": "Marina-Mao3D", "_from": "aluno/Marina", "_to": "grupo_extensao/Mao3D"},
     {"_key": "Ana-Pandas", "_from": "aluno/Ana", "_to": "grupo_extensao/Pandas"},
     {"_key": "Roberto-Pandas", "_from": "aluno/Roberto", "_to": "grupo_extensao/Pandas"},
     {"_key": "Maycon-Mao3D", "_from": "aluno/Maycon", "_to": "grupo_extensao/Mao3D"},
     {"_key": "Victor-Atletica", "_from": "aluno/Victor", "_to": "grupo_extensao/Atletica"}]
)