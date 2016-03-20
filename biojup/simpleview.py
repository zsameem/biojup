import ipywidgets as widgets
from traitlets import Unicode, List

class SimpleViewWidget(widgets.DOMWidget):
    _view_name = Unicode('SimpleView').tag(sync=True)
    value = Unicode('https://raw.githubusercontent.com/greenify/msa/master/test/dummy/samples/p53.clustalo.clustal').tag(sync=True)

def simpleview():
    w = SimpleViewWidget()
    return w
