# What is this?
BART Large MNLI as a JSON web API
- Basically a web wrapper around this: https://huggingface.co/facebook/bart-large-mnli

# Dev Set Up

1. Ensure Python3 is installed

```
which python3
```

2. Pip Install Pytorch
- Find the exact Pytorch installation needed for your environment https://pytorch.org/get-started/locally/
- But for Mac, it's

```
pip3 install torch
```

3. Install transformers

```
pip3 install transformers
```

4. Install flask

```
pip3 install flask
```

5. Run flask

```
cd app
export FLASK_APP=main
export FLASK_ENV=development
flask run
```

6. Test it out

```
curl -X POST http://localhost:5000/transform -d '{"sequence_to_classify": "one day I will see the world", "candidate_labels":["travel","cooking","dancing"]}' -H 'Content-Type: application/json'
```


# Heroku support
- Note the presence of `requirements.txt`, `Procfile`, and `wsgi.py`.  This app can be pushed to Heroku and it would just work.

