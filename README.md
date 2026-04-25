# Multimodal Product Understanding System (CLIP + LLM)

## 🚀 Overview
This project demonstrates a multimodal AI system that combines image and text understanding using CLIP embeddings and LLMs for downstream tasks like product tagging and retrieval.

## 🧠 Problem
Product catalogs often have inconsistent descriptions and images. This system improves tagging and retrieval by aligning visual and textual representations.

## 🏗️ Architecture
- CLIP for image & text embeddings
- FAISS for vector similarity search
- LLM for tag generation

## ⚙️ Pipeline
1. Generate embeddings using CLIP
2. Store embeddings in FAISS
3. Perform similarity search
4. Pass retrieved context to LLM
5. Generate tags / classification

## 📊 Dataset
A curated dataset of ~3K product samples collected from real-world product listings, including noisy descriptions and varying image quality.

## ⚔️ Challenges
- Embedding misalignment
- Noisy text data
- LLM hallucination

## 📈 Evaluation
- Top-K retrieval accuracy
- Semantic relevance of tags
- Manual evaluation

## 🛠️ Tech Stack
Python, CLIP, FAISS, OpenAI API, Transformers

## 🔮 Future Improvements
- Fine-tuning CLIP
- Better multimodal fusion
- Real-time deployment
