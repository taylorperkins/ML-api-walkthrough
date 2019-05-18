from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class IrisFeaturesForm(FlaskForm):
    FlowerID = IntegerField('FlowerID', validators=[DataRequired()])
    SepalLength = FloatField('SepalLength', validators=[DataRequired()])
    SepalWidth = FloatField('SepalWidth', validators=[DataRequired()])
    PetalLength = FloatField('PetalLength', validators=[DataRequired()])
    PetalWidth = FloatField('PetalWidth', validators=[DataRequired()])

    submit = SubmitField('Submit')
