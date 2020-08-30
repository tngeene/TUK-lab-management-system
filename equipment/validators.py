from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_quantities(value, obj):
    if value < obj.equipment.batch.equipment_quantities :
        raise ValidationError(
            _('%(value)s is higher than available quantities, please allocate a lower quantity.'),
            params={'value': value},
        )