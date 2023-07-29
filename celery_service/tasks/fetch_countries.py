from typing import List

import requests
from sqlalchemy.orm import Session

from celery_service.celery import celery_app
from helpers.constants import rest_countries_url
from models import Country
from db import get_db


@celery_app.task
def fetch_countries_data():
    """
    Fetch countries data

    Returns:
        None
    """
    db = next(get_db())
    response = requests.get(rest_countries_url)
    if response.status_code == 200:
        countries_data = response.json()
        save_countries_to_db(db, countries_data)


def save_countries_to_db(db: Session, countries_data: List[dict]):
    """
    Parse the countries data and save it into the database.

    Args:
        db: Session
        countries_data: List of country data dictionaries

    Returns:
        None
    """
    country_names = [country_data["name"]["common"] for country_data in countries_data]
    existing_countries = db.query(Country).filter(Country.name.in_(country_names)).all()
    existing_country_names = set(country.name for country in existing_countries)

    countries_list = []
    for country_data in countries_data:
        country_name = country_data["name"]["common"]
        if country_name in existing_country_names:
            continue

        country = Country(
            name=country_data["name"]["common"],
            population=country_data["population"],
            area=country_data["area"],
            data=country_data,
        )
        countries_list.append(country)
    db.bulk_save_objects(countries_list)
    db.commit()
