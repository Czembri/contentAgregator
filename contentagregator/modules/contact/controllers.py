from contentagregator import app, db, mail
from contentagregator.config import MAIL_SENDER, MAIL_RECEIVER

from flask_mail import Message
from flask import render_template, redirect, url_for, Blueprint, request, flash


contact_module = Blueprint('contact',__name__, static_folder='static', template_folder='templates', url_prefix='/contact')

@app.route('/contact')
def contact_form_view():
    return render_template('contact.html')


@app.route('/contact',methods=['POST'])
def contact_form_post():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    country = request.form.get('country')
    subject = request.form.get('subject')
    message = request.form.get('content')
    fullname = f'{fname} {lname}'
    msg = Message(
        sender=(fullname, MAIL_SENDER),
        recipients=MAIL_RECEIVER.split()
    )
    msg.subject = subject
    msg.body = message

    try:
        mail.send(msg)
    except Exception as err:
        flash(f"Couldn't send message: error [{err}]")
        return redirect(url_for('contact_form_view'))
    finally:
        return redirect(url_for('index'))