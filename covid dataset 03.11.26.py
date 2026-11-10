import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly # same as matplotlib but with higher graphical standards
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

covid_dataset = 'data science folder\\covid_data.csv'
data = pd.read_csv(covid_dataset)
print(f'\n Covid Data columns: \n {data.columns} \n')

# selecting specific sets of columns from the original dataset
data = data[["Province_State", "Country_Region", 'Last_Update', 
             'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths',
       'Active']]

#renaming columns

data.columns = ('state','Country','lastUpdate', 'Lat','Long', 'Confirmed',
                'Recovered','Deaths', 'Active')

print(f'covid dataset after renaming columns: \n')
print(f'\n{data.head} \n')

data['state'].fillna(value = '',inplace = True) 
'''fillna (value) - will fill any missing value (NaN)
in this "State" column with an empty string ('')
'''

#top ten most effected countries
top10_confirmed = pd.DataFrame(data.groupby("Country")['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
print(f'\ntop 10 confirmed most affected countries: \n {top10_confirmed}\n countries \n')

print(f'\n top ten countries:\n {top10_confirmed.index} \n')

#creating plotly, express scatter plot
figure1 = px.scatter(top10_confirmed,x=top10_confirmed.index,
                     y="Confirmed",size="Confirmed",size_max = 120,
                     color = top10_confirmed.index,
                     title= "Top 10 countries by confimred cases")
figure1.write_html("Fig1.html",auto_open=True)

#top 10 countries with the highest number of deaths

top10_deaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest().sort_values(ascending=False))
print(f'\n top 10 countries with highest death toll: \n {top10_deaths}\n')




