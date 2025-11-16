from ner_simple import run_ner

if __name__ == '__main__':
    text = """Barack Obama was born in Hawaii and was the 44th President of the United States."""
    entities = run_ner(text)
    print(entities)