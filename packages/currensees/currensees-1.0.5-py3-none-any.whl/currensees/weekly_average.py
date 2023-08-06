import requests

class WeeklyAverage:
    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to
        self.base_url = "https://currensees.com/v1/weekly_average"

    def fetch_weekly_average(self):
        url = f"{self.base_url}/{self.date_from}/{self.date_to}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return response.text