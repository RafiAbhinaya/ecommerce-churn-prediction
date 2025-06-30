# import libraries
import streamlit as st
from streamlit_option_menu import option_menu
import eda, prediction

# create sidebar
with st.sidebar:
    # create option menu
    page = option_menu(
        menu_title='Navigation',
        options=['Home', 'EDA', 'Inference'],
        icons=['house', 'bar-chart', 'gear-fill'],
        menu_icon='geo',
        default_index=0
    )

# if home (default)
if page == "Home":
    # title and stuff
    st.title("Ecommerce Customer Churn Analysis and Prediction🛍️")
    st.caption('By Muhammad Rafi Abhinaya')
    st.image("https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png", use_container_width=True)

    # desc
    st.markdown("""
    In an E-commerce business, retaining existing customers is as crucial as attracting new ones, since customers are key revenue sources who purchase products through the platform.
    When customers stop using the service—a phenomenon known as churning—the company loses potential income. While churn is common in business, companies can work to minimize it by identifying
    customers at risk of churning and offering them targeted incentives or special treatment to encourage continued engagement and loyalty.
    """)
    
    # divider
    st.divider()

    # desc
    st.markdown("""
    In this app, I've conducted an exploratory data analysis on an Ecommerce customer churn dataset to uncover insights on what features indicates that a customer will churn. Not only that, I trained
    a machine learning model using the XGBoost algorithm to predict the likeliness of a customer to churn. Feel free to check them out from the navigation pane on the left side of the page.
                
    The dataset used in this project is obtained from Kaggle and can be acessed [here](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/discussion?sort=hotness).
    """)

# if eda
elif page == "EDA":
    eda.run()

# if inference
elif page == "Inference":
    prediction.run()

# xreate spacer to push contact info to bottom
st.sidebar.markdown("---")
spacer = st.sidebar.empty()  # acts as a flexible spacer
for _ in range(10):
    spacer.text("")  # add blank lines to push content downward

# contact info
st.sidebar.markdown("Feel free to reach out to me through my contact links below!", unsafe_allow_html=True)

# contact links
st.sidebar.link_button('📧 Email',
                       url='mailto:mr.abhinaya26@gmail.com',
                       use_container_width=True)
st.sidebar.link_button('💼 LinkedIn',
                       url='https://www.linkedin.com/in/RafiAbhinaya/',
                       use_container_width=True)
st.sidebar.link_button('🐙 GitHub',
                       url='https://github.com/RafiAbhinaya',
                       use_container_width=True)