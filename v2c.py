import gzip
import bz2
import lzma
import zlib
import base64

from moviepy.editor import VideoFileClip

def encode_data(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Lzma Compression
    lzma_compressed = lzma.compress(data, format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=9)

    return lzma_compressed

def decode_data(encoded_data):
    lzma_decompressed = None
    
    # Lzma Decompression
    try:
        lzma_decompressed = lzma.decompress(encoded_data)
    except:
        pass

    return lzma_decompressed

# Call the function with the path to your video file
encoded_data = encode_data('tntfireshorts.mp4')

# Save the encoded data to a file
with open("encoded.txt", "wb") as file:
    file.write(encoded_data)

print(f"File 'encoded.txt' has been saved.")
with open('encoded.txt', 'rb') as file:
        endata = file.read()
# Now let's decode the data
decoded_data = decode_data(endata)

# And save it back to a video file
with open("decoded_video.mp4", "wb") as file:
    file.write(decoded_data)

print(f"File 'decoded_video.mp4' has been saved.")
