# FastAPI CI Practice API

A small FastAPI project for learning automated testing with pytest and GitHub Actions.

## 1. Create and activate a virtual environment

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Ubuntu / Linux / macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Run the API

```bash
uvicorn main:app --reload
```

Open these addresses in your browser:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## 4. Run the tests

In a second terminal, activate the same virtual environment and run:

```bash
pytest -v
```

All four tests should pass initially.

## 5. Your GitHub Actions assignment

Create a workflow at:

```text
.github/workflows/ci.yml
```

Configure it to run when code is pushed to `main`. The job should:

1. Run on `ubuntu-latest`.
2. Check out the repository.
3. Set up Python 3.12.
4. Install dependencies from `requirements.txt`.
5. Run `pytest -v`.

Useful action to research: `actions/setup-python`.

Do not copy your local `.venv` folder into Git. Add `.venv/` and `__pycache__/` to `.gitignore`.

## Notes

- The task data is stored in memory, so it resets whenever the application restarts.
- This is a learning project, not a production database-backed API.
