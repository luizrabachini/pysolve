from pyramid.config import Configurator
from pyramid.exceptions import NotFound


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    #config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')

    config.add_static_view('static', 'static', cache_max_age=3600)

    ## Project urls
    config.add_route('home', '/')
    config.add_route('coin_determiner', '/coindeterminer')

    ## Error custom pages
    config.add_view('pysolve.views.notfound_view', context=NotFound)
    
    config.scan()
    return config.make_wsgi_app()
