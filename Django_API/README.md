# DJANGO API

## Instrucciones de instalación (Windows)
1. Abrir un **CMD** *(Command Prompt)* en la carpeta principal.

2. Crear un ambiente virtual de python los siguientes codigos.
    ``` sh
    pip install virtualenv
    virtualenv -p python env
    ```
3. Activar el ambiente virtual con el que se va a correr el programa.
    ``` sh
    .\env\Scripts\activate
    ```
    > Para salir ir a la carpeta de este archivo y escribir *"deactivate"* en vez de *"activate"*
4. Revisar que el ambiente fue activado, si en la terminal aparece *"(env)"* antes de la dirección, todo esta correcto. Por ejemplo:
    ``` sh 
    (env) C:\...
    ```
5. Una vez estando en el ambiente virtual, es necesario importar las librerias que se van a utilizar, estas se encuentran descritas en el documento ***requirements.txt***. Para importarlas de una manera más sencilla se puede utilizar el siguiente comando:
    ``` sh
    pip3 install -r requirements.txt
    ```
6. Antes de correr la API es necesario entrar a la carpeta del projecto.
    ``` sh 
    cd API_PROJECT
    ```
7. Para correr la API se puede utilizar el siguiente comando:
    ``` sh
    python manage.py runserver
    ```
    > Para salir utilizar Ctrl+C
8. A parte del api, se debe de correr un servidor de redis con el siguiente comando en una terminal aparte, no dentro del ambiente de python
    ```sh
    docker run -d -p 6379:6379 --name redis-server redis
    ```
    Para correr este server se requiere instalar WSL 2 y docker en un ambiente windows
    Instrucciones para la instalacion de docker: https://docs.docker.com/desktop/windows/install/ <br>
    Tras instalar docker, este le mencionara si es necesario instalar WSL 2 y como hacerlo 

9. Finalmente se requiere correr workers de celery
    1. Abrir otra terminal en el directorio del projecto
    2. Activar el ambiente virtual
    ``` sh
    .\env\Scripts\activate
    ```
    3. Entrar a la carpeta del api
    ``` sh 
    cd API_PROJECT
    ```
    4. Correr siguiente comando
    ```sh
    celery -A API_PROJECT worker -l info --pool=solo
    ```
