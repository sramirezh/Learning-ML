import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from sklearn import preprocessing
import sklearn.metrics as sklm
import scipy.stats as ss


def hist_plot(df,cols):
    """
    Plots a histogram of the desired numerical data

    Args:
        vals: data_frame column
        lab: string containing the label
    """
    for col in cols:
        sns.distplot(df[col])
        plt.title('Histogram of ' + col)
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.show()
        
    
def plot_box(df, col, col_y = 'hits'):
    """
    Plots a seaborn boxplot 
    
    Args:
        df is a pandas dataframe
        col is a column with the categorical values
        col_y is the column with the quantitative values
    """
    fig, ax = plt.subplots()
    sns.set_style("whitegrid")
    sns.boxplot(col, col_y, data=df,ax = ax)
    plt.xlabel(col) 
    plt.ylabel(col_y)
    plt.show()

    return fig, ax

def frequency_table(data, cols):
    """
    Builds a frequency table for the specific columns
    Args:
        df is a pandas dataframe
        cols columns to analyse
    """
    for col in cols:
        print('\n' + 'For column ' + col)
        print(data[col].value_counts())
        print('There are %s unique values' %data[col].unique().shape[0])

def plot_bars(df, cols):
    """
    Bars for categorical variables
    df: data frame
    cols: columns to plot
    """
    for col in cols:
        fig = plt.figure(figsize=(6,6)) 
        ax = fig.gca()    
        counts = df[col].value_counts() 
        counts.plot.bar(ax = ax, color = 'blue') 
        ax.set_title('Counts' + col) 
        ax.set_xlabel(col) 
        ax.set_ylabel('Counts')
        plt.show()
    
    return fig , ax 

def plot_scatter(df, cols, col_y , alpha = 1.0):
    """
    Scatter plots of the desired columns
    Args:
        df is a pandas dataframe
        cols columns to analyse
        col_y column in the y-axis
    """
    for col in cols:
        fig = plt.figure(figsize=(7,6)) 
        ax = fig.gca() 
        df.plot.scatter(x = col, y = col_y, ax = ax, alpha = alpha)
        ax.set_title('Scatter plot of ' + col_y + ' vs. ' + col) 
        ax.set_xlabel(col) 
        ax.set_ylabel(col_y)
        plt.show()

def path_counter(data):
    """
    Return the number of path_ids in the data, assuming that each path is separated by ;
    """

    if isinstance(data, str):
        n_ids = len(data.split(';'))
    elif math.isnan(data):
        n_ids = 0
    else:
        n_ids = 1
    
    return n_ids

def path_id_splitter(data):
    """
    Splits the path id
    """
    if ';' in data:
        splitted = data.split(';')
        splitted = [float(item) for item in splitted]
    else: 
        splitted = [float(data)]
    return splitted



def group_cat(df, col, threshold ):
    """
    Groups categorical variables into a group called "other"
    Args:
        df:data_frame
        col:column to group
        threshold: threshold to decide if the variable is grouped or not
    """
    frequencies = pd.DataFrame(df[col].value_counts())
    frequencies = frequencies.reset_index()
    frequencies.columns = [col, 'frequency']
    total = frequencies['frequency'].sum()
    frequencies['perc']= frequencies['frequency']/total
    group = frequencies[col].loc[frequencies['perc']<threshold].values

    return group, frequencies

def cat_aggregation(x,group):
    """
    Assigns the variable "other" to the variables in the group
    """
    if x in group:
        x = 'other'
    else: 
        x = str(x)
    return x

def encode_string(cat_feature):
    """
    Creates dummy variables out of categorical features and encodes them. 
    """
    ## First encode the strings to numeric categories
    enc = preprocessing.LabelEncoder()
    enc.fit(cat_feature)
    enc_cat_feature = enc.transform(cat_feature)
    ## Now, apply one hot encoding
    ohe = preprocessing.OneHotEncoder()
    encoded = ohe.fit(enc_cat_feature.reshape(-1,1))
    return encoded.transform(enc_cat_feature.reshape(-1,1)).toarray()

def print_metrics(y_true, y_predicted):
    ## First compute R^2 and the adjusted R^2
    r2 = sklm.r2_score(y_true, y_predicted)
    
    ## Print the usual metrics and the R^2 values
    print('Mean Square Error      = ' + str(sklm.mean_squared_error(y_true, y_predicted)))
    print('Root Mean Square Error = ' + str(math.sqrt(sklm.mean_squared_error(y_true, y_predicted))))
    print('Mean Absolute Error    = ' + str(sklm.mean_absolute_error(y_true, y_predicted)))
    print('Median Absolute Error  = ' + str(sklm.median_absolute_error(y_true, y_predicted)))
    print('R^2                    = ' + str(r2))

def hist_resids(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
    ## now make the residual plots
    sns.distplot(resids)
    plt.title('Histogram of residuals')
    plt.xlabel('Residual value')
    plt.ylabel('count')

def resid_qq(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
    ## now make the residual plots
    ss.probplot(resids.flatten(), plot = plt)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')

def resid_plot(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
    ## now make the residual plots
    sns.regplot(y_score, resids, fit_reg=False)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')
    
    
def print_format(f,x):
    print('Fold %2d    %4.3f ' % (f, x))

def print_cv(scores):
    fold = [x + 1 for x in range(len(scores['test_neg_root_mean_squared_error']))]
    print('test_neg_root_mean_squared_error')
    [print_format(f,x) for f,x in zip(fold, scores['test_neg_root_mean_squared_error'])]
    print('-' * 40)
    print('Mean       %4.3f' % 
          (np.mean(scores['test_neg_root_mean_squared_error'])))
    print('Std        %4.3f' % 
          (np.std(scores['test_neg_root_mean_squared_error'])))
