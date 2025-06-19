# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy.stats as stats
import numpy as np

# function for cramer's v
def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = stats.chi2_contingency(confusion_matrix, correction=False)[0]
    n = confusion_matrix.sum().sum()
    r, k = confusion_matrix.shape
    return np.sqrt(chi2 / (n * (min(k - 1, r - 1))))

# fucntion to run file
def run():
    # read file
    df_eda = pd.read_csv('df_eda.csv')

    # create new column
    df_eda['TenureCategory'] = ''
    # categorize customer
    df_eda.loc[df_eda['Tenure'] <= 6, 'TenureCategory'] = 'Newcomer' 
    df_eda.loc[(df_eda['Tenure'] >= 7) & (df_eda['Tenure'] <= 12), 'TenureCategory'] = 'Recent Adopter' 
    df_eda.loc[(df_eda['Tenure'] >= 13) & (df_eda['Tenure'] <= 24), 'TenureCategory'] = 'Regular Customer'
    df_eda.loc[df_eda['Tenure'] > 24, 'TenureCategory'] = 'Veteran Customer' 

    ###
    # TITLE SECTION
    ###
    # title and desc
    st.title('Exploratory Data Analysis📊')
    st.caption('By Muhammad Rafi Abhinaya')
    st.markdown("""
        In this section we'll dive into our dataset and see if we can dig up valuable insights!
        These insights will give us a better idea of our customers characteristcs and behaviours.
    """)

    # divider
    st.divider()

    ###
    # DEMOGRAPHIC SECTION
    ###

    # title and desc
    st.header('**Customer Demographics 🌏**')
    st.markdown(
        "Let's start by exploring our customer's demographics. this can give us a better idea of who are our customers and what are their characteritics." 
        "Demographic includes their gender, marital status, and city tier."
    )

    # demographic columns
    demo_cols = ['Gender', 'MaritalStatus', 'CityTier']
    # create figure
    fig, axs = plt.subplots(1, 3, figsize=(14,5), facecolor='#FFFFFF05')
    # loop each feature
    for i, col in enumerate(demo_cols):
        # group by col
        df5 = df_eda.groupby(col).agg(UserCount=('CustomerID', 'count')).sort_values('UserCount', ascending=False)
        #create pie chart 
        wedges, texts, autotexts = axs[i].pie(
            x=df5['UserCount'],
            labels=df5.index,
            startangle=90,
            colors=sns.color_palette('flare', n_colors=len(df5)),
            autopct='%1.1f%%',
            textprops={'color': 'white', 'size':11.5},
            wedgeprops={'edgecolor': 'white'}
        )
        axs[i].set_title(f'Proportion of {col}', fontweight='bold', color='white', size=13) 
    # show chart
    st.pyplot(fig)

    # show description
    st.markdown("""
        Here is what we can conclude from the pie charts above:
        - **Our customers are mostly male** having a percentage of 60.1%, while female customers have 39.9%. The proportions are pretty balanced,
            there's no gender that dominates our customer demographic. In future decisions, we should minimize favorating one gender, as our the proportions
            are pretty balanced.
        - **Most of our customers are married** having a percentage of 53%, followed by single having 31.9%, and divorced having only 15.1%. Married customers
            may tend to use ecommerce platforms more to order items for their family and household.
        - **A big portion of our customers comes from city tier 1** having a percentage of 65.1%, followed by tier 3 with 30.6%, and tier 2 having only 4.3%.
            Our dataset doesn't provide any information about what these tier means, but it makes sense that tier 1 is the highest as it is supposed to have
            the better facilitation and infrastructure to support ecommerce transactions.
    """)

    # divider
    st.divider()

    ###
    # PREFERRED ORDER CAT
    ###

    # title and desc
    st.header('**Most Popular Item Category Ordered 🎁**')
    st.markdown("""
    Next, let's explore some behaviour of our customers. Let's see what product category are our customers most interested in.
    """)

    # group by preferred order category
    df6 = df_eda.groupby('PreferredOrderCat', as_index=False).agg(UserCount=('CustomerID', 'count')).sort_values('UserCount', ascending=False)
    # create figure
    fig, ax = plt.subplots(figsize=(14, 5), facecolor="#FFFFFF05")
    # create bar chart
    sns.barplot(data=df6,
                x='UserCount',
                y='PreferredOrderCat',
                palette=sns.color_palette('flare', n_colors=len(df6['PreferredOrderCat'].unique())),
                ax=ax)
    # set style
    ax.set_title("Customer's Preferred Product Category", fontweight='bold', fontsize=16, color='white')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.set_facecolor('none')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # show chart
    st.pyplot(fig)

    # description
    st.markdown("""
        From the chart above, we can see that laptop & accessory are the most popular product category preferred by our customers.
        The second most popular is mobile phone, which means a big portion of our customers prefer to order technologies from our platform.
        I think it will be interesting if we compare what each gender like to order, so let's check it!
    """)

    # group by order cat and gender
    df6 = df_eda.groupby(['PreferredOrderCat','Gender'], as_index=False).agg(UserCount=('CustomerID','count')).sort_values('UserCount',ascending=False)
    # create figure
    fig, ax = plt.subplots(figsize=(14, 5), facecolor="#FFFFFF05")
    # create bar chart
    sns.barplot(data=df6,
                x='UserCount',
                y='PreferredOrderCat',
                hue='Gender',
                palette=sns.color_palette('flare', n_colors=len(df6['Gender'].unique())),
                ax=ax)
    # set style
    ax.set_title("Customer's Preferred Product Category", fontweight='bold', fontsize=16, color='white')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.set_facecolor('none')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # show chart
    st.pyplot(fig)

    # show description
    st.markdown("""
        Eventhough the usual stigma is that male and female have different preferences in items, it seems that's not the case here.
        Both gender almost have identical preferences, the only difference is female prefer fashion more than mobile, while male prefers mobile more.
        Other than that, Laptop & Accessory and Mobile phone are still the two most preferred category on both gender. This shows that our most of our
        customer loves technology.
    """)

    # divider
    st.divider()

    ###
    # PROPORTION OF CHURN SECTION
    ###

    # title and desc
    st.header('**Proportion of Churned Customers 🏃‍♂️**')
    st.markdown("""
    Now let's explore the the most interesting part, churned customer. In the next sections, we'll explore the dataset to find what might motivate
    a customer to churn. First, let'se see the proportions of churned and not churned customers.
    """)

    # count each label
    df1 = df_eda['Churn'].value_counts()
    # create figure, divide to 3 ax and only use the middle one
    fig, axs = plt.subplots(1, 3, figsize=(10,5), facecolor='none', gridspec_kw={'width_ratios': [1, 2, 1]})
    # create pie chart
    wedges, texts, autotexts = axs[1].pie(
            x=df1,
            labels=['Not Churn','Churn'], 
            colors=sns.color_palette('flare', n_colors=2),
            autopct='%1.1f%%',
            startangle=90,
            textprops={'color': 'white', 'size':11.5},
            wedgeprops={'edgecolor': 'white'})
    # set style
    axs[1].set_title('Proportion of Churned Customers', color='white', fontweight='bold')
    axs[0].axis('off')
    axs[2].axis('off')
    fig.patch.set_facecolor("#FFFFFF05")
    # show chart
    st.pyplot(fig)

    # show description
    st.markdown("""
        From the chart above, we can see that most of the customers are not churned, holding only 16.8\% from the all of the customers.
                The data we have currently are user data from the last one month, meaning 16.8\% is our monthly churn rate.
                Having this amount of churn rate is actually bad, because according to [Kumar (2024)](https://www.chargebee.com/blog/ecommerce-churn-rate/),
                the good monthly churn rate is around 5%. This means our 16.8\% churn rate is actually high and not ideal.
                We aim to decrese this rate by creating this machine learning model later.
    """)

    # divider
    st.divider()

    ###
    # CORRELATION SECTION
    ###

    # title and desc
    st.header('**Features Correlation to Customer Churn 🤔**')
    st.markdown("""
    Knowing what feature directly correlates to the churn label can help give us an idea on what affects a customer's decision to churn. The target column is
    binary, therefore we'll use the proper correlation coefficients according to the data types.
    - For numerical features, we'll use point biserial correlation to calculate the correlation.
    - For binary and categorical features, we'll use cramer's v to calculate the correlation.
    """)

    # numerical and categorical columns
    num_cols = ['CustomerID', 'Tenure', 'WarehouseToHome', 'HourSpendOnApp', 'NumberOfDeviceRegistered', 'SatisfactionScore',
                'NumberOfAddress', 'OrderAmountHikeFromLastYear', 'CouponUsed', 'OrderCount', 'DaySinceLastOrder', 'CashbackAmount']
    cat_cols = df_eda.select_dtypes(include='object').columns.to_list() + ['CityTier', 'Complain']
    # correlation values list
    corr_num = []
    corr_cat = []
    # calculate correlation of numerical columns
    for col in num_cols:
        corr,_ = stats.pointbiserialr(df_eda[col], df_eda['Churn'])
        corr_num.append(corr)
    # calculate correlation of categorical columns
    for col in cat_cols:
        corr = cramers_v(df_eda[col], df_eda['Churn'])
        corr_cat.append(corr)
    # convert to dataframe
    df2 = pd.DataFrame({'Column':num_cols+cat_cols, 'Correlation':corr_num+corr_cat}).set_index('Column').sort_values('Correlation',ascending=False)
    # show heatmap
    fig, ax = plt.subplots(figsize=(6, 5), facecolor="#FFFFFF05")    
    heatmap = sns.heatmap(df2[['Correlation']],
                          annot=True,
                          cmap='coolwarm',
                          center=0,
                          vmin=-1,
                          vmax=1,
                          ax=ax)
    plt.tight_layout()
    # set style
    cbar = heatmap.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color='white') 
    plt.setp(cbar.ax.get_yticklabels(), color='white')
    ax.set_title('Corelation to Target Heatmap', color='white', fontweight='bold')
    ax.tick_params(colors='white')  
    ax.xaxis.label.set_color('white')  
    ax.yaxis.label.set_color('white')
    # show chart
    st.pyplot(fig)

    # show description
    st.markdown("""
        From the chart above, we can see that all of our feature doesn't have a strong correlation to the target.
        Having a correlation value  of +-0.5 to +-1 is considered as strong correlation, and none of our features have a correlation value of this range.
        The strongest correlation is with `Tenure` with -0.34, this is considered as moderate correlation with a negative direction.
        The rest of the features have weak correlation, proven by their values being close to 0.

        From this, we can conclude that there are no individual feature that directly and strongly affects the decision of a customer to churn or not.
    """)

    # divider
    st.divider()

    ###
    # TENURE AND CHURN SECTION
    ###

    # header and desc
    st.header('**Pattern Between Tenure and Churned Customers 🕑**')
    st.markdown("""
    Since `Tenure` is the strongest correlated feature to `Churn`, let's see if we can find a pattern of churned an not churned customers through this feature.
    `Tenure` in this dataset is a bit ambiguos. It's supposed to tell how long the customer have been a user of the product, but we don't know the time interval
    that it explains. Since the tenure ranges until 60, I thought that the interval is by months. But, when customers have a `Tenure` of 0, they still have a
    value in `OrderAmountHikeFromlastYear`, which doesn't make sense since the customer have just joined. For ease of analysis, I'll assume that `Tenure` is how
    many months the customer have been using the platform.
                
    I will now categorize customers based on how long they have been a customer based on `Tenure`
    - if `Tenure` ranges from 0-6 months ---> Newcomer
    - if `Tenure` ranges from 7-12 months ---> Recent Adopter
    - if `Tenure` ranges from 13-24 months ---> Regular Customer
    - if `Tenure` is above 24 months ---> Veteran Customer
    """)

    # group by tenure category
    df3 = df_eda.groupby('TenureCategory').agg(Amount=('CustomerID','count'))
    # create chart
    fig, axs = plt.subplots(1, 3, figsize=(10,5), facecolor="#FFFFFF05", gridspec_kw={'width_ratios': [1, 2, 1]})
    # pie chart
    wedges, texts, autotexts = axs[1].pie(
            x=df3['Amount'],
            labels=df3.index,
            startangle=90,
            colors=sns.color_palette('flare', n_colors=4),
            autopct='%1.1f%%',
            textprops={'color': 'white', 'size':11.5},
            wedgeprops={'edgecolor': 'white'})
    # set style
    axs[1].set_title('Proportion of Tenure Category', color='white', fontweight='bold')
    axs[0].axis('off')
    axs[2].axis('off')
    # show chart
    st.pyplot(fig)

    st.markdown("""
    From the chart above, we can see that most of our customers are newcomers with 38.2%, followed by recent adopters, regular customers, and veteran
    customers with only 7.6%. The company seems to have attracted a lot of new customers within the past year, proven by 66.3% of our customers have a
    tenure of under 12 months.

    Now let's divide it to churn and not churned customer, to see if there are any patterns.
    """)

    # split dataset based on churn
    df3_1 = df_eda.loc[df_eda['Churn'] == 0, :]
    df3_2 = df_eda.loc[df_eda['Churn'] == 1, :]
    # group by tenure category
    df3_1 = df3_1.groupby('TenureCategory').agg(Amount=('CustomerID','count'))
    df3_2 = df3_2.groupby('TenureCategory').agg(Amount=('CustomerID','count'))
    # create figure
    fig, axs = plt.subplots(1, 2, figsize=(10,5), facecolor="#FFFFFF05")
    # pie chart not churned
    wedges, texts, autotexts = axs[0].pie(
            x=df3_1['Amount'],
            labels=df3_1.index,
            startangle=90,
            colors=sns.color_palette('flare', n_colors=4),
            autopct='%1.1f%%',
            textprops={'color': 'white', 'size':11.5},
            wedgeprops={'edgecolor': 'white'})
    # pie chart churned
    wedges, texts, autotexts = axs[1].pie(
            x=df3_2['Amount'],
            labels=df3_2.index,
            startangle=90,
            colors=sns.color_palette('flare', n_colors=4),
            autopct='%1.1f%%',
            textprops={'color': 'white', 'size':11.5},
            wedgeprops={'edgecolor': 'white'})
    # set style
    axs[0].set_title('Not Churned Customes', color='white', fontweight='bold')
    axs[1].set_title('Churned Customes', color='white', fontweight='bold')
    # show chart
    st.pyplot(fig)

    st.markdown("""
    We can see some interesting insights from the charts above. The pattern for the not churned customers follows the previous proportions from the previuous
    pie chart of all the customers. The interesting one is the churned customers proportions, 73.5% of churned customers are newcomers, which means that they
    only lasted a few months using our platform. We can also see that no veteran customers have churned, showing that they truly have high loyalty to the platform.

    We previously inferred that the company recently attracted many new customers (Newcomer), especially within the last 6 months. And from the pie chart,
    we can see that most of our churned customers are these newcomers. It seems the company's recent campaign have successfully attracted many new customers,
    but they weren't able to rettain these customers. These newcomers seems to be interested in using the platform, but failed to find a reason to keep using it. 
    """)

    # divider
    st.divider()

    st.markdown("""
    That's all for the EDA! If you're interested in trying to predict a customers likeliness to churn, feel free to use the trained model on the inference page!
    """)

# run if in file
if __name__ == '__main__':
    run()
