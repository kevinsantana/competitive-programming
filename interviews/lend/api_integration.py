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
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    api_key: str = ""
    env: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv("ENV", "dev") not in DEV_ENVS:
            load_dotenv(dotenv_path=None, override=True)


config = Config()


def main(n_days: int, city_code: str):
    try:
        url = URL.format(n_days=n_days, city_code=city_code, api_key=config.api_key)
        logger.info(
            f"Fetching data from weather API. With days {n_days}, city {city_code} and URL {URL}"
        )
        forecasts = requests.get(url)
        if forecasts.status_code != 200:
            logger.exception("Exception while fetching data from weather API.")
            raise Exception(
                "Unexpected error while fetching data from weather API."
                f"Code {forecasts.status_code} Body {forecasts.text}"
            )
        forecasts = forecasts.json()
        weather_forecast = {"forecasts": []}

        for day in forecasts["DailyForecasts"]:
            logger.info(f"Fetching day {day['Date']} weather data")
            day_formatted = _format_date(day["Date"])
            max_temp = day["Temperature"]["Maximum"]["Value"]
            max_temp_cloth = _max_temp_cloth(max_temp)
            logger.info(f"Cloth for maximum temperature {max_temp}: {max_temp_cloth}")
            weather_prob = _get_prob_from_weather(day)
            cloth_for_weather = _cloth_for_weather(*weather_prob)
            logger.info(
                f"Cloth for weather {weather_prob[1]} with prob {weather_prob[0]}"
            )
            forecast = _format_response(
                day_formatted, max_temp_cloth, cloth_for_weather
            )
            weather_forecast["forecasts"].append(forecast)

        return weather_forecast

    except Exception as e:
        logger.exception(f"An unexcepted exception occured: {str(e)}")
        raise Exception


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--n-days", type=int, default=5, help="", dest="n_days")
    parser.add_argument(
        "-c",
        "--city-code",
        type=str,
        dest="city_code",
        choices=["60449", "45881", "349727", "101924", "127164"],
        help="",
        default="45881",
    )
    return parser


def _format_date(date: str) -> str:
    try:
        datetime_obj = datetime.fromisoformat(date)
        formatted_date = datetime_obj.strftime(DATE_FORMAT)
        return formatted_date
    except Exception as e:
        logger.exception(f"Unexpected error on _format_date: {str(e)}")
        raise Exception(f"Unexpected error on _format_date: {str(e)}")


def _max_temp_cloth(temp: int) -> Optional[Union[str, Tuple[str, str]]]:
    if temp < 45:
        return "Coat", "Winter jacket"

    if temp >= 45 and temp <= 79:
        return "Fleece", "Short Sleeves"

    if temp >= 80:
        return "Shorts"


def _get_prob_from_weather(day: Dict[str, str]) -> Tuple[int, str]:
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


def _cloth_for_weather(prob: int, weather: str) -> str:
    if weather == "rain":
        if prob > 50:
            return "Rain Coat"

    if weather == "snow":
        if prob > 50:
            return "Snow Outfit"

    if weather == "ice":
        if prob > 50:
            return "Shell Jacket"


def _format_response(
    date: str, max_temp_cloth: Union[str, Tuple[str, str]], cloth_weather: str
) -> Dict[str, List[str]]:
    cloths = []
    if isinstance(max_temp_cloth, tuple):
        cloths.extend(max_temp_cloth)
    else:
        cloths.append(max_temp_cloth)
    cloths.append(cloth_weather)

    return {"date": date, "cloths": cloths}


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    ans = main(args.n_days, args.city_code)
    print(ans)
