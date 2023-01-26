import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")





@st.cache()
def get_data():
    df = pd.read_csv("F:\\Divyraj\\churn-bigml-80.csv")
    return df
df = get_data()

df1 = df.groupby(by=["State", "Churn"]).size().reset_index(name="counts")
fig = px.bar(df1, x="State", y="counts", color="Churn", title="Long-Form Input", width=900, height=400)
fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
#fig.show()
st.plotly_chart(fig)
cl1, cl2 = st.columns([1,1])
df2 = df.groupby(by=["International plan", "Churn"]).size().reset_index(name="counts")
df3 = df.groupby(by=["Voice mail plan", "Churn"]).size().reset_index(name="counts")
fig1 = px.pie(df2, values='counts',names='International plan', title='Population of European continent',width=400, height=400)
fig2 = px.pie(df3, values='counts',names='Voice mail plan', title='Population of European continent1',width=400, height=400)
cl1.plotly_chart(fig1)
cl2.plotly_chart(fig2)

df4 = df.groupby(by=["State"]).size().reset_index(name="counts")
st.dataframe(df4)
fig = px.choropleth(df4, #geojson=geojson,
                            color="counts",
                            locations="State", locationmode = 'USA-states'# featureidkey="properties.district",
                            #projection="mercator"
                           )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)


