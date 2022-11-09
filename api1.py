from fastapi import FastAPI
app = FastAPI(title='MY FASTAPI')


# Flask way we use:
# @app.route('/', methods=['GET','POST'])

@app.get('/')
def index():
    # return 'MY FIRST API'
   
    return 'this is the index/first page of my serve'


    # if __name__ == '__main__':
    #     app.run()
