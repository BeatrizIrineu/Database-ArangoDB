from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "_system" database as root user.
# This returns an API wrapper for "_system" database.
sys_db = client.db('_system', username='root', password='')

# List all databases.
sys_db.databases()

# Create a new database named "universidades" if it does not exist.
# Only root user has access to it at time of its creation.
if not sys_db.has_database('universidades'):
    sys_db.create_database('universidades')