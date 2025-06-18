# import libraries
import pandas as pd
import cloudpickle
import streamlit as st

# run function
def run():
    # load model
    with open('final_model.pkl', 'rb') as file:
        model = cloudpickle.load(file)

    # show title
    st.title('Ecommerce Customer Churn Predicition🔍')
    st.caption('By Muhammad Rafi Abhinaya')

    # show description
    description = '''
    In this section, you'll be able to predict whether a customer will churn or not! All you need to do is fill out
    this form below, and our model will predict the results.
    '''
    st.markdown(description)

    # create form to contain data input
    with st.form('inference', enter_to_submit=False):
        # create columns
        col1, col2, col3 = st.columns(3)

        # inputs in column 1
        with col1:
            Tenure = st.number_input('📆 Tenure',0,70,1,1,
                                    label_visibility='visible',
                                    help='Tenure period of customer in months',
                                    placeholder="0-70")
            WarehouseToHome = st.number_input('🏠 Warehouse to home',1,150,1,1,
                                    label_visibility='visible',
                                    help='Distance in between warehouse to home of customer',
                                    placeholder="5-150")
            CouponUsed = st.number_input('🎟️ Coupon used',0,20,1,1,
                                    label_visibility='visible',
                                    help='Number of coupons used in the last month',
                                    placeholder="1-20")
            HourSpendOnApp = st.number_input('🕑 Monthly average hour',0,5,1,1,
                                    label_visibility='visible',
                                    help='Monthly average hours spent on platform',
                                    placeholder="0-5")
                        
        # inputs in column 2
        with col2:
            OrderCount = st.number_input('📦 Order count',0,20,1,1,
                                    label_visibility='visible',
                                    help='Number of order made in the last month',
                                    placeholder="1-20")
            NumberOfAddress = st.number_input('📍 Number of address',1,25,1,1,
                                    label_visibility='visible',
                                    help='Total number of address added on a customer',
                                    placeholder="1-25")
            CashbackAmount = st.number_input('📈 Cashback amount',0,400,1,1,
                                    label_visibility='visible',
                                    help='Amount of cashback received in the last month',
                                    placeholder="0-400")
            OrderAmountHikeFromLastYear = st.number_input('📈 Order Amount Hike',0,100,1,1,
                                    label_visibility='visible',
                                    help='Percentage increases in order from last year',
                                    placeholder="0-50")
                    
        
        # inputs in column 3
        with col3:
            SatisfactionScore = st.number_input('⭐ Satisfaction score',0,5,1,1,
                                    label_visibility='visible',
                                    help='Customer\'s satisfaction score',
                                    placeholder="1-5")
            NumberOfDeviceRegistered = st.number_input('📱 Number of device',1,7,1,1,
                                    label_visibility='visible',
                                    help='Total number of devices that\'s registered on a customer',
                                    placeholder="1-7") 
            DaySinceLastOrder = st.number_input('🗓️ Day since last order',0,50,1,1,
                                    label_visibility='visible',
                                    help='Days since the customer last ordered',
                                    placeholder="0-50")
            
        
        # divider
        st.divider()

        # create columns
        col4, col5, col6 = st.columns(3)

        # inputs in column 4
        with col4:
            Gender = st.selectbox(label='🚻 Gender',
                                    options=['Male', 'Female'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Customer\'s gender')
            PreferredLoginDevice = st.selectbox(label='💻 Preferred login device',
                                    options=['Mobile Phone', 'Computer'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Customer\'s preferred device to use')
            Complain =  st.selectbox(label='📃Complain',
                                    options=['Yes', 'No'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Any complaint has been raised in last month')
            Complain = 1 if Complain == 'Yes' else 0
            
        # inputs in column 5
        with col5:
            MaritalStatus =  st.selectbox(label='💍Marital status',
                                    options=['Single', 'Divorced', 'Married'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Customer\'s marital status')
            PreferredOrderCat = st.selectbox(label='🎁 Preferred order category',
                                    options=['Laptop & Accessory', 'Mobile', 'Mobile Phone', 'Others', 'Fashion', 'Grocery'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Customer\'s preferred product category to order')
            
        # inputs in column 6
        with col6:
            CityTier = st.selectbox(label='🏙️ City Tier',
                                    options=[1,2,3],
                                    index=0,
                                    label_visibility='visible',
                                    help='City tier of customer\'s main location')
            PreferredPaymentMode = st.selectbox(label='💳 Preferred payment mode',
                                    options=['Debit Card', 'UPI', 'Cash on Delivery', 'E wallet', 'Credit Card'],
                                    index=0,
                                    label_visibility='visible',
                                    help='Customer\'s preferred payment method')

        # submit button
        submit = st.form_submit_button()

        # rub if submit button is pressed
        if submit:
            # store values in a list
            values = [Tenure, WarehouseToHome, HourSpendOnApp, NumberOfDeviceRegistered, NumberOfAddress,
                    OrderAmountHikeFromLastYear, OrderCount, CouponUsed, DaySinceLastOrder, CashbackAmount,
                    SatisfactionScore, CityTier, PreferredLoginDevice, PreferredPaymentMode, Gender,
                    PreferredOrderCat, MaritalStatus, Complain, 0]

            # if there are missing values
            if None in values:
                # show error
                st.error("🚫 Please fill out all fields before submitting!")
            
            # if no missing values        
            else:
                # column names
                columns = ['Tenure', 'WarehouseToHome', 'HourSpendOnApp', 'NumberOfDeviceRegistered', 'NumberOfAddress',
                        'OrderAmountHikeFromLastYear', 'OrderCount', 'CouponUsed', 'DaySinceLastOrder', 'CashbackAmount',
                        'SatisfactionScore', 'CityTier', 'PreferredLoginDevice', 'PreferredPaymentMode', 'Gender',
                        'PreferredOrderCat', 'MaritalStatus', 'Complain', 'CustomerID']
                
                # convert into dataframe
                data = pd.DataFrame([values], columns=columns)

                # predict results
                result = model.predict(data)

                # if customer won't churn
                if result == 0:
                    st.success('Customer will not churn!😆')

                # if customer will churn
                elif result == 1:
                    st.error('Customer will churn!😱')

# run if in file
if __name__ == '__main__':
    run()
