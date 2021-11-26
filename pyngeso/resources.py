from typing import Dict

api_resource_ids: Dict[str, Dict[str, str]] = {
    "historic-day-ahead-demand-forecast": {
        "id": "9847e7bb-986e-49be-8138-717b25933fbb",
        "url": "https://data.nationalgrideso.com/demand/1-day-ahead-demand-forecast/r/historic_day_ahead_demand_forecasts"
    },
    "day-ahead-demand-forecast": {
        "id": "aec5601a-7f3e-4c4c-bf56-d8e4184d3c5b",
        "url": "https://data.nationalgrideso.com/demand/1-day-ahead-demand-forecast/r/day_ahead_national_demand_forecast"
    },
    "historic-2day-ahead-demand-forecast": {
        "id": "24abd271-5936-45c7-85f4-2a6b450ef6b7",
        "url": "https://data.nationalgrideso.com/demand/2-day-ahead-demand-forecast/r/historic_2_day_ahead_demand_forecasts"
    },
    "2day-ahead-demand-forecast": {
        "id": "cda26f27-4bb6-4632-9fb5-2d029ca605e1",
        "url": "https://data.nationalgrideso.com/demand/2-day-ahead-demand-forecast/r/2_day_ahead_demand_forecast"
    },
    "historic-day-ahead-wind-forecast": {
        "id": "7524ec65-f782-4258-aaf8-5b926c17b966",
        "url": "https://data.nationalgrideso.com/demand/day-ahead-wind-forecast/r/historic_day_ahead_wind_forecasts"
    },
    "day-ahead-wind-forecast": {
        "id": "b2f03146-f05d-4824-a663-3a4f36090c71",
        "url": "https://data.nationalgrideso.com/demand/day-ahead-wind-forecast/r/day_ahead_wind_forecast"
    }
}

file_resource_ids: Dict[str, Dict[str, str]] = {
    "historic-generation-mix": {
        "dataset_id": "88313ae5-94e4-4ddc-a790-593554d8c6b9",
        "resource_id": "f93d1835-75bc-43e5-84ad-12472b180a98",
        "filename": "df_fuel_ckan.csv",
        "url": "https://data.nationalgrideso.com/carbon-intensity1/historic-generation-mix"
    }
}
