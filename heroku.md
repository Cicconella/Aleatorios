## Comandos do Heroku

### Entrar no bash

```
heroku run bash
```

### Criar Fixture

```
heroku run python manage.py dumpdata banco auth.User --indent=2 > dumperson.json
```

### Apagar tudo

```
./manage.py flush
```

### Carregar tudo da fixture

```
./manage.py loaddata banco/fixtures/dumperson.json 
```

### Push to heroku

```
git push heroku master
```

### Adicionar o heroku no git

```
heroku git:remote -a liverdatabase
```

