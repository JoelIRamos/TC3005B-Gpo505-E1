# API Endpoints

## GET_HISTORY_LIST
> Funcion: Obtiene el historial de las corridas realizadas

### URL: 
    /api/getHistoryList/

### Parametros: 
    N/A


### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
> Decidir Cual Opción

**Opción 1**
``` json
    {
        "message": "found",
        "result": [
            {
                "_id": "NombreArchivo2022-01-04T06:00:00.000+00:00",
                "name": "NombreArchivo",
                "date": "2022-01-04T06:00:00.000+00:00"
            },
            {
                "_id": "NombreArchivo2022-04-01T06:01:20.000+00:00",
                "name": "NombreArchivo",
                "date": "2022-04-01T06:01:20.000+00:00"
            },
            {
                "_id": "NombreArchivo22022-04-04T06:23:16.000+00:00",
                "name": "NombreArchivo2",
                "date": "2022-04-04T06:23:16.000+00:00"
            }
        ]
    }
```
**Opción 2**
``` json
    {
        "message": "found",
        "result": [
            {
                "name": "NombreArchivo",
                "versions": [
                    {
                        "_id": "NombreArchivo2022-01-04T06:00:00.000+00:00",
                        "name": "2022-01-04T06:00:00.000+00:00"
                    }, 
                    {
                        "_id": "NombreArchivo2022-04-01T06:01:20.000+00:00",
                        "name": "2022-04-01T06:01:20.000+00:00"
                    }
                ]
            },
            {
                "name": "NombreArchivo2",
                "versions": [
                    {
                        "_id": "NombreArchivo22022-04-04T06:23:16.000+00:00",
                        "date": "2022-04-04T06:23:16.000+00:00"
                    }
                ]
            }
        ]
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "Not found"
    }
```

----
## **GET_USER_ID**
> Funcion: Iniciar una session de una corrida, para que este pueda crear las gráficas 

### URL: 
    /api/getUserID/<str:historyID>/

### Parametros: 
**historyID:** El id del historial (el cual fue enviado cuando se hizo la peticion getHistoryList)

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "success",
        "userID": "627fd92b7ca61d828d29ca10"
    }
```

### Objeto Retorno Incorrecto
**Versión 1**
``` json
    {
        "message": "session already in use"
    }
```
**Versión 2**
``` json
    {
        "message": "session unexistent"
    }
```
> ToDo: revisar session inexistente

----
## **GET_LAST_SESSION**
> Funcion: Obtener la información de las gráficas que estaba manejando el usuario

### URL: 
    /api/getLastSession/<str:userID>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "found",
        "result": {
            "historyID": "historyID",
            "date": "date",
            "interno": [
                "PlantaPorteria_num",
                "EmpresaTransportista_num"
            ],
            "externo": [
                "UsuarioPesadaEntrada_num",
                "UsuarioDescarga_num"
            ],
            "graphs": [
                {
                    "type": "bar graph",
                    "x-axis": "UsuarioPesadaEntrada_num",
                    "y-axis": "EmpresaTransportista_num"
                },
                {
                    "type": "pi",
                    "values": "PlantaPorteria_num"
                }
            ],
            "file": {
                "PlantaPorteria_num": ["1", "3"],
                "ClaveTransportista_num": ["86", "24"],
                "EmpresaTransportista_num": ["34", "12"]
            }
        }
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "Not found"
    }
```

----
## **DELETE_LAST_SESSION**
> Funcion: Cuando el usuario terminó, liberar la sesion para que pueda seguirse modificando si es que llega a volver. 

### URL: 
    /api/deleteLastSession/<str:userID>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "Success"
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "Not found"
    }
```
> ToDo: y hacer un timer dentro de la base de datos (10 minutos)
----
## **GET_BAR_GRAPH**
> Funcion: Obtener los valores para crear una grafica de barras en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variableA>/<str:variableB>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variableA:**

**variableB:**

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "success",
        "result": {
            "graphID": "",
            "valuesX": [],
            "valuesY": []
        }
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "not found"
    }
```

----
## **GET_BUBBLE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de burbuja en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variableA>/<str:variableB>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variableA:**

**variableB:**

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "success",
        "result": {
            "graphID": "",
            "valuesX": [],
            "valuesY": []
        }
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "not found"
    }
```

----
## **GET_AREA_GRAPH**
> Funcion: Obtener los valores para crear una grafica de area en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variableA>/<str:variableB>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variableA:**

**variableB:**

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "success",
        "result": {
            "graphID": "",
            "valuesX": [],
            "valuesY": []
        }
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "not found"
    }
```

----
## **DELETE_GRAPH**
> Funcion: 

### URL: 
    /api/deleteGraph/<str:userID>/<graphID>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**graphID** El id de la grafica (el cual fue generado cuando se hizo alguna de las peticiones para obtener una gráfica)

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "success"
    }
```

### Objeto Retorno Incorrecto
**Versión 1**
``` json
    {
        "message": "user not found"
    }
```

**Versión 2**
``` json
    {
        "message": "graph not found"
    }
```

<!-- ----
## **a**
> Funcion: 

### URL: 
    /api/

### Parametros: 
    N/A

### Bodys
``` json
    
```

### Objeto Retorno Correcto
``` json
    
```

### Objeto Retorno Incorrecto
``` json

```  -->

----
----
## **GET_HISTORY_DETAIL**
> Funcion: Obtiene toda la información de una sola corrida

### URL: 
    /api/getHistoryDetail/<str:historyID>/

### Parametros: 
**historyID:** El id del historial (el cual fue enviado cuando se hizo la peticion getHistoryList)

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "message": "found",
        "result": {
            "historyID": "historyID",
            "date": "date",
            "interno": [
                "PlantaPorteria_num",
                "EmpresaTransportista_num"
            ],
            "externo": [
                "UsuarioPesadaEntrada_num",
                "UsuarioDescarga_num"
            ],
            "graphs": [
                {
                    "type": "bar graph",
                    "x-axis": "UsuarioPesadaEntrada_num",
                    "y-axis": "EmpresaTransportista_num"
                },
                {
                    "type": "pi",
                    "values": "PlantaPorteria_num"
                }
            ],
            "file": {
                "PlantaPorteria_num": ["1", "3"],
                "ClaveTransportista_num": ["86", "24"],
                "EmpresaTransportista_num": ["34", "12"]
            }
        }
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "Not found"
    }
```

----
## **PUT_GRAPH**
> Funcion: Actualizar las gráficas que estaba haciendo el usuario

### URL: 
    /api/putGraph/<str:userID>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

### Bodys
``` json
    {
        "type": "bar graph",
        "x-axis": "UsuarioPesadaEntrada_num",
        "y-axis": "EmpresaTransportista_num"
    }
```

### Objeto Retorno Correcto
``` json
    {
        "message": "Success"
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "Not found"
    }
```

