# -*- coding: utf-8 -*-
"""
Text Generation Model using GPT

This notebook demonstrates text generation using a pre-trained GPT-2 model
from the Transformers library.
"""

# ## Install Transformers Library
# If you don't have it installed already, run this:
# ```bash
# pip install transformers
# ```

# ## Import the pipeline for text generation
from transformers import pipeline

# ## Load the pre-trained GPT-2 model
# We'll use the 'gpt2' model, which is a good general-purpose model.
# You can experiment with other models like 'gpt-neo' or 'gpt2-medium' if you like.
generator = pipeline('text-generation', model='gpt2')

# ## Define a function to generate text
def generate_text_gpt(prompt, max_length=100, num_return_sequences=3):
    """
    Generates text based on a given prompt using the loaded GPT-2 model.

    Args:
        prompt (str): The text to start the generation from.
        max_length (int): The maximum length of the generated text.
        num_return_sequences (int): The number of different sequences to generate.

    Returns:
        list: A list of generated text sequences.
    """
    generated_sequences = generator(prompt,
                                     max_length=max_length,
                                     num_return_sequences=num_return_sequences,
                                     do_sample=True, # Enable sampling for more diverse outputs
                                     top_k=50,       # Consider only the top k tokens
                                     top_p=0.95)     # Nucleus sampling
    return [seq['generated_text'] for seq in generated_sequences]

# ## Demonstrate text generation with user prompts

print("=" * 30)
print("Text Generation using GPT-2")
print("=" * 30)

user_prompts = [
    "Write a short story about a robot who learns to love.",
    "Explain the concept of quantum entanglement in simple terms.",
    "Give me some creative ideas for a weekend trip.",
    "The importance of exercise is",
    "Once upon a time in a faraway land,"
]

for prompt in user_prompts:
    print(f"\nPrompt: '{prompt}'")
    generated_texts = generate_text_gpt(prompt)
    for i, text in enumerate(generated_texts):
        print(f"  Generated {i+1}: '{text}'")
    print("-" * 20)

# ## You can also try your own prompts here:
custom_prompt = input("\nEnter your own prompt: ")
if custom_prompt:
    generated_texts = generate_text_gpt(custom_prompt)
    print(f"\nGenerated text for your prompt:")
    for i, text in enumerate(generated_texts):
        print(f"  {i+1}: '{text}'")