import os
import pkg_resources
from mako.lookup import TemplateLookup
from formbar.renderer import FieldRenderer
from ringo.lib.renderer.form import renderers


base_dir = pkg_resources.get_distribution("ringo_diagram").location
template_dir = os.path.join(base_dir, 'ringo_diagram', 'templates')
template_lookup = TemplateLookup(directories=[template_dir],
                                 default_filters=['h'])


class DiagramFieldRenderer(FieldRenderer):

    def __init__(self, field, translate):
        FieldRenderer.__init__(self, field, translate)
        self.template = template_lookup.get_template("diagramfield.mako")

renderers['diagram'] = DiagramFieldRenderer
