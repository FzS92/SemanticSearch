"""
Semantic Search Interface

This script implements a Gradio interface for performing semantic search
on a given text. It allows users to input an encoder model,
a search query, and a main text, and retrieves the top five paragraphs
that share similar meaning.


Usage:
1. Set the desired valuess.
2. Run the script.
3. The Gradio interface will be launched, allowing you to interact with
the semantic search functionality.
"""

import gradio as gr

from src import read_string_from_file, semantic_search

# Inputs
text_example = read_string_from_file("./example/text_example.txt")
model_name = gr.Textbox(
    value="all-mpnet-base-v2", label="Encoder model (See the code)"
)  # find the list here: https://www.sbert.net/docs/pretrained_models.html
searching_for = gr.Textbox(value="IoT in healthcare", label="Semantic search for")
text = gr.Textbox(value=text_example, label="Your main text")

# outputs
out = gr.Textbox(
    value="Press submit", label="Top five paragraphs that share similar meaning"
)

if __name__ == "__main__":
    iface = gr.Interface(
        fn=semantic_search,
        title="Semantic Search",
        inputs=[model_name, searching_for, text],
        outputs=[out],
    )

    iface.launch(share=False)  # share=False to share with others
