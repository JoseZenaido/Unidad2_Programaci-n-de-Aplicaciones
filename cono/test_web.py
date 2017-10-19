"""Importacion de la definicion del metodo"""
from volumes import cono_area

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

"""Directiva"""


@app.route('/')
def home() -> '302':
    return redirect('/entry')


"""Redirege una pagina web como retorno"""


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the form')


"""Direccion para ocupar en el entry"""


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    """Valores a recibir en las cajas de texto"""

    R = float(request.form['R'])
    g = float(request.form['g'])

    result = cono_area(R, g)
    title = "Resultado del area del cono"

    """Valores a retornar, para visualizar en el front"""
    return render_template('result.html',
                           the_R=R,
                           the_g=g,
                           the_result=result,
                           the_title=title)


app.run(debug=True)
