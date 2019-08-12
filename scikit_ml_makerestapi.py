from flask import Flask
from flask_restplus import Resource, Api, reqparse

import sys
from scikit_ml_loadmodel2 import scikit_learn_ml

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')

name_space = api.namespace('main/aaa/', description='Main APIs')
id_parser = api.parser()


# parameters for url key/value parameters 
id_parser.add_argument('function',      type=str, help='write your function name')
id_parser.add_argument('accessKey',     type=str, help='accessKey')
id_parser.add_argument('id',             type=str, help='test id')
id_parser.add_argument('password',      type=str, help='test password')

# parameters body parameters 
# (Caution) it uses for only HTTP Post Method.)
id_parser.add_argument('massive_data', type=list, help='massive_data', location='json')

{"product" : 
    [
        {
            "product_id" : 33,
            "total_price": 50,
            "quantity" : 2
        },
        {
            "product_id" : 22,
            "total_price": 33,
            "quantity" : 4
        }
    ]
}

# order = api.model("product" : { "product_id" : fields.String,
# "total_price":fields.Integer,
# "quantity":fields.Integer
# })

# uri argument 
@api.doc(params={'function':'executing function name'})

# parameters
@api.doc(parser=id_parser)
# @api.expect([order])
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
        #massive_data  = reqparse.request.args.get('massive_data')
        json_data       = reqparse.request.json
        customer_id     = json_data['customer_id']
        service_id      = json_data['service_id']
        customer_name  = json_data['customer_name']
        site_name       = json_data['site_name']
        service_type    = json_data['service_type']

        print("customer_id = [" + customer_id + "]")
        print("service_id = [" + service_id + "]")
        print("customer_name = [" + customer_name + "]")
        print("site_name = [" + site_name + "]")
        print("service_type = [" + service_type + "]")

        call_func      = getattr(self, function, func_not_found)()
        return {'hello': 'world test id = ['+ disp_id + ']' + disp_password + call_func }

    def test_func1(self) :
        disp_id        = reqparse.request.args.get('id')
        disp_password = reqparse.request.args.get('password')
        

        return str(scikit_learn_ml(disp_id, disp_password))
        #return "You just executed test_func1"

    def test_func2(self) :
        return "You just executed test_func2"

#api.add_resource(HelloWorld, '/modelergateway/uuid12313231/<function>')



"""
for obj in dir(HelloWorld) : 
   print(obj)
"""

if __name__ == '__main__':
    app.run(debug=True)
