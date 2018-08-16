# Sirius Intelligence

Sirius Intelligence is a backend API used in Sirius Music.

This API runs on Python 3.6. Make sure you have Python 3.6 and pip installed.


# Clone the Repository

Open the terminal and run the command:

		git clone https://shwetabhk@bitbucket.org/shwetabhk/sirius-intelligence.git

# Create a virtual environment

open your working directory in the terminal and run the following commands:

		pip install virtualenv

		virtualenv Sirius

		source sirius/bin/activate


# Install the requirements

Open the cloned folder in the terminal(virtual environment) and run the following commands:

		pip install -r Requirements/requirements.txt

Install and Configure Postgresql in your Linux, Visit this link: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04


# Changing the config file:

The Config file is where all the secrets related to this API go, eg: credentials, Database details, API keys, file_paths, etc.

Open congif.py and make changes to following fields according to your setup:

		NAME = 'siriusmusic'
		USER = 'sirius'
		PASSWORD = 'sirius_black'
		HOST = 'localhost'
		PORT = 5432
		SONG_DIRECTORY='/media/shwetabh/76FC340DFC33C661/Documents and Settings/Shwetabh Kumar/My Documents/Rockstar Games/GTA V/User Music'

# Migrating the database

Run the following commands to make changes in the database:

		python manage.py makemigrations

		python manage.py migrate


# Run the server

		python manage.py runserver




	
