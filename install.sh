#Create virtual environment
virtualenv virtenv
source virtenv/bin/activate

#Setup dependencies
DEPENDENCIES=(py-trello requests requests-oauthlib python-dateutil pytz numpy)
for dependency in ${DEPENDENCIES[@]}; do
    pip2 install ${dependency}
done

#Deactivate environment
deactivate

#Creating credentials file
credentials_path="csv_to_trello/credentials.py" 
touch "$credentials_path"
echo -n "Enter your Trello API key (https://trello.com/app-key) and press [ENTER]: "
read api_key
echo "API_KEY = '$api_key'" >> "$credentials_path"
echo -n "Generate and enter your Trello token and press [ENTER]: "
read token
echo "TOKEN = '$token'" >> "$credentials_path"
