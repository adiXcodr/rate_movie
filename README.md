<h1 align="center" >RATE MOVIE</h1>
<h3 align="center"> A Web App made with Sentiment Analysis with the help of Flask API</h3>

## Technologies used
* Python
* textblob
* flask
* HTML, CSS

### Demo
https://ratemovie.herokuapp.com/

![kcdemo](https://i.imgur.com/Pir6xTR.gif)

### Project Structure
This project has three major parts :
1. app.py - This contains Flask APIs that receives movie a review through GUI or API calls, computes the precited value based on our model and returns it.
2. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
3. app.html - The HTML template to allow user to enter the movie review.

### Steps to run the application

1. Run app.py using the command below to start Flask API
```
python app.py
```
   
3. Navigate to URL http://localhost:5000

4. To close the server, press Ctrl+C 

5. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the command below to send the request with some pre-popuated values -
```
python request.py
```

<br>

### Author

#### [Adittya Dey](https://github.com/adiXcodr)

[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/adittya-dey-3966b916b/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/adittya.dey.3)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/adixdey/)

