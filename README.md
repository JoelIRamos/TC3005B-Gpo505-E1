# Pasos para correr la API localmente

## Instrucciones de instalación (Windows)
1. Abrir un **CMD** *(Command Prompt)* en la carpeta de [Django_API](/Django_API/).

2. Crear un ambiente virtual de python los siguientes codigos.
    ``` sh
    pip install virtualenv
    virtualenv -p python env
    ```
3. Activar el ambiente virtual con el que se va a correr el programa.
    ``` sh
    .\env\Scripts\activate
    ```
    > Para salir ir a la misma carpeta y escribir *"deactivate"* en vez de *"activate"*
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
8. A parte del api, se debe intallar  el broker de RabbitMQ el cual a su mismo requiere instalar Erlang. Para instalar ambos, estan las siguiente ligas
    ```
    https://www.erlang.org/downloads

    https://github.com/rabbitmq/rabbitmq-server/releases
    ```

9. Finalmente se requiere correr workers de celery
    1. Abrir otra terminal en el mismo directorio del projecto
    2. Activar el ambiente virtual
    ``` sh
    .\env\Scripts\activate
    ```
    3. Entrar a la carpeta del api
    ``` sh 
    cd API_PROJECT
    ```
    4. Correr con el siguiente comando
    ```sh
    celery -A API_PROJECT worker -l info --pool=solo
    ```
