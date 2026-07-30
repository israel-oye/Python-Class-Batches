from app import settings

if settings.get("DB") == 'SQL':
    print("Database is SQL-based")