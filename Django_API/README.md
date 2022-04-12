# DJANGO API

## Instrucciones de instalación (Windows)
1. Abrir un **CMD** *(Command Prompt)* en la carpeta principal.

2. Crear un ambiente virtual de python con el siguiente codigo.
    ``` sh
    virtualenv -p python env
    ```
3. Es necesario activar el ambiente virtual con el que se va a correr el programa.
    ``` sh
    .\env\Scripts\activate
    ```
    > Para salir ir a esta carpeta y escribir "deactivate en vez de activate"
4. El ambiente fue activado si en la terminal aparece *"(env)"* antes de la dirección.
    ``` sh 
    (env) C:\...
    ```
5. Una vez estando en el ambiente virtual, es necesario importar las librerias que se van a utilizar, estas se encuentran descritas en el documento ***requirements.txt***. Para importarlas de una manera más sencilla se puede utilizar el siguiente comando:
    ``` sh
    ""
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