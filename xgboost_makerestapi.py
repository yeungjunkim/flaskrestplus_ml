from flask import Flask
from flask_restplus import Resource, Api, reqparse

import sys


from xgboost_loadmodel2 import xgboost_model_predict

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')
name_space = api.namespace('main/aaa/', description='Main APIs')



id_parser = api.parser()
# uri argument 
id_parser.add_argument('function', type=str, help='write your function name')
# parameters
id_parser.add_argument('accessKey', type=str, help='accessKey')
id_parser.add_argument('id', type=str, help='test id')
id_parser.add_argument('password', type=str, help='test password')

# uri argument 
@api.doc(params={'function':'executing function name'})
# parameters
@api.doc(parser=id_parser)
@api.route('/modelergateway/uuid12313231/<function>')
class HelloWorld(Resource):
    
    def get(self, function):
        def func_not_found():
            return ("No Function Found!")
        
        disp_id        = reqparse.request.args.get('id')
        disp_password = reqparse.request.args.get('password')
        call_func      = getattr(self, function, func_not_found)()
        return {'hello': 'world test id = ['+ disp_id + ']' + disp_password + call_func }

    def post(self, function):
        def func_not_found():
            return ("No Function Found!")

        disp_id        = reqparse.request.args.get('id')
        disp_password = reqparse.request.args.get('password')
        call_func      = getattr(self, function, func_not_found)()
        return {'hello': 'world test id = ['+ disp_id + ']' + disp_password + call_func }

    def test_func1(self) :
        disp_id        = reqparse.request.args.get('id')
        disp_password = reqparse.request.args.get('password')
        
        return str(xgboost_model_predict(disp_id, disp_password))
        #return "You just executed test_func1"

    def test_func2(self) :
        return "You just executed test_func2"



if __name__ == '__main__':
    app.run(debug=True)
