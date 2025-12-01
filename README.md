# 📌 Image Integrity Agent  
### A lightweight AI agent that detects image tampering using Google ADK + Gemini.

---

## 🚀 Overview

Image Integrity Agent is designed to identify digital image manipulation including:

- Copy-move forgery  
- Splicing  
- Inpainting  
- Resampling  
- Metadata manipulation  
- Noise pattern inconsistencies  

Powered by **Gemini 2.0 Flash** and the **Google Agent Development Kit (ADK)**, this agent accepts text or images and returns a structured forensic analysis.

---

## 🏗 Tech Stack

| Component        | Technology Used |
|-----------------|-----------------|
| LLM Engine       | Gemini 2.0 Flash |
| Agent Framework  | Google ADK |
| API Server       | FastAPI |
| Image Processing | Pillow, OpenCV |
| Deployment       | Local or Cloud |

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/image-integrity-agent
cd image-integrity-agent
pip install -r requirements.txt
cp .env.example .env
