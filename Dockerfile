#Configuracion para instalar uvicorn y tesseract en un contenedor de Ubuntu: lastest (23/11/2022) Docker en el puerto 8000

FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

RUN apt-get update \
  && apt-get -y install tesseract-ocr \
  && apt-get install -y python3 python3-distutils python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN apt update \
  && apt-get install ffmpeg libsm6 libxext6 -y

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code
 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
