# Automated and Context-Aware Code Documentation by Leveraging Advanced LLMs

This repository contains the code for our paper *Automated and Context-Aware Code Documentation by Leveraging Advanced LLMs*, submitted to ACL Rolling Review.

## 🚀 Getting Started

### Prerequisites

Ensure you have Conda installed or use a virtual environment.

### Installation Steps

```bash
# Create a new conda environment
conda create --name javadoc python=3.8 -y

# Activate the environment
conda activate javadoc

# Clone the repository
git clone https://anonymous.4open.science/r/automated-documentation-generation-using-llm/
cd documentation-generation-using-llm

# Open the project in VS Code
code .
```

### Running the Graph Maker

```bash
cd graph-maker
python3 graph.py
```

## 🖥️ Model Training and Evaluation

We evaluated multiple models across zero-shot, one-shot, and few-shot settings. Fine-tuning was performed on Google Colab Pro (A100 GPU) for Gemma-2 and on Kaggle P100 GPU for LLAMA3.1, Mistral, Phi-3.5, and Qwen-2.5-Coder.

## 📌 Key Contributions

- **New dataset**: Contains reference documentation for methods, lambdas, packages, and classes from multiple public codebases.
- **Data filtering**: Combination of automated and manual techniques to remove noisy data.
- **Model fine-tuning**: Evaluation of multiple LLMs including LLAMA-3.1, Gemma-2, Phi-3, Mistral, and Qwen-2.5.
- **Comprehensive analysis**: Performance and efficiency comparison of fine-tuned models.

## 📊 Evaluation Results

### Zero-shot, One-shot, and Few-shot Performance

| Setting   | Model                | BLEU   | R1     | R2     | RL     | RLsum  |
|-----------|---------------------|--------|--------|--------|--------|--------|
| Zero-shot | Gemma-9B            | 0.3098 | 0.5522 | 0.2552 | 0.4491 | 0.5429 |
|           | LLaMA3.1-8B         | 0.3118 | 0.5734 | 0.2667 | 0.4696 | 0.5490 |
|           | Phi-3.5-Mini-Instruct| 0.2953 | 0.5230 | 0.2261 | 0.4381 | 0.5029 |
|           | Qwen2.5-Coder-3B    | 0.3362 | 0.5620 | 0.2770 | 0.4627 | 0.5431 |
|           | Mistral-7B-v0.3     | 0.3118 | 0.5104 | 0.2221 | 0.4342 | 0.5037 |
| One-shot  | Gemma-9B            | 0.4018 | 0.6270 | 0.2905 | 0.5055 | 0.6140 |
|           | LLaMA3.1-8B         | 0.4156 | 0.6428 | 0.2966 | 0.5211 | 0.6222 |
|           | Phi-3.5-Mini-Instruct| 0.3682 | 0.6016 | 0.2745 | 0.4961 | 0.5830 |
|           | Qwen2.5-Coder-3B    | 0.4101 | 0.6457 | 0.3243 | 0.5263 | 0.6294 |
|           | Mistral-7B-v0.3     | 0.4135 | 0.6200 | 0.2815 | 0.5147 | 0.6141 |
| Few-shot  | Gemma-9B            | 0.4422 | 0.6780 | 0.3522 | 0.5524 | 0.6715 |
|           | LLaMA3.1-8B         | 0.4478 | 0.6677 | 0.3422 | 0.5440 | 0.6579 |
|           | Phi-3.5-Mini-Instruct| 0.4010 | 0.6279 | 0.2942 | 0.4968 | 0.6217 |
|           | Qwen2.5-Coder-3B    | 0.4743 | 0.6852 | 0.3774 | 0.5708 | 0.6783 |
|           | Mistral-7B-v0.3     | 0.4404 | 0.6514 | 0.3294 | 0.5424 | 0.6444 |

### Performance After Fine-Tuning

| Model                | BLEU   | R1     | R2     | RL     | RLsum  |
|---------------------|--------|--------|--------|--------|--------|
| Gemma-9B            | 0.5318 | 0.8023 | 0.6734 | 0.7782 | 0.7997 |
| LLaMA3.1-8B         | 0.6606 | 0.9301 | 0.7213 | 0.8125 | 0.8279 |
| Phi-3.5-Mini-Instruct| 0.5987 | 0.8156 | 0.6947 | 0.7986 | 0.8136 |
| Qwen2.5-Coder-3B    | 0.5763 | 0.7936 | 0.6737 | 0.7676 | 0.7908 |
| Mistral-7B-v0.3     | 0.6260 | 0.7288 | 0.6372 | 0.7164 | 0.7275 |
