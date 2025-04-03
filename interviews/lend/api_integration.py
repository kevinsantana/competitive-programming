import argparse
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

import requests
from dotenv import load_dotenv
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from constants import DATE_FORMAT, DEV_ENVS, URL


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )
    api_key: str = ""
    env: str = "dev"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv("env", "dev") not in DEV_ENVS:
            load_dotenv(dotenv_path=None, override=True)


config = Config()


def main(n_days: int, city_code: str):
    try:
        logger.info(
            f"Start fetching data from weather API. Days {n_days}, City {city_code}, URL {URL}"
        )
        url = URL.format(n_days=n_days, city_code=city_code, api_key=config.api_key)
        forecasts = requests.get(url=url)
        if forecasts.status_code != 200:
            text = "Unexpected error occured in main func. "
            f"Status code {forecasts.status_code}, Response {forecasts.text}"
            logger.exception(text)
            raise Exception(text)

        forecasts = forecasts.json()
        weather_forecast = {"forecasts": []}
        for day in forecasts["DailyForecasts"]:
            date_formatted = _format_date(day["Date"])
            logger.info(f"Fetching weather data on day {date_formatted}")
            max_temp = day["Temperature"]["Maximum"]["Value"]
            max_temp_cloth = _max_temp_clothing(max_temp)
            weather_prob = _get_highest_prob_weather(day)
            weather_clothing = _clothing_from_weather(*weather_prob)
            forecast = _format_response(
                date=date_formatted,
                max_temp_cloth=max_temp_cloth,
                weather_clothing=weather_clothing,
            )
            weather_forecast["forecasts"].append(forecast)
            logger.info(
                f"Fetched weather clothing. Max temp {max_temp}, Max temp clothing {max_temp_cloth}, "
                f"Weather probability {weather_prob}, Weather clothing {weather_clothing}"
            )

        return weather_forecast

    except Exception as e:
        text = f"Unexpected error on main func: {str(e)}"
        logger.exception(text)
        raise Exception(text)


def get_parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--n-days",
        help="Number of days to fetch from the weather API.",
        default=5,
        type=int,
        dest="n_days",
    )
    parser.add_argument(
        "-c",
        "--city-code",
        default="45881",
        dest="city_code",
        type=str,
        help="City code to fetch from weather API. Options are "
        "60449 (Santiago), 45881 (São Paulo), 349727 (New York), 101924 (Beijing), 127164 (Cairo).",
    )
    return parser


def _format_date(date: str) -> str:
    try:
        datetime_obj = datetime.fromisoformat(date)
        dt_formatted = datetime_obj.strftime(DATE_FORMAT)
        return dt_formatted

    except Exception as e:
        text = f"Unexpected error occured in _format_date: {str(e)}"
        logger.exception(text)
        raise Exception(text)


def _max_temp_clothing(temp: int) -> Optional[Union[str, Tuple[str, str]]]:
    try:
        if temp < 45:
            return "Coat", "Winter Jacket"
        if temp >= 45 and temp <= 79:
            return "Fleece", "Short Sleeves"
        if temp >= 80:
            return "Shorts"

    except Exception as e:
        text = f"An unexpected error occured in _max_temp_clothing: {str(e)}"
        logger.exception(text)
        raise Exception(text)


def _get_highest_prob_weather(day: Dict[str, str]) -> Tuple[int, str]:
    try:
        day_rain_prob = day["Day"]["RainProbability"]
        night_rain_prob = day["Night"]["RainProbability"]
        day_snow_prob = day["Day"]["SnowProbability"]
        night_snow_prob = day["Night"]["SnowProbability"]
        day_ice_prob = day["Day"]["IceProbability"]
        night_ice_prob = day["Night"]["IceProbability"]
        probabilities = [
            (max(day_rain_prob, night_rain_prob), "rain"),
            (max(day_snow_prob, night_snow_prob), "snow"),
            (max(day_ice_prob, night_ice_prob), "ice"),
        ]
        return max(probabilities, key=lambda x: x[0])

    except Exception as e:
        text = f"An unexpected error occured in _get_highest_prob_weather {str(e)}"
        logger.exception(text)
        raise Exception(text)


def _clothing_from_weather(prob: int, weather: str) -> str:
    cloth = ""
    if weather == "rain":
        cloth = "Rain Coat"
    elif weather == "snow":
        cloth = "Snow Outfit"
    elif weather == "ice":
        cloth = "Shell Jacket"

    return cloth if prob > 50 else None


def _format_response(
    date: str, max_temp_cloth: str, weather_clothing: str
) -> Dict[str, List[str]]:
    cloths = []
    if isinstance(max_temp_cloth, tuple):
        cloths.extend(max_temp_cloth)
    else:
        cloths.append(max_temp_cloth)

    if weather_clothing:
        cloths.append(weather_clothing)

    return {"date": date, "cloths": cloths}


if __name__ == "__main__":
    parser = get_parse_args()
    args = parser.parse_args()
    ans = main(args.n_days, args.city_code)
    print(ans)
