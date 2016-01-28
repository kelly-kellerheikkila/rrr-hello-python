# Statement for enabling the development environment
DEBUG = True

# DEV, STAGING, PRODUCTION
MODE = 'DEV'

SQLALCHEMY_ECHO = False

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

