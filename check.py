import google.generativeai as genai

genai.configure(api_key="AIzaSyAyO7L6SBjzhImODOkWU7WjFVjZYa85_gM")

for m in genai.list_models():
    print(f"{m.name} - {m.supported_generation_methods}")
