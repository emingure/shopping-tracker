from apistar import App, Route
from scraper_hb import get_price

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def price(url):
    price = get_price(url)
    return {'url': url, 'price': price}

routes = [
    Route('/', method='GET', handler=welcome),
    Route('/price/', method='POST', handler=price),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
