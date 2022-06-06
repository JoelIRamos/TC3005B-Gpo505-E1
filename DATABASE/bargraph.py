import pandas as pd
import numpy as np

#serie = pd.Series([1,2,3])

#serie.name = 'nombre'
#print(serie)


# obtener la lista de atributo... obtener lista de anomalias
# df = pd.DataFrame({'atributo': [......], 'anomalia': [1,-1,-1.....]})

df = pd.DataFrame({'atributo' :[1,1,1,2,2], 'anomalia': ['1','-1','1','1','-1']})
#print(pd)
# obtener los valores unicos de atributo
# ! checar desde cuando hace el sort
atributo = df['atributo'].unique()
atributoReal = np.array_str(atributo)

atributoList = atributo.tolist()

# print(type(atributo.tolist()))
# print(atributoList)
# cambiar a series para hacerlo string


# obtener total de anomalias

#anomalias = df.pivot_table( columns=['atributo', 'anomalia'], aggfunc='size')

anomalias = df.groupby(df.columns.tolist(),as_index=False).size()

# grouped = anomalias.groupby('atributo')

# attr1 = grouped.get_group(1)
# print(attr1.iloc[0][1])
# atrSize = len(atributoList)


normalList = []
anomalyList = []

for i in range(len(anomalias.columns) + 1):
    if anomalias.iloc[i][1] == "-1":
        anomalyList.append(anomalias.iloc[i][2])
    else:
        normalList.append(anomalias.iloc[i][2])
        

print(normalList)
print(anomalyList)

    




#df1 = df[df['Score'] >= 80]

data = {
    'labels' : atributoList,
    'datasets' : [
        {
            'label': 'Normal',
            'data': '########',
            'backgroundColor': 'rgba(255, 99, 132, 0.5)',
        },
        {
            'label': 'Anomalia',
            'data':  '########',
            'backgroundColor' :  'rgba(53, 162, 235, 0.5)'
        }
    ]
}

#print(data)
#print(anomalias.iloc[0][2])
#print(anomalias)

#print(anomalias['atributo'][1])
#print(anomalias['atributo'])
#import pandas as pd

# boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
#          'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle']
#         }

# df = pd.DataFrame(boxes, columns= ['Color','Shape'])

# dups_color = df.pivot_table(columns=['Color'], aggfunc='count')
# print (dups_color)