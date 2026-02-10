import asyncio
import sys

async def async_type(text, delay=0.05):
    """
    Non-blocking typewriter effect. 
    Allows other code to run in the background if needed.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        await asyncio.sleep(delay) # Yields control instead of freezing
    print()

async def main():
    # You can run two of these "at the same time" (concurrently)
    task1 = asyncio.create_task(async_type("Loading Module A...", 0.1))
    task2 = asyncio.create_task(async_type("Loading Module B...", 0.05))
    
    await task1
    await task2

# Example usage:
# asyncio.run(main()) 
# Note: Uncomment the line above to run this in a local script.
# Jupyter/Colab users should use 'await main()' instead.

# Credits to Google Gemini
