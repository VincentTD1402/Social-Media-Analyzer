import os

os.system('alembic revision --autogenerate')
os.system('alembic upgrade head')