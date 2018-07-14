from app import app, api
from app.resources.index import Index

api.add_resource(Index, "/", "/index")

if __name__ == '__main__':
    app.run(debug = True)
