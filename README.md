
# SASHLab Stress CLI

## Overview

**SASHLab Stress** is a collection of scripts that run common stress-inducing tasks, designed for use in psychology experiments or stress-response testing. The CLI is intended to facilitate the application of various stress protocols in a streamlined manner.

## Features

The curernt script will run the available stress task for specified durations and save the output to an easily mungable csv file.

### Current stressors

 - Mental arithmatic task
   - This is a mental subtraction task in which participants are asked to subtract digits in thier head under time pressure. The task difficulty will increase or decrease depending on a streak of correct or incorrect answers (the streak length is currently 3). 


### Planned stressors

 - digit span
 - nonsense syllable task




## Installation
Ensure you have Python 3.12 or newer. To install the CLI, run:

```{shell}
pip install sashlab-stress
```
## Usage
You can run the main functionality of **SASHLab Stress** using the following command:

```{shell}
sashlab_stress [options]
```

### Examples
- To run the basic mental arithmatic stress task:

  ```{shell}  
    sashlab_stress --time-limit 600 --trial-time 20 --path ./data
  ```

- To show help and view available commands:

  ```{shell}  
    sashlab_stress --help
  ```

## Options
Below are the command-line arguments supported by the **SASHLab Stress** CLI:

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
Contributions are welcome! If you have ideas for new stress tasks or improvements, feel free to open an issue or submit a pull request on the [GitHub repository](URL_TO_REPOSITORY).

## Authors
- **Kevin O'Malley** - [kevomalley743@gmail.com](mailto:kevomalley743@gmail.com)
- **Sandra O'Brien** - [sandra.obrien@ul.ie](mailto:sandra.obrien@ul.ie)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Keywords
`stress`, `psychology`, `CLI`his project is licensed under the MIT License - see the LICENSE file for details.
