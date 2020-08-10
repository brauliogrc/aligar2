import os
import json
from flask import flash

class Escritor():

    def __init__(self, nombreCat, elemetos):
        self.__nombreCatoPres = nombreCat
        self.__elemento = elemetos
    
    def busquedaArchivo(self):
        if (self.__elemento == "categorias"):
            #Comprobando existencia de archivo "categorias.json"
            self.__nombreArchivo = self.__elemento + ".json"
            #flash(" buscando archivo: "+ self.__nombreArchivo)
            encontrado = os.path.isfile(self.__nombreArchivo)
            if encontrado:
                self.__agregarCat()
            else:
                self.__crearArchivoCat()

        elif (self.__elemento == "presentaciones"):
            #Comprobando existencia de archivo "presentaciones.json"
            self.__nombreArchivo = self.__elemento + ".json"
            #flash("buscando archivo: "+ self.__nombreArchivo)
            encontrado = os.path.isfile(self.__nombreArchivo)
            if encontrado:
                self.__agregarPres()
            else:
                self.__crearArchivoPres()
        else:
            pass

        #flash('Dentro de la funcion busqueda de archivo: {}'.format(self.__saludar))

    #Categorias
    def __agregarCat(self):
        #Agrega la nueva categoria al archivo JSON
        try:
            with open(self.__nombreArchivo, 'r') as archivo:
                '''Convierte el contenido del archivo JSON en un diccionario de Python
                para poder manipularlo y agregar la nueva categoria'''
                datos = json.load(archivo)
                datos['categorias'].append(self.__nombreCatoPres)
                
            with open(self.__nombreArchivo, 'w') as archivo:
                '''Sobre escribe el contenido del archivo JSON con el nuevo diccionario
                que ya cuenta con la nueva categoria'''
                json.dump(datos, archivo, indent=4)
                flash('Categoria "{}" agregada de manera exitosa'.format(self.__nombreCatoPres))
        except Exception as error:
            flash('Error al agregar la categoria: "{}"'.format(str(error)))

    def __crearArchivoCat(self):
        '''Creacion de un diccionario que contiene nuestra primer categoria'''
        datos = {}
        datos['categorias'] = []
        datos['categorias'].append(self.__nombreCatoPres)
        try:
            with open(self.__nombreArchivo, 'w') as archivo:
                '''Creacion de archivo JSON en el cual se escribira nuestro diccionario
                convertido en formato JSON'''
                json.dump(datos, archivo, indent=4)
                flash('Archivo creado con exito y categoria "{}" creada!'.format(self.__nombreCatoPres))
        except Exception as error:
            flash('Error al crear archivo "categorias.json: "{}"'.format(str(error)))

    #Presentaciones
    def __agregarPres(self):
        #Agrega la nueva categoria al archivo JSON
        try:
            with open(self.__nombreArchivo, 'r') as archivo:
                '''Convierte el contenido del archivo JSON en un diccionario de Python
                para poder manipularlo y agregar la nueva categoria'''
                datos = json.load(archivo)
                datos['presentaciones'].append(self.__nombreCatoPres)
                
            with open(self.__nombreArchivo, 'w') as archivo:
                '''Sobre escribe el contenido del archivo JSON con el nuevo diccionario
                que ya cuenta con la nueva categoria'''
                json.dump(datos, archivo, indent=4)
                flash('presentacion "{}" agregada de manera exitosa'.format(self.__nombreCatoPres))
        except Exception as error:
            flash('Error al agregar la presentacion: "{}"'.format(str(error)))

    def __crearArchivoPres(self):
        '''Creacion de un diccionario que contiene nuestra primer presentacion'''
        datos = {}
        datos['presentaciones'] = []
        datos['presentaciones'].append(self.__nombreCatoPres)
        try:
            with open(self.__nombreArchivo, 'w') as archivo:
                '''Creacion de archivo JSON en el cual se escribira nuestro diccionario
                convertido en formato JSON'''
                json.dump(datos, archivo, indent=4)
                flash('Archivo creado con exito y presentacion "{}" creada!'.format(self.__nombreCatoPres))
        except Exception as error:
            flash('Error al crear archivo "presentaciones.json: "{}"'.format(str(error)))

    def generaKeys(self):
        if (self.__elemento == "categorias"):
            self.__key = 'categorias'
        elif (self.__elemento == "presentaciones"):
            self.__key = 'presentaciones'
        else:
            pass
            
    
    '''def crearCategoria(self, nombreCat):
		if (nn):
			try:
				with open('categorias.json', 'r') as archivo:
					datos = json.load(archivo)	
					archivo.close()
					datos['categorias'].append(self.nombreCat)

				with open('categorias.json', 'w') as archivo:
					json.dump(datos, archivo, indent=4)
					flash('Categoria "{}" agregada de manera exitosa'.format(self.nombreCat))

			except Exception as error:
				flash('Error al agregar la categoria: "{}"'.format(str(error)))
				
		else:
			datos = {}
			datos['categorias'] = []
			datos['categorias'].append(self.nombreCat)
			try:
				with open('categorias.json', 'w') as archivo:
					json.dump(datos, archivo, indent=4)
					flash('Archivo creado con exito!')
			except Exception as error:
				flash('Error al crear archivo "categorias.json: "{}"'.format(str(error)))'''
    