# import libraries
import streamlit as st
import eda, prediction

st.sidebar.header("📌 Navigation Pane")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 EDA", "🔍 Inference"])

# Route to selected page
if page == "🏠 Home":
    st.title("Ecommerce Customer Churn Analysis and Prediction🛍️")
    st.caption('By Muhammad Rafi Abhinaya')
    st.image("https://www.cleartouch.in/wp-content/uploads/2022/11/Customer-Churn.png", use_container_width=True)
    st.markdown("""
    In running a business, customers are one of the most important stakeholders. In an E-commerce business, customers are the one who purchase products from merchants through the company's platform. While attracting new customers will increase the platform's user count, what's important is also retaining existing customers. Now what happens when customers doesn't return to use the the product? The company will lose a source of income because this customer won't be making anymore purchases through the platform. This phenomenon of not continuing to use a product is called a Churning.

Churning is a common thing that happens in businesses, what the company can do is minimize the churn rate of their customers. One way of doing this is by detecting which customers has the potential for churning. By detecting the customers that have the potential to churn, the company can give them special treatments to convince them to keep using their products in hopes of retaining these customers.
    """)
    
    st.divider()
    st.markdown("""
    I've conducted EDA on an Ecommerce customer churn dataset and trained a model to predict the likeliness of a customer to churn. Feel free to check them out from the navigation pane on the left side of the page.
                
    The dataset used in this project is obtained from Kaggle and can be acessed [here](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/discussion?sort=hotness)}
    """)

elif page == "📊 EDA":
    eda.run()
elif page == "🔍 Inference":
    prediction.run()

# Create spacer to push contact info to bottom
st.sidebar.markdown("---")
spacer = st.sidebar.empty()  # acts as a flexible spacer
for _ in range(10):
    spacer.text("")  # add blank lines to push content downward

# Add contact info
st.sidebar.header('📱Contact Links')
st.sidebar.markdown("Feel free to reach out to me through my contact links below!", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    [📧 Email](mailto:mr.abhinaya26@gmail.com)  
    [💼 LinkedIn](https://www.linkedin.com/in/RafiAbhinaya/)  
    [🐙 GitHub](https://github.com/RafiAbhinaya)
    """,
    unsafe_allow_html=True
)