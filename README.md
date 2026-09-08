# 0x00. AirBnB Clone - The Console (Part I)

## Description

The **AirBnB Clone** is a full-stack web application project created as part of the **SE 203: Application of Programming Concepts I** curriculum. This first phase focuses on establishing the project's foundation by building a custom data model (`BaseModel`) and a persistent JSON serialization engine (`FileStorage`).

---

## Command Interpreter & Architecture

The project is structured into modular Python packages:
- **`models/`**: Defines data models for objects in the system.
  - **`base_model.py`**: Parent class providing unique IDs (`uuid`), creation/update timestamps (`datetime`), string representations, and serialization dictionary conversion (`to_dict()`).
- **`models/engine/`**: Contains persistent storage implementations.
  - **`file_storage.py`**: Handles object serialization to a JSON file (`file.json`) and deserialization back into Python instances.
- **`tests/`**: Unit testing suite for validating models and storage engine logic.

---

## Environment & Requirements

- **OS**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.8.5
- **Style Standard**: `pycodestyle` (version 2.8.*)

---

## How to Run Unit Tests

All unit tests are located inside the `tests/` directory and use Python's built-in `unittest` module.

### Interactive Mode:
```bash
python3 -m unittest discover tests
```

### Non-Interactive Mode:
```bash
echo "python3 -m unittest discover tests" | bash
```

### Run a specific test file:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

---

## Authors

- **Kingsley Kipkoech**
- **Lamis Diyaa**
