# Deployment
## IDE: PyCharm
## Download similarity.pkl file: https://drive.google.com/file/d/1ceY8ePl20fBFV5-cqq0P9x-3Lqr8KX47/view?usp=sharing (Recommended way to store large pkl files - Use compress-pickle package)
## Steps:
* Create a new project in PyCharm with Python 3.10 and a new virtual environment. (.idea and venv folder will be automatically created)
* Install just once in terminal having (venv):
1. pip install requests
2. pip install pandas
3. pip install streamlit
* To run the app, use play button for app.py or in terminal write streamlit run app.py.
* To stop the app, use stop button for app.py or in terminal, click on cross at top and then Terminate.
* Deploying Dashboard (App) on Heroku:
1. Open PyCharm and create a project with venv (Python 3.10)
2. Install all the above packages in terminal (Check in app.py for errors to make sure all done)
3. Run and stop app locally to check that app is working (Add debug=True also before running)
4. Create a few files in folder:
4.1 app.py where we will code our streamlit application
4.2 .gitignore to make sure that unnecessary files are not pushed to production -> venv
4.3. setup.sh with below code
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
4.4 requirements.txt that will contain all the Python dependencies and their versions -> run pip freeze > requirements.txt
4.5 Procfile for deployment -> web: sh setup.sh && streamlit run app.py

5. Install Heroku Client and then check installation using heroku --version via cmd as administrator.
6. Deploy on Heroku using git: Create web app movie-freak on Heroku and then do as follows in terminal:
6.1 heroku login
6.2 git init (Will create .git folder)
6.3 heroku git:remote -a movie-freak
6.4 git add .
6.5 git commit -m 'deploying movie freak app'
6.6 git push heroku master
