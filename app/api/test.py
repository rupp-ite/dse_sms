from flask_restx import Namespace, Resource

ns_test = Namespace('test', description='Testing API', path='/test')

@ns_test.doc(responses={200: 'Success',400: 'Validation Error'}, description='This is the description of Test1 API')
@ns_test.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello':'world'}

@ns_test.route('/test1')
class Test1(Resource):
    def get(self):
        dt = {
            'id':1,
            'name':'Sok Dara'
        }
        return dt