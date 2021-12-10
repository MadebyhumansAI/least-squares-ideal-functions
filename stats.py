from numpy.lib.function_base import append
from database import *
from plot import *

    
class Stats():
    
    '''
    This class is responsible for all statistics needed for the assignment like, 
    choosing the Ideal function, calculating least squares, mean squared error etc.
    '''
        
    def choose_ideal_functions(self):
    
        '''

        This function chooses the ideal functions from the ideal table in the SQLite database table.
        For each Y-value in the training data columns it computes the Total Least Squares deviation and 
        compares this with the computed Y-value deviations from the ideal data columns. 
        The one column from the ideal data that has the smallest difference in 
        Total Least Squares deviation with the training data is then choosen as ideal. 


        Raises:
        ..

        Returns:
        
        Tuple with choosen ideal functions for each training function and the value of the deviation

        '''
        np.set_printoptions(suppress=True) #Disable scientific notation in Numpy, so we can 
        #more easily see what our data looks like
        data_actions = DataBase()
        training_data = data_actions.read_training_data()
        ideal_data = data_actions.read_ideal_data()
        
        ty = np.delete(training_data, 0, axis=1) #remove column with x values from matrix, since we don't need it to choose Ideal function
        iy = np.delete(ideal_data, 0, axis=1) #remove column with x values from matrix, since we don't need it to choose Ideal function
        
        #Create dictionaries with mean sqaured errors
        mse_y_1 = {} 
        mse_y_2 = {}
        mse_y_3 = {}
        mse_y_4 = {}
        
        for t_yn in range(0, 4):
            for i_yn in range(0, 50):
                mse = np.square(np.subtract(ty[:, t_yn],iy[:, i_yn])).mean() # calculate mean squared errors between training-y and ideal-y functions
                if (t_yn == 0):
                    mse_y_1[i_yn] = mse
                if (t_yn == 1):
                    mse_y_2[i_yn] = mse
                if (t_yn == 2):
                    mse_y_3[i_yn] = mse
                if (t_yn == 3):
                    mse_y_4[i_yn] = mse
        
        # Create tuples y1..yn with the choosen ideal function minimum deviation and the value 
        # of the deviation
        y_1 = min(mse_y_1.items(), key=lambda x: x[1]) 
        y_2 = min(mse_y_2.items(), key=lambda x: x[1]) 
        y_3 = min(mse_y_3.items(), key=lambda x: x[1]) 
        y_4 = min(mse_y_4.items(), key=lambda x: x[1]) 
        
        return y_1, y_2, y_3, y_4
        

    def map_test_data(self):

        '''

        This function will map the test data to the ideal data and save the deviation at hand
        when the maximum deviation of the calculated regression does not exceed the largest deviation 
        between training dataset (A) and the ideal function (C) chosen for it by more than 
        factor sqrt(2) 

        Parameters:
        ..

        Raises:
        ..

        Returns:
        ..

        '''
        np.set_printoptions(suppress=True) #Disable scientific notation in Numpy, so we can 
        #more easily see what our data looks like
        data_actions = DataBase()
        test_data = data_actions.read_test_data()
        ideal_data = data_actions.read_ideal_data()
        
        #Create lists of the ideal function columns from the matrix with ideal data
        i_y1 = [i_y1[16] for i_y1 in ideal_data]
        i_y2 = [i_y1[20] for i_y1 in ideal_data]
        i_y3 = [i_y1[11] for i_y1 in ideal_data]
        i_y4 = [i_y1[18] for i_y1 in ideal_data]
        ideal_data_point_x = [i_x[0] for i_x in ideal_data]
       

        
        ty = test_data
        # max deviation 
        max_dev = 0.08778705256534793
        
        max_dev_square_root = math.sqrt(max_dev) #error band, not exactly sure what teacher means, keep both, and ask Lino 
        devsquared = max_dev * math.sqrt(2)
        
        # create lists of mapped points to pass to plotter class
        mapped_test_data_point_x = []
        mapped_test_data_point_y = []
        mapped_ideal_data_point_x = []
        mapped_ideal_data_point_y = []
        
        for idt, t_yn in enumerate(ty):
            for idi, ideal_data_point in enumerate(i_y1):
                mse = np.square(np.subtract(t_yn[1],ideal_data_point)).mean() # calculate mean squared errors between training-y and ideal-y functions
                if mse <= devsquared:
                    data_actions.insert_mapped_test_data(t_yn[0], t_yn[1], mse, 16)
                    mapped_test_data_point_x.append(t_yn[0])
                    mapped_test_data_point_y.append(t_yn[1])
                    mapped_ideal_data_point_x.append(ideal_data_point_x[idi])
                    mapped_ideal_data_point_y.append(ideal_data_point)
                    
            for idi2, ideal_data_point2 in enumerate(i_y2):
                mse = np.square(np.subtract(t_yn[1],ideal_data_point2)).mean() # calculate mean squared 
                if mse <= devsquared:
                    data_actions.insert_mapped_test_data(t_yn[0], t_yn[1], mse, 20)
                    mapped_test_data_point_x.append(t_yn[0])
                    mapped_test_data_point_y.append(t_yn[1])
                    mapped_ideal_data_point_x.append(ideal_data_point_x[idi2])
                    mapped_ideal_data_point_y.append(ideal_data_point2)

                    
            for idi3, ideal_data_point3 in enumerate(i_y3):
                mse = np.square(np.subtract(t_yn[1],ideal_data_point3)).mean() 
                if mse <= devsquared:
                    data_actions.insert_mapped_test_data(t_yn[0], t_yn[1], mse, 11)
                    mapped_test_data_point_x.append(t_yn[0])
                    mapped_test_data_point_y.append(t_yn[1])
                    mapped_ideal_data_point_x.append(ideal_data_point_x[idi3])
                    mapped_ideal_data_point_y.append(ideal_data_point3)
                    
            for idi4, ideal_data_point4 in enumerate(i_y4):
                mse = np.square(np.subtract(t_yn[1],ideal_data_point4)).mean() 
                if mse <= devsquared:
                    data_actions.insert_mapped_test_data(t_yn[0], t_yn[1], mse, 18)
                    mapped_test_data_point_x.append(t_yn[0])
                    mapped_test_data_point_y.append(t_yn[1])
                    mapped_ideal_data_point_x.append(ideal_data_point_x[idi4])
                    mapped_ideal_data_point_y.append(ideal_data_point4)
        
        return mapped_test_data_point_x, mapped_ideal_data_point_x, mapped_test_data_point_y, mapped_ideal_data_point_y
            
