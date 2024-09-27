def decoder_ring(message, decoder_key):
    match = False 
    message_index = 0
    for char in decoder_key:
        if char == '*':
