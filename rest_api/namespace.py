from io import BytesIO
from flask_restplus import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage
from ML.classifier import train_classifier,make_predictions,get_df

ns_1 = Namespace('ML model')
upload_parser_tr = reqparse.RequestParser()
upload_parser_tr.add_argument('training_file', location='files', type=FileStorage, required=True, help='training file in csv format')
upload_parser_tr.add_argument('classification_variable', default='species', choices=['species'],help='dependent varible in the ML model')

@ns_1.route('/training')
class Statistics(Resource):
    @ns_1.expect(upload_parser_tr, validate=False)
    def post(self):
        args = upload_parser_tr.parse_args()
        mem_file = BytesIO()
        args['training_file'].save(mem_file)
        train_df = get_df(mem_file.getvalue().decode('UTF-8'))
        result = train_classifier(train_df,args['classification_variable'])
        return result
    
upload_parser_te = reqparse.RequestParser()
upload_parser_te.add_argument('testing_file', location='files', type=FileStorage, required=True, help='testing file in csv format')
upload_parser_te.add_argument('classification_variable', default='species', choices=['species'],help='dependent varible in the ML model')

@ns_1.route('/testing')
class Paths(Resource):
    @ns_1.expect(upload_parser_te, validate=False)
    def post(self):
        args = upload_parser_te.parse_args()
        mem_file = BytesIO()
        args['testing_file'].save(mem_file)
        test_df = get_df(mem_file.getvalue().decode('UTF-8'))
        result = make_predictions(test_df,args['classification_variable'])
        return result

