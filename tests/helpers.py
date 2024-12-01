import json
import os

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
SCHEMA_DIR = os.path.join(os.path.dirname(DIRECTORY), "schemas")

def get_schema(file_name):
    with open(os.path.join(SCHEMA_DIR, file_name)) as file:
        return json.loads(file.read())

