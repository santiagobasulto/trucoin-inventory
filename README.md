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

    $ django-admin.py test inventory  # Entire app
    $ django-admin.py test inventory.tests.test_resources:ProductResourceTestCase.test_DELETE_a_product  # Individual test method

To test the frontend:

    $ grunt test
