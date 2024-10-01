"""
WSGI config for Noob project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os #imporing os modules

from django.core.wsgi import get_wsgi_application #importing function from wsgi modules

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Noob.settings')#defiing setting modules to environmrnt variable

application = get_wsgi_application() #this function returns Wsgi callable
#object callable
 