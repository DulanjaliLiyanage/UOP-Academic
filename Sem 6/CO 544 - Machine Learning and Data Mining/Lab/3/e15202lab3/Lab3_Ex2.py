#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets #import standard data sets 
from sklearn.linear_model import LogisticRegression #import the Logistic regression model 
from sklearn.model_selection import train_test_split #split data set into a train and test set

#importing modules to measure classification performance 
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix,accuracy_score


# In[2]:


dataset =datasets.load_digits() #load ’wine’ data set from standard data sets 
x = dataset["data"] #defining features values 
y = dataset["target"] #defining target variable values


# In[3]:


#splitting data set into a train and test set with 80% and 20% 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


# In[4]:


log_reg = LogisticRegression() #creating an instance of the model 
log_reg.fit(x_train,y_train) #fitting the relationship between data


# In[5]:


predictions = log_reg.predict(x_test) #predict labels for test data


# In[8]:


print("Confusion Matrix = \n",confusion_matrix(y_test, predictions)) 
print("Accuracy = ",accuracy_score(y_test, predictions)) 


# In[ ]:




