PENV=.env
PENV_BIN_PATH=
ifdef $(PENV)
PENV_BIN_PATH=./$(PENV)/bin/
endif
PINST=$(PENV_BIN_PATH)pip install -U
PINSTR=$(PINST) -r
WSGI=$(PENV_BIN_PATH)gunicorn
REQ_DIR=requirements
READ=more
ISSUES_URL=https://github.com/bluebirrrrd/nau-timetable/issues
OPEN_URL=xdg-open
MIGRATOR=$(PENV_BIN_PATH)alembic -c config/alembic.ini
NODE_BIN_PATH=./node_modules/.bin/
NPM=npm
PRECOMMIT=$(PENV_BIN_PATH)pre-commit
MNGPY=$(PENV_BIN_PATH)python ./manage.py
USER_SHELL=/bin/zsh
ACTIVATE_ENV=if test -d ./$(PENV); then . ./$(PENV)/bin/activate; fi; if test -f ./.exports; then . ./.exports; fi
USE_NVM=if test -d ~/.nvm; then . ~/.nvm/nvm.sh; nvm use 5.0.0 ; fi

.PHONY: all
all: dev

.PHONY: clean
clean:
	@rm -rf staticfiles/* node_modules etc $(PENV) && echo "Cleanup successful"

.PHONY: deps
deps: front-deps
	@$(ACTIVATE_ENV); \
	$(PINSTR) requirements.txt

.PHONY: dev-deps
dev-deps: front-deps
	@$(PINST) pip; \
	$(PINSTR) dev.txt && \
	$(PRECOMMIT) install

.PHONY: front-deps
front-deps:
	@$(USE_NVM); \
	$(NPM) i

.PHONY: env
env:
	@virtualenv --clear --prompt="[NAU Timetable NG2][py3.5] " -p python3.5 $(PENV); \
	touch ./$(PENV)/.zshrc && \
	chmod +x ./$(PENV)/.zshrc && \
	if test -f ~/.zshrc; then cat ~/.zshrc >> ./$(PENV)/.zshrc; fi && \
	cat ./$(PENV)/bin/activate >> ./$(PENV)/.zshrc

.PHONY: activate-env
activate-env:
	@$(ACTIVATE_ENV) && \
	ZDOTDIR=$(PENV) $(USER_SHELL) -i

.PHONY: readme
readme:
	@$(READ) README.md

.PHONY: issues
issues:
	@echo "Please check out issues at $(ISSUES_URL)"

.PHONY: issue
issue:
	@$(OPEN_URL) "$(ISSUES_URL)/$1"

.PHONY: help
help: readme issues
	@$(OPEN_URL) "$(ISSUES_URL)"

.PHONY: static
static:
	@$(MNGPY) collectstatic --merge --noinput

.PHONY: db
db:
	@$(MNGPY) migrate --merge

.PHONY: prod-db
prod-db:
	@$(MNGPY) migrate --merge --noinput

.PHONY: test-style
test-style:
	@$(PRECOMMIT) run --all-files

.PHONY: compile
compile:
	@$(USE_NVM); \
	tsc -w &

.PHONY: serve-dev
serve-dev:
	@$(ACTIVATE_ENV); \
	$(MNGPY) runserver_plus --traceback

.PHONY: run-dev
run-dev: compile serve-dev

.PHONY: dev
dev: dev-deps run-dev

.PHONY: run
run: deps db
	@$(ACTIVATE_ENV) ; \
	$(WSGI) nau_timetable.wsgi

.PHONY: run-prod
run-prod: run

.PHONY: prod
prod: deps prod-db static run-prod
