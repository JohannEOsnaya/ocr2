<h3 align="center">
    <img height="150" src="/lib/assets/logoAthena.png" width="150"/>

<FONT SIZE=3>APIText de Athena</FONT>
</h3>

# Intro
<i align = "right">
Código para control y monitoreo de temperaturas en sistema ECMO para corazón
</i>

---

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#comenzando">Comenzando 🚀</a>
    </li>
    <li>
      <a href="#pre-requisitos">Pre-Requisitos 📋</a>
      <ul>
        <li><a href="#requisitos-desarrollador">Requisitos Desarrollador 💻</a></li>
        <li><a href="#requisitos-usuario">Requisitos Usuario 👨‍🦱</a></li>
      </ul>
    </li>
    <li><a href="#instalación">Instalación 🔧</a></li>
    <li>
      <a href="#pruebas">Pruebas 🔩</a>      
      <ul>
        <li><a href="#pruebas-software">Pruebas Software 👨‍💻</a></li>
        <li><a href="#pruebas-hardware">Pruebas Hardware 🔌</a></li>
      </ul>
    </li>
    <li><a href="#diagramas">Diagramas 📚</a></li>
    <li><a href="#despliegue">Despliegue 📦</a></li>
    <li><a href="#construcción">Construido con</a></li>
    <li><a href="#versionado">Versionado 📌</a></li>
    <li><a href="#wiki">Wiki 📖</a></li>
    <li><a href="#autores">Autores 🖋</a></li>
    <li><a href="#licencia">Licencia 📄</a></li>
    <li><a href="#expresiones-de-gratitud">Expresiones De Gratitud 🎁</a></li>
  </ol>
</details>

<p align="right">(<a href="#intro">Inicio</a>)</p>

## Comenzando 🚀          
<div align="left">
  <a href = "https://github.com/ThunderGer23/APImg">
    <img width="20" height="20" src="/lib/assets/icons/GitHub.webp"/>
  </a>
  <i>click para obtener el código de la API</i>
</div>

<p align="right">(<a href="#intro">Inicio</a>)</p>

### Pre-requisitos 📋

_Conocimientos intermadios en bases de datos, servidores, microservicios y python. Además del manejo de entornos virtuales con las siguientes instalaciones_


#### Requisitos Desarrollador 💻

_Debe contar con el siguiente conjunto de herramientas instaladas_

- [ ] Python
- [ ] Editor de texto/IDE
- [ ] MongoDB
- [ ] Postman

_Con lo anterior en mente es importante mencionar que se recomienda la integración de un entorno virtual para el desarrollo de nuevas funcionalidades dentro de la API, ya que pudiera existir el caso en el que alguna instalación ajena dentro del equipo produzca inconvenientes con la integración de nuestro software._

**Comandos a ejecutar en la terminal:**
      
      > pip install virtualenv
      > python -m venv APImg
      > cd APImg/Scripts/activate
      > cd ../..
      > pip install Fastapi uvicorn pymongo


#### Requisitos Usuario 👨‍🦱

_Se hace caso omiso de este apartado puesto que no debería haber intervención alguna por parte de usuarios finales o terceros ajenos al desarrollo del proyecto._

<p align="right">
  (<a href="#requisitos-desarrollador">Requisitos Desarrollador</a>)
  (<a href="#requisitos-usuario">Requisitos Usuario</a>)
  (<a href="#intro">Inicio</a>)
</p>

### Instalación 🔧

_Con nuestro entorno virtual creado y en ejecución mencionado en el punto anterior podemos proceder a ejecutar nuestro proyecto con los siguientes comandos_

_**Dentro de la carpeta principal de la API ejecutar:**_

      > uvicorn app:app

_El comando anterior levantará nuestro servidor para comenzar a trabajar, sin embargo lo realizará con una configuración predeterminada y bastante deficiente para un constante desarrollo de nuevas funcionalidades e integraciones al sistema, por lo cual se recomienda utilizar la siguiente adición de parametros._

      > uvicorn app:app --reload

_Haciendo que nuestro servidor se reinicie cada que detecte algún cambio dentro de nuestro código de ruteo._
_Adicional a esto es posible adicionar mayor cantidad de parametros como el host, port, entre otros._

      > uvicorn app:app --reload --host: <param> --port: <param>

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Pruebas 🔩

_De manera adicional se incluiran archivos de la arquitectura y funcionamiento del sistema, así como un conjunto de datos que puede utilizar para realizar las pruebas pertinentes del sistema._

