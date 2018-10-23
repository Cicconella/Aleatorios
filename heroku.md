## Comandos do Heroku

### Entrar no bash

```
heroku run bash
```

### Create Fixture

```
heroku run python manage.py dumpdata banco auth.User --indent=2 > dumperson
```
