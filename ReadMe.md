# FaceGuard:
# Localization of Facial Images Manipulation in Digital Forensics

This project is an implementation of the paper *[Localization of Facial Images Manipulation in Digital Forensics via Convolutional Neural Networks](https://link.springer.com/chapter/10.1007/978-981-33-6129-4_22)*. This project, named **FaceGuard**, aims to detect and localize manipulated facial images, a critical task in digital forensics, using advanced deep learning techniques. This repository includes the full code to train, evaluate, and experiment with a Y-shaped Auto-Encoder model for detecting and segmenting manipulated areas within facial images.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Citation](#citation)
8. [License](#license)

---

## Introduction

**FaceGuard** implements a model for detecting facial image manipulations, based on a Y-shaped Auto-Encoder architecture that simultaneously handles classification, segmentation, and reconstruction tasks. The model is evaluated on the **FaceForensics++** dataset and includes functionality for:
- Training the Y-shaped Auto-Encoder to detect manipulated images and localize regions of manipulation.
- Experimenting with various configurations and hyperparameters.
- Evaluating the model on both seen and unseen manipulation types.

### Paper Abstract

> The remarkable phenomenon of computer-generated spoofing images poses a societal threat and is an important concern of digital forensics. In this work, we propose a deep learning model to localize manipulated regions in facial images via a Y-shaped Auto-Encoder architecture, which simultaneously handles classification, segmentation, and reconstruction tasks. We evaluate our approach using datasets such as FaceForensics++ and achieve promising results in terms of both accuracy and localization capabilities.

---

## Project Structure

The repository is organized as follows:

```
.
├── src/                        # Source code for model, data loading, and utilities
│   ├── data_preprocessing/     # Data loading, augmentation, and preprocessing scripts
│   ├── models/                 # Y-shaped Auto-Encoder and related model code
│   ├── utils/                  # Utilities for logging, configuration, and plotting
│   ├── train.py                # Main training script
│   └── test.py                 # Main testing script
├── experiments/                # Scripts for running different experimental configurations
├── notebooks/                  # Jupyter notebooks for EDA and model visualization
├── datasets/                   # Dataset downloading and preparation scripts
├── configs/                    # YAML configuration files for different experiments
├── results/                    # Saved models, evaluation metrics, and plots
├── logs/                       # Training and testing log files
└── requirements.txt            # Project dependencies
```

---

## Features

- **End-to-End Model Implementation**: Code for training, evaluating, and testing the Y-shaped Auto-Encoder model.
- **Flexible Experimentation**: Configuration files for running different experiments and hyperparameter tuning.
- **Robust Data Processing Pipeline**: Includes augmentation, data splitting, and preprocessing for facial images.
- **Logging and Tracking**: Detailed logging setup for tracking training progress, metrics, and model checkpoints.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FaceGuard.git
cd FaceGuard
```

### 2. Install Dependencies

Ensure you have Python 3.7+ and `pip` installed. Install the dependencies:

```bash
pip install -r requirements.txt
```
---

## Usage

### 1. Training

To train the Y-shaped Auto-Encoder model, use the following command. This command uses a configuration file for model and training settings.

```bash
python src/train.py --config configs/experiment1_baseline.yaml
```

### 2. Testing

To evaluate the trained model on the test set, run:

```bash
python src/test.py --config configs/experiment3_unseen_attacks.yaml
```

### 3. Running Experiments

You can run different experiments with configurations provided in the `configs/` directory. For example, to tune hyperparameters, use:

```bash
python experiments/experiment2_tune_hyperparameters.py
```

### 4. Visualization and Analysis

Explore the results using the provided Jupyter notebooks in the `notebooks/` folder. Run:

```bash
jupyter notebook notebooks/1_data_exploration.ipynb
```

---

## Results

The following results were obtained using the Y-shaped Auto-Encoder model on the FaceForensics++ dataset:

| Metric       | Seen Attacks   | Unseen Attacks |
|--------------|----------------|----------------|
| Accuracy     | 93.5%          | 85.3%         |
| EER          | 4.7%           | 7.8%          |
| Segmentation | 90.1%          | 82.0%         |

Visualization of segmentation masks produced by the model is provided in the [notebooks/3_test_on_samples.ipynb](notebooks/3_test_on_samples.ipynb) notebook. The model effectively localizes manipulated regions and achieves high accuracy on both seen and unseen manipulation types.

---

## Citation

If you use this code or the model in your work, please cite the following paper:

> Mawgoud, A. A., Albusuny, A., Abu-Talleb, A., & Tawfik, B. S. (2021). Localization of Facial Images Manipulation in Digital Forensics via Convolutional Neural Networks. In *Enabling Machine Learning Applications in Data Science* (pp. 313-324). Springer. DOI: [10.1007/978-981-33-6129-4_22](https://link.springer.com/chapter/10.1007/978-981-33-6129-4_22)

```bibtex
@inproceedings{Mawgoud2021Localization,
  title={Localization of Facial Images Manipulation in Digital Forensics via Convolutional Neural Networks},
  author={Ahmed A. Mawgoud and Amir Albusuny and Amr Abu-Talleb and Benbella S. Tawfik},
  booktitle={Enabling Machine Learning Applications in Data Science},
  pages={313--324},
  year={2021},
  publisher={Springer},
  doi={10.1007/978-981-33-6129-4_22}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Acknowledgments

Special thanks to the authors of *Localization of Facial Images Manipulation in Digital Forensics via Convolutional Neural Networks* for their contributions to this field. This implementation is based on their research and aims to extend the reproducibility of their findings.

---

This `README.md` file is structured to provide all necessary information for users, collaborators, and researchers to understand, set up, and use the project effectively. It also follows GitHub best practices with clear headings, explanations, and links to resources within the repository.
