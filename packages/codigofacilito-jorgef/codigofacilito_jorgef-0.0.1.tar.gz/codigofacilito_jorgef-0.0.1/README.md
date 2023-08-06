python -m venv .venv
venv\Scripts\activate

pip install requests
pip freeze > requirements.txt

## provando un paquete
python -m nome_paquete

python setup.py sdist
pip install pip --upgrade
pip install twine
twine upload dist/*


