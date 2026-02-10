import sys
import time
import random

def human_type_text(text, min_delay=0.03, max_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Calculate a random delay between the min and max
        delay = random.uniform(min_delay, max_delay)
        
        # Add a longer pause for punctuation to simulate thinking
        if char in ",.?!":
            time.sleep(0.3)
        else:
            time.sleep(delay)
            
    print()

# Example usage:
message = "Wake up, Neo... The Matrix has you."
human_type_text(message)

# Credits to Google Gemini
