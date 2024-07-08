import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd

import plotly_express as px
import plotly.figure_factory as ff

df=pd.read_json("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/price.json")
df2=pd.read_json("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/availability.json")
df3=pd.read_json("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/fortrends.json")
df4=pd.read_json("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/filtereddata.json")

#rate of total availability utilized.
def rate(a,b,c):
    df60=a[b==c]
    rate60=((len(df60["avail_60"])/5555)*100)
    rate60=round(rate60,2)
    return rate60,len(df60["avail_60"])

#Streamlit
st.set_page_config(page_title="Airbnb",
                   page_icon=":ab:",
                   layout="wide")

selected = option_menu(None, ["Home", 'Analysis','Key Insights'], 
           icons=['house', 'activity'], menu_icon="cast", default_index=1,
           orientation="horizontal")

if selected=="Home":
    st.image("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/airbnblogo.png")
    st.image("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/airbnb1.png")
    st.markdown("---")

    #About
    st.title("Industry: :orange[*Lodging*]")
    st.markdown('''### Airbnb, Inc. (AIR-BEE-en-BEE) is an American company operating an online marketplace for short and long term "Homestays" and "Experiences".''')
    st.markdown('''####  👉  The company acts as a broker and charges a commission from each booking.''')
    st.markdown('''####  👉  Airbnb is a shortened version of its original name, ⭐ AirBedandBreakfast.com 🎉.''')
    st.markdown('''####  👉  Airbnb is the most well known company for short term housing rentals.''')
    st.markdown('''####  👉  The company was founded in 2008 by''')
    st.image("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/airbnb2.png")

    #Story
    st.title("Story:")
    st.write('''After moving to San Francisco in October 2007, roommates and former schoolmates Brian Chesky and Joe Gebbia came up with an idea of putting an air mattress in their living room and turning it into a bed and breakfast.
              In February 2008, Nathan Blecharczyk, Chesky's former roommate, joined as the chief technology officer and the third co-founder of the new venture, which they named AirBed & Breakfast.
              They put together a website that offered short-term living quarters and breakfast for those who were unable to book a hotel in the saturated market. The site Airbedandbreakfast.com officially launched on August 11, 2008.
              The founders had their first customers in the summer of 2008, during the Industrial Design Conference held by Industrial Designers Society of America, where travelers had a hard time finding lodging in the city.''')
    st.write("")
    st.write("In March 2009, the name of the company was shortened to Airbnb.com to eliminate confusion over air mattresses...")
    st.write("")
    st.write("At the March 2011 South by Southwest conference, Airbnb won the **app** award...")
    st.write("")

    #Lanches
    st.markdown("### New Launches")
    tl5,tl6=st.columns([1,4])
    with tl6:
        st.markdown("#### 🚩 In November 2012, Airbnb launched ⭐ Neighborhoods ⭐, a travel guide of 23 cities that helps travelers choose a neighborhood in which to stay based on certain criteria and personal preferences.")
        st.markdown("#### 🚩 In November 2016, Airbnb launched ⭐ Experiences ⭐, whereby users can use the platform to book activities...")

    #Guests and hosts
    st.title("Key Features and Benefits for Users (Guests and Hosts)")
    st.markdown("### :blue[Guests:]")
    tl1,tl2=st.columns([1,4])
    with tl2:
        st.markdown("#### ✅ Diverse accommodation options: Apartments, houses, unique spaces etc...,")
        st.markdown("#### ✅ Flexible booking: Short-term or extended stays,")
        st.markdown("#### ✅ Immersive travel experiences: Feel like a local, connect with the community,")
        st.markdown("#### ✅ Potential cost savings compared to traditional hotels,")
        st.markdown("#### ✅ Reviews and ratings for informed decision-making....& much more.")
    st.write("")

    st.markdown("### :blue[Hosts:]")
    tl3,tl4=st.columns([1,4])
    with tl4:
        st.markdown("#### ✅ Generate income by sharing underutilized spaces,")
        st.markdown("#### ✅ Flexible scheduling and pricing control,")
        st.markdown("#### ✅ Opportunity to connect with travelers and showcase their property...& much more")
        st.write("")

    st.write("")
    st.image("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/airbnb3.png")
    st.image("https://raw.githubusercontent.com/HRLeo19/Airbnb/main/map.png")

