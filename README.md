# Streamlit GPT

## Initialize project
```
poetry install
```

## To execute GPT (Streamlit)
```
poetry run gpt
```

## To execute core engine and execute prompt from cli
```
poetry run chat
```

## To ingest new data
### Download the html content in 'langchain-docs'
```
wget -r -A.html -p langchain-docs <URL>
```
### Execute ingestion engine to read data from 'langchain-docs' path and push it into vector DB
```
poetry run ai
```