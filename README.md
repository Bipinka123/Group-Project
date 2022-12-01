# Group Project Anup Shah, Bipin Kaderiya, Binod Subedi

<h1 align = "center" > My Day </h1>

<h5 target = "_blank"> Deployed on https://mayday.fly.dev/ </h5>


### Description
Myday app built with flask, html/css using The New York Times API and Weather API. Users can log into their personalized account to get details about today's news, weather, Top ten bestselling books details which is dynamically generated.

### Requirements
python3+, Flask framework, and other packages, html/css

### Getting Started

* **1** : Clone the repository using this code block:
                ''' git clone https://github.com/Bipinka123/Group-Project.git '''

* **2** : Once Cloned, extract the repo, go to the project directory and install pipenv with all dependencies
                ''' pipenv install  '''
                ''' pipenv shell   # start the virtual environment. '''
                ''' pipenv install -r requirements.txt # if install didn't work. ''' 

* **3** : These packages should be installed from the '** requirements.txt **' file.
            '** flask - The framework for retrieving the API and processing the data for frontend display/ ' **
            '** python-dotenv - Package to read the  .env files '**
            '** requests - To query requests while interacting with the API's 

* **4** : Duplicate the .example.env file and rename it to .env and fill the value. 
                ''' cp .example.env .env '''
                ''' Go to the [NYT] (https://developer.nytimes.com/) website and [NWS] (https://www.weather.gov/documentation/services-web-api) to generate  API keys. '''

* **5** : Once all the prerequisites are complete, you can run the program by using 

                ''' flask run '''

### Technical Issues Encountered 


* **1** : Generating the buttons on login display, we encountered issue with size of the button and ended up resizing signup and sign in buttons. We looked for StackOverflow examples and read the documentation in details.


* **2** : We couldn't load the API to the html pages when using render_template function, the Flask expects those html files to be under templates folde. After using Google and StackOverflow for a while and we could only find the solution.








