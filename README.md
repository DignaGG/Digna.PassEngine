# Digna.PassEngine

![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A modular, cryptographically secure password generation engine built with Python. 

## 🎯 Overview
Digna.PassEngine is not just a simple script; it is a structured logic engine designed with a **Security-First** approach. This project marks the transition of my **developer journey** from C#/.NET to the Python ecosystem, focusing on modularity and clean code standards.

## 🏗️ Architecture
The project is divided into discrete modules to ensure single responsibility and high maintainability:

* **Core Engine (`generator.py`)**: Handles the password generation logic using the `secrets` module for cryptographically secure randomness.
* **Validator (`validator.py`)**: A rule-based validation system that ensures every generated password meets strict security criteria.
* **Data Models (`password_config.py`)**: Utilizes Python `dataclasses` for type-safe and structured configuration management.
* **Enums (`password_type.py`)**: Defines password complexity levels for future strategy-based generation.

## 🔒 Security
Unlike standard `random` libraries, this engine utilizes the **CSPRNG** (Cryptographically Secure Pseudo-Random Number Generator) provided by the Python `secrets` module, making it suitable for security-sensitive applications.

## 🚀 Roadmap & Evolution
This repository follows an evolutionary development path:

- [x] **v1.0.0 (Baseline)**: Core logic, terminal interface, and modular class structure.
- [ ] **v2.0.0 (Modular Refactoring)**: Transitioning to a professional Python package structure with directory-based modularity.
- [ ] **v3.0.0 (GUI Integration)**: Implementation of a modern Graphical User Interface (CustomTkinter/PyQt).

## 🛠️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/DignaGG/Digna.PassEngine.git](https://github.com/DignaGG/Digna.PassEngine.git)
2. Navigate to the directory:
   ```bash
    cd Digna.PassEngine
3. Run the engine:
   ```bash
    python main.py

## ✍️ Author & Documentation Notes
**Author:** DignaGG (DignaSoftware)

**Design & Translation Note:** The core architecture, algorithms, and system logic of this engine are natively designed and developed in Turkish. To comply with international open-source coding standards, the code comments, docstrings, and this README were translated into English with AI assistance. The primary focus remains strictly on **cryptographic security**, **architectural stability**, and **clean development principles**.

License: This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
