# job-hunter-cli# Job Hunter CLI

A simple and user-friendly command-line job search tool for finding job postings on Indeed. Easily search by job title or keyword, location, and the number of pages to explore, with results displayed in a clean, readable table format.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.6+
- pip (Python package manager)

## Installation

1. Clone this repository:

   git clone https://github.com/noxvix/job-hunter-cli.git

2. Navigate to the project directory:

   cd job-hunter-cli

3. Install the required libraries:

   pip install -r requirements.txt

## Usage

To use Job Hunter CLI, simply run the following command:

   python job_finder.py

You'll be prompted to enter the job title or keywords, location, and the number of pages you'd like to search. The results will be displayed in a readable table format within the terminal.

## Customization

Currently, Job Hunter CLI is focused on Indeed job search results. However, you can customize the search query parameters directly within the `job_finder.py` file. For example, you could modify the `scrape_indeed_jobs()` function call with additional parameters supported by the Indeed API.

For more customization options or to add support for other job boards, you can extend the code in `job_finder.py`.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest new features.

1. Fork the repository.
2. Create a new branch with a descriptive name: `git checkout -b your-feature-branch`
3. Make your changes.
4. Commit your changes with a clear commit message: `git commit -m "Add a new feature"`
5. Push your changes to your fork: `git push origin your-feature-branch`
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
