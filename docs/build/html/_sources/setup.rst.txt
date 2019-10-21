############
Setup
############

Requirements:

* Python 3.7
* pipenv (`pip install pipenv`)

Open jcc directory and install dependencies with pipenv:

.. code-block:: console

    pipenv install

For development dependencies (unit testing, etc...) (if required)

.. code-block:: console

    pipenv install --dev

Create pipenv virtual environment

.. code-block:: console

    pipenv shell

If you would like to use the verilog unit test functionality,
Icarus-verilog must be installed (Linux only).

.. code-block:: console

    sudo apt-get install iverilog

Setup should now be complete. The program can be run as
`pipenv run python main.py`, or this can be compiled to
an executable with `pipenv run pyinstaller --onefile jcc.spec`
(only works if dev libraries installed)
