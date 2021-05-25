# Concertbot

Example bot that contains only story data.

## What’s inside this example?

This example contains some training data and the main files needed to build an
assistant on your local machine. The `cyencebot` consists of the following files:

- **data/stories.md** contains training stories for the Core model
- **actions/actions.py** contains some custom actions
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant
- **endpoints.yml** contains the webhook configuration for the custom actions

## How to use this example?

Have a python enviornment with rasa installed. Check google.

To train cyence model, run (this would train both model)
```
rasa train
```

To create new training data using interactive learning, execute
```
rasa interactive core -d domain.yml -m models -c config.yml --stories data
```

To visualize your story data, run
```
rasa visualize
```

To chat with your bot on the command line, run
```
rasa run actions&
rasa shell
```

If you wanna run with cyence score specific, have the
connections.py file updated with app40 password and then try in interactive chat with:
```
cyence score of domain guidewire.com
```
This would get the original cyence score.