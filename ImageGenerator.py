import click
from FreeStableDiffusion.Generate import GenerateImageFromPrompt, InpaintFromPrompt
import os

os.environ["WDM"] = "false"


@click.command()
@click.argument(
    "function_name", type=click.Choice(["GenerateImageFromPrompt", "InpaintFromPrompt"])
)
@click.option("-prompt", "--prompt", help="The prompt to use.")
@click.option(
    "-savepath",
    "--savepath",
    help="The path to save the generated image. If not specified image will be saved in current working directory",
    type=click.Path(exists=True),
)
@click.option(
    "-mask_prompt",
    "--mask-prompt",
    help="The prompt telling what part of image should be inpainted.",
)
@click.option(
    "-inpaint_prompt",
    "--inpaint-prompt",
    help="The prompt describing what should be added/removed from selected mask.",
)
@click.option(
    "-imagepath",
    "--image-path",
    help="The path to the image to inpaint.",
    type=click.Path(exists=True),
)
def main(function_name, prompt, savepath, mask_prompt, inpaint_prompt, image_path):
    """Parses the command line arguments and runs the appropriate function."""
    if function_name == "GenerateImageFromPrompt":
        if not prompt:
            print("Please specify a prompt for generating the image.")
            return

        GenerateImageFromPrompt(
            prompt, os.path.abspath(savepath) if savepath is not None else None
        )

    elif function_name == "InpaintFromPrompt":
        if not (mask_prompt and inpaint_prompt and image_path):
            print("Please specify a mask prompt, an inpaint prompt, and an image path.")
            return

        InpaintFromPrompt(
            mask_prompt,
            inpaint_prompt,
            os.path.abspath(image_path),
            os.path.abspath(savepath) if savepath is not None else None,
        )

    elif function_name in ("-h", "--help"):
        print_help()

    else:
        print("Unknown function: {}".format(function_name))


def print_help():
    """Prints the help information."""
    print("Usage: python ImageGenerator.py [function] [args]")
    print("\nFunctions:")
    print("  GenerateImageFromPrompt: Generates an image from the given prompt.")
    print(
        "  InpaintFromPrompt: Inpaints an image from the given mask and inpaint prompt."
    )
    print("\nArgs:")
    print("  prompt: The prompt to use.")
    print(
        "  savepath: The path to save the image to. If not specified, the image will not be saved."
    )
    print("  mask_prompt: The prompt to use for the mask.")
    print("  inpaint_prompt: The prompt to use for the inpaint.")
    print("  imagepath: The path to the image to inpaint.")
    print("\nExamples:")
    print(
        '  python ImageGenerator.py GenerateImageFromPrompt --prompt "This is a prompt" --savepath output_image.png'
    )
    print(
        '  python ImageGenerator.py InpaintFromPrompt --mask-prompt "This is a mask" --inpaint-prompt "This is an inpaint" --image-path input_image.png --path output_image.png'
    )


if __name__ == "__main__":
    main()
