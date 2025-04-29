
<br/>
<div align="center">
<img src="pylog_logo.png" alt="Logo" width="80" height="80">
</a>
<h3 align="center">PyLog</h3>
<p align="center">
Get rid of the <code><a href="https://logging.apache.org/log4j/2.x/index.html">log4j</a></code> based logging module, become a better debugger.
<br/>
<br/>
<a href="https://github.com/brodycritchlow/PyLog"><strong>Explore the docs »</strong></a>
<br/>
<br/>
<a href="https://github.com/brodycritchlow/PyLog/issues/new">Report Bug</a>
<a href="https://github.com/brodycritchlow/PyLog/issues/new">Request Feature</a>
</p>
</div>

## About The Project

`PyLog` is a Pythonic logging module designed to address the common complaints of the built-in [`logging`](https://docs.python.org/3/library/logging.html) module. It simplifies the logging process by providing a more intuitive configuration system, built-in context support, a flexible design, and a more Pythonic API. Additionally, `PyLog` offers better defaults, easier JSON logging, and improved debugging and introspection capabilities, making it easier to manage and maintain your application's logs.

Here's why PyLog is a game-changer:

- Your time should be focused on crafting a better debugging experience. PyLog simplifies the logging process, allowing you to focus on what matters most.
- You shouldn't be bogged down by tedious logging configurations. PyLog's intuitive configuration system and built-in context support streamline your workflow.
- You should be able to easily manage and maintain your application's logs. PyLog's flexible design, Pythonic API, and improved debugging capabilities make it easier to do just that.

Of course, PyLog is designed to be adaptable to different project needs. If you have suggestions for improvements or additional features, please fork this repo and create a pull request or open an issue. I appreciate any and all contributors.

### Built With

`PyLog` was choosen to be written in pure-python, rather than some other flavour, or even creating a module in C. This is mainly due to the fact that the libary is generally simple and doesn't require "insanely fast build times".

- [Python 3.13.2](https://www.python.org/downloads/release/python-3132/)

I personally choose **3.13.2t** due to the fact it is the most recent release version. I will be backporting PyLog to atleast **3.10.x**, and may go even further in the future.

### Installation

If you don't have Python installed, follow these steps to install Python and Pip:

1. **Install Python**: Go to the [Python download page](https://www.python.org/downloads/) and follow the installation instructions for your operating system.
2. **Install Pip**: Pip is usually installed with Python. If not, you can install it by following the instructions on the [Pip installation page](https://pip.pypa.io/en/stable/installation/).

If you prefer to use Conda, you can install Python and Pip using Conda:

1. **Install Conda**: Go to the [Conda download page](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions for your operating system.
2. **Create a new Conda environment**: Open a terminal or command prompt and run `conda create --name myenv python=3.8`.
3. **Activate the Conda environment**: Run `conda activate myenv`.
4. **Install Pip**: Pip is usually installed with Python. If not, you can install it by running `conda install pip`.

Once you have Python and Pip installed, you can install the `pylog` module using Pip:

```sh
python3 -m venv myenv
source myenv/bin/activate
pip install pythonlog
```

After installation, you can use `pylog` in your Python projects.

## Usage

Here is a quick snippet of how to use PyLog, it really is that simple:

```python
from pylog import logger
from pylog._enums import Levels

# Configure the logger with a custom format and output
logger.change(
    output="app.log",  # Log output to a file named "app.log"
    level=Levels.INFO,  # Set the logging level to INFO
    format="<green>{timestamp}<reset> - <blue>{level}<reset>: {message}"  # Define a log format with colors
)

# Log messages at different levels
logger.debug("This is a DEBUG message.")  # This won't appear because the level is set to INFO
logger.info("This is an INFO message.")  # This will appear
logger.warning("This is a WARNING message.")  # This will appear
logger.error("This is an ERROR message.")  # This will appear
logger.critical("This is a CRITICAL message.")  # This will appear
```

_For more examples, please refer to the [Documentation](https://example.com)_

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
## Contact

Brody Critchlow - [@thornily](http://discordapp.com/users/1190937272279912518) - brody@playprodix.com

Project Link: [https://github.com/brodyritchlow/pylog](https://github.com/brodyritchlow/pylog)

## Acknowledgments

- [othneildrew](https://github.com/othneildrew/Best-README-Template)
