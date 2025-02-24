
message_queue = []

def send_message(message):
    message_queue.append(message)


def process_messages():
    processed_queue = []
    while message_queue:
        message = message_queue.pop(0)
        processed_queue.append(message)
    return {"processed_queue": processed_queue}
    
