from sqlalchemy import create_engine, MetaData, Table, Column, Float, insert
import pandas as pd
from  collections import defaultdict
import sqlalchemy as db
from sqlalchemy.sql import text
import math 
import numpy as np


class DataBase(object):
    
    '''
    This class is responsible for all data manipulation tasks e.g.: reading from CSV, writing to SQLite, updating data etc., also 
    the database connection and the creation of tables is done in this class.
    '''
    
    def __init__(self):
        
        '''

        Here we initiate the class with the parameters needed.
        For convenience the creation of the SQLite engine for connecting to the database, the creation of
        the table with test-data, with mapping and y-deviation is done here also.

        '''
        
        self.training_data_df =  pd.read_csv('data/train.csv') #create Pandas dataframe from training csv file
        self.table_name_training = "training"
        self.ideal_data_df =  pd.read_csv('data/ideal.csv') #create Pandas dataframe from ideal data csv file
        self.table_name_ideal = "ideal"
        self.test_data_df =  pd.read_csv('data/test.csv') #create Pandas dataframe from test csv file
        self.database_url = "sqlite:///data/linear-regression.db"
        self.metadata = db.MetaData()
        self.trainingdatamatrix = np.empty(shape=(400,5)) #create ndarray with training data, self.trainingdatamatrix is a (K x L matrix), where K = 400, and L is 5
        self.idealdatamatrix = np.empty(shape=(400,51)) #create ndarray with ideal data, self.idealdatamatrix is a (K x L matrix), where K = 400, and L is 51        
        
        # create SQLite engine and create table three to save test data, deviations 
        # and choosen ideal functions later
        try:
            self.engine = create_engine(self.database_url, echo = False)
            
            table_three = Table(
            'table_three', self.metadata, 
            Column('x_test', Float), 
            Column('y_test', Float), 
            Column('delta_y', Float),
            Column('ideal_n_y', Float),)
            self.metadata.create_all(self.engine)
            
        except Exception as e:
            print("This error occurred during the creation of the SQLite engine:")
            print(e)
            

            
    def insert_training_data(self):
        
        '''

        This function inserts the training data from a CSV file into the SQLite database.

        '''
        
        self.training_data_df.to_sql( #convert Pandas dataframe with training data to SQL
        self.table_name_training,
        self.engine,
        if_exists='replace',
        index=False,
        chunksize=500,
        dtype={
            "x": Float,
            "y1": Float,
            "y2": Float,
            "y3": Float,
            "y4": Float,
        }
    )
        
    def insert_ideal_data(self):
        
        '''

        This function inserts the ideal data from a CSV file into the SQLite database.

        '''
        
        self.ideal_data_df.to_sql( # convert Pandas dataframe with ideal data to SQL
        self.table_name_ideal,
        self.engine,
        if_exists = 'replace',
        index = False,
        chunksize = 500,
        dtype = self.create_ideal_data_dict() # create ideal data dictionary, so we don't get 50 lines of y-value declarations
    )

    def create_ideal_data_dict(self):
        
        '''

        This function creates a dictionary to pass to the "dtype" argument in the "to_sql" function 
        of Pandas. Without this we would have 50 lines of column declarations in our code.
        
        Returns:
        dict: with columnnames as keys and "float" as value for each pair

        '''
        
        self.ideal_data_dict = {"x": Float}
        for i in range(1,51):
            self.ideal_data_dict['y'+str(i)]=Float
            
        return self.ideal_data_dict
        
    
    def read_training_data(self):
        
        '''

        This function reads the x and y-values from the SQLite database tables and creates 
        ndarray with shape (400, 5)
        
        Raises:
        A custom exception if there is an error reading the database 

        Returns:
        ndarray with shape (400, 5)

        '''
        
