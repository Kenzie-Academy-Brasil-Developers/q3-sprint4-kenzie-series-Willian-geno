from http import HTTPStatus
from tkinter import S
from flask import jsonify, request
from itsdangerous import Serializer
from app.models.series_modle import Series
from flask import request
from psycopg2.errors import UniqueViolation


def create():
    data = request.get_json()
    
    serie = Series(**data)
    try:
        inserted_series = serie.cretate_serie()
    except UniqueViolation as e:
        return {"error": "serie alrady registerd"}, HTTPStatus.UNPROCESSABLE_ENTITY
    
    serie_columns = [
        "id",
        "serie", 
        "seasons", 
        "released_date", 
        "genre", 
        "imdb_rating"
    ]

    seriealized_serie = dict(zip(serie_columns, inserted_series))

    return seriealized_serie, HTTPStatus.CREATED
    
def series():

    series = Series.read_series()

    serie_columns = [
        "id",
        "serie", 
        "seasons", 
        "released_date", 
        "genre", 
        "imdb_rating"
    ]

    serializer_series = [dict(zip(serie_columns, seire)) for seire in series]

    return jsonify(serializer_series), HTTPStatus.OK

def select_by_id(serie_id):
    
    serie = Series.read_series_by_id(serie_id)

    if not serie:
        return jsonify([]), HTTPStatus.NOT_FOUND
    
    serie_columns = [
        "id",
        "serie", 
        "seasons", 
        "released_date", 
        "genre", 
        "imdb_rating"
    ]

    serializer_series = dict(zip(serie_columns, serie))

    return jsonify(serializer_series), HTTPStatus.OK