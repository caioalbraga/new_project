python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact




git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git remote add origin git@github.com:caioalbraga/new_project.git

Migrando a base de dados do django

```
python manage.py makemigrations
python manage.py migrate
```
Criando e modificando a senha de super usuario Django

```

python manage.py createsuperuser
python manage.py changepassword USERNAME
```