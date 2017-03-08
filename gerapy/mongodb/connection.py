from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_PASSWORD = ''
MONGODB_DATABASE = 'spider'
MONGODB_SHEET = 'sheet'

def from_settings(settings):
    host = settings.get('MONGODB_HOST', MONGODB_HOST)
    port = int(settings.get('MONGODB_PORT', MONGODB_PORT))
    password = settings.get('MONGODB_PASSWORD', MONGODB_PASSWORD)
    db = settings.get('MONGODB_DATABASE', MONGODB_DATABASE)
    sheet = settings.get('MONGODB_SHEET', MONGODB_SHEET)
    client = MongoClient(host=host, port=port)
    db = client[db]
    sheet = db[sheet]
    if sheet:
        return sheet
    else:
        return False
