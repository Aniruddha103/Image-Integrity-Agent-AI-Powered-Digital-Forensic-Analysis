# 🛡️ Image Integrity Agent  
### AI-Powered Digital Image Forensics using Google ADK + Gemini 2.0 Flash

---

## 📌 Overview

Digital image manipulation has become widespread due to powerful editing tools and generative models.  
Detecting tampered images manually is slow, inconsistent, and requires forensic expertise.

**Image Integrity Agent** is an autonomous LLM-powered agent that performs:

- Image authenticity triage  
- Tampering classification  
- Forensic artifact explanation  
- Noise, texture, and compression anomaly analysis  
- Structured report generation  

The agent is built using the **Google Agent Development Kit (ADK)** and the **Gemini 2.0 Flash** model.

This project is submitted as part of the **Kaggle AI Agents Intensive Capstone Project (Google × Kaggle)**.

---

## 🎯 Goals of the Project

1. **Automate Digital Forensics**  
   Provide fast, accessible tampering detection for journalists, investigators, students, and enterprises.

2. **Demonstrate Agent Development Skills**  
   Showcase practical use of ADK features such as:  
   - LLM-powered agent  
   - Handlers (`on_text`, `on_binary`)  
   - Model configuration via `agent.yaml`  
   - Agent runtime via FastAPI  
   - Clean modular architecture  

3. **Prepare a scalable foundation**  
   Build a simple but extensible single-agent system that can later evolve into a full **multi-agent forensic pipeline**, including:
   - YOLO-based region detection  
   - Metadata extraction  
   - Noise-level estimation  
   - Evidence heatmaps  

---

## 🧠 What the Agent Can Do

✔ Accept images as binary input  
✔ Analyze them with Gemini  
✔ Detect possible tampering types  
✔ Provide human-readable forensic explanations  
✔ Output structured JSON-like findings  
✔ Respond to text queries for guidance  

### Example Response:


{
  "tampered": true,
  "confidence": 0.82,
  "tampering_type": "Copy-Move Splicing",
  "explanation": "The right side contains repeated patterns and inconsistent noise.",
  "artifacts_detected": [
      "Texture discontinuity",
      "Edge inconsistencies",
      "Noise variation anomalies"
  ]
}
