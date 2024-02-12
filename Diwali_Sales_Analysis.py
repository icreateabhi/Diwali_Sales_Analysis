#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Project Name - Diwali_Sales_Analysis


# In[ ]:


Project Type - EDA
Contribution - Individual
Name :- ABHINAV KUMAR JHA


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df= pd.read_csv('D:\\diwali_sales_analysis\\data.csv',encoding='unicode_escape')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


null_percent=df.isnull().sum()/df.shape[0]*100
null_percent


# In[9]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[10]:


df.isnull().sum()


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


df.info()


# In[14]:


df['Amount']=df['Amount'].astype('int')


# In[15]:


df.info()


# In[16]:


ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[17]:


sales_by_gender=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender', y='Amount', data=sales_by_gender)


# In[18]:


#From the above graph we can clearly see that most of the buyer are women and even 
#the purchasing power offemales are more then men


# In[19]:


ax=sns.countplot(x='Age Group',data=df,hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[20]:


#Total Amount vs Age Group


# In[21]:


sales_by_agegroup=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Age Group',y='Amount',data=sales_by_agegroup)


# In[22]:


#According to Above graph we can say that most of the buyers are from age group between 26-35,
#we can also say youth are more buyers,
#Also in this age group Females are more buyers.


# In[23]:


#State vs Orders


# In[24]:


order_by_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(5)


ax=sns.barplot(x='State',y='Orders',data=order_by_state)

for bars in ax.containers:
    ax.bar_label(bars)


# In[25]:


#State vs Amount


# In[26]:


sales_by_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)

ax=sns.barplot(x='State',y='Amount',data=sales_by_state)


# In[27]:


#According to above graph we can see that most orders and total amount are from
#uttar pradesh, maharashtra and karnataka respectively


# In[28]:


#Martial_Status


# In[29]:


df.columns


# In[30]:


ax = sns.countplot(x='Marital_Status', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


#Martial_Status vs Gender


# In[32]:


df.columns


# In[33]:


status = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(data=status, x='Marital_Status', y='Amount', hue='Gender')


# In[34]:


#From above graph we can easily say that most of the buyers are married(women) and they have high purchasing power


# In[35]:


#Occupation


# In[36]:


sns.set(rc={'figure.figsize':(15,5)})
ax=sns.countplot(x='Occupation',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


#Occupation vs Total Sales(Amount)


# In[38]:


sales_by_occupation=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)

ax=sns.barplot(x='Occupation',y='Amount',data=sales_by_occupation)


# In[39]:


#from above graph we can clearly see that most of the buyers are from it sectors, healthcare etc respectively


# In[40]:


#Product category


# In[41]:


sns.set(rc={'figure.figsize':(20,8)})
ax=sns.countplot(x='Product_Category',data =df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


total_sales_by_produstcategory=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(5)

sns.barplot(x='Product_Category',y='Amount',data=total_sales_by_produstcategory)


# In[43]:


#from above graph we can say that maximum order by product category is from food, clothing, electronics etc respectively


# In[44]:


#product_id vs order


# In[45]:


most_product_order=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(5)

sns.barplot(x='Product_ID',y='Orders',data=most_product_order)


# In[ ]:


# Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, 

# Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category



# Thank you!

