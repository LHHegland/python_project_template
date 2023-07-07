# python_project_template

**NAMESPACE:** me.hegland-lance

**PURPOSE:** Offer a template collection of common Python project files to help create new  projects more quickly, easily, and reliably. See [more specific features](#features) for additional details.

.

## Table of Contents

- [Features](#features)
- [Background](#background)
- [Known Issues](#known-issues)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authors](#authors)
- [Roadmap](#roadmap)
- [License](#license)

.

## **Features**

- README.md template, including many of suggestions from [GitHub README Tips](https://readmetips.github.io/) and [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) written by Hillary Nyakundi and published by freeCodeCamp on December 8, 2021
- LICENSE.txt with basic [MIT License](https://choosealicense.com/licenses/mit/)
- Python module and function template, including the following:
  - docstring templates based on [Python docstring conventions](https://peps.python.org/pep-0257/)
  - sample code using [Python style coding conventions](https://peps.python.org/pep-0008/), including the following:
    - [function annotations](https://peps.python.org/pep-0008/#function-annotations)
    - [type hints](https://peps.python.org/pep-0484/)
    - [variable annotations](https://peps.python.org/pep-0008/#variable-annotations) and [variable annotation syntax](https://peps.python.org/pep-0526/)
  - command line interface help and usage instructions using [The Python Standard Library's argparse package](https://docs.python.org/3/library/argparse.html)
  - logging using an intra-project module [config_log.py](config_log.py) and [The Python Standard Library's logging package](https://docs.python.org/3/library/logging.html)
    - output (stderr) to either screen or file based on user instructions (see `py config_log.py -h`)
    - short "FYI" messages for info and debug logging levels
    - more detailed "alert" messages for warning, error, and critical logging levels
    - sample logging message testing for various levels (e.g. info, debug, warning, error, critical)
  - common and unexpected [exception trapping](https://docs.python.org/3/tutorial/errors.html) (i.e. error handling)
    - specified exception and unknown exception testing available based on user instructions (see `py config_log.py -h`)

.

## **Background**

Lance Hegland wanted application development templates for his personal use that might improve the readability, usability, testability, debuggability, and sustainability of his projects. So, he began developing and testing these templates while practicing [lean methodologies](https://www.lean.org/explore-lean/what-is-lean/), specifically the following activities:
- [5S (Sort, Set in Order, Shine, Standardize, and Sustain)](https://www.lean.org/lexicon-terms/five-s/)
- [Poka-Yok (mistake-proofing)](https://www.lean.org/lexicon-terms/poka-yoke/)
- [Just-in-Time (JIT)](https://www.lean.org/lexicon-terms/just-in-time-production/)

For more information about the lean methodology, visit the following:

- [Lean Enterprise Institute (LEI)](https://www.lean.org/explore-lean/what-is-lean/)
- [Lean Global Network (LGN)](https://leanglobal.org/what-is-lean/)
- [ASQ (American Society for Quality)](https://asq.org/quality-resources/lean)

.

## **Known Issues**

None

.

## **Requirements**

1. Familiarity and access to Python development tools, such as recent versions of the following:
   | Tool                         | Download | Reference | with VSCode |
   |------------------------------|----------|-----------|-------------|
   | VSCode | [Link](https://code.visualstudio.com/Download) | [Link](https://code.visualstudio.com/learn) | |
   | + Markdown Preview Github Styling | [Link](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) | | |
   | + GitHub Pull Requests and Issues | [Link](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) | | |
   | + Python Tools | [Link](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | | |
   | Python | [Link](https://www.python.org/downloads/) | [Link](https://wiki.python.org/moin/BeginnersGuide) | [Link](https://code.visualstudio.com/docs/languages/python) |
   | Git | [Link](https://git-scm.com/downloads) | [Link](https://git-scm.com/videos) | [Link](https://vscode.github.com/) |
   | GitHub  | | [Link](https://github.com) | [Link](https://code.visualstudio.com/docs/sourcecontrol/github) |

.

## **Installation**

1. Review [README.md](https://github.com/LHHegland/python_project_template/blob/master/README.md)
1. Perform the necessary actions to satisfy [minimum requirements](https://github.com/LHHegland/python_project_template/blob/master/README.md#requirements).
1. From your local projects directory, copy the entire remote GitHub repository LHHegland/python_examples into a local working area (`git clone git@github.com:LHHegland/python_project_template.git`)

.

## **Configuration**

None

.

## **Usage**

Review and adapt the code samples as you begin developing a new Python project to meet your specific needs.

.

## **Authors**

- Lance Hegland ([lance.hegland@gmail.com](mailto:lance.hegland@gmail.com))

.

## **Roadmap**

None

.

## **License**

[MIT License](https://choosealicense.com/licenses/mit/)

- See [LICENSE.txt](LICENSE.txt)
- See [GNU General Public License v3.0 (GNU GPLv3)](https://choosealicense.com/licenses/gpl-3.0/)