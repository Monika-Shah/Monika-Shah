import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.offline as po
import plotly.graph_objs as pg
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import hashlib

st.set_page_config(layout="wide")



# Convert Pass into hash format

User = st.sidebar.text_input("User")
Pasw = st.sidebar.text_input("Password", type='password')

@st.cache()
def get_data():
    df = pd.read_csv("F:\\Divyraj\\churn-bigml-80.csv")
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


#def main_page():
#    st.markdown("# Main page 🎈")
#    import pandas as pd
#
#
#    # Check password matches during login
#    def check_hashes(password, hashed_text):
#        if make_hashes(password) == hashed_text:
#            return hashed_text
#        return False
#
#    # DB Management
#    import sqlite3
#
#    conn = sqlite3.connect('user_data.db')
#    c = conn.cursor()
#
#    # DB Functions for create table
#    def create_usertable():
#        c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,email TEX, password TEXT)')
#
#    # Insert the data into table
#    def add_userdata(username, email, password):
#        c.execute('INSERT INTO userstable(username,email,password) VALUES (?,?,?)', (username, email, password))
#        conn.commit()
#
#    # Password and email fetch
#    def login_user(email, password):
#        c.execute('SELECT * FROM userstable WHERE email =? AND password = ?', (email, password))
#        data = c.fetchall()
#        return data
#
#    def view_all_users():
#        c.execute('SELECT * FROM userstable')
#        data = c.fetchall()
#        return data
#
#    # """Login page"""
#    st.title("welcome! ")
#    menu = ["Login", "SignUp"]
#    choice = st.selectbox("Select Login or SignUp from dropdown box ▾", menu, )
#    st.markdown(
#        "<h10 style='text-align: left; color: #ffffff;'> If you do not have an account, create an accouunt by select SignUp option from above dropdown box.</h10>",
#        unsafe_allow_html=True
#    )
#    if choice == 'Login':
#        st.write('-------')
#        st.subheader('Log in to the App')
#
#        email = st.text_input("User Name", placeholder='email')
#
#        password = st.text_input("Password", type='password')
#
#        if st.checkbox("Login"):
#            # if password == '12345':
#            # Hash password creation and store in a table
#            create_usertable()
#            hashed_pswd = make_hashes(password)
#
#            result = login_user(email, check_hashes(password, hashed_pswd))
#            if result:
#
#                st.success("Logged In as {}".format(email))
#
#                if st.success:
#                    st.subheader("User Profiles")
#                    user_result = view_all_users()
#                    clean_db = pd.DataFrame(user_result, columns=["Username", "Email", "Password"])
#                    st.dataframe(clean_db)
#
#                ab = "Yes"
#            else:
#                st.warning("Incorrect Username/Password")
#                ab = "No"
#        #abc = ab
#    elif choice == "SignUp":
#        st.write('-----')
#        st.subheader("Create New Account")
#        new_user = st.text_input("Username", placeholder='name')
#        new_user_email = st.text_input('Email id', placeholder='email')
#        new_password = st.text_input("Password", type='password')
#
#        if st.button("Signup"):
#            if new_user == '':  # if user name empty then show the warnings
#                st.warning('Inavlid user name')
#            elif new_user_email == '':  # if email empty then show the warnings
#                st.warning('Invalid email id')
#            elif new_password == '':  # if password empty then show the warnings
#                st.warning('Invalid password')
#            else:
#                create_usertable()
#                add_userdata(new_user, new_user_email, make_hashes(new_password))
#                st.success("You have successfully created a valid Account")
#                st.info("Go up and Login to you account")
#        #abc = "No"
#    #return abc
#
#def page2():
#    st.markdown("# Page 2 ❄️")
#    st.sidebar.markdown("# Page 2 ❄️")
#    st.write("it's Work")
#
#
#
#page_names_to_funcs = {
#    "Main Page": main_page,
#    "Page 2": page2,
#}
#selec_file = st.sidebar.selectbox("Select page",("Main Page", "Page 2"))
##abc = " "
#for i in ['Main Page','Page 2']:
#    page_names_to_funcs[i]()


#        pass
#    elif abc == "Yes":
#        page_names_to_funcs[selec_file]()
#    pass


#page_names_to_funcs["Page 2"]()
#abc = page_names_to_funcs["Main Page"]()
#page_names_to_funcs["Page 2"]()






