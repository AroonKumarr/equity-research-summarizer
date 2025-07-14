import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Read CSV
pd.set_option('display.max_colwidth', 100)
df = pd.read_csv("sample_text.csv")
print(df.shape)
print(df)

# Encode text
encoder = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
vectors = encoder.encode(df.text)

# Create FAISS index
dim = vectors.shape[1]
index = faiss.IndexFlatL2(dim)
print(index)

index.add(vectors)

# Encode search query
search_query = "I want to buy a polo t-shirt"
query_vec = encoder.encode([search_query])  # Shape: (1, dim)

# Search top 2 most similar texts
D, I = index.search(query_vec, k=2)

print("\nTop matches:")
for i, idx in enumerate(I[0]):
    print(f"{i+1}. {df.text[idx]} (Score: {D[0][i]:.4f})")
