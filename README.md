

# Curvetopia

## Overview

**Curvetopia** is a Python project for processing and visualizing curve data. It involves reading CSV files containing curve data, performing various data processing steps (including regularization, symmetry detection, and curve completion), and finally rasterizing the results into SVG format.

## Project Structure

- `read_csv.py`: Module for reading CSV files containing curve data.
- `plot.py`: Module for visualizing the initial and processed curves.
- `regularize.py`: Module for regularizing curves.
- `symmetry.py`: Module for finding symmetries in curves.
- `complete.py`: Module for completing incomplete curves.
- `rasterization.py`: Module for converting curves to SVG format.
- `main.py`: The main script that processes the data files and generates SVG outputs.
- `.gitignore`: Specifies which files and directories to ignore in version control.
- `README.md`: This file.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/twin-techs.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd twin-techs
    ```

3. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv myenv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        myenv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source myenv/bin/activate
        ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your CSV files:** Place your CSV files with curve data in the `data` directory.

2. **Run the main script:**

    ```bash
    python main.py
    ```

3. **Check the output:** The processed SVG files will be saved in the `data` directory.

## Configuration

The `.gitignore` file is configured to exclude the following:

- `*.pyc` files
- `__pycache__` directories
- Virtual environment directories (e.g., `myenv/`)
- Any other files or directories you wish to exclude from version control

