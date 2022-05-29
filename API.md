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
## **GET_HISTORY**
> Funcion: Obtener la información que estaba manejando el usuario

### URL: 
    /api/getHistory/<str:historyID>/

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

----
## **GET_BAR_GRAPH**
> Funcion: Obtener los valores para crear una grafica de barras en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:historyID>/<str:attribute>/<str:filter>/

### Parametros: 
**historyID:** El id del historial (el cual fue enviado cuando se hizo la peticion getHistoryList)

**attribute:** La variable que quieren usar para sacar la gráfica.

**filter** Filtro para separar anomalias de no anomalias

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
## **GET_LINE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de linea en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:historyID>/<str:attribute>/<str:filter>/

### Parametros: 
**historyID:** El id del historial (el cual fue enviado cuando se hizo la peticion getHistoryList)

**attribute:** La variable que quieren usar para sacar la gráfica.

**filter** Filtro para separar anomalias de no anomalias

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
> Falta Definir
## **GET_BUBBLE_GRAPH**
> Funcion: Obtener los valores para crear una grafica de burbuja en el frontend de acuerdo a la sesion del usuario y las variables que quiera usar

### URL: 
    /api/getBarGraph/<str:historyID>/<str:attribute1>/<str:attribute2>/<str:filter>/

### Parametros: 
**historyID:** El id del historial (el cual fue enviado cuando se hizo la peticion getHistoryList)

**attribute1:** La variable que representa los actores internos.

**attribute2:** La variable que representa los actores externos.

**filter** Filtro para separar anomalias de no anomalias

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
        "message": "Not found"
    }
```

----
## **GET_STATISTICS**
> Funcion: Dar estadisticas importantes al usuario

### URL: 
    /api/getStatistics/<str:historyID>/<str:filter>/

### Parametros: 
**historyID:** El id del una version de un archivo
**filter:** Filtro de las anomalias

### Bodys
``` json
N/A
```

### Objeto Retorno Correcto
``` json
    {
        "TotalAnomalys": "#",
        "AnomatyPercentage": "#",
        "AnomalyRelations": "#"
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
    /api/putGraphs/<str:historyID>/<int:graphID>/

### Parametros: 
**historyID:** El id del una version de un archivo
**graphID:** El id del una grafica

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
**Versión 1**
``` json
    {
        "message": "Not found"
    }
```

**Versión 2**
``` json
    {
        "message": "graphID not found"
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

```  

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
``` -->

----
----

# Revisión de Endpoints
### GET_HISTORY_LIST

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### GET_HISTORY

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** No

**Descripción del pendiente:** N/A

**Revision hecha por:** Joel Ramos

### GET_BAR_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Si

**Descripción del pendiente:** Ordenar Datos
**Revision hecha por:** Joel Ramos

### GET_LINE_GRAPH

**Hay algún problema?** No

**Descripción del problema:** N/A 

**Hay algún pendiente?** Si

**Descripción del pendiente:** Ordenar Datos

**Revision hecha por:** Joel Ramos

### GET_BUBBLE_GRAPH

**Hay algún problema?** Si

**Descripción del problema:** Falta hacer la función

**Hay algún pendiente?** Si

**Descripción del pendiente:** Entender como generar los datos para aplicar la grafica

**Revision hecha por:** Joel Ramos

### PUT_GRAPHS

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
