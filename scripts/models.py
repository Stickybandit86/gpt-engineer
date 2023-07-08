import os
import openai
import json
openai.api_key = "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"

models = openai.Model.list()

# Convert the models data into a JSON string
models_json = json.dumps(models, indent=4)


# Write the JSON string to a text file
with open('models.txt', 'w') as f:
    f.write(models_json)

print(models)