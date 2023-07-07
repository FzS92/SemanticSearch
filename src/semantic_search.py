"""
Semantic Search

This script performs semantic search by measuring the similarity between two texts.
"""
from typing import List

import torch
from sentence_transformers import SentenceTransformer
from torch.nn.functional import cosine_similarity

from .utils import remove_extra_newlines, separate_paragraphs


def encode_text(text: List[str], model: SentenceTransformer) -> torch.Tensor:
    """
    Encode the given list of texts using the specified model.

    Args:
        text (List[str]): The input texts to be encoded.
        model (SentenceTransformer): The model used for encoding.

    Returns:
        torch.Tensor: The encoded texts as a tensor.
    """
    with torch.no_grad():
        outputs = model.encode(text)
        outputs = torch.tensor(outputs)
    return outputs


def get_top_n_cosine_similarity_rows(
    tensor1: torch.Tensor, tensor2: torch.Tensor, topk: int
) -> torch.Tensor:
    """
    Get the indices of the top N rows with highest cosine similarity scores
    between two tensors.

    Args:
        tensor1 (torch.Tensor): The first tensor.
        tensor2 (torch.Tensor): The second tensor.
        n (int): The number of top rows to retrieve.

    Returns:
        torch.Tensor: The indices of the top N rows.
    """
    similarity_scores = cosine_similarity(tensor1, tensor2)
    top_n_indices = torch.topk(similarity_scores.squeeze(), topk)[1]
    return top_n_indices


def semantic_search(model_name: str, searching_for: str, text: str) -> str:
    """
    Perform semantic search by measuring the similarity between the
    searching_for text and the text corpus.

    Args:
        model_name (str): The name of the SentenceTransformer model.
        searching_for (str): The text to search for.
        text (str): The corpus of text to search in.

    Returns:
        str: The search results as a formatted string.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SentenceTransformer(model_name).to(device)

    text = remove_extra_newlines(text)
    text = separate_paragraphs(text)
    searching_for = remove_extra_newlines(searching_for)
    search_and_text = [searching_for]
    search_and_text.extend(text)

    encoded = encode_text(search_and_text, model)

    encoded_search = encoded[0]  # Encode of searching_for
    encoded_text = encoded[1:]  # Encode of text

    n_similar_texts = 5  # 5 top search results
    n_similar_texts = min(n_similar_texts, len(text))

    index_of_similar = get_top_n_cosine_similarity_rows(
        encoded_search, encoded_text, n_similar_texts
    )

    output = f"Top {n_similar_texts} are as follows:\n\n"
    for i in range(n_similar_texts):
        output += f"Match number {i+1}:\n"
        output += text[index_of_similar[i]] + "\n\n"

    return output
