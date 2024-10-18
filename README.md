

# SASHLab Stress CLI

## Overview

**SASHLab Stress** is a collection of scripts that run common stress-inducing tasks, designed for use in psychology experiments or stress-response testing. The CLI is intended to facilitate the application of various stress protocols in a streamlined manner.

## Features

The current script will run the available stress task for specified durations and save the output to an easily mungable CSV file.

### Current stressors

- **Mental Arithmetic Task**:
  - A mental subtraction task where participants subtract digits under time pressure. Task difficulty adjusts based on streaks of correct or incorrect answers (streak length is 3).

- **Negative/Neutral Speech Task**:
  - A speech task where participants are asked to recall either negative or neutral experiences. The task condition (negative or neutral) is determined by the user.

### Planned stressors

- Digit Span Task
- Nonsense Syllable Task

## Installation
Ensure you have Python 3.12 or newer. To install the CLI, run:

```sh
pip install sashlab-stress
```

## Usage
For the best results, ensure your terminal is pointed to the folder where you'd like participant data to be stored:

```sh
cd <path/to/your/project/data>
```

Run the main functionality of **SASHLab Stress** with default options:

```sh
sashlab_stress
```

### Examples

- To run the **mental arithmetic stress task**:

  ```sh  
    sashlab_stress --time-limit 600 --trial-time 20 --path ./data
  ```

- To run the **negative/neutral speech task** in neutral condition:

  ```sh
    sashlab_stress --task-type neg-neu-speech --condition 1 --time-limit 600 --path ./data
  ```

- To show help and view available commands:

  ```sh  
    sashlab_stress --help
  ```

## Options

- `--task-type`: The kind of task to run, either the mental subtraction task ('mental-subtraction') or the negative/neutral speech task ('neg-neu-speech').
  - **Type**: `str`
  - **Default**: `mental-subtraction`
  - **Example**: `--task-type neg-neu-speech` (runs the speech task)

- `--time-limit`: Set the time limit for the entire session in seconds.
  - **Type**: `int`
  - **Default**: `300` seconds (5 minutes)
  - **Example**: `--time-limit 600` (Sets the session duration to 10 minutes)

- `--trial-time`: Specify the maximum duration allowed for each individual trial before it times out due to lack of interaction.
  - **Type**: `int`
  - **Default**: `15` seconds
  - **Example**: `--trial-time 20` (Sets each trial timeout to 20 seconds)

- `--path`: Provide the path where session data will be saved.
  - **Type**: `path`
  - **Default**: Current working directory (`cwd`)
  - **Example**: `--path ./data` (Saves session data to a folder named "data" in the current directory)

- `--condition`: Set the condition for the speech task, with 0 representing negative condition and 1 representing neutral condition.
  - **Type**: `int`
  - **Default**: `0` (Negative condition)
  - **Example**: `--condition 1` (Runs the task in neutral condition)

## Dependencies
This project relies on the following packages:
- **black** (>=24.8.0): For code formatting.
- **inputimeout** (>=1.0.4): For handling time-based input during tasks.
- **keyboard** (>=0.13.5): To capture keyboard events during tasks.

All dependencies will be installed automatically with the package.

## Requirements
- Python 3.12 or higher
- Operating System: OS Independent

## Contributing
Contributions are welcome! If you have ideas for new stress tasks or improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/spider-z3r0/sashlab_stress/).

## Authors
- **Kevin O'Malley** - [kevomalley743@gmail.com](mailto:kevomalley743@gmail.com)
- **Sandra O'Brien** - [sandra.obrien@ul.ie](mailto:sandra.obrien@ul.ie)

## License
This project is licensed under the MIT License
