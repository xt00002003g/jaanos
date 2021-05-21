import os
import bottle
from bottle import *


class Route(bottle.Route):
    """
    Nadomestni razred za poti s privzetimi imeni.
    """
    def __init__(self, app, rule, method, callback, name=None, plugins=None, skiplist=None, **config):
        if name is None:
            name = callback.__name__
        super().__init__(app, rule, method, callback, name, plugins, skiplist, **config)


def template(*largs, **kwargs):
    """
    Izpis predloge s podajanjem funkcije url.
    """
    return bottle.template(*largs, **kwargs, url=bottle.url)


bottle.Route = Route
bottle.request.environ['SCRIPT_NAME'] = os.environ.get('BOTTLE_ROOT', '')
