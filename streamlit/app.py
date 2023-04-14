import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np # linear algebra
import plotly.offline as py 


# loading gapminder dataset from plotly 
gapminder = px.data.gapminder()

st.write("# Study of GDP & Life Expectancy ")

st.header("Input plotly data:")
st.write(gapminder)
#fetch all unique dates
years = gapminder['year'].unique().tolist()
years_select = st.selectbox('Select year for data',years,0)

country = gapminder['country'].unique().tolist()
country_select = st.selectbox('Select country',country,0)
country_data = gapminder[gapminder['country']==country_select]
fig1 = px.bar(country_data, x='year', y='gdpPercap',labels={'gdpPercap': 'GDP per capital'}, height=400)
fig1.update_layout(width=700)
st.write(fig1)

fig5 = px.bar(country_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of '+ country_select},
             height=400, template='seaborn')
#fig5.show()
fig5.update_layout(width=700)
st.write(fig5)

fig6 = px.bar(country_data, x='pop', y='gdpPercap', color='lifeExp', labels={'gdpPercap': 'GDP per capital','pop': 'Population of '+ country_select}, height=400,template='plotly_dark')
st.write(fig6)

 


df = gapminder[gapminder['year']==years_select]
# color by continent 
fig2 = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[10,100000],range_y=[25,90])
fig2.update_layout(width=700)
#fig.show() displays on another tab
st.write(fig2)

fig3 = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[10,100000],range_y=[25,90],animation_frame='year',animation_group='country')
fig3.update_layout(width=700)
st.write(fig3)

# choropleth map
fig4 = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', 
                    animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig4.update_layout(width=700)   
st.write(fig4) 



