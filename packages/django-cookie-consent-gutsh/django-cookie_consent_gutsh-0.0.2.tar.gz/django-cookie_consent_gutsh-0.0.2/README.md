# Cookie consent

Cookie consent is a Django app to conduct consent component for web-cookies.
Detailed documentation is in the "docs" directory.

## Quick start

1. Add "cookie\_consent" to your `INSTALLED_APPS` setting like this::
```
    INSTALLED_APPS = [
        "cookie_consent",
        ...,
    ]
```
2. Include the cookie\_consent URLconf in your project urls.py like this::
```
    path("cookie_consent/", include("cookie_consent.urls")),
```
3. Run ``python manage.py migrate`` to create the models.
4. Start the development server and visit http://127.0.0.1:8000/.
