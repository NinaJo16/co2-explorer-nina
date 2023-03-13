#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:50:29 2023

@author: ninalamers
"""

import pandas as pd
import plotly.express as px
from pandas_datareader import wb

#from jupyter_dash import JupyterDash  #this needs to be removed to convert Dash app in .py file
from dash import dcc, html, Dash # adding capital Dash here
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css'
load_figure_template('bootstrap')


app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css]) # removing Jupyter # adding __name__
server = app.server # adding this line of code

app.layout = dbc.Container(
    children = [
        
        # Header
        html.H1('CO2 emissions around the world'),
        dcc.Markdown(
            """Data on emissions and potential drivers are extracted from the 
               [World Development Indicators](https://datatopics.worldbank.org/world-development-indicators/) 
               database."""
        ),
        
        html.P('This is a new paragraph')
        
    ],
    className = 'dbc'
)

if __name__ == '__main__': # adding this line to be able to import (plotting) function to other scripts but it is not necessary
    app.run_server(debug = True) # adding debug = True # debug will automatically update url when adding new lines to layout # debug means the app is under development and updates

