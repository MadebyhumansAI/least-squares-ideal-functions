from math import e
from sqlalchemy import create_engine, MetaData, Table, Column, Float
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from bokeh.plotting import figure
from bokeh.io import show, output_notebook, output_file
from bokeh.layouts import gridplot, row
from database import *
from stats import *
from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Circle, ColumnDataSource, Grid, LinearAxis, Plot



class Plot:
    
    '''
    This class is responsible for all plotting tasks e.g.: plotting charts with training/test data etc.
    '''    
    
    def plot_training_and_ideal(self):

        output_file("output/chosen-ideal-functions.html")

        # Get data from database class
        data_actions = DataBase()
        td = data_actions.read_training_data()
        td_ideal = data_actions.read_ideal_data()
        
        x = [row[0] for row in td]
        
        y1 = [y1[1] for y1 in td]
        i_y1 = [i_y1[16] for i_y1 in td_ideal]
        
        # create plot with training data y1
        s1 = figure(width=215, height=170, background_fill_color="#fafafa", title="Y1 from Training data")
        s1.circle(x, y1, size=3, color="#53777a", alpha=0.8)

        # create plot with ideal data y16
        s2 = figure(width=215, height=170, background_fill_color="#fafafa", title="Chosen ideal function (Y16)")
        s2.circle(x, i_y1, size=3, color="#c02942", alpha=0.8)
    
        y2 = [y2[2] for y2 in td]
        i_y2 = [i_y2[20] for i_y2 in td_ideal]
        
        # create plot with training data y2
        s3 = figure(width=215, height=170, background_fill_color="#fafafa", title="Y2 from Training data")
        s3.circle(x, y2, size=3, color="#53777a", alpha=0.8)

        # create plot with ideal data y20
        s4 = figure(width=215, height=170, background_fill_color="#fafafa", title="Chosen ideal function (Y20)")
        s4.circle(x, i_y2, size=3, color="#c02942", alpha=0.8)
        
        y3 = [y3[3] for y3 in td]
        i_y3 = [i_y3[11] for i_y3 in td_ideal]
        
        # create plot with training data y2
        s5 = figure(width=215, height=170, background_fill_color="#fafafa", title="Y3 from Training data")
        s5.circle(x, y3, size=3, color="#53777a", alpha=0.8)

        # create plot with ideal data y3
        s6 = figure(width=215, height=170, background_fill_color="#fafafa", title="Chosen ideal function (Y11)")
        s6.circle(x, i_y3, size=3, color="#c02942", alpha=0.8)

        y4 = [y4[4] for y4 in td]
        i_y4 = [i_y4[18] for i_y4 in td_ideal]
        
        # create plot with training data y2
        s7 = figure(width=215, height=170, background_fill_color="#fafafa", title="Y4 from Training data")
        s7.circle(x, y4, size=3, color="#53777a", alpha=0.8)

        # create plot with ideal data y3
        s8 = figure(width=215, height=170, background_fill_color="#fafafa", title="Chosen ideal function (Y18)")
        s8.circle(x, i_y4, size=3, color="#c02942", alpha=0.8)
        
        # make a grid
        grid = gridplot([[s1, s2], [s3, s4], [s5, s6], [s7, s8]])
        show(grid)

    def plot_test_ideal_data_points(self):

        # output to static HTML file
        output_file("output/testdata-mapped-to-idealdata.html")

        # Get data from stats class
        data = Stats()

        mapped_test_data_point_x, mapped_ideal_data_point_x,\
        mapped_test_data_point_y, mapped_ideal_data_point_y\
        = data.map_test_data()

        p = figure(plot_width = 600, plot_height=600, title = "Test datapoints mapped to ideal datapoints") #, x_range=(-1000, 1000), y_range=(-1000, 1000)

        circles1 = p.circle(mapped_test_data_point_x, mapped_test_data_point_y, size=5, color="red", line_color=None, legend_label="Test data points")
        circles1.selection_glyph    = Circle(fill_color="blue", line_color=None)
        circles1.nonselection_glyph = Circle(fill_color="red",  line_color=None)

        circles2 = p.circle(mapped_ideal_data_point_x, mapped_ideal_data_point_y, size=5, color="blue", line_color=None, legend_label="Ideal data points")
        circles2.selection_glyph    = Circle(fill_color="blue", line_color=None)
        circles2.nonselection_glyph = Circle(fill_color="red",  line_color=None)

        # display legend in top right corner
        p.legend.location = "top_right"
 
        # give title to legend
        p.legend.title = "Mapped points"

        show(p)
        

        
        
        
        
        
        
            