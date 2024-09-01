# Deployment
## IDE: PyCharm
## Steps:
* Create a new project in PyCharm with Python 3.10 and a new virtual environment. (.idea and venv folder will be automatically created)
* Install just once in terminal having (venv):
1. pip install requests
2. pip install pandas
3. pip install streamlit
* To run the app, use play button for app.py or in terminal write streamlit run app.py.
* To stop the app, use stop button for app.py or in terminal, click on cross at top and then Terminate.
* Deploying Dashboard (App) on Heroku:
1. Open PyCharm and create a project with venv
2. Install all the above packages in terminal (Check in app.py for errors to make sure all done)
3. Run and stop app locally to check that app is working (Add debug=True also before running)
4. Install gunicorn web server to serve streamlit application (Never use Flask's development server in production) -> pip install gunicorn 
5. Create a few files in folder:
5.1 app.py where we will code our streamlit application
5.2 .gitignore to make sure that unnecessary files are not pushed to production -> venv
5.3. setup.sh with below code
```
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
5.4 requirements.txt that will contain all the Python dependencies and their versions -> run pip freeze > requirements.txt
5.5 Procfile for deployment -> web: sh setup.sh && streamlit run app.py (Make sure to access app and server instances in app.py)
6. Install Heroku Client and then check installation using heroku --version via cmd as administrator.
7. Deploy on Heroku using git: Create web app movie-freak on Heroku and then do as follows in terminal:
7.1 heroku login
7.2 git init (Will create .git folder)
7.3 heroku git:remote -a movie-freak
7.4 git add .
7.5 git commit -m 'deploying movie freak app'
7.6 git push heroku master
