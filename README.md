# Evas Closet

[![CI Pipeline](https://github.com/dylan-ramer/evas-closet/actions/workflows/ci.yml/badge.svg)](https://github.com/dylan-ramer/evas-closet/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-yellow.svg)](LICENSE)

A simple wardrobe tracking application. Manage clothes per-piece with image, color, size, and condition data.

## Setup

1. Clone the repository:
```bash
> git clone https://github.com/dylan-ramer/evas-closet.git
> cd evas-closet
```

2. Establish virtual environment:
```bash
> python -m venv venv
# Windows
> venv\Scripts\activate
# Mac/Linux
> source venv/bin/activate
```

3. Install dependencies:
```bash
> pip install -r requirements.txt
```

4. Run the Flask app:
```bash
> FLASK_APP=src
> Flask run
```

5. Open browser to [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)

## Features

TBD

## Future Roadmap

TBD

## Contributors

Project and Development Lead: [`@dylan-ramer`](https://github.com/dylan-ramer)

## License

This project is licensed under the **GNU General Public License v3.0**.
Anyone is free to use, alter, or distribute this software, however derivative work must be released open-source under the same license.

See [LICENSE](./LICENSE) for more information.