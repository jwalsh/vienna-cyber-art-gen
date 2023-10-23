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
    default="images",
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
            "filename": "exploration_of_mind",
            "prompt": "Generate an artistic image representing the exploration of the unconscious mind through the lens of Vienna's art and science at the turn of the 20th century blended with a futuristic cyberpunk aesthetic. The image should visualize probing the boundaries of identity and consciousness.",
        },
        {
            "filename": "interplay_of_art_and_science",
            "prompt": "Create a vivid image showcasing the intersection of art and science in understanding the human mind. Blend the art and science of Vienna 1900 with a high-tech cyberpunk world where technology and artistry shape society.",
        },
        {
            "filename": "identity_and_self",
            "prompt": "Visualize the questions of identity and self through an imaginative cyberpunk scene. Show how technological enhancements and virtual realities in a futuristic world can shift characters' self-awareness and identity. Combine with turn-of-the-century Vienna aesthetics.",
        },
        {
            "filename": "societal_change",
            "prompt": "Generate an image highlighting societal and cultural transformation. Contrast Vienna at the turn of the 20th century with a cyberpunk future where technological progress radically alters the social landscape. Blend the two visual styles.",
        },
        {
            "filename": "dystopian_elements",
            "prompt": "Create a haunting cyberpunk scene with dystopian elements, blended with glimpses of the turbulent early 20th century Vienna setting. Show a darkly atmospheric, oppressive vision of the future.",
        },
        {
            "filename": "ethical_and_moral_questions",
            "prompt": "Visualize the ethical dilemmas raised by exploring the mind and unchecked technological progress. Combine thought-provoking imagery from turn-of-the-century Vienna with a cyberpunk future filled with moral questions.",
        },
        ## Original prompts
        {
            "filename": "cyberpunk_vienna",
            "prompt": "Imagine a cityscape that fuses the neon-lit, cyberpunk future with the opulent elegance of early 20th-century Vienna. Capture the contrast and blend between these two worlds.",
        },
        {
            "filename": "artistic_dystopia",
            "prompt": "Visualize an art exhibit that showcases a dystopian vision, where cybernetic enhancements and avant-garde art coexist, highlighting the juxtaposition of innovation and societal turmoil.",
        },
        {
            "filename": "virtual_bohemians",
            "prompt": "Create an image of a modern-day bohemian salon where artists, intellectuals, and cyberpunk enthusiasts gather in a virtual world, discussing avant-garde ideas amidst holographic displays and traditional art.",
        },
        {
            "filename": "reimagined_fashion",
            "prompt": "Reimagine the fashion of Vienna in the early 20th century with a futuristic cyberpunk twist. Blend the elegance of that era with technological enhancements and urban street style.",
        },
    ]

    for prompt_data in prompts:
        filename = prompt_data["filename"]
        prompt_text = prompt_data["prompt"]
        generator.generate_image(filename, prompt_text)
        # generator.generated_texts[filename] = prompt_text

    generator.save_generated_images(output_dir)
    # generator.save_generated_texts(output_dir)


if __name__ == "__main__":
    cli()
