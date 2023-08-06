# argus-toolbelt

Argus Toolbelt is a framework for unifying commandline tools to interact with
Argus under one command. This framework also makes it easy for others to develop
their own commands with a simple pythonic interface.

While any command can be made, Argus is also a first class citizen, meaning that
a command developer won't have to deal with auth and HTTP requests.

Complete documentation for this project can be found at: [argus toolbelt documentation](https://argus-toolbelt.dev-docs.mnemonic.no)

This repository is maintained by the [tooling team](https://wiki.mnemonic.no/display/DEV/Tooling+Team)

### Usage

As with most other packages, Argus Toolbelt is available on PyPi.

```bash
pip install argus-toolbelt
```

After the package has been installed, it can be ran as `argus-cli` on the
commandline. You'll find

For a full list of commands, try:

```bash
argus-cli --help
```

If you for example want to check statistics for all cases, you can write:

```bash
argus-cli cases statistics
```

### Development
This repository is using [Poetry](https://python-poetry.org/) as it's dependency
system, meaning it has to be installed on your system first.

```bash
pip install poetry
```

To install this repository use:

```bash
poetry install
```

Now you should be able to run with:
```bash
poetry run argus-cli
```


## prerequisites

 - a python 3.6 or higher interpreter
 - [poetry](https://python-poetry.org/)
 - Requisite access in Argus to the data you are trying to access.


## processes

### requesting changes

To request a change in this repository, create an [ARGUSUSER ticket in JIRA](https://jira.mnemonic.no/secure/CreateIssue.jspa?pid=11342&issuetype=4)

See [existing tickets for this project](<https://jira.mnemonic.no/issues/?jql=project%20in%20(ARGUSUSER%2C%20ARGUS)%20and%20component%20in%20(%22tools%2Ftoolbelt-framework%22)%20and%20status%20not%20in%20(Done%2C%20Deployed%2C%20Rejected%2C%20Closed)>)

### contributing

- All changes must be submitted as a PR towards the [toolbelt-framework repository on stash](https://gitlab.mnemonic.no/development/tooling/toolbelt-framework)
- All commits must be tagged with the correct JIRA ticket.
- All PRs be built successfully before merging.
- All changes must be reviewed and approved by one of the maintainers.
- Non-trivial changes SHOULD be reviewed by two individuals. This is not enforced, and is up to the author to decide.
- Any emergency changes MUST be documented properly in the associated JIRA ticket.


## build and deployment

### build process

- This project uses the [standard tooling build in gitlab](https://gitlab.mnemonic.no/development/cicd/gitlab-templates/-/blob/main/Pipelines/Python.Poetry.Tooling.v3.yml).
- In addition, documentation is built in the pipeline.

### deployment process

- When a merge request is merged, a Python package is built and pushed to pypi.
- Documentation is automatically deployed to the internal and public documentation host.
