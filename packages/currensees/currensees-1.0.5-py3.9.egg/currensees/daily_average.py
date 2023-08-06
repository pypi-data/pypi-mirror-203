import requests

class DailyAverage:
    def __init__(self, date):
        self.date = date
        self.base_url = "https://currensees.com/v1/daily_average"

    def fetch_daily_average(self):
        url = f"{self.base_url}/{self.date}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return response.text