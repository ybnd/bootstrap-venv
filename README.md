# bootstrap-venv
Run code in a newly configured virtual environment from a single Python call, using only builtin modules.

This is a quick proof-of-concept, which is worked out in more detail [here](https://github.com/ybnd/gitploy).
* The scripts contain some post-Python 3.6 syntax
* The structure of a `venv` cirtual environment directory differs between operating systems; I assume you're using Linux.

### Usage
After cloning or downloading this repository:
1. Have [Python](https://www.python.org/downloads/) installed.
2. Run it; `python deploy.py`

A new virtual environment will be created in `.venv` and dependencies in `requirements.txt` will be installed in it. Finally, `generate.py` will be run within this new environment; it uses [Faker](https://faker.readthedocs.io/en/master/) to print some nonsense to a file.

### Cleaning up
Remove the virtual environment and generated file with `python undeploy.py`.

### Why?
Try running `generate.py` with a 'clean' Python. With this method, you can distribute code with dependencies and have people run it in one step without installing it in pip.
