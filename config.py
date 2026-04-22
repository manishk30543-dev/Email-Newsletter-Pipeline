import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input_newsletters")
DATA_FOLDER = os.path.join(BASE_DIR, "data")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output", "batches")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")
DB_FOLDER = os.path.join(BASE_DIR, "database")

SUBSCRIBER_FILE = os.path.join(DATA_FOLDER, "subscribers.csv")
DB_FILE = os.path.join(DB_FOLDER, "newsletter.db")
LOG_FILE = os.path.join(LOG_FOLDER, "audit.log")

BATCH_SIZE = 2

# Optional MySQL configuration. Set ENABLED to True and fill credentials
# to store final output in a MySQL server. When disabled the project uses
# the local SQLite DB at `DB_FILE`.
MYSQL = {
	"ENABLED": False,
	"HOST": "localhost",
	"PORT": 3306,
	"USER": "root",
	"PASSWORD": "",
	"DATABASE": "newsletter_db"
}