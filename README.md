# Flask-Skeleton  
Branch **base**: Flask, Blueprints  
Branch **base-api**: Flask, Flask-Restful  
Branch **base-db**: Flask, Peewee  
Branch **base-core**: Flask, Peewee, *Flask-Security*  
Branch **cms**: **cms-core**, Flask-Admin
  
## Install
```bash
$ git clone git@github.com:mariofix/flask-skeleton.git my-project  
$ cd my-project  
$ git ch [-b] [base|base-api|base-db]  
$ git pull github [base|base-api|base-db]  
$ poetry install  
```  
Optional:
```bash
$ git remote rename origin github
```

## Run
```bash
$ poetry run flask run
```