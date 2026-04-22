import os
import logging
from config import INPUT_FOLDER, SUBSCRIBER_FILE
from logger_setup import setup_logger
from content_processor import process_markdown_files
from subscriber_manager import clean_subscribers
from delivery_manager import create_batches
from database_manager import create_tables, save_newsletter, save_batch

def main():
    setup_logger()
    create_tables()

    logging.info("Pipeline Started")

    subscribers, before, after = clean_subscribers(SUBSCRIBER_FILE)

    logging.info(f"Subscribers before cleaning: {before}")
    logging.info(f"Subscribers after cleaning: {after}")

    newsletters = process_markdown_files(INPUT_FOLDER)

    for newsletter in newsletters:
        logging.info(f"Processing: {newsletter['title']}")

        save_newsletter(newsletter, len(subscribers))

        batch_files = create_batches(newsletter, subscribers)

        for batch in batch_files:
            save_batch(newsletter["title"], batch)

        logging.info(f"{newsletter['title']} ready with {len(batch_files)} batches")

    logging.info("Pipeline Finished")
    print("Project executed successfully.")

if __name__ == "__main__":
    main()