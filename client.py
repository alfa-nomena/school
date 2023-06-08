#!/usr/bin/env python
import requests
from dotenv import dotenv_values
import pandas as pd
import us
from tqdm import tqdm


config=dotenv_values('.env')
APPKEY = config['APPKEY']
APPID = config['APPID']
URL = config['URL']
RESULTS= config['FILE']

params = {
    'appID': APPID,
    'appKey': APPKEY,
    'page':1,
    'perPage':20,
}

States = pd.DataFrame()
for state in tqdm([state.abbr for state in us.STATES], f'Retrieving data from {URL}'):
    params['st']=state
    raw_datas = requests.get(URL, params=params)
    data = raw_datas.json()
    current_school = pd.DataFrame(columns = ['Value', 'Number'])
    for school in data['schoolList']:
        for value in school['schoolYearlyDetails']:
            if value['year'] not in current_school.index:
                current_school.loc[value['year']] = 0
            current_school.loc[value['year'], 'Value'] += value['percentofAfricanAmericanStudents'] or 0
            current_school.loc[value['year'], 'Number'] += int(value['percentofAfricanAmericanStudents'] is not None)
    current_school['Value'] /= current_school['Number']
    results = current_school['Value']
    States.loc[state,results.index]=results
States = States.fillna(0)
States['states'] = list(map(us.states.lookup, States.index))
States = States.set_index('states', append=True).round(2)
print(f'Saving result in the file {RESULTS}.xlsx ...')
with pd.ExcelWriter('Results.xlsx') as xls:
    for year in States.columns:
        States.loc[:,year].sort_values(ascending=False).iloc[:5].to_excel(xls, sheet_name=f"Result for {year}")
    States.mean(axis=1).round(2).sort_values(ascending=False).iloc[:5].to_excel(xls, sheet_name="Global result")
print(f'The result is in the file: {RESULTS}.xlsx')