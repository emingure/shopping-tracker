from apistar import App, Route
from scraper_hb import get_data
import os

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def data(url):
    result = get_data(url)
    return result

routes = [
    Route('/', method='GET', handler=welcome),
    Route('/data/', method='POST', handler=data),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve(os.environ['URL'], 5000, debug=True)
