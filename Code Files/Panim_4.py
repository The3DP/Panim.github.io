import sys
import time
import random
import string

def decrypt_effect(text, scramble_duration=0.1):
    """
    Cycles through random characters before revealing the actual letter.
    """
    for char in text:
        if char == " ":
            # Don't scramble spaces, just print them
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
            continue
            
        # Scramble loop: show random characters briefly
        end_time = time.time() + scramble_duration
        while time.time() < end_time:
            random_char = random.choice(string.ascii_letters + string.digits)
            sys.stdout.write(random_char)
            sys.stdout.flush()
            time.sleep(0.01)
            sys.stdout.write('\b') # Backspace to overwrite
        
        # Lock in the correct character
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

# Example usage:
decrypt_effect("ACCESS GRANTED... SYSTEM UNLOCKED.")

# Credits to Google Gemini
