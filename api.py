import requests
import pandas as pd


class Covid19API:
    @staticmethod
    def world():
        response = requests.get('https://api.covid19api.com/world/total').json()

        world_status = dict()
        world_status['Total Cases'] = response['TotalConfirmed']
        world_status['Deaths'] = response['TotalDeaths']
        world_status['Recovered'] = response['TotalRecovered']
        world_status['Active Cases'] = response['TotalConfirmed'] - response['TotalDeaths'] - response['TotalRecovered']

        return world_status

    @staticmethod
    def country_code():
        response = requests.get('https://api.covid19api.com/countries').json()

        country = dict()
        for i in range(len(response)):
            country[response[i]['Country'] + ' - ' + response[i]['ISO2']] = response[i]['Slug']

        return country

    @staticmethod
    def world_summary():
        response = requests.get('https://api.covid19api.com/summary').json()

        world = dict()
        world['New Cases'] = response['Global']['NewConfirmed']
        world['Total Cases'] = response['Global']['TotalConfirmed']
        world['New Deaths'] = response['Global']['NewDeaths']
        world['Total Deaths'] = response['Global']['TotalDeaths']
        world['New Recovered'] = response['Global']['NewRecovered']
        world['Total Recovered'] = response['Global']['TotalRecovered']
        world['Active Cases'] = world['Total Cases'] - world['Total Deaths'] - world['Total Recovered']

        countries = dict()
        for i in range(len(response['Countries'])):
            country = dict()
            country['Country'] = response['Countries'][i]['Country']
            country['Country Code'] = response['Countries'][i]['CountryCode']
            country['New Confirmed'] = response['Countries'][i]['NewConfirmed']
            country['Total Confirmed'] = response['Countries'][i]['TotalConfirmed']
            country['New Deaths'] = response['Countries'][i]['NewDeaths']
            country['Total Deaths'] = response['Countries'][i]['TotalDeaths']
            country['New Recovered'] = response['Countries'][i]['NewRecovered']
            country['Total Recovered'] = response['Countries'][i]['TotalRecovered']

            countries[i] = country

        countries_table = pd.DataFrame.from_dict(countries).transpose()

        return world, countries_table

    @staticmethod
    def india_summary():
        response = requests.get('https://api.covid19api.com/dayone/country/india').json()
        n = len(response)

        status_by_day = dict()
        for i in range(n):
            day = dict()
            day['Date'] = response[i]['Date'][0:10]
            day['Cases'] = response[i]['Confirmed']
            if i == 0:
                day['New Cases'] = response[i]['Confirmed']
            else:
                day['New Cases'] = response[i]['Confirmed'] - response[i - 1]['Confirmed']
            day['Deaths'] = response[i]['Deaths']
            if i == 0:
                day['New Deaths'] = response[i]['Deaths']
            else:
                day['New Deaths'] = response[i]['Deaths'] - response[i - 1]['Deaths']
            day['Recovered'] = response[i]['Recovered']
            if i == 0:
                day['New Recovered'] = response[i]['Recovered']
            else:
                day['New Recovered'] = response[i]['Recovered'] - response[i - 1]['Recovered']
            day['Active Cases'] = response[i]['Active']
            status_by_day[i] = day

        status_current = dict()
        status_current['Cases'] = response[n - 1]['Confirmed']
        status_current['New Cases'] = response[n - 1]['Confirmed'] - response[n - 2]['Confirmed']
        status_current['Deaths'] = response[n - 1]['Deaths']
        status_current['New Deaths'] = response[n - 1]['Deaths'] - response[n - 2]['Deaths']
        status_current['Recovered'] = response[n - 1]['Recovered']
        status_current['New Recovered'] = response[n - 1]['Recovered'] - response[n - 2]['Recovered']
        status_current['Active'] = response[n - 1]['Active']

        status_by_day_table = pd.DataFrame.from_dict(status_by_day).transpose()

        return status_current, status_by_day_table
