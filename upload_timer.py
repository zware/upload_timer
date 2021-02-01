import os
import sys


filename = sys.argv[1]

size = os.stat(filename).st_size * 8  # bits

upload_rate = (
    600  # Kbps
    * 1024  # bps
    )

seconds = size // upload_rate

minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f'Upload should take roughly {hours}:{minutes}:{seconds}')
