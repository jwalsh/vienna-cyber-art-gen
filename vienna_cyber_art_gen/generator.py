# vienna_cyber_art_gen/generator.py

import openai
from typing import Dict

class PromptGenerator:
    """
    PromptGenerator: A class for generating images based on prompts using the OpenAI API.

    Args:
    api_key (str): Your OpenAI API key.

    Attributes:
    api_key (str): The provided OpenAI API key.
    generated_texts (Dict[str, str]): A dictionary to store generated image texts.

    Methods:
    generate_prompt(filename, prompt_text):
    save_generated_texts(output_dir):
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.generated_texts = {}

    def generate_prompt(self, filename: str, prompt_text: str):
        """
        Generate an image prompt based on the given text.

        Args:
        filename (str): The filename for the generated image.
        prompt_text (str): The text prompt to generate the image.

        Raises:
        openai.error.OpenAIError: If there is an error with the OpenAI API.
        """

        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt_text,
                max_tokens=100,  # Adjust as needed
                api_key=self.api_key
            )

            generated_text = response.choices[0].text
            self.generated_texts[filename] = generated_text

        except openai.error.OpenAIError as e:
            raise e

    def save_generated_texts(self, output_dir: str):
        """
        Save the generated image texts to files in the specified output directory.

        Args:
        output_dir (str): The directory where generated texts will be saved.

        Raises:
        IOError: If there is an issue with file operations.
        """
        try:
            for filename, generated_text in self.generated_texts.items():
                with open(f"{output_dir}/generated_{filename}.txt", "w") as file:
                    file.write(generated_text)

        except IOError as e:
            raise e
