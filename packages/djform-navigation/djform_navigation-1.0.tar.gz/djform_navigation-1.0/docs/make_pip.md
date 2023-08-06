**Make PIP your self**

1. `git clone https://github.com/humblesami/djform_navigation.git`
2. `cd djform_navigation`

3. Find and replace `djform_navigation` with your own `your_module_name`

**Build and test using sample_usage locally**

rm -r dist/*

rm -r build/*

python setup.py sdist bdist_wheel -v=1.0

pip uninstall -y djform_navigation

pip install dist/djform_navigation-1.0-py3-none-any.whl

cd sample_usage

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

#python manage.py initsql

cd ..

echo "done"

#you can uncomment `python manage.py initsql` if you want to reset database

**Upload your pip**

Install twine

`sudo apt-get update`

`sudo apt-get install twine`

https://twine.readthedocs.io/en/stable/

`pip install twine`

`twine upload dist/* --config-file ~/.pypirc_test`

`twine upload dist/* --config-file ~/.pypirc_prod`


**Sample config files for twine**

    .pypirc_test

    [distutils]
    index-servers = pypi

    [pypi]
    repository: https://test.pypi.org/legacy/
    username: __token__
    password: token1


*Install the uploaded package*
pip install -i https://test.pypi.org/simple/ djform_navigation


    .pypirc_prod

    [distutils]
    index-servers = pypi

    [pypi]
    repository: https://pypi.org/legacy/
    username: __token__
    password: token2

*Install the uploaded package*
pip install djform_navigation