#### Pruebas Unitarias 👨‍💻

_El uso de pruebas unitarias dentro del proyecto nos permite detectar errores dentro de cada funcionalidad del sistema, son de gran ayuda a la hora de intentar agregar una nueva funcionalidad así como ahorrar tiempo al momento de testear el sistema_.


Primero es necesario crear un entorno virtual con el siguiente comando en una terminal **CMD**:

<h5 align="center"><code>python -m venv "nombre del entorno virtual"</code></h5>

Una vez que nuestro entorno virtual este creado debemos ponerlo en marcha; primero entratemos hasta la carpeta _Scripts_

<code>cd .\\"nombre del entorno virtual"\Scripts</code>

Ya dentro del directorio escribimos lo siguiente en la terminal

<h5 align="center"><code>activate.bat </code></h5>

Para confirmar que el entorno virtual esta encendido debe aparecernos entre parentesis el nombre que le asignamos a nuestro entorno virtual seguido de la ruta como se muestra en este ejemplo

```
(nombre del entorno virtual) C:\Users\toled\Documents\APIText>
```

Como ya confirmamos que nuestro entorno virtual esta encendido procederemos a instalr las herramientas necesarias para poder usar la API (estas herramientas y sus versiones estan en el documento <a href="https://github.com/ThunderGer23/APIText/blob/R2D2/requirements.txt">**requirements.txt**</a>)

<h5 align="center"><code>pip install -r requirements.txt</code></h5>

#### Pruebas de Integración 🔌

_El uso de pruebas de integración dentro del proyecto nos da la ventaja de poder identificar de manera rápida las conexiones fallidas entre este y más microservicios que componen al software así como la integración al backend principal._

Para esta parte se hace uso de la herramienta de docker, la cual nos permite hacer un contenedor que almacene la API; para lograr esto se deben realizar las siguientes configuraciones

Primero se crea un documento llamado <a href="https://github.com/ThunderGer23/APIText/blob/R2D2/Dockerfile">**Dockerfile**</a> con la siguiente configuración:

~~~
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
~~~

Despues un documento llamado <a href="https://github.com/ThunderGer23/APIText/blob/R2D2/docker-compose.yml">**docker-compose.yml**</a> con la siguiente configuración:

~~~
version: "3.9"
services:
  apidocker:
    build: ./
    ports:
      - "8000:8000"
    environment:
      - TESSDATA_PREFIX=/code   
~~~

Y ahora se deben ejecutar los siguientes comandos en la terminal

<h5 align="center"><code>docker compose up</code></h5>

Una vez creado el contenedor podra acceder a la siguiente direccion **local** en su navegador

<h5 align="center"><code><a>http://localhost:8000/docs#/default/testing_test_get</a></code></h5>

<p align="right">
  (<a href="#pruebas-software">Pruebas Software</a>)
  (<a href="#pruebas-hardware">Pruebas Hardware</a>)
  (<a href="#ecmo">Inicio</a>)
</p>

## Diagramas 📚

_A continuación se muestran los diagramas de funcionamiento general de la API_

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Despliegue 📦

_El despliegue se realiza de manera automatico con railway._

Primero nos dirigimos a la siguiente direccion <a href="https://railway.app/dashboard">https://railway.app/dashboard</a>

* Nota.- Es necesario contar con una cuenta de <a href="https://railway.app/">Railway</a>

Hacemos click en "New Project"

![1](lib/assets/steps/1.PNG)

Click en ""Deploy from GitHub repo"

![2](lib/assets/steps/2.PNG)

Type "dock[\[enter]]"

Click en "Add variables"

![3](lib/assets/steps/3.PNG)

Click en "Add"

![4](lib/assets/steps/4.PNG)

Click en "New Variable"

![5](lib/assets/steps/5.PNG)

Click en el campo "Value"

![6](lib/assets/steps/6.PNG)

Oprima \[[ctrl]]+\[[V]]

Click en "Add"

![7](lib/assets/steps/7.PNG)

Oprima este icono

![8](lib/assets/steps/8.PNG)

Oprima este boton

![9](lib/assets/steps/9.PNG)

Oprima aqui

![10](lib/assets/steps/10.PNG)

Click en "Settings"

![11](lib/assets/steps/11.PNG)

Click en "Generate Domain"

![12](lib/assets/steps/12.PNG)

Click en "View Logs"

![13](lib/assets/steps/13.PNG)

Click en este icono

![14](lib/assets/steps/14.PNG)

