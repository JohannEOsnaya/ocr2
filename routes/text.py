from fastapi import APIRouter, File, UploadFile, FileResponse
from PIL import Image
from models.files import Files
from pytesseract import pytesseract
from config.db import conn
from os import getcwd, remove
#import os 
from docs import tags_metadata
import io
from typing import List
from gtts import gTTS
#import pyglet
from time import sleep

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

text = APIRouter()

@text.get('/test', response_model=str, tags=["Text"])
def testing():
    """
    It takes an image, converts it to text, and returns the text
    :return: The text that is in the image.
    """
    im = Image.open(getcwd()+'/Pruebame.png')
    texto = pytesseract.image_to_string(im)
    return texto

@text.post('/submit', response_model= str, tags=["Text"])
async def submit_image(file: UploadFile = File(...),):
    """
    It takes an image file as input, and returns the text in the image as output
    
    :param file: UploadFile = File(...)
    :type file: UploadFile
    :return: The text that was extracted from the image.
    """
    data = await file.read()
    image = {
        "name": file.filename,
        "data": data
    }
    id = conn.local.testimage.insert_one(image).inserted_id
    with Image.open(io.BytesIO(data)) as pic:
        texto = pytesseract.image_to_string(pic)
        tts = gTTS(text = str(texto), lang = 'es')
        tts.save(getcwd() + '/temp.mp3')
    return str({texto, id})

@text.post('/submit_more', response_model= dict(), tags=["Text"])
async def submit_images(files: List[UploadFile]):
    """
    It takes a list of files, reads them, and returns a dictionary of the file names and their text
    
    :param files: List[UploadFile]
    :type files: List[UploadFile]
    :return: A dictionary with the filename as the key and the text as the value.
    """
    res = dict()
    for file in files:
        with Image.open(io.BytesIO(await file.read())) as pic:
            res[file.filename] = pytesseract.image_to_string(pic)
    return res

@text.get("/play_audio")
async def play_audio():
    return FileResponse(getcwd() + '/temp.mp3', media_type="audio/mpeg")