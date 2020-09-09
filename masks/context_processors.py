from .models import AdminMgmt
from django.core.exceptions import ObjectDoesNotExist
try:
    ADMIN_DETAILS = AdminMgmt.objects.filter()[:1].get()
except ObjectDoesNotExist:
    ADMIN_DETAILS = ''
    
def add_variable_to_context(request):
    return {
        'admin': ADMIN_DETAILS
    }