if selected=="Analysis":

    tab1,tab2,tab3=st.tabs(["Price Variance","Availability Patterns","Location Based Ratings"])
    with tab1:
        with st.sidebar:
            st.title("Price Variance")
        Country=st.sidebar.multiselect("Select the country:",options=df["country"].unique(),default=df["country"].unique())
        Market=st.sidebar.multiselect("Select Market:",options=df["market"].unique(),default=df["market"].unique())
        Propertytype=st.sidebar.multiselect("Select Property:",options=df["property_type"].unique(),default=df["property_type"].unique())
        Roomtype=st.sidebar.multiselect("Select Room Type:",options=df["room_type"].unique(),default=df["room_type"].unique())
        bedtype=st.sidebar.multiselect("Select Bedtype:",options=df["bed_type"].unique(),default=df["bed_type"].unique())
       
    
        filtered_df = df[df['country'].isin(Country) & df['room_type'].isin(Roomtype) & df['property_type'].isin(Propertytype) & 
                         df['bed_type'].isin(bedtype) & df["market"].isin(Market)]

        col1,col2=st.columns(2)
        with col1: #country
            pp=filtered_df.groupby("country")[["monthly_price","weekly_price","cleaning_fee","security_deposit"]].mean()
            pp.reset_index(inplace=True)
            fig1 = px.bar(pp,x="country",y=["monthly_price","weekly_price","security_deposit","cleaning_fee"],title="Price variance by Country",color_discrete_sequence=px.colors.sequential.Rainbow,
                          text_auto=True)
            st.plotly_chart(fig1)

            #bedtype
            bt=pd.DataFrame(filtered_df.groupby("bed_type")["price"].mean())
            bt.reset_index(inplace=True)
            fig4 = px.bar(bt,x="bed_type",y="price",hover_name="price",title="Price variance by Bedtype",color_discrete_sequence=px.colors.sequential.Cividis,
                          height=600)
            st.plotly_chart(fig4)

        with col2:#Room type
            rt=pd.DataFrame(filtered_df.groupby("room_type")["price"].mean())
            rt.reset_index(inplace=True)
            fig2 = px.bar(rt,x="room_type",y="price",hover_name="price",title="Price variance by Room Type",color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig2)

            #Property type
            pt=pd.DataFrame(filtered_df.groupby("property_type")["price"].mean())
            pt.reset_index(inplace=True)
            fig3 = px.bar(pt,x="property_type",y="price",hover_name="price",title="Price variance by Property",color_discrete_sequence=px.colors.sequential.Sunsetdark_r,
                          height=600)
            st.plotly_chart(fig3)
        
        mk=pd.DataFrame(filtered_df.groupby("market")["price"].mean())
        mk.reset_index(inplace=True)
        fig5 = px.bar(mk,x="price",y="market",hover_name="price",title="Price variance by Market",color_discrete_sequence=px.colors.sequential.deep_r,
                      height=700)
        st.plotly_chart(fig5)

    with tab2:
        with st.sidebar:
            st.title("Availability Patterns")

        Market2=st.sidebar.multiselect("Market:",options=df2["market"].unique(),default=df2["market"].unique())
        Roomtype2=st.sidebar.multiselect("Roomtype:",options=df2["room_type"].unique(),default=df2["room_type"].unique())
        Propertytype2=st.sidebar.multiselect("Property",options=df2["property_type"].unique(),default=df2["property_type"].unique())

        filtered_df2=df2[df2["market"].isin(Market2) & df2["room_type"].isin(Roomtype2) & 
                         df2["property_type"].isin(Propertytype2)]


        avrate=filtered_df2.groupby("property_type")[["minimum_nights","maximum_nights","accommodates","bedrooms","extra_people","guests_included",
                                                "avail_30","avail_60","avail_90","avail_365","accuracy","cleanliness","location","value","rating"]].mean().round()
        avrate.reset_index(inplace=True)

        co1,co2=st.columns(2)
        with co1:#minium Nights
            fig6 = px.bar(avrate, x="property_type", y='minimum_nights',title="Minium Nights Available",
                          color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig6)

            #avail_365
            fig7=px.pie(avrate,values="avail_365",names="property_type",title=f"Availability 365 by Property ",
                        color_discrete_sequence=px.colors.sequential.YlOrRd_r,hole=0.5)
            st.plotly_chart(fig7)

            #avail_60
            fig14=px.pie(avrate,values="avail_60",names="property_type",title=f"Availability 60 by Property ",
                        color_discrete_sequence=px.colors.sequential.YlOrRd_r,hole=0.5)
            st.plotly_chart(fig14)

        with co2:
            #max nights
            fig15 = px.bar(avrate, x="property_type", y='maximum_nights',title="Maximum Nights Available",
                          color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(fig15)

            #avail_90
            fig13=px.pie(avrate,values="avail_90",names="property_type",title=f"Availability 90 by Property ",
                        color_discrete_sequence=px.colors.sequential.YlOrRd_r,hole=0.5)
            st.plotly_chart(fig13)

            #avail_30
            fig7=px.pie(avrate,values="avail_30",names="property_type",title=f"Availability 30 by Property ",
                        color_discrete_sequence=px.colors.sequential.YlOrRd_r,hole=0.5)
            st.plotly_chart(fig7)

        #Acc,Guest,XTrappl
        fig8=px.line(avrate,x="property_type",y=["accommodates","extra_people","guests_included"],height=700,
                     hover_name="_value",text="bedrooms",title="Accommodates,Extra people & Guests Included by Property")
        st.plotly_chart(fig8)  

    with tab3:
        st.sidebar.title("Location")
        Country3=st.sidebar.multiselect("Country",df3["country"].unique(),default=df3["country"].unique())
        Market3=st.sidebar.multiselect("Market",df3["market"].unique(),default=df3["market"].unique())

        filtered_df3=df3[df3["country"].isin(Country3)]
        filtered_df4= df3[df3["market"].isin(Market3)]

        cougby=filtered_df3.groupby("country")[["number_of_reviews","accuracy","cleanliness","checkin",
                                                "communication","location","value","rating"]].mean().round(1)
        cougby.reset_index(inplace=True)

        margby=filtered_df4.groupby("market")[["number_of_reviews","accuracy","cleanliness","checkin",
                                        "communication","location","value","rating"]].mean().round(1)
        margby.reset_index(inplace=True)

        #Country
        fig9=px.line(cougby,x="country",y=["accuracy","cleanliness","checkin","communication","location","value"],
                     text="number_of_reviews",title="Different Ratings by Country")
        st.plotly_chart(fig9)
        with st.expander("Summary Ratings by Countries"):
            df3_sample=cougby[:][["country","number_of_reviews","accuracy","cleanliness","checkin","communication",
                                  "location","value","rating"]]
            fig10=ff.create_table(df3_sample,colorscale="YlOrRd_r")
            st.plotly_chart(fig10)
        
        st.markdown("---")
        st.markdown("---")

        #Market
        fig11=px.line(margby,x="market",y=["accuracy","cleanliness","checkin","communication","location","value"],
                     text="number_of_reviews",title="Different Ratings by Markets")
        st.plotly_chart(fig11)

        with st.expander("Summary Ratings by Markets"):
            df3_sample2=margby[:][["market","number_of_reviews","accuracy","cleanliness","checkin","communication",
                                   "location","value","rating"]]
            fig12=ff.create_table(df3_sample2,colorscale="Aggrnyl")
            st.plotly_chart(fig12)

if selected=="Key Insights":
    st.title("Summarizing Overall Project:")
    st.markdown("#### As the airbnb data available is scraped data having limitations compared to official Airbnb data.")
    st.markdown('''#### So made Geospatial Analysis means Analyze data with a location component, like country and markets. 
                This can reveal interesting trends in pricing variations, popular property in demand, and occupancies in different locations with available informations.''')
    st.write("")

    #point 1
    st.markdown("### 1. Top 3 Markets by Users/host")
    st.markdown("##### ➡ Istanbul, Turkey.")
    st.markdown("##### ➡ Montreal, Canada.")
    st.markdown("##### ➡ Barcelona, Spain.")
    st.write("")
    ba1,ba2,ba3=st.columns([1,5,1])
    with ba2:
        dfids=df4.groupby("market")[["ID","host_id"]].count()
        dfids.reset_index(inplace=True)
        sortedvalues=dfids.sort_values(by="host_id",ascending=False)

        fig21=px.funnel(sortedvalues,x="market",y="host_id",title="Total Number of Users by Market with available data(Total=5555)",
                     hover_name="ID",color_discrete_sequence=px.colors.sequential.Redor_r)
        st.plotly_chart(fig21)
    st.markdown("---")

    #point2
    st.markdown("### 2. Top 3 Markets,Property Type by Price")

    l1,r1=st.columns(2)
    with l1:
        st.markdown("##### ➡ Hong Kong.")
        st.markdown("##### ➡ Rio De Janeiro, Brazil.")
        st.markdown("##### ➡ Istanbul, Turkey.")

        dfprice1=df4.groupby("market")[["Price","host_response_rate"]].sum().round()
        dfprice1.reset_index(inplace=True)
        sortedvalues2=dfprice1.sort_values(by="Price",ascending=False)
        fig22=px.funnel(sortedvalues2,x="market",y="Price",title="Price Variations by Market",
           hover_name="Price")
        st.plotly_chart(fig22)
    
    with r1:
        st.markdown("##### ➡ Apartment.")
        st.markdown("##### ➡ House.")
        st.markdown("##### ➡ Serviced apartment.")
        dfprice2=df.groupby("property_type")[["price","monthly_price"]].sum().round()
        dfprice2.reset_index(inplace=True)
        sortedvalues3=dfprice2.sort_values(by="price",ascending=False)
        fig23=px.bar(sortedvalues3,x="property_type",y="price",title="Price Variations by Property",
           hover_name="monthly_price")
        st.plotly_chart(fig23)
    st.markdown("---")
    
    #point 3
    st.markdown("### 3. Top 3 Markets by Overall Rating ⭐⭐⭐")
    st.markdown("##### ➡ Other (International) ⭐100.00.")
    st.markdown("##### ➡ The Big Island ⭐96.50.")
    st.markdown("##### ➡ Maui ⭐95.80.")
    p3l,p3c,p3r=st.columns([1,5,1])
    with p3c:
        margby2=df3.groupby("market")[["number_of_reviews","accuracy","cleanliness","checkin",
                                            "communication","location","value","rating"]].mean().round(1)
        margby2.reset_index(inplace=True)
        sortedvalues4=margby2.sort_values(by="rating",ascending=False)
        fig24=px.line(sortedvalues4,x="market",y="rating",title="Overall Ratings by Markets")
        st.plotly_chart(fig24)

        with st.expander("Summary Ratings by Markets"):
            df3_sample8=sortedvalues4[:][["market","number_of_reviews","accuracy","cleanliness","checkin","communication",
                                    "location","value","rating"]]
            fig25=ff.create_table(df3_sample8,colorscale="YlOrRd_r")
            st.plotly_chart(fig25)
    st.markdown("---")

    #point 4
    r30,c30=rate(df2,df2["avail_30"],30)
    r60,c60=rate(df2,df2["avail_60"],60)
    r90,c90=rate(df2,df2["avail_90"],90)
    r365,c365=rate(df2,df2["avail_365"],365)

    percent={"Availability":["Avail_30","Avail_60","Avail_90","Avail_365"],
             "Rate":[r30,r60,r90,r365],"Count":[c30,c60,c90,c365]}
    ratedf=pd.DataFrame(percent)

    ra1,ra2=st.columns(2)
    with ra1:
        st.markdown("### 4. Rate of Avialable Nights fully Booked")
        st.write("")
        st.markdown(f"##### ➡ Availability 30 Nights ⭐{r30}'% & Count is {c30}/5555.")
        st.markdown(f"##### ➡ Availability 60 Nights ⭐{r60}'% & Count is {c60}/5555.")
        st.markdown(f"##### ➡ Availability 90 Nights ⭐{r90}'% & Count is {c90}/5555.")
        st.markdown(f"##### ➡ Availability 365 Nights ⭐{r365}'% & Count is {c365}/5555.")
    with ra2:
        fig26=px.bar(ratedf,x="Availability",y="Rate",height=300,hover_name="Rate",
                     color_discrete_sequence=px.colors.sequential.Mint_r,title="30/60/90/365 fully booked by % & total count",
                     text="Count")
        st.plotly_chart(fig26)
    st.markdown("---")

    #point 5
    st.markdown("### 5. Informative Points")
    st.write("")
    ip1,ip2=st.columns([1,5])
    with ip2:
        st.markdown("#### ➡ Mostly Preferred property is :blue[Apartment].")
        st.markdown("#### ➡ Mostly Preferred Room type is :blue[Private Room].")
        st.markdown("#### ➡ Mostly Preferred Bed type is :blue[Real Bed].")
        st.markdown("#### ➡ Mostly Preferred atleast 1 bed and 1 bathroom.")
        st.markdown("#### ➡ Avg host response rate is ⭐93.11'% .")
        st.markdown("#### ➡ Mostly Host responsing time is within a hour,few hours,atleast by the day.")
        st.markdown("#### ➡ Miniumum documents required for verification is :red[Email, Phone, Government ID proof, Reviews, Jumio](online identity verification process).")
