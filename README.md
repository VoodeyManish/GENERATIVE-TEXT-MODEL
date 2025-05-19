# GENERATIVE-TEXT-MODEL
# Text Generation Model

This project demonstrates text generation using a pre-trained GPT-2 model from the Transformers library. It allows users to input prompts and generate coherent text based on those prompts.

## Overview

The script `text_generation_gpt.py` uses the `transformers` library to load a pre-trained GPT-2 model and generate text.  The `generate_text_gpt` function takes a prompt and generates multiple text sequences.

## Setup

1.  **Prerequisites:**
    * Python 3.6 or higher
    * pip

2.  **Installation:**
    * Clone this repository (if applicable) or save the code as `text_generation_gpt.py`.
    * Install the `transformers` library:

        ```bash
        pip install transformers
        ```

## How to Use

1.  Save the Python code as `text_generation_gpt.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script:

    ```bash
    python text_generation_gpt.py
    ```

5.  The script will:
    * Print examples of text generated from predefined prompts.
    * Prompt you to enter your own prompt.
    * Generate text based on your input.

## Code Description

* `text_generation_gpt.py`: The main Python script.
    * Imports the `pipeline` function from the `transformers` library.
    * Loads the pre-trained GPT-2 model using `pipeline('text-generation', model='gpt2')`.
    * Defines the `generate_text_gpt` function:
        * Takes a `prompt` (string) as input.
        * Uses the `generator` pipeline to generate text sequences.
        * Parameters:
            * `max_length`:  Maximum length of the generated text.
            * `num_return_sequences`: Number of text sequences to generate.
            * `do_sample`:  Enables sampling for more diverse output.
            * `top_k`:  Limits the token selection to the top K most likely tokens.
            * `top_p`:  Uses nucleus sampling to balance diversity and coherence.
        * Returns a list of generated text strings.
    * The main part of the script:
        * Defines a list of example prompts.
        * Calls `generate_text_gpt` for each prompt and prints the output.
        * Prompts the user to enter their own prompt using `input()`.
        * Generates and prints text based on the user's prompt.

## Example Output


============================== Text Generation using GPT-2
Prompt: 'Write a short story about a robot who learns to love.' Generated 1: 'Write a short story about a robot who learns to love. \n\nUnit 734 was designed for efficiency. Its metallic fingers moved with precision, assembling components on the factory line. It calculated, it processed, it obeyed. Love was not in its programming.' Generated 2: 'Write a short story about a robot who learns to love. \n\nUnit 7, designated "Custodian," moved through the gleaming corridors of the Orbital Habitat with quiet efficiency. Its programming dictated cleanliness, order, and the maintenance of optimal environmental conditions. Emotions were irrelevant, illogical, a human quirk best ignored.' Generated 3: 'Write a short story about a robot who learns to love. The rusty gears of Unit 7 creaked as it slowly extended a metallic arm. Its optical sensors, once a cold, calculating blue, flickered with a nascent warmth. It had been observing Elara, the biologist, for 734 cycles.'
Prompt: 'Explain the concept of quantum entanglement in simple terms.' Generated 1: 'Explain the concept of quantum entanglement in simple terms. Imagine you have two coins, and you flip them both at the same time, but you don't look at them. They're linked in a special way. Until you look, they're both in a mixed state of heads and tails. But the moment you look at one and see it's heads, you instantly know the other one is tails, even if they're miles apart. That's kind of like entanglement.' Generated 2: 'Explain the concept of quantum entanglement in simple terms. It's like having two gloves, one left and one right, and putting them in separate boxes. You don't know which box has which glove until you open one. Once you open a box and see the left glove, you instantly know the other box has the right glove. Entanglement is similar, but with quantum particles, and it's much weirder.' Generated 3: 'Explain the concept of quantum entanglement in simple terms. Think of it like two tiny dancers, perfectly synchronized. No matter how far apart they are, if one twirls to the left, the other instantly twirls to the right. They're connected in a way that defies classical physics. That's entanglement – a spooky connection between particles.'
... (Output for other predefined prompts) ...

Enter your own prompt:  The best way to learn a new language is
Generated text for your prompt:
1: 'The best way to learn a new language is to immerse yourself in it. That means surrounding yourself with the language as much as possible, both inside and outside of the classroom. Here are a few tips to help you get started:'
2: 'The best way to learn a new language is to immerse yourself in the culture of the language. This means not only learning the grammar and vocabulary, but also learning about the history, customs, and traditions of the people who speak the language.'
3: 'The best way to learn a new language is to find a method that works for you. There are many different ways to learn a language, and what works for one person may not work for another. Experiment with different methods until you find one that you enjoy and that helps you make progress.'

