from flask import Blueprint
import app.controllers as controllers

bp = Blueprint("series", __name__, url_prefix=("/series"))



bp.post("")(controllers.create)

bp.get("")(controllers.series)

bp.get("/<serie_id>")(controllers.select_by_id)
