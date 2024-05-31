from openai import OpenAI
import yaml

class YamlConverter():
    def __init__(self) -> None:
        OPENAI_API_KEY = 'some-api-key'
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=OPENAI_API_KEY,
        )
        self.messages = [{'role':'system', 'content': 'You are a kind helpful assistant'}]

    def yaml_to_human_readable_text(self) -> str:
        # Load YAML data
        with open('./files/person.yaml', 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Convert YAML data to string for the prompt
        yaml_string = yaml.dump(yaml_data, default_flow_style=False)
        # Prepare the prompt

        prompt = f'Convert the following YAML data to a human-readable description in the format: "I am [name]. I am [age] years old, I live in [street], [city], [state], and I enjoy [hobbies]."YAML data:{yaml_string}'

        message = {"role": "user", "content": prompt}
        self.messages.append(message)

        response = self.client.chat.completions.create(model='gpt-3.5-turbo', messages=self.messages)
        human_readable_text  = response.choices[0].message.content

     
        # Print the result
        print(human_readable_text)
        return human_readable_text
