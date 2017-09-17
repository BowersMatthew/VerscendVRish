from flask import Flask
from flask_restful import Resource, Api, reqparse
import csv
from Data import Data
from DataProcessing import DataProcessing

app = Flask(__name__)
api = Api(app)



# columns should be a list containing the numbers you want to return
def temp_csv_parser(arg_lvl, columns, surfacetype=None):
    with open("test.txt", 'r') as csv_file:
        data_sheet = csv.reader(csv_file)
        array_result = []
        for row in data_sheet:
            result_row = []
            if str(row[1]) == arg_lvl:
                print(row)
                result_row.append(row[1])
                # remember columns will be in list order
                for i in columns:
                    result_row.append(int(row[int(i)]))

            #print(result_row)
            array_result.append(result_row)

    return array_result


#class example(Resource):
#    def get(self):
#        return {'hello': 'world'}
class data1(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('service', type=str)
        args = parser.parse_args()
        test = Data()
        test.setLocation('all')
        test.data.append('state')
        test.setDateRange(5)
        test.setService(args['service'])
        test.setAxisX('number_of_fee_for_service_beneficiaries')
        test.setAxisY('number_of_providers')
        test.setAxisZ('number_of_users')
        proccess = DataProcessing(test)
        proccess.getData()
        return proccess.createJSON()


class data2(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('service', type=str)
        parser.add_argument('location', type=str)
        args = parser.parse_args()
        test = Data()
        test.setDateRange(5)
        test.setLocation(args['location'])
        test.data.append('state')
        test.setService(args['service'])
        test.setAxisX('number_of_fee_for_service_beneficiaries')
        test.setAxisY('number_of_providers')
        test.setAxisZ('number_of_users')
        proccess = DataProcessing(test)
        proccess.getData()
        return proccess.createJSON()

class data_sheet(Resource):
    def get(self):

        # Parser stuff
        parser = reqparse.RequestParser()
        parser.add_argument('location', type=str)
        parser.add_argument('service', type=str)
        parser.add_argument('AxisX', type=str)
        parser.add_argument('AxisY', type=str)
        parser.add_argument('AxisZ', type=str)
        parser.add_argument('date_range', type=int)
        args = parser.parse_args() # Returns dictionary
        print(args)
        test = Data()
        test.setLocation(args['location'])
        test.setService(args['service'])
        test.setDateRange(args['date_range'])
        test.setAxisX(args['AxisX'])
        test.setAxisY(args['AxisY'])
        test.setAxisZ(args['AxisZ'])
        proccess = DataProcessing(test)
        proccess.getData()
        return proccess.createJSON()


api.add_resource(data_sheet, '/data')
# adds a class onto the site
api.add_resource(data1,'/data1')
api.add_resource(data2,'/data2')

app.run(port=8080, debug=True)
# this will run the server