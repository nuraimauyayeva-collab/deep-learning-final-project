import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def compare_models(results, save_path):

    df = pd.DataFrame(results)

    plt.figure(figsize=(8,5))

    sns.barplot(
        x="model",
        y="f1",
        data=df
    )

    plt.title("Model Comparison")

    plt.savefig(save_path)

    plt.show()
