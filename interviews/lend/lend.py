from collections import defaultdict

import requests


url = "https://dataservice.accuweather.com/forecasts/v1/daily/5day/60449?apikey=Z1F1GUzpMaHfSKq7Qz3e7lqygFhPVliP&details=true"


def rules(condition, weather=""):
    ans = []
    
    if condition < 45: # Coat", "Winter jacket"
        ans.append("Coat")
        ans.append("Winter jacket")

    if condition >= 45 and condition <= 79: # Fleece", "Short Sleeves"
        ans.append("Fleece")
        ans.append("Short Sleeves")

    if condition > 80: # Shorts
        ans.append("Shorts")

    if weather == "rain":
        if condition > 50:
            ans.append("Rain coat")

    if weather == "snow":
        if condition > 50:
            ans.append("Snow Outfit")

    if weather == "ice":
        if condition > 50:
            ans.append("Shell jacket")

    return ans


def main():
    forecast = requests.get(url=url).json()
    forecasts = defaultdict(list)

    for day in forecast['DailyForecasts']:
        temp_max = day['Temperature']['Maximum']['Value']

        day_rain_prob = day['Day']['RainProbability']
        night_rain_prob = day['Night']['RainProbability']

        day_snow_prob = day['Day']['SnowProbability']
        night_snow_prob = day['Night']['SnowProbability']

        day_ice_prob = day['Day']['IceProbability']
        night_ice_prob = day['Night']['IceProbability']

        forecasts[day.get('Date')].extend(rules(temp_max))
        forecasts[day.get('Date')].extend(rules(day_rain_prob, weather="rain"))
        forecasts[day.get('Date')].extend(rules(night_rain_prob, weather="rain"))
        forecasts[day.get('Date')].extend(rules(day_snow_prob, weather="snow"))
        forecasts[day.get('Date')].extend(rules(night_snow_prob, weather="snow"))
        forecasts[day.get('Date')].extend(rules(day_ice_prob, weather="ice"))
        forecasts[day.get('Date')].extend(rules(night_ice_prob, weather="ice"))

    return forecasts


if __name__ == "__main__":
    ans = main()
    print(ans)
