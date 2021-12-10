from database import *
from plot import *
from stats import *
from unit_test import *

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(DataTest))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

def main():

    # run tests to check if datafiles are in place
    my_suite()

    data_actions = DataBase()
    # Create Tables
    data_actions.insert_training_data()
    data_actions.insert_ideal_data()

    #print(data_actions.read_training_data())
    plot_actions = Plot()
    plot_actions.plot_training_and_ideal()

    # stats_actions = Stats()
    # stats_actions.map_test_data()

    plot_actions.plot_test_ideal_data_points()

# run the program
if __name__ == "__main__": 
    main()