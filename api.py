"""
API calls
--> https://api.covid19api.com/world/total           : Worldwide status
--> https://api.covid19api.com/summary               : Worldwide country status
--> https://api.covid19api.com/dayone/country/india  : India status
"""

# import packages
import requests
import pandas as pd


class Covid19API:
    @staticmethod
    def world():
        """ Worldwide status """
        # API call
        response = requests.get('https://api.covid19api.com/world/total').json()

        # dict to store worldwide status
        world_status = dict()

        # total cases
        world_status['Total Cases'] = response['TotalConfirmed']
        # total deaths
        world_status['Deaths'] = response['TotalDeaths']
        # total recovered
        world_status['Recovered'] = response['TotalRecovered']
        # active cases
        world_status['Active Cases'] = response['TotalConfirmed'] - response['TotalDeaths'] - response['TotalRecovered']

        return world_status

    @staticmethod
    def world_summary():
        """ Worldwide country status """
        # API call
        response = requests.get('https://api.covid19api.com/summary').json()

        # dict to store worldwide status
        world = dict()

        # new cases
        world['New Cases'] = response['Global']['NewConfirmed']
        # total cases
        world['Total Cases'] = response['Global']['TotalConfirmed']
        # new deaths
        world['New Deaths'] = response['Global']['NewDeaths']
        # total deaths
        world['Total Deaths'] = response['Global']['TotalDeaths']
        # new recovered
        world['New Recovered'] = response['Global']['NewRecovered']
        # total recovered
        world['Total Recovered'] = response['Global']['TotalRecovered']
        # active cases
        world['Active Cases'] = world['Total Cases'] - world['Total Deaths'] - world['Total Recovered']

        # dict to store country wise status
        countries = dict()
        for i in range(len(response['Countries'])):
            # dict to store single country data
            country = dict()

            # country name
            country['Country'] = response['Countries'][i]['Country']
            # country code
            country['Country Code'] = response['Countries'][i]['CountryCode']
            # new cases
            country['New Confirmed'] = response['Countries'][i]['NewConfirmed']
            # total cases
            country['Total Confirmed'] = response['Countries'][i]['TotalConfirmed']
            # new deaths
            country['New Deaths'] = response['Countries'][i]['NewDeaths']
            # total deaths
            country['Total Deaths'] = response['Countries'][i]['TotalDeaths']
            # new recovered
            country['New Recovered'] = response['Countries'][i]['NewRecovered']
            # total recovered
            country['Total Recovered'] = response['Countries'][i]['TotalRecovered']
            # active cases
            country['Active Cases'] = country['Total Confirmed'] - country['Total Deaths'] - country['Total Recovered']

            # adding all country data into single dict
            countries[i] = country

        # country status: dict to dataframe
        countries_table = pd.DataFrame.from_dict(countries).transpose()

        return world, countries_table

    @staticmethod
    def india_summary():
        """ India status """
        # API call
        response = requests.get('https://api.covid19api.com/dayone/country/india').json()
        n = len(response)

        # dict to store india's day by day status
        status_by_day = dict()
        for i in range(n):
            # dict to store single day status
            day = dict()

            # date
            day['Date'] = response[i]['Date'][0:10]

            # confirmed cases
            day['Cases'] = response[i]['Confirmed']

            # new cases
            if i == 0:
                day['New Cases'] = response[i]['Confirmed']
            else:
                day['New Cases'] = response[i]['Confirmed'] - response[i - 1]['Confirmed']

            # total deaths
            day['Deaths'] = response[i]['Deaths']

            # new deaths
            if i == 0:
                day['New Deaths'] = response[i]['Deaths']
            else:
                day['New Deaths'] = response[i]['Deaths'] - response[i - 1]['Deaths']

            # total recovered
            day['Recovered'] = response[i]['Recovered']

            # new recovered
            if i == 0:
                day['New Recovered'] = response[i]['Recovered']
            else:
                day['New Recovered'] = response[i]['Recovered'] - response[i - 1]['Recovered']

            # active cases
            day['Active Cases'] = response[i]['Active']

            # adding day by day dat to single dict
            status_by_day[i] = day

        # India current status
        status_current = dict()

        # confirmed cases
        status_current['Cases'] = response[n - 1]['Confirmed']
        # new cases
        status_current['New Cases'] = response[n - 1]['Confirmed'] - response[n - 2]['Confirmed']
        # total deaths
        status_current['Deaths'] = response[n - 1]['Deaths']
        # new deaths
        status_current['New Deaths'] = response[n - 1]['Deaths'] - response[n - 2]['Deaths']
        # total recovered
        status_current['Recovered'] = response[n - 1]['Recovered']
        # new recovered
        status_current['New Recovered'] = response[n - 1]['Recovered'] - response[n - 2]['Recovered']
        # active cases
        status_current['Active'] = response[n - 1]['Active']

        # india day by day status: dict to dataframe
        status_by_day_table = pd.DataFrame.from_dict(status_by_day).transpose()

        return status_current, status_by_day_table
