#Create virtual environment
virtualenv virtenv
source virtenv/bin/activate

#Setup dependencies
DEPENDENCIES=(py-trello requests requests-oauthlib python-dateutil pytz)
for dependency in ${DEPENDENCIES[@]}; do
    pip2 install ${dependency}
done

#Deactivate environment
deactivate
