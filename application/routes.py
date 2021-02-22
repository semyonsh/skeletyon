from flask import current_app as app
from flask import redirect, render_template, url_for, flash
from .forms import ExampleForm
from .models import ExampleTable, db


site_name = app.config['SITE_NAME']


@app.route('/', methods=('GET', 'POST'))
def index():
    form = ExampleForm()

    if form.validate_on_submit():
        item = ExampleTable(username=form.username.data,
                    )
        db.session.add(item)
        try:
            db.session.commit()
        except:
            flash('This nickname already exists, please try something else', 'warning')
            return redirect(url_for('index'))

        return redirect(url_for('index'))

    return render_template('index.html', site_name=site_name, form=form, )


@app.errorhandler(404)
def page_not_found(e):
    flash('Something went wrong, back to the homepage with you', 'warning')
    return redirect(url_for('index'))
