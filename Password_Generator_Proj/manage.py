#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from datetime import date, datetime


def main():
    """Run administrative tasks."""
    print(f'running manage.py project file...' + # {date.today()}
        f'\n\tbuild at: {datetime.now()}')
    print(f'arguments: {sys.argv}')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PasswordGenerator.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