#         if not 1 <= y_column < 5:
#             raise CustomException(y_column, "There are only four y-columns in the training dataset, please provide 1, 2, 3 or 4 as values {}".format(y_column))
            
        self.training_data = db.Table('training', self.metadata, autoload=True, autoload_with=self.engine)
        self.query = db.select([self.training_data.columns.x, self.training_data.columns.y1, self.training_data.columns.y2, self.training_data.columns.y3, self.training_data.columns.y4])
        self.results = self.engine.execute(self.query).fetchall()
        
        start = 0 
        for value in self.results:
            self.trainingdatamatrix[start] = self.results[start] #add values from SQLite to ndarray
            start += 1    
        
        return self.trainingdatamatrix # (self.trainingdatamatrix is (K x L) matrix, where K = 400, and L is 5)
    
    
    def read_ideal_data(self):
        
        '''

        This function reads the x and y-values from the SQLite database tables (Ideal data ) and creates 
        ndarray with shape (400, 51)

        Raises:
        A custom exception if there is an error reading the database 

        Returns:
        ndarray with shape (400, 51)

        '''
        self.ideal_data = db.Table('ideal', self.metadata, autoload=True, autoload_with=self.engine)
        self.query = db.select([self.ideal_data.columns.x, self.ideal_data.columns.y1, self.ideal_data.columns.y2, self.ideal_data.columns.y3, self.ideal_data.columns.y4, self.ideal_data.columns.y5, self.ideal_data.columns.y6, self.ideal_data.columns.y7, self.ideal_data.columns.y8, self.ideal_data.columns.y9, self.ideal_data.columns.y10, self.ideal_data.columns.y11, self.ideal_data.columns.y12, self.ideal_data.columns.y13, self.ideal_data.columns.y14, self.ideal_data.columns.y15, self.ideal_data.columns.y16, self.ideal_data.columns.y17, self.ideal_data.columns.y18, self.ideal_data.columns.y19, self.ideal_data.columns.y20, self.ideal_data.columns.y21, self.ideal_data.columns.y22, self.ideal_data.columns.y23, self.ideal_data.columns.y24, self.ideal_data.columns.y25, self.ideal_data.columns.y26, self.ideal_data.columns.y27, self.ideal_data.columns.y28, self.ideal_data.columns.y29, self.ideal_data.columns.y30, self.ideal_data.columns.y31, self.ideal_data.columns.y32, self.ideal_data.columns.y33, self.ideal_data.columns.y34, self.ideal_data.columns.y35, self.ideal_data.columns.y36, self.ideal_data.columns.y37, self.ideal_data.columns.y38, self.ideal_data.columns.y39, self.ideal_data.columns.y40, self.ideal_data.columns.y41, self.ideal_data.columns.y42, self.ideal_data.columns.y43, self.ideal_data.columns.y44, self.ideal_data.columns.y45, self.ideal_data.columns.y46, self.ideal_data.columns.y47, self.ideal_data.columns.y48, self.ideal_data.columns.y49, self.ideal_data.columns.y50])
        self.results = self.engine.execute(self.query).fetchall()
        
        start = 0 
        for value in self.results:
            self.idealdatamatrix[start] = self.results[start] # add values from SQLite to ndarray
            start += 1    
        
        return self.idealdatamatrix # (self.idealdatamatrix is (K x L) matrix, where K = 400, and L is 51)

    def read_test_data(self):
        
        '''

        This function reads the x and y-values from the test data CSV file and creates 
        ndarray with shape (100, 2)

        Raises:
        A custom exception if there is an error reading the CSV file 

        Returns:
        ndarray with shape (100, 2)

        '''
        return (self.test_data_df.to_numpy(copy=False)) 
    
    def insert_mapped_test_data(self, x_test, y_test, delta_y, ideal_n_y):
        
        '''

        This function saves the mapped testdata to the database

        Raises:
        A custom exception if there is an error saving the data

        Returns:
        Boolean: success or failure
        
        Parameters:
        x_test: decimal
        y_test: decimal
        delta_y: decimal
        ideal_n_y: decimal
        
        '''

        with self.engine.connect() as con:
            self.rs = con.execute('INSERT INTO table_three (x_test, y_test, delta_y, ideal_n_y) VALUES (?, ?, ?, ?)', (x_test, y_test, delta_y, ideal_n_y))
            print (self.rs)