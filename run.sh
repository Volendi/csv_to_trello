#Activates virtual env
source virtenv/bin/activate

#Run script
python2 csv_to_trello/main.py "$@"

#Deactivate virtual env
deactivate
