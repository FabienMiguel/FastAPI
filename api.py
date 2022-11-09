from datetime import datetime
from fastapi import FastAPI
storage = FastAPI(title='MY FASTAPIY ')


# Flask way we use:
# @app.route('/', methods=['GET','POST'])

@storage.get('/ ')
def index():
    
    return 'My name is Miguel, This is my first API'

@storage.get('/today')  #route with get method
def today():
    
    return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool = True, last_name :bool= True ):
    full_names = ''
    if first_name:
        full_names += 'Miguel'
    if last_name:
            full_names += 'Wiz'

    return full_names


