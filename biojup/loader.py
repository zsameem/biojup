from IPython.display import Javascript, display

__has_initialized__ = False

def init():
    # FIXME
    # Loads the JS extensions. This is still a bit of a
    # hack: calls to  methods cannot occur in the
    # same cell as the import statement.
    #
    # Potential alternatives would be to re-factor the
    # init statement into a line magic.

    global __has_initialized__
    if not __has_initialized__:
        display(Javascript("""
                require(['base/js/namespace'],
            function(IPython) {
                IPython.utils.load_extensions('biojup_js/biojup_view');

            });
            """))
        __has_initialized__ = True
