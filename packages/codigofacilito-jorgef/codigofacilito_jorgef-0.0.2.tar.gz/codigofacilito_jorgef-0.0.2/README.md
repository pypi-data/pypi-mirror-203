
python -m venv .venv
venv\Scripts\activate

pip install requests
pip freeze > requirements.txt

## provando un paquete
python -m nome_paquete

python setup.py sdist
##pip install pip --upgrade  DA ERRORE
pip install twine
twine upload dist/*


##TEST 
pip install codigofacilito-jorgef==0.0.1
python
>>> from codigofacilito_jorgef import unreleased
>>> unreleased()
