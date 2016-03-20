# biojup
A custom jupyter notebook widget extension for biojs visualization components using the jupyter notebook implemented using the ipywidgets framework.

# Install
To install __biojup__ from git you will need Jupyter notebook and ipywidgets. Install using conda is the simplest

```
conda create -n venv jupyter ipywidgets
source activate venv
git clone https://github.com/zsameem/biojup.git
cd biojup
```
For a normal install do
```
python setup.py install
```
For dev install
```
python setup.py develop
```

# Usage
The functionality is very limited right now. Here is an [example notebook](https://github.com/zsameem/biojup/blob/master/biojup/examples/from_url.ipynb).
 . This notebook parses a clustal file from a url and displays it in
[biojs msa viewer](https://github.com/greenify/msa).
