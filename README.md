# NoGPU-Free-StableDiffusion
## Unlimited AI Image Generator and Inpainter using Stable Diffusion


This repository contains a Command-Line Interface (CLI) tool that provides unlimited AI image generation and inpainting capabilities. The tool is completely free to use, with no need to buy credits or access any APIs.

## Features

- Generate AI images from prompts
- Inpaint specific parts of an image based on prompts.
- Easy-to-use command-line interface.

## Requirements

- Python 3.6+
- Libraries mentioned in requirements.txt

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/HassanMuhammadSannaullah/NoGPU-Free-StableDiffusion.git
   cd NoGPU-Free-StableDiffusion
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

The CLI tool provides two main functionalities: generating AI images from prompts and inpainting specific parts of an image based on prompts.

To run the tool, use the `ImageGenerator.py` script with appropriate options:

```bash
Usage: ImageGenerator.py [OPTIONS] {GenerateImageFromPrompt|InpaintFromPrompt}

  Parses the command line arguments and runs the appropriate function.

Options:
  -prompt, --prompt TEXT                    The prompt for generating image (Specific for GenerateImageFromPrompt).

  -savepath, --savepath PATH                The path to save the generated image. If not
                                            specified, the image will be saved in the current
                                            working directory. (this should have only directory path not the image name)

  -mask_prompt, --mask-prompt TEXT          The prompt indicating what part of the image should
                                            be inpainted. (Specific For InpaintFromPrompt option)

  -inpaint_prompt, --inpaint-prompt TEXT    The prompt describing what should be added/removed
                                            from the selected mask. (Specific For InpaintFromPrompt option)

  -imagepath, --image-path PATH             The path to the image to inpaint. (Specific For InpaintFromPrompt option)

  --help                                    Show this message and exit.
```

### Examples

1. Generate AI image from a prompt:

   ```bash
   python ImageGenerator.py GenerateImageFromPrompt --prompt "A beautiful landscape with mountains and rivers"
   ```

2. Inpaint an image using prompts:

   ```bash
   python ImageGenerator.py InpaintFromPrompt --image-path path/to/img(png format) --mask-prompt "The sky" --inpaint-prompt "white fluffy clouds"
   ```

## Contributing

We welcome contributions to enhance the functionality and usability of this CLI tool. If you find any issues or have suggestions, feel free to open an issue or submit a pull request.
