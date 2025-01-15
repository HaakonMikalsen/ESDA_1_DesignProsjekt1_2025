import matplotlib.pyplot as plt

# List all available styles
print("Available styles:")
print(plt.style.available)

# Optionally, display all styles as a grid of plots
for style in plt.style.available:
    plt.style.use(style)
    plt.figure(figsize=(6, 4))
    plt.plot([0, 1, 2, 3], [10, 20, 25, 30], label="Sample Line")
    plt.title(f"Style: {style}")
    plt.legend()
    plt.grid(True)
    plt.show()
