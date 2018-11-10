# wget_busking

Windows Task Scheduler runs wget_busking.exe every time a user signs on, which wgets a url and checks if it has changed since the last time

Workflow:
1) edit wget_busking.py
2) pre-commit hook triggers pyinstaller to build exe
3) wget_busking.exe gets updated
4) Task Scheduler finds wget_busking.exe from a fixed path
