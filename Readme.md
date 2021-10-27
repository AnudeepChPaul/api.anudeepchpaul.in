## Env setup

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## VSCode Launch.json

{
  "name": "Flask",
  "type": "python",
  "request": "launch",
  "stopOnEntry": false,
  "pythonPath": "/run/media/acp/eeaf70d4-08a7-4deb-a182-5e74d2241c25/Projects/api.anudeepchpaul.in/venv/bin/python3",
  "program": "${workspaceRoot}/manage.py",
  "env": {
      "FLASK_APP": "${workspaceRoot}/manage.py"
  },
  "args": [
    "run"
    // --no-debug and one more line removed.
  ],
  "envFile": "${workspaceFolder}/.env",
  "debugOptions": [
    "RedirectOutput"
  ]
}
