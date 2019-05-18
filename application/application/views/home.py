from flask import render_template

from application import api
from application.forms.iris_features import IrisFeaturesForm

from application.logic.predict import predict as predict_logic


@api.route('/', methods=['GET', 'POST'])
def home():
    form = IrisFeaturesForm()

    if form.validate_on_submit():
        prediction = predict_logic(
            FlowerID=form.FlowerID._value(),
            PetalLength=form.PetalLength._value(),
            PetalWidth=form.PetalWidth._value(),
            SepalLength=form.SepalLength._value(),
            SepalWidth=form.SepalWidth._value(),
        )
        return render_template('prediction.html', form=form, prediction=prediction)

    return render_template('prediction.html', form=form)
