#### Introduction to EnvisionRisk's Python Library: EnvisionRiskRaaS.py ####
#
# Hello and welcome to the introductory guide on how to use the EnvisionRiskRaaS.py library. 
# This Python package is developed by EnvisionRisk to provide you with powerful tools to manage 
# market risks. Let's take a step-by-step approach to get you started:
#
# Step 1: Installation
#
# To start with, you'll need to install the EnvisionRiskRaaS.py library. You can do this by running 
# the following command in your terminal:
#
# pip install EnvisionRiskRaaS (*** THIS IS NOT SETUP YET ***)
#
# Step 2: Importing the Library
# Once the installation is successful, you can import the library into your Python environment as follows:
#
# python: import EnvisionRiskRaaS as erv
#
# Step 3: API Authentication
# Before using the functionalities of the library, you need to authenticate with the EnvisionRisk API using 
# your access token. Here's how to do it:
# 
# python: 
# erv.envrsk_auth_log_in_interactively() or erv.envrsk_auth_log_in('<user_id>','<user_password>')
#
# Step 4: Using the Library Functions
#
# Now that you're all set up, you can start using the library's functionalities. For instance, let's 
# assume you want to get the risk snapshot for a portfolio:
#
# python:
# date = "2023-07-01"
# positions = [{"instrument_id": "AAPL", "quantity": 100}, {"instrument_id": "GOOG", "quantity": 50}]
# erv.envrsk_portfolio_risk_regular(date, positions)
#
# In the example above, workflow_risk_snapshot() is a function that takes a date and a list of positions 
# (each position is a dictionary containing an instrument_id and its quantity), and it returns a risk snapshot 
# for the given portfolio.
#
# Remember to refer to the library's documentation for comprehensive details about all the available functions, 
# their parameters, and the information they return. 
# 
# Using EnvisionRiskRaaS.py, you can access a plethora of risk management tools and services with just a few lines 
# of code. The library's user-friendly interface and robust capabilities make it a valuable addition to your risk 
# management toolkit.
#
# Happy coding!

envrsk_auth_log_in_interactively()

#################################################################################################################
#*** Available Instrument
#################################################################################################################
df_available_instruments = envrsk_instrument_search()

#################################################################################################################
#*** Request Risk Estimates for your bespoken portfolio
#################################################################################################################
# Define your portfolio 
my_portfolio_positions = pd.DataFrame(
    {"symbol": ["AAPL.US", "DANSKE.CO", "CashUSD", "AGG.US"],
     "position_type": ["single_stock", "single_stock", "cash", "etf"],
     "quantity": [129, 768, 69000, 89]})

# Add unique ID's to the positions

#****************************************************************************************************************
# *** Request unconditional risk estimates ***
#****************************************************************************************************************
portfolio_risk_regular = envrsk_portfolio_risk_regular(
    date = "2023-07-13", 
    positions = my_portfolio_positions,
    base_cur = "GBP") 

#Print the assumption behind the calculation
portfolio_risk_regular['Input']

#Print the result
portfolio_risk_regular['Output'].merge(
        portfolio_risk_regular['Positions_Mapped'][['symbol', 'uid', 'name']], 
        left_on='UID', 
        right_on='uid',
        how='left')[['UID', 'symbol', 'name', 'Location', 'PortfolioTreeDepthLevel', 'PortfolioType', 'VaR', 'ES']]

#****************************************************************************************************************
# *** Request conditional risk estimates ***
#****************************************************************************************************************
portfolio_risk_comp = envrsk_portfolio_risk_component(
    date = "2023-07-13", 
    positions = my_portfolio_positions,
    base_cur = "GBP") 

#Print the assumption behind the calculation
portfolio_risk_comp['Input']

#Print the result
portfolio_risk_comp['Output'].merge(
        portfolio_risk_comp['Positions_Mapped'][['symbol', 'uid', 'name']], 
        left_on='UID', 
        right_on='uid',
        how='left')[['UID', 'symbol', 'name', 'Location', 'PortfolioTreeDepthLevel', 'PortfolioType', 'VaR', 'ES']]