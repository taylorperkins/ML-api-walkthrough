from marshmallow import Schema, fields


def _required_err_config(x):
    return {
        'required': {'message': f'{x} required'},
        'code': 400
    }


class RequestSchema(Schema):
    # id of the flower / request?
    FlowerID = fields.Int(required=True, error_messages=_required_err_config('FlowerID'))

    # Values to be used in predicting flower category
    SepalLength = fields.Float(required=True, error_messages=_required_err_config('SepalLength'))
    SepalWidth = fields.Float(required=True, error_messages=_required_err_config('SepalWidth'))
    PetalWidth = fields.Float(required=True, error_messages=_required_err_config('PetalWidth'))
    PetalLength = fields.Float(required=True, error_messages=_required_err_config('PetalLength'))


class ResponseSchema(Schema):
    # id of the flower / request?
    FlowerID = fields.Int(required=True, error_messages=_required_err_config('FlowerID'))

    # label of prediction
    Species = fields.Str(required=True, error_messages=_required_err_config('Species'))
