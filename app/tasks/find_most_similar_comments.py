import os
import numpy as np
from itertools import combinations
from ..file_utils import read_lines
from ..openai_client import OpenAI

def get_embeddings(texts):
    """Fetch embeddings for multiple texts in a single API call."""
    client = OpenAI()
    response = client.get_embeddings(texts)
    return {text: np.array(embed["embedding"]) for text, embed in zip(texts, response["data"])}

def cosine_similarity_matrix(embeddings):
    matrix = np.array(list(embeddings.values()))
    norm = np.linalg.norm(matrix, axis=1, keepdims=True)
    similarity_matrix = (matrix @ matrix.T) / (norm @ norm.T)
    return similarity_matrix

def find_most_similar_comments(input_file: str, output_file: str):
    comments = read_lines(input_file)
    if len(comments) < 2:
        raise ValueError("Not enough comments to find a similar pair")

    embeddings = get_embeddings(comments)

    similarity_matrix = cosine_similarity_matrix(embeddings)

    np.fill_diagonal(similarity_matrix, -1)
    most_similar_idx = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)

    most_similar_pair = (comments[most_similar_idx[0]], comments[most_similar_idx[1]])

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(most_similar_pair[0] + "\n")
        file.write(most_similar_pair[1] + "\n")
