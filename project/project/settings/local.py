from django.conf import settings

if settings.DEBUG:
	import os
	print "--------"
	print "ON LOCAL"
	ALLOWED_HOSTS = []

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
	    }
	}