import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")



User = st.sidebar.text_input("User")
Pasw = st.sidebar.text_input("Password", type='password')

@st.cache()
def get_data():
    df = pd.read_csv("churn-bigml-80.csv")
    return df
df = get_data()



if User == "Draj":
    if Pasw == "123":
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

        data = dict(type = 'choropleth',locations = df1['State'],  locationmode = 'USA-states', z = df1['counts'])
        layout = dict(geo = {'scope':'usa'})
        #   fig4 = go.Scattergeo(locations= df1['State'], locationmode = 'USA-states',)
        #   fig3 = px.scatter_geo(locations= df1['State'], locationmode = 'USA-states')
        #   st.plotly_chart(fig4)
        #   #x = pg.Figure(data = [data] ,layout = layout)
        #po.iplot(x)

        #df = px.data.election()
        #geojson = px.data.election_geojson()
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
