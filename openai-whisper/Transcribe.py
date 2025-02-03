import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
transcription = model.transcribe("Recording_3.m4a", fp16=False)

# Save the transcription to a text file
with open("transcription_3.txt", "w", encoding="utf-8") as file:
    file.write(transcription["text"])

print("Transcription saved to transcription.txt")
