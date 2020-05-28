# Web-App-to-Visualize-Nueral-Nets
This is a Web App Visualizer of Neural Networks with MNIST dataset using Keras, Flask and Streamlit


## Requirements:
* pip install streamlit
* pip install sklearn
* pip install flask
* pip(in conda terminal) install tensorflow(preferably make a virtual environment)
* pip install numpy

## Steps to run:

* Clone the repository using "git clone --url of this repository-- ".

* Run all the cells of "Main Notebook".(Make sure you have installed all the requirements)

* Open the two terminals

* Type "python ml_server.py"(for windows)/"python3 ml_server.py"(linux) in one terminal as show below:

![Screenshot](/images/ml_server.PNG)

* Open the show local host post and check if the server is successfully connected or not.

* Type "streamlit run app.py" in another terminal as show below:

![Screenshot](/images/streamlit.PNG)

* Streamlit will now open a local host port which will display our Web App as shown below:

![Screenshot](/images/web_app.png)

* Click on "generate random number" and you'll visualize the Layer wise Neural Networks, final layer displaying the prediction of the model

* Note: More the lighter/darker the block shown is, more sure the model is about that block

* For ex: in the image shown above in the last layer model shows 4 and 9 as most probable choices but it is more sure about 9 than 4 therefore it makes 9 more lighter as compared to 4
