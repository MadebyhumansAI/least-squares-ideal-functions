## Create Virtual environment 
 
pip install virtualenv virtualenvwrapper 

## Update ~/.bashrc 
 
Use vim or nano to open ~/.bashrc and paste the next three line, save the file when done: 
 
export WORKON_HOME=$HOME/.virtualenvs

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 

source /usr/local/bin/virtualenvwrapper.sh 

## Source ~/.bashrc for changes to take place 
 
source ~/.bashrc 
 
## Create virtual environment for the project 

mkvirtualenv nameofvirtualenv -p python3 

## Install requirements.txt 
 
pip install -r requirements.txt 

## Run main program 

python3 run_output.py
