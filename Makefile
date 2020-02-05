.PHONY: requirements

# Set environment variables
# ENVIRONMENT = set -o allexport; . ./.env; set +o allexport;

# Set the following variable to you project name
PROJECT_NAME = twilio_v0
DEFAULT_VIRTUALENV = .venv
# Possible virtualenv if virtualenvwrapper is used
POSSIBLE_VIRTUALENV = $(VIRTUAL_ENV)
# Use possible virtualenv if it exists and virtualenvwrapper is used, otherwise use default one
VIRTUALENV = $(if $(wildcard $(POSSIBLE_VIRTUALENV)),$(POSSIBLE_VIRTUALENV),$(DEFAULT_VIRTUALENV))

PYVERSION=3.6
PIP = $(VIRTUALENV)/bin/pip
PYTHON = $(VIRTUALENV)/bin/python

app=
apps=

default: env requirements-local requirements-frontend webpack migrate loaddata collectstatic

collectstatic:
	@echo "Collecting static files for Django site"
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py collectstatic -v 0 --noinput

syncdb:
	-@echo "### Creating database tables and loading fixtures"
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py makemigrations
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py migrate

migrations:
	@echo "Generating migrations"
	@$(ENVIRONMENT)$(PYTHON) $(PROJECT_NAME)/manage.py makemigrations $(apps)

migrate:
	@echo "Applying migrations"
	@$(ENVIRONMENT)$(PYTHON) $(PROJECT_NAME)/manage.py migrate -v 0 --noinput $(app)

superuser:
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py createsuperuser

shell:
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py shell

dbshell:
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py dbshell

exec:
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py $(RUN_ARGS)

up:
	-@docker-compose -f docker-compose.yml up -d --build

down:
	-@docker-compose -f docker-compose.yml down

ps:
	-@docker-compose -f docker-compose.yml ps

logs:
	-@docker-compose -f docker-compose.yml logs -f

test:
	-@docker-compose -f docker-compose.yml exec web python3 twilio_v0/manage.py test
