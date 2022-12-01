# Group Project Anol Saha, Bipin Kaderiya, Binod Subedi

<h1 align = "center" > My Day </h1>

<h5 target = "_blank"> Deployed on https://mayday.fly.dev/ </h5>

### Group Proposal 
            ''' Google Doc link : https://docs.google.com/document/d/1NWkmTldOlEkKz9oeSCJ2IgNRSkMFJGBN_Q0vxiUz6HQ/edit# '''

### Public GitHub Link
            ''' https://github.com/Bipinka123/Group-Project '''


### Description
Myday app built with flask, html/css using The New York Times API and Weather API. Users can log into their personalized account to get details about today's news, weather, Top ten bestselling books details which is dynamically generated. This app serves to start off user's day very smoothly with weather data and news data. 

### Technical Requirements
python3+, Flask framework, html/css, postgress database, Rest API Integration and other packages, Flask Login

### Stretch Features 

            * OzoKJNg84mTqstj
             Weather API: OpenWeather
             UI will have a weather dashboard displaying weather for your current location (which will be detected)
             There will be an icon (not static, it will be based on the weather) with a temperature and location
            
            *0MFeFkB9CIkw3MW
             Login with password (password will be hashed and the hash will be stored)
             Password will be hashed in the flask server before being sent to database
             We may use bcrypt library
             
            *GU2HEOMXDGXaURY
            NYT API to fetch top books
            They will be listed in order
            There will a button or link that will take users to the amazon page for that book


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


### Things we enjoyed:
            ''' Working together with flexible time frame with the help of Git Branch '''
            ''' Enjoyed working with API and implementing a password. Was able to generate the hashed password which was nice to learn '''

### Challenges we faced:
            ''' Time because of Final Exams approaching and physical proximity because we could solve some issues within minutes if we were in close physical proximity'''
            
            ''' We had many problems while working with beautification. There was a resize issue we spent a lot of time on where the content on the page would resize if moniter resolution changed'''
            
            ''' We also had problem accessing a good API for sharemarket as most were not free and had to paid. As a result, we did not implement sharemarket API'''

### Pull Requests:
            
            Binod
            ''' https://github.com/Bipinka123/Group-Project/pull/19'''
            '''https://github.com/Bipinka123/Group-Project/pull/18'''
            
            Anol:
            '''https://github.com/Bipinka123/Group-Project/pull/13'''
            '''https://github.com/Bipinka123/Group-Project/pull/8'''
            
            Bipin:
           '''https://github.com/Bipinka123/Group-Project/pull/6'''
           ''' https://github.com/Bipinka123/Group-Project/pull/10'''
            
