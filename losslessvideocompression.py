import ffmpeg                                                         

def compress_video(input_file, output_file, crf_value):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vcodec='libx264', crf=crf_value)
        .run()
    )

# Usage
compress_video("your-input-file.mp4", "Hx264EncodedVid.mp4", 23)
