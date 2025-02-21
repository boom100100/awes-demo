# CLI Tools

## Setup

    cd projectDir
    brew install python@3.13

### Pipenv

    brew install pipenv
    pipenv shell
    pipenv install --python 3.13


## Changing Dependencies
Only run the following as needed!

Run

    pipenv install dependencyname

to add a new dependency.

Run

    pipenv uninstall dependencyname

to remove a dependency.

Run

    pipenv uninstall --all

to get rid of everything.

Run

    rm Pipfile.lock

to delete Pipfile.lock. 

## Run
Run the following from the project's root directory:

    flask run --debug

## Troubleshooting

### Shell Doesn't Recognize Dependencies

In some sytem states, the Pipenv shell may not recognize dependencies after they were installed. One such case is when running `deactivate` while in the shell:

> `> deactivate`
> `> pipenv shell`
> Loading .env environment variables...
> Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.
> New shell not activated to avoid nested environments.
> `> flask --version`
> zsh: command not found: flask

Users should `exit` instead of `deactivate`.

In any case (e.g. even if `deactivate` *is* accidentally used), just exit and reenter the shell as usual:

```
exit 
pipenv shell
flask --version
```
