import sys, os
import numpy as np

sys.path.append(os.path.join(
        os.path.dirname(__file__),
        "../"))
import src.plotting as plotting 


def test_plot():
    assert(plotting.plot() == None)

import sys, os
import numpy as np
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

import src.plotting as plotting

def test_plot():
    assert(plotting.plot() == None)

def test_process_data():
    input_data = np.array([[0,32],[1,212]])
    function_output = plotting.process_data(input_data)
    expected_output = np.array([[0,32,273],[1,212,373]])
    
    assert(np.all(function_output == expected_output))

def test_read_data():
    input_file = "110-tavg-12-12-1950-2020.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    temperature_data = plotting.read_data(input_filename, starting_row=0)

    assert(temperature_data.shape == (71,3))
    assert(temperature_data[0,1] == 51.39)

def test_plot_data():
    plot_file = "test_plot_data.pdf"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[0,32,273],[1,212,373]])

    if os.path.exists(plot_filename):
        os.remove(plot_filename)
        
    plotting.plot_data(input_data, plot_filename)

    assert (os.path.exists(plot_filename))

def test_convert_data():
    input_file = "110-tavg-12-12-1950-2020.csv"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    json_filename = os.path.join(results_directory,json_output_file)

    plotting.convert_data(input_filename, json_filename)

    input_data = pd.read_csv(input_filename, index_col='Date', header=4)
    output_data = pd.read_json(json_filename)

    assert (True)
