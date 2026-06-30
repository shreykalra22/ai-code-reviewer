from app.config import model

print("Connecting to Gemini...")

response = model.generate_content(
    "Reply with exactly these words: Gemini connection successful!"
)

print("\nGemini Response:\n")
print(response.text)