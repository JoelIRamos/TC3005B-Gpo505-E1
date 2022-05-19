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
                "base_file_name": "NombreArchivo",
                "date": "2022-01-04T06:00:00.000+00:00"
            },
            {
                "_id": "NombreArchivo2022-04-01T06:01:20.000+00:00",
                "base_file_name": "NombreArchivo",
                "date": "2022-04-01T06:01:20.000+00:00"
            },
            {
                "_id": "NombreArchivo22022-04-04T06:23:16.000+00:00",
                "base_file_name": "NombreArchivo2",
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
                "base_file_name": "NombreArchivo",
                "versions": [
                    {
                        "_id": "NombreArchivo2022-01-04T06:00:00.000+00:00",
                        "date": "2022-01-04T06:00:00.000+00:00"
                    }, 
                    {
                        "_id": "NombreArchivo2022-04-01T06:01:20.000+00:00",
                        "date": "2022-04-01T06:01:20.000+00:00"
                    }
                ]
            },
            {
                "base_file_name": "NombreArchivo2",
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
        "message": "historyID unexistent"
    }
```

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
            "historyID": "Archivo2022-01-04T06:00:00.000+00:00",
            "base_file_name": "Archivo",
            "date": "2022-01-04T06:00:00.000+00:00",
            "internal_attributes": [
                "PlantaPorteria_num",
                "EmpresaTransportista_num"
            ],
            "external__attributes": [
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
            ]
        }
    }
```

### Objeto Retorno Incorrecto
**Versión 1**
``` json
    {
        "message": "Not found"
    }
```

**Version 2**
``` json
    {
        "message": "userID is not a valid ObjectID"
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
**Versión 1**
``` json
    {
        "message": "Not found"
    }
```

**Version 2**
``` json
    {
        "message": "userID is not a valid ObjectID"
    }
```

> ToDo: y hacer un timer dentro de la base de datos (10 minutos)
----
> Falta Definir
## **GET_BAR_GRAPH**
> Funcion: Obtener los valores para crear una grafica de barras en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variable>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variable:** La variable que quieren usar para sacar la gráfica.

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "labels" : [1, 2, 3, 4, 5, 6, 7],
        "datasets": [
            {
                "label": "Normal",
                "data": [20, 50, 60, 70, 80, 90, 20],
                "backgroundColor": "rgba(255, 99, 132, 0.5)"
            },
            {
                "label": "Anomalia",
                "data": [20, 50, 60, 70, 80, 90, 20],
                "backgroundColor": "rgba(53, 162, 235, 0.5)"
            }
        ]
    }
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "not found"
    }
```

----
> Falta Definir
## **GET_BUBBLE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de burbuja en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variable>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variable:** La variable que quieren usar para sacar la gráfica.

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    
```

### Objeto Retorno Incorrecto
``` json
    {
        "message": "not found"
    }
```

----
> Falta Definir
## **GET_LINE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de linea en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:variable>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**variable:** La variable que quieren usar para sacar la gráfica.

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "labels" : "labels",
        "datasets": [
            {
                "label": "Normal",  
                "data": [20,50,60,70,80,90,20],
                "borderColor": "Utils.CHART_COLORS.red",
                "backgroundColor": "rgba(255, 99, 132, 0.5)"
            },
            {
                "label": "Anomalia",
                "data": [20,50,60,70,80,90,20],
                "borderColor": "Utils.CHART_COLORS.blue",
                "backgroundColor": "rgba(53, 162, 235, 0.5)"
            }
        ]
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
> Funcion: Eliminar una grafica de acuerdo a su indice de posición

### URL: 
    /api/deleteGraph/<str:userID>/<int:graphID>/

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
        "message": "Success"
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

**Versión 3**
``` json
    {
        "message": "userID is not a valid ObjectID"
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

# Funciones tipo "Helpers"

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
            "historyID": "Archivo2022-01-04T06:00:00.000+00:00",
            "base_file_name": "Archivo",
            "date": "2022-01-04T06:00:00.000+00:00",
            "internal_attributes": [
                "PlantaPorteria_num",
                "EmpresaTransportista_num"
            ],
            "external__attributes": [
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
            "data": {
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
## **PUT_GRAPHS**
> Funcion: Actualizar las gráficas que estaba haciendo el usuario

### URL: 
    /api/putGraphs/<str:historyID>/

### Parametros: 
**historyID:** El id del una version de un archivo

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

----
# Revisión de Endpoints
### GET_HISTORY_LIST

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### GET_USER_ID

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### GET_LAST_SESSION

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### DELETE_LAST_SESSION

**Hay algún problema?** No

**Descripción del problema:** N/A

**Hay algún pendiente?** Si

**Descripción del pendiente:** Crear el trigger en MongoDB 

**Revision hecha por:** Joel Ramos

### GET_BAR_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Revisar que exista la columna en la base de datos

**Descripción del pendiente:** Falta definir el endpoint

**Revision hecha por:** Joel Ramos

### GET_BUBBLE_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Si

**Descripción del pendiente:** Falta definir el endpoint

**Revision hecha por:** Joel Ramos

### GET_AREA_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Si

**Descripción del pendiente:** Falta definir el endpoint

**Revision hecha por:** Joel Ramos

### DELETE_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### GET_HISTORY_DETAIL

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### PUT_GRAPHS

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos
