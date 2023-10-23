import click

from .generator import PromptGenerator  # Changed this line


def cli():
    print("Hello world!")


@click.command()
@click.option(
    "--api-key", prompt="Enter your OpenAI API key", help="Your OpenAI API key"
)
@click.option(
    "--output-dir",
    default="generated_images",
    help="Output directory for generated images",
)
def main(api_key, output_dir):
    """
    vienna-cyber-art-gen: Generate images blending early 20th-century Vienna and cyberpunk aesthetics.

    This CLI tool generates images based on prompts that combine the elegance of Vienna in the early 20th century with futuristic cyberpunk elements.

    Args:
    api_key (str): Your OpenAI API key.
    output_dir (str): Output directory for generated images (default: generated_images).
    """
    generator = PromptGenerator(api_key)
    prompts = [
        {
            "filename": "cyberpunk_vienna.jpg",
            "prompt_text": "Imagine a cityscape that fuses the neon-lit, cyberpunk future with the opulent elegance of early 20th-century Vienna. Capture the contrast and blend between these two worlds.",
        },
        {
            "filename": "artistic_dystopia.jpg",
            "prompt_text": "Visualize an art exhibit that showcases a dystopian vision, where cybernetic enhancements and avant-garde art coexist, highlighting the juxtaposition of innovation and societal turmoil.",
        },
        {
            "filename": "virtual_bohemians.jpg",
            "prompt_text": "Create an image of a modern-day bohemian salon where artists, intellectuals, and cyberpunk enthusiasts gather in a virtual world, discussing avant-garde ideas amidst holographic displays and traditional art.",
        },
        {
            "filename": "reimagined_fashion.jpg",
            "prompt_text": "Reimagine the fashion of Vienna in the early 20th century with a futuristic cyberpunk twist. Blend the elegance of that era with technological enhancements and urban street style.",
        },
    ]

    for prompt_data in prompts:
        filename = prompt_data["filename"]
        prompt_text = prompt_data["prompt_text"]
        generator.generate_prompt(filename, prompt_text)

    generator.save_generated_texts(output_dir)


if __name__ == "__main__":
    cli()
