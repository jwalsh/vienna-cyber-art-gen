from pathlib import Path
from typing import Dict

import openai
import requests

class PromptGenerator:

  def __init__(self, api_key: str) -> None:
    self.api_key = api_key
    self.generated_texts: Dict[str, str] = {}
    self.generated_images: Dict[str, str] = {}

  def generate_text(self, filename: str, prompt: str) -> None:
    """Generate text using GPT-3 and store result."""
    try:
      response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        api_key=self.api_key
      )
      generated_text = response.choices[0].text
    except openai.error.OpenAIError as err:
      print(f"Error generating text: {err}")
      return

    self.generated_texts[filename] = generated_text

  def generate_image(self, filename: str, prompt: str) -> None:
    """Generate image using DALL-E and store URL."""
    try:
      response = openai.Image.create(
        prompt=prompt, 
        n=1, 
        size="1024x1024",
        api_key=self.api_key
      )
      image_url = response['data'][0]['url'] 
    except openai.error.OpenAIError as err:
      print(f"Error generating image: {err}")
      return

    self.generated_images[filename] = image_url

  def save_generated_texts(self, output_dir: str) -> None:
    """Save generated texts to files in output directory."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for filename, generated_text in self.generated_texts.items():
      with open(Path(output_dir) / f"generated_{filename}.txt", "w") as f:
        f.write(generated_text)

  def save_generated_images(self, output_dir: str) -> None:
    """Save generated images to files in output directory."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for filename, image_url in self.generated_images.items():
      response = requests.get(image_url)
      if response.status_code == 200:
        image_data = response.content
        with open(Path(output_dir) / f"{filename}.png", "wb") as f:
          f.write(image_data)
      else:
        print(f"Error downloading {image_url}, status {response.status_code}")