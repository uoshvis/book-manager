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



More details: [simpleisbetterthancomplex production-ready](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html)

---

## Custom User Model

When starting the project always replace the default User model.

Create an app named `acounts`:

`django-admin startapp accounts`

Create an empty migration to install Psql extensions:

`python manage.py makemigrations accounts --empty --name="postgres_extensions"`

Modify `0001_postgres_extensions.py`:

```
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        CITextExtension()
    ]
```

Grab `AbstractUser` from Django source and modify:
- switch `username_validator` to use `ASCIIUsernameValidator`
- The username field now is using `CICharField` which is not case-sensitive
- The `email` field is now mandatory, unique and is using `CIEmailField` which is not case-sensitive

On the settings module, add the following configuration:

**settings.py**

`AUTH_USER_MODEL = "accounts.CustomUser"`

Apply migrations:

`python manage.py migrate`

In db: there is no `auth_user` (default one), and now the user
is stored on table `accounts_customuser`


More details: [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/article/2021/07/08/what-you-should-know-about-the-django-user-model.html)


#### UserManager definition

The existing manager defines `create_user` and `create_superuser` methods.


`is_staff` is required to login using django admin site

`username` is required for `create_superuser`

### User Registration, Login and Logout

Uses django forms

Pre-built register form `UserCreationForm` connects to
the pre-built model `User`.

`UserCreationForm` requires only: username and password.

Customization is implemented in `NewUserForm`.

[More details](https://www.ordinarycoders.com/blog/article/django-user-register-login-logout)
