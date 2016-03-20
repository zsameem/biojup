#!/usr/bin/env python

from setuptools import setup
import os

import biojup
version = biojup.__version__

long_description = """
Biojs for jupyter notebook
"""

classifiers = [
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: BSD License',
    'Framework :: IPython',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Scientific/Engineering',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: JavaScript',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Scientific/Engineering :: Visualization',
    ]


def write_readme():
    """
    Create README file from LONG_DESCRIPTION, replacing non-standard
    bits of re-structured text.
    """
    with open("README.rst","w") as f:
        f.write("""\
.. Automatically generated from LONG_DESCRIPTION keyword in
.. setup.py. Do not edit directly.\
""")
        f.write(long_description.replace(".. code:: python","::"))


if __name__ == "__main__":

    #write_readme()

    try:
        # IPython 4
        from jupyter_core.paths import jupyter_data_dir
        ipython_dir = jupyter_data_dir()
    except ImportError:
        import IPython
        ipython_dir = IPython.get_ipython().ipython_dir


    setup(name="biojup",
          version=version,
          description="Jupyter widget for biojs",
          long_description=long_description,
          author="Sameem Zahoor",
          author_email="mail@zsameem.me",
          data_files=[(os.path.join(ipython_dir, "nbextensions/biojup_js"),
              ["biojup/js/biojup_view.js"])],
          classifiers=classifiers,
	  install_requires=[i.strip() for i in open("requirements.txt").readlines()],
          url=r"https://github.com/zsameem/biojup",
          license="MIT License",
          platforms=["Linux"]
    )
