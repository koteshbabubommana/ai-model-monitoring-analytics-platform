import asyncio
from app.utils.logger import logger


async def process_prediction_event(event_data):
    await asyncio.sleep(0.1)

    logger.info(
        "Processed async prediction event: %s",
        event_data
    )

    return {
        "status": "processed",
        "event": event_data
    }