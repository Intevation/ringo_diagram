import logging

# Import renderer to register the renderers 
import ringo_diagram.renderer

log = logging.getLogger(__name__)


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul
    """
    config.add_static_view('ringo_diagram-static', path='ringo_diagram:static',
                           cache_max_age=3600)
