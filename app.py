from fastapi import FastAPI
#from routes.user import user
from routes.text import text
from docs import tags_metadata


# Creating a FastAPI object.
app = FastAPI(
    title= "ThunderAPI para Docker",
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
app.include_router(text)