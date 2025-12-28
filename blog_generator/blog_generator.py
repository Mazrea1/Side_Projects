import blog_key
import openai
key = blog_key.key
openai.api_key = key

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3,
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog

print(generate_blog('Are AI companions healthy?'))


