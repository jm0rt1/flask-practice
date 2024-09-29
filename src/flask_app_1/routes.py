from flask import Blueprint, render_template, redirect, url_for, flash
from flask_app_1.forms import ExampleForm
from flask_app_1.models import ExampleModel
from flask_app_1 import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/form', methods=['GET', 'POST'])
def form():
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(name=form.name.data)
        db.session.add(example)
        db.session.commit()
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('main.home'))

    # Query the database to get all entries in ExampleModel
    table_data = ExampleModel.query.all()

    return render_template('form.html', form=form, table_data=table_data)
