    echo "export DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings.development" >> ${HOME}/.virtualenvs/${PROJECT_NAME}/bin/postactivate
    echo "unset DJANGO_SETTINGS_MODULE" >> ${HOME}/.virtualenvs/${PROJECT_NAME}/bin/postdeactivate
    add2virtualenv ${HOME}/${PROJECT_NAME}/src

# Tests
    django-admin.py test inventory  # Entire app
    django-admin.py test inventory.tests.test_resources:ProductResourceTestCase.test_DELETE_a_product  # Individual test method