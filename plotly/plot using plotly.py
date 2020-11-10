import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

name = 'test_forces'
data_filepath = f"C:/Users/Danis/Desktop/ArAr/GAMESS/excel/{name}.csv"
df = pd.read_csv(data_filepath, encoding = 'CP1251', sep =';')

hartree2kcal = 627.5095 

df['dkcal'] = df['forces'] * hartree2kcal
# forces => dkcal

fig = px.line(df, x = 'R', y = 'dkcal', facet_col ='moleculeName', color="dft", #line_group="CCSD", 
              title = 'Delta Energies in Nobel Gases') 


indexes = []
for i in range(0, len(fig['data'])):
    if fig['data'][i]['name'] == 'CCSD':
        indexes.append(i)
print(indexes)

for i in indexes:
    fig['data'][i]['line']['color']="black"

#CCSD color => black

fig.update_xaxes(title_text='Distance, Angstrom', constraintoward = 'bottom',
                 range=[1.8,7.2],  # sets the range of xaxis
                 constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
)
fig.update_yaxes(title_text='Delta energies', showticklabels=True, matches=None) #title, черточки, yaxis отвязаны
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1])) # moleculeName=HeHe => HeHe 


yaxis1min = -0.363158573
yaxismin = [-4.032878055, -7.628714568]

        
for n in range(1,4):
    if n == 1:
        fig['layout']['yaxis']['range'] = [yaxis1min + 0.2*yaxis1min, -2*yaxis1min - 0.75*yaxis1min]
    else:
        fig['layout'][f'yaxis{n}']['range'] = [yaxismin[n-2] + 0.2*yaxismin[n-2], -2*yaxismin[n-2] - 0.75*yaxismin[n-2]]
    print(fig['layout'][f'yaxis{n}']['range'])

#scale (y(min),-2y(min))

fig.show()
fig.write_html(f"C:/Users/Danis/Desktop/ArAr/graphics/GAMESS_{name}.html")
