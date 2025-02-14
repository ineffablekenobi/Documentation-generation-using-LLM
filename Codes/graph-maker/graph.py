import matplotlib
import matplotlib.pyplot as plt
import re
import numpy as np

matplotlib.use('Agg')

def parse_input_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    data = {}
    model_name = None
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        if re.match(r'^[a-zA-Z]+:$', line):
            model_name = line[:-1]
            data[model_name] = []
        elif model_name:
            parts = line.split()
            if parts[0].isdigit():
                data[model_name].append([float(x) for x in parts])
    
    return data

def plot_loss_metrics(data, output_file="loss_plot.png"):
    colors = ["r", "g", "b", "c", "m", "y", "k"]
    plt.figure(figsize=(10, 6))
    for i, (model, values) in enumerate(data.items()):
        values = np.array(values)
        steps = values[:, 0]
        if values.shape[1] > 2:
            color = colors[i % len(colors)]
            plt.plot(steps, values[:, 1], marker="o", linestyle="-", label=f"{model} - Training Loss", color=color)
            plt.plot(steps, values[:, 2], marker="s", linestyle="--", label=f"{model} - Validation Loss", color=color)
    
    plt.xlabel("Step")
    plt.ylabel("Loss Value")
    plt.title("Training and Validation Loss")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    plt.close()

def plot_bleu_metrics(data, output_file="bleu_plot.png"):
    colors = ["r", "g", "b", "c", "m", "y", "k"]
    plt.figure(figsize=(10, 6))
    for i, (model, values) in enumerate(data.items()):
        values = np.array(values)
        steps = values[:, 0]
        if values.shape[1] > 3:
            plt.plot(steps, values[:, 3], marker="o", linestyle="-", label=f"{model} - Bleu Score", color=colors[i % len(colors)])
    
    plt.xlabel("Step")
    plt.ylabel("Bleu Score")
    plt.title("Bleu Score Progression")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    filename = "input.txt"
    data = parse_input_file(filename)
    plot_loss_metrics(data, "loss_plot.png")
    plot_bleu_metrics(data, "bleu_plot.png")
