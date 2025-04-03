import argparse
import os
from datetime import datetime
from typing import Dict, Optional, Tuple, Union

import requests
from dotenv import load_dotenv
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from constants import DATE_FORMAT, DEV_ENVS, URL


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    env: str = "dev"
    api_key: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv("ENV") in DEV_ENVS:
            load_dotenv(".env")


config = Config()


def main(n_days: int, city_code: str):
    try:
        url = URL.format(n_days=n_days, city_code=city_code, api_key=config.api_key)
        logger.info(
            f"Fetching data from weather API. Days {n_days}, City {city_code}"
            f" on URL {url}"
        )
        forecast = requests.get(url)
        if forecast.status_code != 200:
            logger.exception(
                "Error to fetch data from API. Status code: "
                f"{forecast.status_code}. Response {forecast.text}"
            )
            raise Exception(
                "Error to fetch data from API. Status code: "
                f"{forecast.status_code}. Response {forecast.text}"
            )

        forecast = forecast.json()
        forecasting = {"forecasts": []}
        for day in forecast["DailyForecasts"]:
            logger.info(f"Fetching day {day['Date']}")
            day_formatted = _format_date(day["Date"])
            day_max_temp = day["Temperature"]["Maximum"]["Value"]
            max_temp_cloth = _max_temp_cloth(day_max_temp)
            highest_prob_weather = _get_highest_prob_weather(day=day)
            cloth_from_day_weather = _cloth_from_weather(*highest_prob_weather)
            cloths = []

            if isinstance(max_temp_cloth, tuple):
                cloths.extend(max_temp_cloth)
            else:
                cloths.append(max_temp_cloth)

            if cloth_from_day_weather:
                cloths.append(cloth_from_day_weather)

            forecasting["forecasts"].append({"date": day_formatted, "cloths": cloths})

        logger.success("Finished fetching data from weather API.")
        return forecasting

    except Exception as e:
        logger.exception(f"An unexpected exception occurred: {str(e)}")
        raise Exception(f"An unexpected exception occurred: {str(e)}")


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--n-days",
        default=5,
        type=int,
        dest="n_days",
        help="Number of days to fetch from wether API. Defaults to 5.",
    )
    parser.add_argument(
        "-c",
        "--city",
        dest="city_code",
        default="45881",
        type=str,
        choices=["60449", "45881", "349727", "101924", "127164"],
        help="Code maps to a city in API. Choices are"
        "60449 (Santiago), 45881 (São Paulo), 349727 (New York), 101924 (Beijing), 127164 (Cairo)",
    )

    return parser


def _format_date(datetime_str: str) -> str:
    try:
        datetime_obj = datetime.fromisoformat(datetime_str)
        formatted_date_str = datetime_obj.strftime(DATE_FORMAT)
        return formatted_date_str

    except Exception as e:
        logger.exception(f"An unexpected error occured in _format_date: {str(e)}")
        raise


def _max_temp_cloth(temp: int) -> Optional[Union[str, Tuple[str, str]]]:
    try:
        if temp < 45:
            return "Coat", "Winter Jacket"

        if temp >= 45 and temp <= 79:
            return "Fleece", "Short Sleeves"

        if temp > 80:
            return "Shorts"

    except Exception as e:
        logger.exception(f"An unexpected error occured in _max_temp_cloth: {str(e)}")
        raise


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
        logger.exception(
            f"An unexpected error occured in _get_highest_prob_weather: {str(e)}"
        )
        raise


def _cloth_from_weather(prob: int, weather: str):
    if weather == "rain":
        if prob > 50:
            return "Rain coat"

    if weather == "snow":
        if prob > 50:
            return "Snow Outfit"

    if weather == "ice":
        if prob > 50:
            return "Shell jacket"

    return None


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    ans = main(args.n_days, args.city_code)
    print(ans)
