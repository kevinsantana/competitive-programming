import argparse
import os
from datetime import datetime
from typing import Dict, List, Union, Tuple

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv("ENV") not in DEV_ENVS:
            load_dotenv(dotenv_path=None, override=True)


config = Config()


def main(n_days: int, city_code: str):
    try:
        logger.info("Starting to fetch data form API")
        forecasts = {"forecast": []}
        url_forecast = URL.format(
            n_days=n_days, city_code=city_code, api_key=config.api_key
        )
        forecast = requests.get(url=url_forecast)
        if forecast.status_code != 200:
            logger.exception(
                "Error requesting external API."
                f"Status code {forecast.status_code}. Response {forecast.text}"
            )
        forecast_data = forecast.json()

        for day in forecast_data["DailyForecasts"]:
            logger.info(f"Processing day {day.get('Date')}")
            day_formatted = _convert_datetime_string(day.get("Date"))
            temp_max = day["Temperature"]["Maximum"]["Value"]
            temp_max_cloth = _max_temperature_rule(temp_max)
            highest_weather_day = _get_highest_prob_weather(day)
            weather_prob_cloth = _apply_rule(weather=highest_weather_day)
            
            clothes_list = []
            if isinstance(temp_max_cloth, tuple):
                clothes_list.extend(list(temp_max_cloth))
            else:
                clothes_list.append(temp_max_cloth)
            
            if weather_prob_cloth:
                clothes_list.append(weather_prob_cloth)

            forecasts["forecast"].append(
                {"date": day_formatted, "clothes": clothes_list}
            )

        logger.success("Finished fetching data from API.")
        return forecasts

    except Exception as e:
        logger.exception(f"An unexpected error occured: {str(e)}")
        raise Exception(f"An unexpected error occured: {str(e)}")


def get_arg_parser():
    parser = argparse.ArgumentParser(
        description=("Fetch wether data from AcuWeather API")
    )
    parser.add_argument(
        "-n",
        "--n-days",
        dest="n_days",
        default=5,
        type=int,
        help="Number of days to fetch from API",
    )
    parser.add_argument(
        "-c",
        "--city-code",
        choices=["60449", "45881", "349727", "101924", "127164"],
        dest="city_code",
        default="45881",
        help="City code, from where the weather should be forescasted.",
    )
    return parser


def _max_temperature_rule(max_temp: int) -> Union[str, Tuple[str, str]]:
    try:
        if max_temp < 45:  # Coat", "Winter jacket"
            return "Coat", "Winter jacket"

        if max_temp >= 45 and max_temp <= 79:  # Fleece", "Short Sleeves"
            return "Fleece", "Short Sleeves"

        if max_temp > 80:
            return "Shorts"

    except Exception as e:
        logger.exception(f"Exception on _max_temperature_rule: {str(e)}")
        raise


def _apply_rule(weather: str) -> Union[str, None]:
    try:
        if weather == "rain":
            return "Rain Coat"

        if weather == "snow":
            return "Snow Outfit"

        if weather == "ice":
            return "Shell Jacket"
        return None

    except Exception as e:
        logger.exception(f"Exception on _apply_rule: {str(e)}")
        raise


def _get_highest_prob_weather(day: Dict[str, str]) -> str:
    try:
        day_rain_prob = day["Day"]["RainProbability"]
        night_rain_prob = day["Night"]["RainProbability"]
        day_snow_prob = day["Day"]["SnowProbability"]
        night_snow_prob = day["Night"]["SnowProbability"]
        day_ice_prob = day["Day"]["IceProbability"]
        night_ice_prob = day["Night"]["IceProbability"]
        prob_weather = [
            (max(day_rain_prob, night_rain_prob), "rain"),
            (max(day_snow_prob, night_snow_prob), "snow"),
            (max(day_ice_prob, night_ice_prob), "ice"),
        ]
        return max(prob_weather, key=lambda x: x[0])[1]

    except Exception as e:
        logger.exception(f"Exception on _get_highest_prob_weather: {str(e)}")
        raise


def _convert_datetime_string(datetime_str: str) -> str:
    try:
        datetime_obj = datetime.fromisoformat(datetime_str)
        formatted_date_str = datetime_obj.strftime(DATE_FORMAT)
        return formatted_date_str

    except ValueError:
        logger.exception("Exception to convert datetime string.")
        raise ValueError(f"Error: Invalid datetime string format: {datetime_str}")


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    ans = main(args.n_days, args.city_code)
    print(ans)
