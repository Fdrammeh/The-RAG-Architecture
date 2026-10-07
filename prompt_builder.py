# Create a file called prompt_builder.py that:
# Takes a user question and a list of retrieved document chunks (simulated)
# Assembles a complete RAG prompt with:
# A system prompt instructing the model to answer from context only
# The retrieved chunks formatted with source labels
# The user’s question
# Instructions to cite sources
# Prints the assembled prompt and its token count estimate (characters / 4 as a rough approximation)
# Tests with at least 2 different questions and different sets of "retrieved" chunks

"""
L2 — The RAG Architecture: Prompt Builder  (STARTER)
======================================================
Run with:
    python prompt_builder.py

Your goal: build the prompt assembly step of a RAG pipeline.

Required features:
    1. A SYSTEM_PROMPT string that instructs the model to:
       - Answer ONLY from the provided context
       - Say "I don't have enough information" when the answer isn't in the context
       - Cite sources by name
    2. A format_chunks(chunks) function that formats a list of chunk dicts into
       a single context string — each chunk labelled with its source
    3. A build_prompt(question, chunks) function that returns the complete
       assembled prompt as a string (system prompt + context + question)
    4. A token_estimate(text) helper that returns characters // 4
    5. A run_test(question, chunks) function that assembles and prints the
       full prompt + token count
    6. At least 2 test cases with different questions and chunk sets

Key concepts:
    Chunk dict format:
        {"text": "...", "source": "filename.txt", "distance": 0.42}

    Prompt assembly pattern:
        [System prompt]
        CONTEXT:
        [Source: doc1.txt]
        <chunk text>

        ---

        [Source: doc2.txt]
        <chunk text>
        USER QUESTION: <question>

    Token estimate:
        A rough approximation: len(text) // 4
        (GPT-4 uses ~4 chars per token on average)
"""

# ── System prompt ──────────────────────────────────────────────────────────
# TODO: Write a SYSTEM_PROMPT string that instructs the model to:
#   - Answer ONLY from the context provided
#   - Say "I don't have enough information" if the answer isn't present
#   - Cite sources by mentioning the document name
from modulefinder import test
from unittest import result


SYSTEM_PROMPT = "Answer ONLY from the context provided\n - Say \"I don't have enough information\" if the answer isn't present\n - Cite sources by mentioning the document name"  # 



# ── Helpers ────────────────────────────────────────────────────────────────

def format_chunks(chunks: list[dict]) -> str:
    """Format a list of chunk dicts into a context string."""
    # TODO: For each chunk, produce:
    #   [Source: <chunk["source"]>]
    #   <chunk["text"]>
    # Separate chunks with "\n\n---\n\n"
    # TODO
    formatted_chunks = []
    for chunk in chunks:
        formatted_chunk = f"[Source: {chunk['source']}]\n{chunk['text']}"
        formatted_chunks.append(formatted_chunk)
    return "\n\n---\n\n".join(formatted_chunks)

def token_estimate(text: str) -> int:
    """Rough token count estimate: characters // 4."""
    # TODO: return len(text) // 4
     # TODO
    return len(text) // 4


def build_prompt(question: str, chunks: list[dict]) -> str:
    """Assemble the full RAG prompt."""
    # TODO: Combine SYSTEM_PROMPT, "CONTEXT:\n" + format_chunks(chunks),
    #   and "USER QUESTION: " + question into one string
    return f"{SYSTEM_PROMPT}\nCONTEXT:\n{format_chunks(chunks)}\nUSER QUESTION: {question}"


# ── Test runner ────────────────────────────────────────────────────────────

def run_test(question: str, chunks: list[dict]) -> None:
    """Assemble and print a prompt with token estimate."""
    # TODO: Call build_prompt(), print the result, print the token estimate
     # TODO
    result = build_prompt(question, chunks)
    print(result)
    print(f"Token estimate: {token_estimate(result)}")

# ── Test cases ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test case 1
    # TODO: Define a question and at least 2 simulated chunks, call run_test()

    # Test case 2
    # TODO: Define a different question and different chunks, call run_test()
    

    test_case1 = "How does FastAPI validate user input?"

    chunks1 = [
    {
        "text": "FastAPI uses Pydantic models to validate incoming request data.",
        "source": "fastapi.txt",
        "distance": 0.25
    },
    {
        "text": "Pydantic checks whether data matches the expected schema.",
        "source": "pydantic.txt",
        "distance": 0.31
    }
]

run_test(test_case1, chunks1)

test_case2 = "What are the benefits of using FastAPI for web development?"

chunks2 = [
    {
        "text": "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.",
        "source": "fastapi.txt",
        "distance": 0.15
    },
    {
        "text": "It allows for automatic generation of OpenAPI and JSON Schema documentation.",
        "source": "documentation.txt",
        "distance": 0.22
    }
]

run_test(test_case2, chunks2)