import sys 
sys.path.append("src")

from flask import Blueprint, render_template, request, redirect, url_for, flash
from controller.credits_controller import CreditsController
from model.credit import Credit

web_bp = Blueprint('web', __name__)
controller = CreditsController()

@web_bp.route('/')
def index():
    return render_template('index.html')

@web_bp.route('/buscar', methods=['GET', 'POST'])
def buscar():
    resultado = None
    if request.method == 'POST':
        credit_id = request.form['credit_id']
        resultado = controller.search_credit(credit_id)
    return render_template('buscar.html', resultado=resultado)

@web_bp.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        credit = Credit(
            credit_id=request.form['credit_id'],
            college_enrollment=request.form['college_enrollment'],
            semesters=int(request.form['semesters']),
            credit_type=request.form['credit_type'],
            payment_fee_while_studying=float(request.form['payment_fee_while_studying']),
            payment_fee_after_studying=float(request.form['payment_fee_after_studying']) if request.form['payment_fee_after_studying'] else None
        )
        controller.insert_credit(credit)
        flash('Crédito insertado correctamente')
        return redirect(url_for('web.index'))
    return render_template('insertar.html')

@web_bp.route('/modificar', methods=['GET', 'POST'])
def modificar():
    if request.method == 'POST':
        credit = Credit(
            credit_id=request.form['credit_id'],
            college_enrollment=request.form['college_enrollment'],
            semesters=int(request.form['semesters']),
            credit_type=request.form['credit_type'],
            payment_fee_while_studying=float(request.form['payment_fee_while_studying']),
            payment_fee_after_studying=float(request.form['payment_fee_after_studying']) if request.form['payment_fee_after_studying'] else None
        )
        controller.update_credit(credit)
        flash('Crédito modificado correctamente')
        return redirect(url_for('web.index'))
    return render_template('modificar.html')

@web_bp.route('/crear_tablas')
def crear_tablas():
    controller.create_table()
    flash('Tablas creadas correctamente')
    return redirect(url_for('web.index'))