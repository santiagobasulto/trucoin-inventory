from tastypie.validation import Validation

from . import config


class TooMuchInventoryValidator(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        if bundle.data.get('inventory_count') >= config.MAX_INVENTORY_COUNT:
            errors['inventory_count'] = ['Invalid inventory count']

        return errors