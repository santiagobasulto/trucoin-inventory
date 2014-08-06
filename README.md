# Trucoin inventory

Small and simple project using Python 3, Django, Tastypie and AngularJS (between other goodies) to manage an inventory list.

### Installation

```bash
$ mkvirtualenv inventory -p $(which python3)
$ pip install -r requirements.txt
$ echo "export DJANGO_SETTINGS_MODULE=inventory_management.settings" >> ${HOME}/.virtualenvs/inventory/bin/postactivate
$ echo "unset DJANGO_SETTINGS_MODULE" >> ${HOME}/.virtualenvs/inventory/bin/postdeactivate
$ add2virtualenv ./inventory_management
$ npm install && bower install
```

### Use

I planned this application to have the frontend decoupled from the backend. I deliberately choose to use [CORS](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing) for this purpose. I know it can be done differently. Serving static files with the django development server on development and setting a reverse proxy on production (using nginx). But I've been really interested in [microservices](http://martinfowler.com/articles/microservices.html) lately and wanted to give it a try.

Said that, to have it fully running you only need to:

```bash
$ django-admin.py runserver &  # You can use a different console if you wish
$ grunt serve
```

### Tests

To test the backend:

```bash
$ django-admin.py test inventory  # Entire app
$ django-admin.py test inventory.tests.test_resources:ProductResourceTestCase.test_DELETE_a_product  # Individual test method
```

To test the frontend:

```bash
$ grunt test
```

### Comments about the Backend

To set up the API on the backend I chose [Tastypie](https://django-tastypie.readthedocs.org). I really wanted to test [django-rest-framework](http://www.django-rest-framework.org) because I've heard great things about it, but I only had time for Tastypie. I've used tastypie for 3 years. I know the entire source code of that module. I feel SUPER confident using it, and it takes me almost no time to develop with it.

Tests on the backend have some special connotations. I don't like the `django.test.client`. It falls in between a "unit" test and a functional test. It's not "unit" because it uses the whole stack of the app (middlewares being the biggest problem) and it's not "functional"/"integration" because it doesn't use `wsgi` properly. That's why I love to use [WebTest](http://webtest.readthedocs.org/en/latest/) (along with [django-webtest](https://github.com/kmike/django-webtest)).

Not much can be said about the backend. I kept it really simple because of my lack of time. I didn't even added south or different settings.

### Comments about the Frontend

It's still incomplete. Sorry about that. I'll finish it as soon as possible.

I've used [yeoman](http://yeoman.io) to set up the front end boilerplate code. Nothing fancy in there. There are tons of stuff I'm not using, but I don't have the time to remove it. I could have used [angular-seed](https://github.com/angular/angular-seed) but the requirement asked for Bootstrap (and Sass) and Grunt, so it was the easiest choice.
