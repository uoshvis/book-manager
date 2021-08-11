# Production-ready Django project example


### Modes

Three code environment dimensions (**modes**):

- local
- tests
- production

Mode is described by different `settings.py`

### Project naming

Project name: `book-manager`

Git repo: `book-manager`

Django project: `book_manager`

Inside git directory: `django-admin startproject <project_name> .`

### Apps configuration

Django apps are inside module named `apps`.
It creates namespace for the app. And helps identify project imports.

To create app:
`django-admin startapp`


### Code edits

After removal of the main `settigns.py` modify `manage.py`:

`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_manager.settings.local')`

**<app_name>/apps.py**

`name='<app_name>'` change to ` name='<prj_name>.apps.<app_name>'`

**namespace in installed apps**

```
    "<prj_name>.apps.<app_name>",
    "<prj_name>.apps.<app_name>",
```


****
More details: [simpleisbetterthancomplex production-ready](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html)
