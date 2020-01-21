def call():
    from rasa.nlu.training_data import load_data
    from rasa.nlu import config
    from rasa.nlu.components import ComponentBuilder
    from rasa.nlu.model import Trainer

    builder = ComponentBuilder(use_cache=True)

    training_data = load_data('./data/weapon.md')
    trainer = Trainer(config.load("./config.yml"), builder)
    trainer.train(training_data)
    model_directory = trainer.persist('./models', fixed_model_name="model")
    print('done')
    return model_directory


call()


def call_for(message):
    # from datetime import datetime
    # s = datetime.now()
    from rasa.nlu.model import Interpreter
    interpreter = Interpreter.load('models/model')
    # from random import choice
    # from json import loads
    import spacy
    nlp = spacy.load('en')
    parsed_sentence = interpreter.parse(message)
    print(parsed_sentence)
    return parsed_sentence
