# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "kirill"
NEVERCACHE_KEY = "kirill*"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# DATABASES = {
#     "default": {
#         # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         # DB name or path to database file if using sqlite3.
#         "NAME": "db_olga",
#         # Not used with sqlite3.
#         "USER": "webadmin",
#         # Not used with sqlite3.
#         "PASSWORD": "zagreb bioluminescent squid piano",
#         # Set to empty string for localhost. Not used with sqlite3.
#         "HOST": "",
#         # Set to empty string for default. Not used with sqlite3.
#         "PORT": "",
#     }
# }



###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = ["localhost"]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }