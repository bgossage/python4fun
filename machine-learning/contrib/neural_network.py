
# coding: utf-8

# In[46]:


import pandas
import numpy
import tensorflow
import tflearn


# In[47]:


# This is reading the csv file
filename = "data/changed_all_substrings.csv"
dataframe = pandas.read_csv(filename)

# This is getting the row and column labels for accessing each element
row_labels = list(dataframe.index)
column_labels = list(dataframe.columns.values)
print(column_labels)
print("column length is: ", len(column_labels))

# Make an empty XY, X and Y matrix
x_rows = len(row_labels)
x_columns = len(column_labels) - 2

# XY contains both X and Y
XY = numpy.zeros([x_rows, x_columns+1]) # plus one for Y
X = numpy.zeros([x_rows, x_columns]) # features
Y = numpy.empty([x_rows, 1]) # correct output

print("X rows = ", x_rows)
print("X columns = ", x_columns)


# In[48]:


# Initialize XY matrix
# Column iterator
column_itr = 0
for i in range(len(column_labels)):
    if (i != 0):
        arr = numpy.asarray(list(dataframe[column_labels[i]]))
        XY[:,column_itr] = arr
        column_itr += 1
        
# Shuffle XY together
numpy.random.shuffle(XY)

std_X = numpy.zeros([x_rows, x_columns]) # Create a variable to store the standardized X 

# Standardize X and store it to std_X 
column_itr = 0
for i in range(x_columns):
    std_X[:,i] = (XY[:,i] - numpy.mean(XY[:,i])) / numpy.std(XY[:,i])

# Initialize Y 
Y[:,0] = XY[:,(len(column_labels) - 2)]

onehot_Y = numpy.zeros([x_rows, 2]) # Create a variable to store onehot encoding of Y
# One hot encode Y
for i in range(x_rows):
    if (Y[i,0] == 1):
        onehot_Y[i,0] = 1
    else:
        onehot_Y[i,1] = 1


# In[49]:


def build_model():
    # Reset all the parameters and variables
    tensorflow.reset_default_graph()
    
    # Inputs
    network = tflearn.input_data([None, x_columns])

    # Hidden layer(s)
    network = tflearn.fully_connected(network, 48, activation='ReLU')
    network = tflearn.fully_connected(network, 12, activation='ReLU')
    
    # Output layer and training model
    network = tflearn.fully_connected(network, 2, activation='softmax')
    network = tflearn.regression(network, optimizer='sgd', learning_rate=0.08, loss='categorical_crossentropy')
    
    model = tflearn.DNN(network)
    return model


# In[50]:


model = build_model()
model.fit(std_X, onehot_Y, validation_set=0.05, batch_size=30, n_epoch=60, show_metric=True)


# In[51]:


# Source Udacity
# Compare the labels that our model predicts with the actual labels

# Find the indices of the most confident prediction for each item. That tells us the predicted digit for that sample.
predictions = numpy.array(model.predict(std_X)).argmax(axis=1)

# Calculate the accuracy, which is the percentage of times the predicated labels matched the actual labels
actual = onehot_Y.argmax(axis=1)
test_accuracy = numpy.mean(predictions == actual, axis=0)

# Print out the result
print("Test accuracy: ", test_accuracy)

