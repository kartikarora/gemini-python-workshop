A simple Gemini SDK on python workshop repo. This is the starting point for the workshop. Please fork this repository if you are a participant in the workshop.

The workshop covers the following features of Gemini SDK
- Basic prompting (generate & chat)
- Code generation (unit tests)
- Search, Information Synthesis & Retrival, using mocked documents
- Function calling, using a fictional business logic
- Tuning, using fake company FAQ data

`API_KEY` will be needed from [Google AI Studio](https://aistudio.google.com/). This is stored in [`utils/utils.py`](utils/utils.py).

For Tuning a model, a Google Cloud Project and OAuth setup is needed. This is documented [here](https://ai.google.dev/palm_docs/oauth_quickstart). It is expected that participant would have completed this setup before the workshop.