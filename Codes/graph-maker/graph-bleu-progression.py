import matplotlib
import matplotlib.pyplot as plt
import re
import numpy as np

matplotlib.use('Agg')

# Evaluation stages
stages = ["Zero-shot", "One-shot", "Few-shot", "Fine-tuned"]

# BLEU scores for each model
models = {
    "Gemma-9B": [0.3098, 0.4018, 0.4422, 0.5318],
    "LLaMA3.1-8B": [0.3118, 0.4156, 0.4478, 0.6606],
    "Phi-3.5-Mini-Instruct": [0.2953, 0.3682, 0.4010, 0.5987],
    "Qwen2.5-Coder-3B": [0.3362, 0.4101, 0.4743, 0.5763],
    "Mistral-7B-v0.3": [0.3118, 0.4135, 0.4404, 0.6260]
}

# Plot the BLEU score progression for each model
plt.figure(figsize=(10, 6))
for model, scores in models.items():
    plt.plot(stages, scores, marker='o', linestyle='-', label=model)

# Labels and title
plt.xlabel("Evaluation Stage")
plt.ylabel("BLEU Score")
plt.legend()
plt.grid(True)
plt.savefig("evaluation_progress.png")
plt.close()
