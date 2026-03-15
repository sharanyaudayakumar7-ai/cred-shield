from setuptools import setup, find_packages

setup(
    name="credshield",
    version="0.1.0",
    description="Cred Shield AI Detection Engine",
    author="Cred Shield Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch",
        "transformers",
        "scikit-learn",
        "numpy",
        "pandas",
        "nltk",
        "spacy",
        "textstat",
        "datasets",
        "accelerate",
        "evaluate",
        "wandb"
    ],
    entry_points={
        "console_scripts": [
            "credshield-train=scripts.train_model:main",
            "credshield-eval=scripts.evaluate_model:main",
            "credshield-demo=scripts.demo_detection:main"
        ]
    },
)
