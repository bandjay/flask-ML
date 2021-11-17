from flask_restplus import Api

from .namespace import ns_1

api = Api(
    title='ML model',
    version='1.0',
    description='Swagger REST API for Machine learnning model',
)
    
api.add_namespace(ns_1)
