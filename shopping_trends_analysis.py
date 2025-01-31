
!pip install WordCloud

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

shop = pd.read_csv('shopping_trends_updated.csv')

shop.shape

shop.to_excel('shopping_trends_updated.xlsx')

shop.head()

shop.dtypes

shop.columns

shop.info()

shop.shape

shop.isnull().sum()

print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")

"""## 1 What is the overall distribution of customer ages in the dataset?"""

shop['Age'].value_counts()

shop['Age'].mean()

shop['Gender'].unique()

shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults'
                                                                                             , 'old'] )

fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()

"""## 2 How does the average purchase amount vary across different product categories?"""

shop.columns

shop['Category'].unique()

shop.groupby('Category')['Purchase Amount (USD)'].mean()

"""## 3 Which gender has the highest number of purchases?"""

shop.columns

sns.barplot(shop , x = 'Gender' , y = 'Purchase Amount (USD)')

"""## 4 What are the most commonly purchased items in each category?"""

shop.columns

shop.groupby('Category')['Item Purchased'].value_counts()

fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()

"""## 5 Are there any specific seasons or months where customer spending is significantly higher?"""

shop['Season'].unique()

shop[shop['Season'] == 'Summer'].value_counts().sum()

shop[shop['Season'] == 'Winter'].value_counts().sum()

shop[shop['Season'] == 'Spring'].value_counts().sum()

shop[shop['Season'] == 'Fall'].value_counts().sum()

fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )

fig.show()

"""## 6 What is the average rating given by customers for each product category?"""

shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()

fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()

"""## 7 Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?"""

shop.columns

shop['Subscription Status'].unique()

sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')

shop['Purchase Amount (USD)'].sum()

shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()

"""## 8 Which payment method is the most popular among customers?"""

shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)

shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()

fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()

sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')

"""## 9 Do customers who use promo codes tend to spend more than those who don't?"""

shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()

fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()

fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()

"""## 10 How does the frequency of purchases vary across different age groups?"""

shop[['Age' , 'Age_category']]

shop['Age_category'].unique()

shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()

px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')

"""## 11 Are there any correlations between the size of the product and the purchase amount?"""

shop.columns

shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()

fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()

"""## 12 Which shipping type is preferred by customers for different product categories?"""

shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)

shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2,
                                                       'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})

shop['Category'].unique()

shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})

"""## 13 How does the presence of a discount affect the purchase decision of customers?"""

shop.columns

shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()

px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')

fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')

fig.show()

"""## 14 Are there any specific colors that are more popular among customers?"""

px.histogram(shop , x = 'Color')

shop['Color'].value_counts().nlargest(5)

"""## 15 What is the average number of previous purchases made by customers?"""

shop['Previous Purchases'].mean()

"""## 16 Are there any noticeable differences in purchase behavior between different locations?"""

shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)

shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()

fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()

"""## 17 Is there a relationship between customer age and the category of products they purchase?"""

shop_group = shop.groupby('Category')['Age'].mean().reset_index()

fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()

"""## 18 How does the average purchase amount differ between male and female customers?"""

shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()

fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()

px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')



def avg_purchase_amount_by_gender(shop):
    avg_purchase_by_gender = shop.groupby('Gender')['Purchase Amount (USD)'].mean()
    return avg_purchase_by_gender

import plotly.express as px

def avg_purchase_amount_by_gender(shop):
    avg_purchase_by_gender = shop.groupby('Gender')['Purchase Amount (USD)'].mean()
    return avg_purchase_by_gender

avg_purchase = avg_purchase_amount_by_gender(shop)


fig = px.bar(avg_purchase,
             x=avg_purchase.index,
             y='Purchase Amount (USD)',
             title='Average Purchase Amount by Gender')
fig.show()
