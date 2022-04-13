# Blood Donation Backend

## Installation

1. Clone the repository.
```sh
git clone https://github.com/abidkhan484/blood_donation_backend
```
2. Go to project directory.
```sh
cd blood_donation_backend
```
3. Create and activate virtual enviornment with the below commands.
```sh
python3 -m venv env
source env/bin/activate
```
5. Install the requirements.
```sh
pip install -r requirements.txt
```
7. Run the below commands for the migration.
```sh
python manage.py makemigrations
python manage.py migrate
```
8. Finally start the server with the below command.
```sh
python manage.py runserver
```

Open http://localhost:8000 to view it in the browser.
