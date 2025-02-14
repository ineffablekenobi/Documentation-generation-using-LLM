import matplotlib
import matplotlib.pyplot as plt
import re
import numpy as np

matplotlib.use('Agg')

# Models
models = ["Gemma-9B", "LLaMA3.1-8B", "Phi-3.5", "Qwen2.5-Coder-3B", "Mistral-7B"]

# ROGUE-L scores across different evaluation stages
rogue_l_scores = {
    "Zero-Shot": [0.5524, 0.544, 0.4968, 0.5708, 0.5424],
    "One-Shot": [0.6231, 0.6012, 0.5384, 0.6497, 0.5915],
    "Few-Shot": [0.7053, 0.6784, 0.6215, 0.7156, 0.6739],
    "Fine-Tuned": [0.7782, 0.8125, 0.7986, 0.7676, 0.7164]
}

# ROGUE-Lsum scores across different evaluation stages
rogue_lsum_scores = {
    "Zero-Shot": [0.6715, 0.6579, 0.6217, 0.6783, 0.6444],
    "One-Shot": [0.7152, 0.7013, 0.6498, 0.7314, 0.6897],
    "Few-Shot": [0.7881, 0.7724, 0.7345, 0.8012, 0.7598],
    "Fine-Tuned": [0.7997, 0.8279, 0.8136, 0.7908, 0.7275]
}

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(models))
width = 0.15

# Colors for different evaluation stages
colors = ["blue", "green", "orange", "red"]
eval_stages = list(rogue_l_scores.keys())

for i, stage in enumerate(eval_stages):
    ax.bar(x + (i - 1.5) * width, rogue_l_scores[stage], width, label=f"ROGUE-L {stage}", color=colors[i], alpha=0.6)

for i, stage in enumerate(eval_stages):
    ax.bar(x + (i - 1.5) * width + 0.05, rogue_lsum_scores[stage], width, label=f"ROGUE-Lsum {stage}", hatch="///", edgecolor="black", fill=False)

# Labels and title
ax.set_xlabel("Models")
ax.set_ylabel("Score")
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=15)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("evaluation_progress.png")
plt.close()

