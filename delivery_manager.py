import os
import math
from config import OUTPUT_FOLDER, BATCH_SIZE

def create_batches(newsletter, subscribers):
    title = newsletter["title"].replace(" ", "_")
    total = len(subscribers)

    batches = math.ceil(total / BATCH_SIZE)

    batch_files = []

    for i in range(batches):
        start = i * BATCH_SIZE
        end = start + BATCH_SIZE

        batch = subscribers.iloc[start:end]

        filename = f"{title}_batch_{i+1}.csv"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        batch.to_csv(filepath, index=False)

        batch_files.append(filename)

    return batch_files