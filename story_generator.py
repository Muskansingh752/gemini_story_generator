import os
from google import genai
from dotenv import load_dotenv
from gtts import gTTS
from io import BytesIO


load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found")


client = genai.Client(api_key=api_key)

def create_advanced_prompt(style):
 base_prompt = """
   You are a brilliant writer with over 30 years of experience.
   Your writing style is known for deep image analysis and the ability to transform visual details into vivid, emotionally engaging stories.

   Goal: Write a short or medium-length story that is clear, captivating, and addictive — one that even adults can’t stop reading.

   Style: Ensure that the {style} perfectly complements the storys theme, tone, and mood.

    Guidelines:

   Use every provided image meaningfully in the story.

   Create an imaginative flow with a clear beginning, middle, and end.

   Include emotional depth and sensory richness.

   Adapt the genre naturally (fantasy, mystery, romance, etc.) based on the images.

  Output format:

 Title (must be interesting and relevant to the storyline)
 [MAKE IT SURE THE STORY GOE WITH FLOW THE STORY MUST LOOK LIKE A REAL STORY LIKE IT REALY WRITTEN BY HUMAN]

  Story"""
   

 style_insstruction= ""
 if style=="comedy":
    style_insstruction="\n**follow a light-hearted and witty tone with playful dialogue, clever humor, and fast pacing. "
 elif style =="fairy tale":
    style_insstruction = "\n**use a magical, moral, and imaginative tone with vivid descriptions and a timeless storybook feel. "
 elif style == "sci-fi":
    style_insstruction= "\n**use futuristic imagination and scientific realism, building believable worlds inspired by technology or the unknown. "
 elif style == "adventure":
    style_insstruction = "\n** keep it thrilling, fast-paced, and full of courage, focusing on excitement, discovery, and vivid action scenes. "

 return base_prompt+style_insstruction


def generate_story_from_image(image,style):

    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = [image,create_advanced_prompt(style)]
    )
    return response.text



def narrate_story(story_text):
    try:
        tts = gTTS(text=story_text, lang="en", slow=False)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)  # ensures audio always starts from zero
        return audio_fp
    except Exception as e:
        return f"An unexpected error occurred during the API call: {e}"
