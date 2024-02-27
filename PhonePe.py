import os
import json
import pandas as pd
import psycopg2
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

#aggre_trans
path1 = "D:/New folder/Phonepe/Pulse/data/aggregated/transaction/country/india/state/"
agg_trans_list = os.listdir(path1)
Transaction_details = {"State":[], "Year":[], "Quarter":[], "Transaction_name":[], "Transaction_count":[], "Transaction_amount":[]}
for state in agg_trans_list:
    cur_state = path1+state+"/"
    agg_year_list = os.listdir(cur_state)
    for year in agg_year_list:
        cur_year = cur_state+year+"/"
        agg_file_list = os.listdir(cur_year)
        for file in agg_file_list:
            cur_file = cur_year+file
            data = open(cur_file, "r")
            A1 = json.load(data)
            #print(A1)
            for i in A1["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                Transaction_details["Transaction_name"].append(name)
                Transaction_details["Transaction_count"].append(count)
                Transaction_details["Transaction_amount"].append(amount)
                Transaction_details["Quarter"].append(int(file.strip(".json")))
                Transaction_details["State"].append(state)
                Transaction_details["Year"].append(year)
            aggre_transaction = pd.DataFrame(Transaction_details, columns = ("State", "Year","Quarter","Transaction_name","Transaction_count","Transaction_amount"))
            #change_state_names(aggre_transaction)
            #print(aggre_transaction.head())
            
### aggre_users
path2 = "D:/New folder/Phonepe/Pulse/data/aggregated/user/country/india/state/"
agg_users_list = os.listdir(path2)
aggregation_users = {"State":[], "Year":[], "Quarter":[], "Brand":[], "Count":[], "Percentage":[]}
for state in agg_users_list:
    cur_state = path2+state+"/"
    agg_year_list = os.listdir(cur_state)
    for year in agg_year_list:
        cur_year = cur_state+year+"/"
        agg_file_list = os.listdir(cur_year)
        for file in agg_file_list:
            cur_file = cur_year+file
            data = open(cur_file, "r")
            B = json.load(data)
            #print(B)
            try:
                for i in B["data"]["usersByDevice"]:
                    brand = i["brand"]
                    count = i["count"]
                    per = i["percentage"]
                    aggregation_users["Brand"].append(brand)
                    aggregation_users["Count"].append(count)
                    aggregation_users["Percentage"].append(per)
                    aggregation_users["Quarter"].append(int(file.strip(".json")))
                    aggregation_users["State"].append(state)
                    aggregation_users["Year"].append(year)
                aggre_users = pd.DataFrame(aggregation_users, columns = ("State", "Year","Quarter","Count","Percentage","Brand"))
                #change_state_names(aggre_users)
            except:
               pass

###map_trans
path3 = "D:/New folder/Phonepe/Pulse/data/map/transaction/hover/country/india/state/"
map_trans = os.listdir(path3)
map_details = {"State":[], "Year":[], "Quarter":[], "District":[], "Transaction_count":[], "Transaction_amount":[]}
for state in map_trans:
    cur_state = path3+state+"/"
    map_cur_state = os.listdir(cur_state)
    for year in map_cur_state:
        cur_year = cur_state+year+"/"
        map_cur_year = os.listdir(cur_year)
        for file in map_cur_year:
            cur_file = cur_year+file
            data = open(cur_file,"r")            
            C = json.load(data)
            #print(A)
            for i in C["data"]["hoverDataList"]:
                name = i["name"]
                #type = i["metric"][0]["type"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                map_details["District"].append(name)
                map_details["Transaction_amount"].append(amount)
                map_details["Transaction_count"].append(count)
                map_details["State"].append(state)
                map_details["Year"].append(year)
                map_details["Quarter"].append(int(file.strip(".json")))
            map_data = pd.DataFrame(map_details, columns = ("State", "Year","Quarter","Transaction_amount","Transaction_count","District"))
            map_data['District'] = map_data['District'].str.title()
            #change_state_names(map_data)
            
### map_users
path4 ="D:/New folder/Phonepe/Pulse/data/map/user/hover/country/india/state/"
map_users = os.listdir(path4)
map_details_2 = {"State":[], "Year":[], "Quarter":[], "District":[], "Users":[], "App_openers":[]}
for state in map_users:
    cur_state = path4+state+"/"
    map_cur_state = os.listdir(cur_state)
    for year in map_cur_state:
        cur_year = cur_state+year+"/"
        map_cur_year = os.listdir(cur_year)
        for file in map_cur_year:
            cur_file = cur_year+file
            data = open(cur_file, "r")
            D = json.load(data)
            for i in D["data"]["hoverData"].items():
                district = i[0]
                user = i[1]["registeredUsers"]
                appopeners = i[1]["appOpens"]
                map_details_2["District"].append(district)
                map_details_2["Users"].append(user)
                map_details_2["App_openers"].append(appopeners)
                map_details_2["State"].append(state)
                map_details_2["Year"].append(year)
                map_details_2["Quarter"].append(int(file.strip(".json")))
            map_data_2 = pd.DataFrame(map_details_2, columns = ("State", "Year","Quarter","App_openers","Users","District"))
            map_data_2['District'] = map_data_2['District'].str.title()
            #change_state_names(map_data_2)
            #print(map_data_2.head())
###top_transaction
path5 = "D:/New folder/Phonepe/Pulse/data/top/transaction/country/india/state/"
top_trans = os.listdir(path5)
top_details = {"State":[], "Year":[], "Quarter":[],"Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}
for state in top_trans:
    cur_state = path5+state+"/"
    top_cur_state = os.listdir(cur_state)
    for year in top_cur_state:
        cur_year = cur_state+year+"/"
        top_cur_year = os.listdir(cur_year)
        for file in top_cur_year:
            cur_file = cur_year+file
            data = open(cur_file, "r")
            E = json.load(data)
            for i in E["data"]["pincodes"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                top_details["Pincodes"].append(name)
                top_details["Transaction_count"].append(count)
                top_details["Transaction_amount"].append(amount)
                top_details["State"].append(state)
                top_details["Year"].append(year)
                top_details["Quarter"].append(int(file.strip(".json")))
            top_data = pd.DataFrame(top_details, columns = ("State", "Year","Quarter","Pincodes","Transaction_count","Transaction_amount"))
            #change_state_names(top_data)
             
## top_users
path6 = "D:/New folder/Phonepe/Pulse/data/top/user/country/india/state/"
top_users = os.listdir(path6)
top_details_2 = {"State":[], "Year":[], "Quarter":[],"RegisteredUsers":[],"Pincodes":[]}
for state in top_users:
    cur_state = path6+state+"/"
    top_cur_state = os.listdir(cur_state)
    for year in top_cur_state:
        cur_year = cur_state+year+"/"
        top_cur_year = os.listdir(cur_year)
        for file in top_cur_year:
            cur_file = cur_year+file
            data = open(cur_file,"r")
            F = json.load(data)
            #print(F)
            for i in F["data"]["pincodes"]:
                name  = i["name"]
                users = i["registeredUsers"]
                top_details_2["Pincodes"].append(name)
                top_details_2["RegisteredUsers"].append(users)
                top_details_2["State"].append(state)
                top_details_2["Year"].append(year)
                top_details_2["Quarter"].append(int(file.strip(".json")))
            top_data_1 = pd.DataFrame(top_details_2, columns = ("State", "Year","Quarter","RegisteredUsers","Pincodes"))        
            ##change_state_names(top_data_1)
            #print(top_data_1.head())
            
## replacing the state_names
def change_state_names(x):
    x['State'] = x['State'].str.title()
    x['State'] = x['State'].str.replace("-"," ")
    x['State'] = x['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")
    x['State'] = x['State'].str.replace("Jammu & Kashmir","Jammu and Kashmir")
    x['State'] = x['State'].str.replace("Andaman & Nicobar Islands","Andaman and Nicobar Islands")
    #print(x['State'].unique())

## connection to sql Database
database = psycopg2.connect(host = "localhost",
                            user = "postgres",
                            database = "PhonePe",
                            password  = "Faizal@2003",
                            port = "5432")
cursor = database.cursor()
database.commit()
drop_query_1 ='''drop table if exists aggregation_transaction'''
cursor.execute(drop_query_1)
#try:
create_query_1 = '''create table if not exists aggregation_transaction(State varchar(80),
                                                                Year int,
                                                                Quarter int, 
                                                                Transaction_name varchar(80), 
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''

cursor.execute(create_query_1)
database.commit()

#except:
 #   print("channel already created.....")
for index,row in aggre_transaction.iterrows():
    insert_query_1  = '''insert into aggregation_transaction(State, Year, Quarter, Transaction_name, Transaction_count, Transaction_amount)
                        values(%s,%s,%s,%s,%s,%s)'''
    values_1 = (row["State"], row["Year"], row["Quarter"], row["Transaction_name"], row["Transaction_count"], row["Transaction_amount"])
    cursor.execute(insert_query_1, values_1)
    database.commit()
cursor = database.cursor()

drop_query_2 = '''drop table if exists aggregation_users'''
cursor.execute(drop_query_2)
create_query_2 = '''create table if not exists aggregation_users(State varchar(80),
                                                                Year int,
                                                                Quarter int,
                                                                Brand varchar(80),
                                                                Count bigint,
                                                                Percentage float)'''
cursor.execute(create_query_2)
database.commit()

for index, row in aggre_users.iterrows():
    insert_query_2 = '''insert into aggregation_users(State, Year, Quarter, Brand, Count, Percentage)
                        values(%s,%s,%s,%s,%s,%s)'''
    values_2 = (row["State"], row["Year"], row["Quarter"], row["Brand"], row["Count"], row["Percentage"])
    cursor.execute(insert_query_2, values_2)
    database.commit()

drop_query_3 = '''drop table if exists map_transactions'''
cursor.execute(drop_query_3)
create_query_3 = '''create table if not exists map_transactions(State varchar(80),
                                                                Year int,
                                                                Quarter int,
                                                                District varchar(80),
                                                                Transaction_count int,
                                                                Transaction_amount float)'''
cursor.execute(create_query_3)
database.commit()
for index, row in map_data.iterrows():
    insert_query_3 = '''insert into map_transactions(State, Year, Quarter, District, Transaction_count, Transaction_amount)
                    values(%s,%s,%s,%s,%s,%s)'''
    values_3 = (row["State"], row["Year"], row["Quarter"], row["District"], row["Transaction_count"], row["Transaction_amount"])  
    cursor.execute(insert_query_3, values_3)
    database.commit()
drop_query_4 = '''drop table if exists map_users'''
cursor.execute(drop_query_4)

create_query_4 = '''create table if not exists map_users(State varchar(80),
                                                         Year int,
                                                         Quarter int,
                                                         District varchar(80),
                                                         Users bigint,
                                                         App_openers bigint)'''

cursor.execute(create_query_4)
database.commit()
for index, row in map_data_2.iterrows():
    insert_query_4 = '''insert into map_users(State, Year, Quarter, District, Users, App_openers)
                    values(%s,%s,%s,%s,%s,%s)'''
    values_4 = (row["State"], row["Year"], row["Quarter"], row["District"], row["Users"], row["App_openers"])
    cursor.execute(insert_query_4, values_4)
    database.commit()
    
drop_query_5 = '''drop table if exists top_transactions'''
cursor.execute(drop_query_5)
create_query_5 = '''create table if not exists top_transactions(State varchar(90),
                                                                Year int,
                                                                Quarter int,
                                                                Pincodes bigint,
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
cursor.execute(create_query_5)
database.commit()
for index, row in top_data.iterrows():
    insert_query_5 = '''insert into top_transactions(State, Year, Quarter, Pincodes, Transaction_count, Transaction_amount)
                    values(%s,%s,%s,%s,%s,%s)'''
    values_5 = (row['State'],row['Year'],row['Quarter'], row["Pincodes"], row["Transaction_count"], row["Transaction_amount"])
    cursor.execute(insert_query_5, values_5)
    database.commit()

drop_query_6 = '''drop table if exists top_users'''
cursor.execute(drop_query_6)
create_query_6 = '''create table if not exists top_users(State varchar(90), Year int, Quarter int, Pincodes bigint, RegisteredUsers bigint)'''
cursor.execute(create_query_6)
database.commit()
for index, row in top_data_1.iterrows():
    insert_query_6 = '''insert into top_users(State, Year, Quarter, Pincodes, RegisteredUsers) values (%s,%s,%s,%s,%s)'''
    values_6 = (row['State'],row["Year"], row["Quarter"], row['Pincodes'], row['RegisteredUsers'])
    cursor.execute(insert_query_6, values_6)
    database.commit()
    
    
# Setting up page configuration
icon = Image.open(r"D:\\New folder\\Phonepe\\download.png")
st.set_page_config(page_title= "PHONEPE DATA VISUALIZATION AND EXPLORATION | By Mohammed Faizal N",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Mohammed Faizal N*!
                                        Data has been cloned from Phonepe Pulse Github Repo"""})

st.sidebar.header(":wave: :violet[**Hello! Welcome to the dashboard**]")

# Creating option menu in the side bar
with st.sidebar:
    selected = option_menu("Menu", ["HOME","TOP CHARTS","EXPLORE DATA","ABOUT"], 
                icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
# MENU 1 - HOME
if selected == "HOME":
    st.markdown("# :violet[Data Visualization and Exploration]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")

    st.write(" ")
    st.write(" ")
    st.markdown("### :violet[Domain :] Fintech")
    st.markdown("### :violet[Technologies used :] Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.")
    st.markdown("### :violet[Overview :] In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.")
    

# MENU 2 - TOP CHARTS
if selected == "TOP CHARTS":
    st.markdown("## :violet[TOP CHARTS]")
    with st.sidebar:
        Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
        col1, col2= st.columns(2)
    with col1:
        Year = st.slider("**Year**", min_value=2018, max_value=2022)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with col2:
         st.info(
                 """
                 #### From this menu we can get insights like :
                 - Overall ranking on a particular Year and Quarter.
                 - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                 - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                 - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                 """,icon="🔍"
                 )
        
# Top Charts - TRANSACTIONS    
    if Type == "Transactions":
        col1,col2,col3= st.columns([1,1,1], gap="medium")
        
        with col1:
            st.markdown("### :violet[State]")
            cursor.execute(f"select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from aggregation_transaction where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            cursor.execute(f"select district , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transactions where year = {Year} and quarter = {Quarter} group by district order by Total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                             names='District',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        with col3:
            st.markdown("### :violet[Pincodes]")
            cursor.execute(f"select Pincodes, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total_Amount from top_transactions where year = {Year} and quarter = {Quarter} group by Pincodes order by Total_Amount desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincodes','Transaction_Count' 'Total_Amount'])
            fig = px.pie(df,
                         values='Total_Amount',
                         names='Pincodes',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Transaction_Count'],
                         labels = {'Transactions_count:Transaction_count'})   
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
# Top Charts - USERS          
    if Type == "Users":
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")
        
        with col1:
            st.markdown("### :violet[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                cursor.execute(f"select brands, sum(count) as Total_Count, avg(percentage)*100 as Avg_Percentage from aggregation_users where year = {Year} and quarter = {Quarter} group by brands order by Total_Count desc limit 10")
                df = pd.DataFrame(cursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.bar(df,
                             title='Top 10',
                             x="Total_Users",
                             y="Brand",
                             orientation='h',
                             color='Avg_Percentage',
                             color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   
    
        with col2:
            st.markdown("### :violet[District]")
            cursor.execute(f"select district, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} group by district order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                         title='Top 10',
                         x="Total_Users",
                         y="District",
                         orientation='h',
                         color='Total_Users',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :violet[Pincodes]")
            cursor.execute(f"select Pincodes, sum(RegisteredUsers) as Total_Users from top_users where year = {Year} and quarter = {Quarter} group by Pincodes order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincodes', 'Total_Users'])
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincodes',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :violet[State]")
            cursor.execute(f"select state, sum(Registereduser) as Total_Users, sum(AppOpens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} group by state order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Appopens'],
                             labels={'Total_Appopens':'Total_Appopens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
# MENU 3 - EXPLORE DATA
if selected == "EXPLORE DATA":
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    col1,col2 = st.columns(2)
    
# EXPLORE DATA - TRANSACTIONS
    if Type == "Transactions":
        
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            st.markdown("## :violet[Overall State Data - Transactions Amount]")
            cursor.execute(f"select state, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transactions where year = {Year} and quarter = {Quarter} group by state order by state")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv(r"D:\\New folder\\Phonepe\\Book1.csv")
            df1.State = df2

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_amount',
                      color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            
        # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
        with col2:
            
            st.markdown("## :violet[Overall State Data - Transactions Count]")
            cursor.execute(f"select state, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transactions where year = {Year} and quarter = {Quarter} group by state order by state")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv(r'D:\\New folder\\Phonepe\\Book1.csv')
            df1.Total_Transactions = df1.Total_Transactions.astype(int)
            df1.State = df2

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_Transactions',
                      color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            
                        
# BAR CHART - TOP PAYMENT TYPE
        st.markdown("## :violet[Top Payment Type]")
        cursor.execute(f"select Transaction_name, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from aggregation_transaction where year= {Year} and Quarter = {Quarter} group by transaction_name order by Transaction_name")
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

        fig = px.bar(df,
                     title='Transaction Types vs Total_Transactions',
                     x="Transaction_type",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=False)
        
# BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                             ('Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                              'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                              'Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                              'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                              'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                              'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
         
        cursor.execute(f"select State, District,year,quarter, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transactions where year = {Year} and quarter = {Quarter} and State = '{selected_state}' group by State, District,year,quarter order by state,district")
        
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State','District','Year','Quarter',
                                                         'Total_Transactions','Total_amount'])
        fig = px.bar(df1,
                     title=selected_state,
                     x="District",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)
        
# EXPLORE DATA - USERS      
    if Type == "Users":
        
        # Overall State Data - TOTAL APPOPENS - INDIA MAP
        st.markdown("## :violet[Overall State Data - User App opening frequency]")
        cursor.execute(f"select state, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} group by state order by state")
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
        df2 = pd.read_csv(r'D:\\New folder\\Phonepe\\Book1.csv')
        df1.Total_Appopens = df1.Total_Appopens.astype(float)
        df1.State = df2
        
        # BAR CHART TOTAL USERS - DISTRICT WISE DATA 
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                              ('Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                              'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                              'Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                              'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                              'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                              'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
        
        cursor.execute(f"select State,year,quarter,District,sum(Registereduser) as Total_Users, sum(AppOpens) as Total_Appopens from map_users where year = {Year} and quarter = {Quarter} and state = '{selected_state}' group by State, District,year,quarter order by state,district")
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Year', 'Quarter', 'District', 'Total_Users','Total_Appopens'])
        df.Total_Users = df.Total_Users.astype(int)
        
        fig = px.bar(df,
                     title=selected_state,
                     x="District",
                     y="Total_Users",
                     orientation='v',
                     color='Total_Users',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

    
# MENU 4 - ABOUT
if selected == "ABOUT":
   # col1,col2 = st.columns([3,3],gap="medium")
    #with col1:
    st.write(" ")
    st.write(" ")
    st.markdown("### :violet[About PhonePe Pulse:] ")
    st.write("##### BENGALURU, India, On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")
    
    st.write("##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")
    
    st.markdown("### :violet[About PhonePe:] ")
    st.write("##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")
    
    st.write("**:violet[My Project GitHub link]** ⬇️")
    st.write("")
    st.write("**:violet[Image and content source]** ⬇️")
    st.write("https://www.prnewswire.com/in/news-releases/phonepe-launches-the-pulse-of-digital-payments-india-s-first-interactive-geospatial-website-888262738.html")
