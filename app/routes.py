import os
import json
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegPresetaciones, RegCategorias
from app.escritor import Escritor

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Braulio'}
	post = [
		{
			'autor':{'username':'Israel'},
			'body':'Beutiful day!'
		},
		{
			'autor':{'username':'Osito'},
			'body':'Bad day!'
		}
	]
	return render_template('index.html', title = 'Home', user = user, posts = post)

@app.route('/regCat', methods = ['GET', 'POST'])
def regCat():
	form = RegCategorias()
	if form.validate_on_submit():
		#flash('Login requested for user {}'.format(form.nombreCat.data))
		agregar = Escritor(form.nombreCat.data, "categorias")
		agregar.busquedaArchivo()
		return redirect(url_for('index'))
	return render_template('regCat.html', title = 'Registro de catgorias', form = form)

@app.route('/regPres', methods = ['GET', 'POST'])
def regPres():
	form = RegPresetaciones()
	if form.validate_on_submit():
		#flash('Login requested for user {}'.format(form.nombrePres.data))
		agregar = Escritor(form.nombrePres.data, "presentaciones")
		agregar.busquedaArchivo()
		return redirect(url_for('index'))
	return render_template('regPres.html', title = 'Registro de presentaciones', form = form)
