from flask import Blueprint
from flask_restx import Api, Resource

api_bp = Blueprint('api_bp',__name__,url_prefix='/api')

api = Api(api_bp, doc='/doc', title='School Management System API', description='Global API, using Blueprint', version='1.0')

from .test import ns_test
api.add_namespace(ns_test)

@api.route('/default_test')
class Test1(Resource):
    def get(self):
        return {'hello':'world'}