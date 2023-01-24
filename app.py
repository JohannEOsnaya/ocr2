from fastapi import FastAPI
from routes.red import red
from docs import tags_metadata
from os import environ as env
from notigram import ping

ping(env['TOKEN'], 'Servidor API para las citas arriba')
# Creating a FastAPI object.
app = FastAPI(
    title= "API para las citas",
    description= "This is a description for the API :v/",
    version = "1.0",
    contact={
        "name": "ThunderGer",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    openapi_tags= tags_metadata
)

# Importing the `user` module from the `routes` folder.
app.include_router(red)