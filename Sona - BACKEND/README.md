# Sona - BACKEND

## Overview

Sona's backend application built with FastAPI(main.py) & index.js . It provides various functionalities necessary for the main application, including [describe the key functionalities or services it provides, e.g., text generation, API interactions, etc.].

## Setup

### Prerequisites

- Python 3.8 or higher
- [Node.js](https://nodejs.org/) (includes Yarn for managing JavaScript dependencies)

### Clone the Repository

```bash
git clone https://github.com/MohamedHamdanA/Virtual-Chatbot-Sona.git
cd "Virtual-Chatbot-Sona/Sona - Backend"
```


## Setup

### Create and Activate a Virtual Environment
Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
#### Windows:
```bash
venv\Scripts\activate
```

#### macOS/Linux:
```bash
source venv/bin/activate
```

### Install Dependencies
Install 'requirements.txt':
```bash
pip install -r requirements.txt
```

For JavaScript dependencies, use yarn:
```bash
yarn
```

Create a `.env` file at the root of the repository to add your **ElevenLabs API Keys**. Refer to `.env.example` for the environment variable names.
And add dotenv if it's not already included:
```bash
yarn add dotenv
```

Download the **RhubarbLibrary** binary for your **OS** [here](https://github.com/DanielSWolf/rhubarb-lip-sync/releases) and put it in your `bin` folder. `rhubarb` executable should be accessible through `bin/rhubarb`.

### Installing Ollama Locally

To install Ollama locally on your machine, follow these steps:

### Prerequisites

- **macOS**: Ensure you have Homebrew installed. If not, you can install it from [brew.sh](https://brew.sh/).
- **Linux**: Ensure you have `curl` and `tar` installed.

### Installation Steps

**Download Ollama**

   Download the latest release of Ollama directly from the [Ollama official website](https://ollama.com/). Choose the appropriate version for your operating system.

### Run the API
Start the FastAPI application with:
```bash
uvicorn main:app --reload
```
You can access the API at http://127.0.0.1:8000.


### Start the development server 
Once the API is running, start the development server with:
```
yarn dev
```

## Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

