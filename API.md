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
``` json
    {
        "message": "found",
        "result": [
            {
                "base_file_name": "Analisis_Chatarra_Ene21-ene22",
                "versions": [
                    {
                    "_id": "Analisis_Chatarra_Ene21-ene22_2022-05-16_19-25-55",
                    "date": "2022-05-16_19-25-55"
                    },
                    {
                    "_id": "Analisis_Chatarra_Ene21-ene22_2022-05-16_19-53-41",
                    "date": "2022-05-16_19-53-41"
                    },
                    {
                    "_id": "Analisis_Chatarra_Ene21-ene22_2022-05-20_20-13-57",
                    "date": "2022-05-20_20-13-57"
                    },
                    {
                    "_id": "Analisis_Chatarra_Ene21-ene22_2022-05-20_20-18-18",
                    "date": "2022-05-20_20-18-18"
                    },
                    {
                    "_id": "Analisis_Chatarra_Ene21-ene22_2022-05-20_20-24-20",
                    "date": "2022-05-20_20-24-20"
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
            "historyID": "Analisis_Chatarra_Ene21-ene22_2022-05-20_20-13-57",
            "base_file_name": "Analisis_Chatarra_Ene21-ene22",
            "date": "2022-05-20_20-13-57",
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
                    "type": "Bar",
                    "labels": [
                        "ABASTECEDORA RIVELL SA DE CV",
                        "ABC METALES SIDERURGICOS S.A. DE C.",
                        "ACEREMEX S. A. DE C. V.",
                        "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
                        "ADN ENERGIA S DE RL DE CV",
                    ],
                    "anomalyList": [
                        85,
                        125,
                        80,
                        6,
                        1,
                    ],
                    "normalList": [
                        0,
                        0,
                        0,
                        0,
                        0
                    ]
                },
                {
                    "type": "Line",
                    "labels": [
                        "ABASTECEDORA RIVELL SA DE CV",
                        "ABC METALES SIDERURGICOS S.A. DE C.",
                        "ACEREMEX S. A. DE C. V.",
                        "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
                        "ADN ENERGIA S DE RL DE CV",
                    ],
                    "anomalyList": [
                        85,
                        125,
                        80,
                        6,
                        1,
                    ],
                    "normalList": [
                        0,
                        0,
                        0,
                        0,
                        0
                    ]
                },
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
## **GET_BAR_GRAPH**
> Funcion: Obtener los valores para crear una grafica de barras en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:attribute>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**attribute:** La variable que quieren usar para sacar la gráfica.

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "type": "Bar",
        "labels": [
            "ABASTECEDORA RIVELL SA DE CV",
            "ABC METALES SIDERURGICOS S.A. DE C.",
            "ACEREMEX S. A. DE C. V.",
            "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
            "ADN ENERGIA S DE RL DE CV"
        ],
        "anomalyList": [
            85,
            125,
            80,
            6,
            1
        ],
        "normalList": [
            0,
            0,
            0,
            0,
            0
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
## **GET_LINE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de linea en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:userID>/<str:attribute>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**attribute:** La variable que quieren usar para sacar la gráfica.

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "type": "Line",
        "labels": [
            "ABASTECEDORA RIVELL SA DE CV",
            "ABC METALES SIDERURGICOS S.A. DE C.",
            "ACEREMEX S. A. DE C. V.",
            "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
            "ADN ENERGIA S DE RL DE CV"
        ],
        "anomalyList": [
            85,
            125,
            80,
            6,
            1
        ],
        "normalList": [
            0,
            0,
            0,
            0,
            0
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
    /api/getBarGraph/<str:userID>/<str:attribute>/

### Parametros: 
**userID:** El id del usuario (el cual fue generado cuando se hizo la peticion getUserID)

**attribute:** La variable que quieren usar para sacar la gráfica.

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

# Funciones de Ayuda para Testing
> No son Endpoints Oficiales, se desactivaran antes del despliegue
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
            "historyID": "Analisis_Chatarra_Ene21-ene22_2022-05-20_20-13-57",
            "base_file_name": "Analisis_Chatarra_Ene21-ene22",
            "date": "2022-05-20_20-13-57",
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
                    "type": "Bar",
                    "labels": [
                        "ABASTECEDORA RIVELL SA DE CV",
                        "ABC METALES SIDERURGICOS S.A. DE C.",
                        "ACEREMEX S. A. DE C. V.",
                        "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
                        "ADN ENERGIA S DE RL DE CV",
                    ],
                    "anomalyList": [
                        85,
                        125,
                        80,
                        6,
                        1,
                    ],
                    "normalList": [
                        0,
                        0,
                        0,
                        0,
                        0
                    ]
                },
                {
                    "type": "Line",
                    "labels": [
                        "ABASTECEDORA RIVELL SA DE CV",
                        "ABC METALES SIDERURGICOS S.A. DE C.",
                        "ACEREMEX S. A. DE C. V.",
                        "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
                        "ADN ENERGIA S DE RL DE CV",
                    ],
                    "anomalyList": [
                        85,
                        125,
                        80,
                        6,
                        1,
                    ],
                    "normalList": [
                        0,
                        0,
                        0,
                        0,
                        0
                    ]
                },
            ]
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
        "type": "Line",
        "labels": [
            "ABASTECEDORA RIVELL SA DE CV",
            "ABC METALES SIDERURGICOS S.A. DE C.",
            "ACEREMEX S. A. DE C. V.",
            "ACEROS Y TRANSPORTES ELLA S.A DE C.V",
            "ADN ENERGIA S DE RL DE CV"
        ],
        "anomalyList": [
            85,
            125,
            80,
            6,
            1
        ],
        "normalList": [
            0,
            0,
            0,
            0,
            0
        ]
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

**Hay algún pendiente?** Si

**Descripción del pendiente:** Añadir el tipo de grafica

**Revision hecha por:** Joel Ramos

### GET_LINE_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Si

**Descripción del pendiente:** Añadir el tipo de grafica

**Revision hecha por:** Joel Ramos

### GET_BUBBLE_GRAPH

**Hay algún problema?** Si

**Descripción del problema:** Falta hacer la función

**Hay algún pendiente?** Si

**Descripción del pendiente:** Entender como generar los datos para aplicar la grafica

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
