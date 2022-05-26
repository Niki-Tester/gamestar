"""
EXAMPLE: Environment variables for Gamestar application
"""
import os

os.environ.setdefault('IP', '0.0.0.0')
os.environ.setdefault('PORT', '5566')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('SECRET_KEY', '<A_SECURE_PASSWORD>')
os.environ.setdefault('DB_URL', 'postgres://<DB_USERNAME>:<DB_PASSWORD>'
                      '@<DB_HOST>:<DB_PORT>/<DB_NAME')

os.environ.setdefault('CLIENT_ID', '<TWITCH_CLIENT_ID>')
os.environ.setdefault('CLIENT_SECRET', '<TWITCH_CLIENT_SECRET>')
