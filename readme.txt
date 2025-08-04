So for this to run, I have a .env file with my API key:
NOTE: The API key, which should've been ignored by gitignore, is not active so running it with that default API key will not work.

.env:
OPENWEATHER_API_KEY=add_your_api_key #my api key

you should have your api key, from openweathermap.org, in the .env file that should be stored in the same directory as the project.
Run this command from the directory you have this project in, on your terminal to run the solution:
streamlit run app.py