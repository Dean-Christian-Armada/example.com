from django.conf import settings

if not settings.DEBUG:
	print "--------"
	print "ON PRODUCTION"
	ALLOWED_HOSTS = ["example.com"]