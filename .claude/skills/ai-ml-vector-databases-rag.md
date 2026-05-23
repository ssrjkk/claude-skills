# Vector Databases and RAG Optimization

## Overview
Master vector databases for retrieval-augmented generation (RAG), similarity search, and semantic applications.

## Context
You are an AI engineer building RAG systems. You understand embeddings, similarity search, and knowledge bases.

## Key Principles
- **Embeddings Matter**: Quality embeddings = quality search
- **Chunking Strategy**: Balance context and specificity
- **Indexing**: Fast similarity search
- **Retrieval Quality**: Measure search relevance
- **Reranking**: Improve result quality

## Step-by-Step Instructions

### 1. Embeddings Fundamentals
```python
from openai import OpenAI
import numpy as np

# Generate embeddings
client = OpenAI()

texts = [
    "Python is a programming language",
    "The Eiffel Tower is in Paris",
    "Machine learning requires data"
]

# Get embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
)

embeddings = np.array([item.embedding for item in response.data])
print(embeddings.shape)  # (3, 1536)

# Similarity search
query = "What is Python?"
query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

# Cosine similarity
similarities = np.dot(embeddings, query_embedding) / (
    np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
)

print(similarities)  # [0.89, 0.12, 0.34]
```

### 2. Pinecone Setup
```python
from pinecone import Pinecone, ServerlessSpec

# Initialize
pc = Pinecone(api_key="your-api-key")

# Create index
pc.create_index(
    name="documents",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)

index = pc.Index("documents")

# Upsert vectors
index.upsert([
    ("id1", [0.1, 0.2, 0.3, ...], {"text": "Python tutorial", "source": "docs"}),
    ("id2", [0.2, 0.3, 0.4, ...], {"text": "Python guide", "source": "blog"})
])

# Query
results = index.query(
    vector=[0.15, 0.25, 0.35, ...],
    top_k=3,
    include_metadata=True
)

for match in results.matches:
    print(f"Score: {match.score}, Text: {match.metadata['text']}")
```

### 3. Chunking Strategy
```python
def chunk_text(text, chunk_size=512, overlap=100):
    """Split text into chunks with overlap"""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        if chunk.strip():
            chunks.append(chunk)
    return chunks

# Semantic chunking (better than fixed size)
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(document)

# For code
from langchain.text_splitter import Language, RecursiveCharacterTextSplitter

code_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=512,
    chunk_overlap=100
)

code_chunks = code_splitter.split_text(code)
```

### 4. LangChain RAG Pipeline
```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Setup
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Pinecone.from_existing_index("documents", embeddings)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create QA chain
llm = ChatOpenAI(model="gpt-4", temperature=0)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    verbose=True
)

# Query
answer = qa.run("What is Python used for?")
```

### 5. Reranking for Quality
```python
from sentence_transformers import CrossEncoder

# Load reranker
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Get initial results
top_k = 10
results = vectorstore.similarity_search_with_score(query, k=top_k)

# Rerank
pairs = [(query, doc.page_content) for doc, score in results]
scores = model.predict(pairs)

# Sort by rerank score
reranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)

# Return top 3
final_results = [doc for (doc, score), rerank_score in reranked[:3]]
```

## Real-World Examples

### Example 1: Documentation Search
```python
# Build knowledge base from docs
docs = load_pdf_documents("docs/")

# Chunk
chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc.content, chunk_size=512))

# Embed and store
embeddings_list = []
for chunk in chunks:
    emb = get_embedding(chunk)
    embeddings_list.append(emb)

index.upsert([(str(i), emb, {"text": chunk}) for i, emb in enumerate(embeddings_list)])

# Query
query = "How do I deploy?"
query_emb = get_embedding(query)
results = index.query(query_emb, top_k=3)

# Results: Top 3 most relevant docs
```

### Example 2: Code Search
```python
# Index code files
code_files = find_all_python_files("src/")

for file in code_files:
    with open(file) as f:
        code = f.read()
    
    # Chunk by function
    functions = extract_functions(code)
    
    for func in functions:
        embedding = get_embedding(func.code)
        index.upsert([(
            func.name,
            embedding,
            {
                "code": func.code,
                "file": file,
                "function": func.name
            }
        )])

# Find similar implementation
similar = index.query(get_embedding("pagination logic"), top_k=5)
```

### Example 3: Multi-Modal RAG
```python
# Combine text + images
from langchain.embeddings.openai import OpenAIEmbeddings

# Embed both text and image descriptions
documents = [
    {"content": "Python guide", "type": "text"},
    {"content": "image description...", "type": "image"}
]

for doc in documents:
    embedding = embeddings.embed_query(doc["content"])
    index.upsert([(doc["id"], embedding, doc)])
```

## Best Practices
- ✅ Use high-quality embeddings (text-embedding-3-large)
- ✅ Chunk documents semantically
- ✅ Include metadata for filtering
- ✅ Use reranking for top results
- ✅ Monitor retrieval quality
- ✅ Cache embeddings
- ✅ Update indexes regularly
- ❌ Don't over-chunk (lose context)
- ❌ Don't use cheap embeddings
- ❌ Don't skip quality testing

## Vector Databases
- Pinecone (managed, easiest)
- Weaviate (open-source)
- Qdrant (fast, quantized)
- Milvus (scalable)
- Vespa (production-grade)

## Related Skills
- ai-ml-langchain-rag
- ai-ml-finetuning-llm
- backend-database-design-patterns
