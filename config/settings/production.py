from .common import *

MIDDLEWARE += (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import django_heroku

django_heroku.settings(locals())
