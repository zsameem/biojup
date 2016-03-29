# biojup
A collection of custom jupyter notebook widget extensions for biojs visualization components using the jupyter notebook. Uses biopython for parsing and biojs for visualization.

# Install

### Setup the environment
To install __biojup__ from git you will need Jupyter notebook and ipywidgets. Install using conda is the simplest

```
conda create -n venv jupyter ipywidgets numpy biopython
source activate venv
```
Alternatively, you can setup a virtual environment (using virtualenv) and install requirements from pip.
```
vitualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Now to install biojup, run the following commands.
```
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
Render MSA visualizations from clustal files. See [examples](https://github.com/zsameem/biojup/tree/master/biojup/examples)