Click en "testdocker-production.up.railway.app"

![15](lib/assets/steps/15.PNG)

Click en "Testing"

![16](lib/assets/steps/16.PNG)

Click en "Try it out"

![17](lib/assets/steps/17.PNG)

Click en "Execute"

![18](lib/assets/steps/18.PNG)

<p align="right">(<a href="#intro">Inicio</a>)</p>

## Construcción🛠️

_El diseño de esta API se realizo en base al siguiente conjunto de tecnologias._

* [Anyio](https://pypi.org/project/anyio/) ➡ Librería de redes y concurrencia asíncrona que funciona sobre asyncio o trio
* [Click](https://pypi.org/project/click/) ➡ Paquete de Python para crear hermosas interfaces de línea de comandos de manera componible con tan poco código como sea necesario
* [Colorama](https://pypi.org/project/colorama/) ➡ Hace que las secuencias de caracteres de escape ANSI (para producir texto de terminal coloreado y posicionamiento del cursor) funcionen bajo MS Windows
* [FastAPI](https://fastapi.tiangolo.com/#installation) ➡ Desarrollo del Servidor
* [H11](https://pypi.org/project/h11/) ➡  Conjunto de herramientas para la construcción de programas que hablan HTTP; h11 hace mucho más fácil implementar algo como requests o twistedweb
* [Idna](https://pypi.org/project/idna/) ➡ Soporte para el protocolo de Nombres de Dominio Internacionalizados en Aplicaciones (IDNA)
* [Pydantic](https://pydantic-docs.helpmanual.io/) ➡ Validación de datos y gestión de configuraciones utilizando sugerencias de tipo de Python
* [Pymongo](https://pymongo.readthedocs.io/en/stable/installation.html) ➡ Distribución de Python que contiene herramientas para trabajar con MongoDB
* [Python 3.10.6](https://www.python.org/) ➡ Lenguaje utilizado
* [Sniffio](https://pypi.org/project/sniffio/) ➡ Pequeño paquete cuyo único propósito es permitirte detectar bajo qué biblioteca asíncrona se está ejecutando tu código
* [Starlette](https://www.starlette.io/) ➡ Framework/toolkit ASGI ligero, ideal para construir servicios web asíncronos en Python
* [Typing_extensions](https://pypi.org/project/typing-extensions/) ➡ Permitir la experimentación con nuevos PEPs del sistema de tipos antes de que sean aceptados y añadidos al módulo de tipado ?
* [Uvicorn](https://www.uvicorn.org/) ➡ Manejo de peticiones HTTP


<p align="right">(<a href="#intro">Inicio</a>)</p>


## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/ThunderGer23/APImg).

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/ThunderGer23/APImg).

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Autores 🖋

* **ThunderGer** - *Trabajo Inicial* - [ThunderGer23](https://github.com/ThunderGer23)
* **R2D2** - *Documentación* - [R2D2](https://github.com/ArturoEmmanuelToledoAguado)
*  **ItzeGar** - ** - [ItzeGar](https://github.com/itzeGar)

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Licencia 📄

Este proyecto está bajo la Licencia "*MIT*" - mira el archivo [LICENSE](LICENSE) para detalles.

<p align="right">(<a href="#intro">Inicio</a>)</p>


## Expresiones de Gratitud 🎁

**ThunderGer**
<div align="left">
    <table border="0">  
      <tbody>
        <tr>
          <td>
            <img height="100" src="/lib/assets/avatars/ThunderGer.png" width="100"/>
          </td>
          <th>
            <li>
              Algun agradecimiento quer agregare despues
            </li>
          </th>
        </tr>
      </tbody>
    </table>
</div>


**R2D2**
<div align="left">
    <table border="0">  
      <tbody>
        <tr>
          <td>
            <img height="100" src="/lib/assets/avatars/Arturo.webp" width="100"/>
          </td>
          <th>
            <li>
              A mis compañeros por brindarme la oportunidad de participar en este proyecto 
            </li>
          </th>
        </tr>
      </tbody>
    </table>
</div>


**ItzeGar**
<div align="left">
    <table border="0">  
      <tbody>
        <tr>
          <td>
            <img height="100" src="/lib/assets/avatars/Itz2.webp" width="100"/>
          </td>
          <th>
            <li>
              Algun agradecimiento quer agregare despues
            </li>
          </th>
        </tr>
      </tbody>
    </table>
</div>

<p align="right">(<a href="#intro">Inicio</a>)</p>