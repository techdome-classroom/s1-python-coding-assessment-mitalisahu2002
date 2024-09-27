def decoder_ring(message, decoder_key):
    match = False 
    message_index = 0
    for char in decoder_key:
        if char == '*':
            match = True
            break
        elif char == '?':
            message_index += 1
        else:
            if message_index < len(message) and char == message
