`cd src/github/`

`mkdir funkadelic.herokuapp.com`

`cd funkadelic.herokuapp.com`

`git init`

`heroku auth:whoami`

`heroku create funkadelic`

`curl -d '{"name": "funkadelic.herokuapp.com"}' -H X-GitHub-OTP:123456 -u davejagoda https://api.github.com/user/repos`

`git remote add origin git@github.com:davejagoda/funkadelic.herokuapp.com.git`

`heroku git:remote -a funkadelic --ssh-git`

`virtualenv3  venv`

`source venv/bin/activate`

`echo gunicorn > requirements.txt`

`pip install -r requirements.txt`

`git add requirements.txt`

`git commit -m "Initial commit"`

`git push origin master`

`git push heroku master`
