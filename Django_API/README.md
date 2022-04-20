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
7. Finalmente se puede correr la API con el siguiente comando:
    ``` sh
    python manage.py runserver
    ```
    > Para salir utilizar Ctrl+C
