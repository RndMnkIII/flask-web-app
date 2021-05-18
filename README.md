# flask-web-app

### Instalar soporte Python3 (Tested with Python 3.8.5):

`sudo apt install -y build-essential libssl-dev libffi-dev python3-d`

`sudo apt-get install python3-venv`

`python3 -m venv myenv`

`source myenv/bin/activate`

`pip install -r requirements.txt`


### Clonar repositiorio con SSH

1. Generar claves:

`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

2. Agregar clava SSH al ssh-agente:

`eval "$(ssh-agent -s)"`

`ssh-add ~/.ssh/id_rsa`

3. Copiar contenido de id_rsa.pub y pegarlo en GitHub>Settings>SSH and GPG keys>New SSH key.

4. Probar la conexión SSH:

`ssh -T git@github.com`

5. Clonar utilizando SSH:

`git clone git@github.com:RndMnkIII/flask-web-app.git`


