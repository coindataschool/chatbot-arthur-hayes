# chatbot-arthur-hayes

A chatbot powered by GPT and Arthur Hayes' essays.

## How to Run

1. add new articles under `/articles`.
2. generate `/index` via `python construct_index.py`. If needed, first open
   the python script and edit the parameter values of the `custom_service_context()` function.
3. run app via `streamlit run app.py`