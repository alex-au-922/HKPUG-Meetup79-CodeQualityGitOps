# HKPUG-Meetup79-CodeQualityGitOps

This repository contains the source codes for the Hong Kong Python User Group Meetup #79 for the talk 'Code Quality and GitOps in Python'.

## Slides

The slides for the talk can be found [here](https://1drv.ms/p/s!AuHrIoMSVvdAgbIgJQ_nrLQWv-NrhQ).

## Branches

To faciliate the demonstration of different tools and pre-commit hooks, the repository contains the following branches:

- `pre-commit-basics`: Contains the basic setup for pre-commit hooks
- `pre-commit-ruff`: Contains the setup for pre-commit hooks with `ruff` to format Python code
- `pre-commit-ruff-pyproject`: Contains the setup for pre-commit hooks with `ruff` to format Python code with configurations in `pyproject.toml`
- `pre-commit-mypy`: Contains the setup for pre-commit hooks with `mypy` to statically type check Python code and ensure type safety
- `pre-commit-poetry`: Contains the setup for pre-commit hooks with `poetry` to check for dependency and output `requirements.txt`
- `pre-commit-pytest`: Contains the setup for pre-commit hooks with `pytest` to run unit tests and show code-coverage
- `pre-commit-radon`: Contains the setup for pre-commit hooks with `radon` to check for code complexity

## Basic Requirements

- Python 3.8+ (Miniconda / Pyenv etc.)

## Installation

### MacOS / Linux

1. Create a virtual environment (or reuse an existing one)

```bash
$ python -m venv venv
$ source venv/bin/activate
$ if which python | grep -q venv; then echo "Virtual environment activated"; fi
```

Make sure the line "Virtual environment activated" is **printed**.

2. Install `pre-commit`

```bash
$ python -m pip install pre-commit
pre-commit --version
```

### Windows

The steps are similar to MacOS / Linux, but the commands are slightly different.

1. Create a virtual environment (or reuse an existing one)

```cmd
> python -m venv venv
> venv\Scripts\activate
> where python | findstr venv
```

Make sure there is a line with the path to the virtual environment.

2. Install `pre-commit`

```cmd
> python -m pip install pre-commit
> pre-commit --version
```

## Usage

1. Write a `.pre-commit-config.yaml` file in the **root** of your repository

```bash
.
├── .gitignore
├── .pre-commit-config.yaml # <-- Add this file
├── LICENSE
└── README.md
```

2. Run the install command to install the pre-commit hooks

```bash
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

3. Run the pre-commit hooks

```bash
$ pre-commit run --all-files
```

4. Run the pre-commit hooks during git commit

```bash
$ git add -A
$ git commit -m "Add pre-commit hooks"
```
