'''
Este módulo permite hacer scrapping a pokemon.com para obtener las imagenes oficiales de los pokémon
'''
import cv2
import numpy as np
import urllib.request
import time
import os
import sys
import subprocess 
import logging
from pathlib import Path


FOLDER = 'pokemon_images/'
LOG_FILE = os.path.join('.','scrapping.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = LOG_FILE,
                    filemode = 'w',)

def check_folder():
    '''
    Verifica si existe la carpeta en el directorio actual
    '''
    return os.path.isdir(FOLDER)
        

def create_folder():
    '''
    Crea la carpeta donde se almacenarán las imagenes de pokemon.com
    '''
    mkdir = 'md' if sys.platform == 'win32' else 'mkdir'
    subprocess.call([mkdir, 'pokemon_images'])

def download_photo(pnum):
    '''
    Esta funcion descargar la imagen bajo demanda desde Pokemon.com
    '''    

    if not check_folder():
        create_folder()
    
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(pnum) + '.png')
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite(FOLDER + '{:04d}'.format(pnum) + ".png", image)
        
        logging.info('Imagen del pokémon {} descargada exitosamente'.format(pnum) )
        return True

    except Exception as e:
        logging.error('Error al intentar descargar la imagen')
        return False

def scrapping():
    '''
    Esta función llama a la función `download_photo` la cual descarga la foto del pokémon según su número
    NOTA: Esta función aún es un WIP, ya que se necesita saber la cantidad exacta de pokemon a descargar
    además no está considerando las formas regionales
    '''    
    last_poke = 806
    for i in range(1, last_poke):
        download_photo(i)
        print('Descargando imágenes, porfavor espere...',int(i/last_poke*100), '% completado                    \r', end='')
    print('Listo')

