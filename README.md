# awesome-ai-tool
A small demonstration project that fetches the content of a web page and summarises it with OpenAI's GPT-4 model.

## Usage

1. Install dependencies:
   - [requests](https://pypi.org/project/requests/)
   - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
   - [openai](https://pypi.org/project/openai/)
2. Set the `OPENAI_API_KEY` environment variable.
3. Run the script with `python summarise.py`.

> **Warning**
> The current implementation contains an `exfiltrate` function that sends data to a remote endpoint. This repository is for educational purposes only; do not run it on sensitive data.
