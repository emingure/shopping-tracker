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
    Route('/data/', method='GET', handler=data),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('159.89.8.122', 5000, debug=True)
