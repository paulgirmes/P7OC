# PAPYBOT

Programmed for the project 7 of OpenClassrooms Python developper certificate.
WEB application that allows user to ask a mini chatbot about places' location.

## Getting Started

* Clone the app directory and the run.py file

* Install Python3 on your computer if you are running a Windows environment.

* Execute the command "pip install -r requirements.txt".

* Write your google-dev API KEY in app/config.py.

* Execute run.py in a shell, by default the app will run in Debug mode feel free to modify run.py if you don't need it.

* open a Web browser and consult the URL : <http://127.0.0.1:5000/>

### Using

* From the URL : <http://127.0.0.1:5000/> or an other url if deployed on the web

* Ask a question about a place by writing it in the text form then submits it,
if any answer the chatbot replies with the adress of the required place and a map
with a marker centered on the location (from Google Maps API).

* if any Wikipedia pages exists about a subject within a range of 500meters from the location the chatbot will also give an intro about a random page within pages found and a link to the Wiki.

* if there are several choices of places returned by google API the chatbot will asks precision about the request

## Authors

**Paul Girmes** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
