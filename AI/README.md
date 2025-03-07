# How to AI

1. start the environment in the project directory

```bash
source env/bin/activate
```

2. move to the "AI_Bilderkennung" folder

```bash
cd AI/AI_Bilderkennung/
```

3. install all the requirements

```python
pip install -r requirements.txt
```

4. start the application

```python
python api_connector.py
```

## possible errors:

- Forbidden -> you are most likely missing an API token, make sure that you have one, default is an api_key.txt file (AI/AI_Bilderkennung/api_key.txt)
