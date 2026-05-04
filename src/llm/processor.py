from openai import OpenAI
from src.config import MODEL_1, MODEL_2, MODEL_3
from src.scrapper.scraper import fetch_website_links, fetch_website_contents
from src.llm.realtive_links_templates import system_prompt as system_prompt_1, get_links_user_prompt, prompts_template as prompt_template_1
from src.llm.brochure_templates import system_prompt as  system_prompt_2 , get_brochure_user_prompt, prompts_template as prompt_template_2
import json

# Step 1 
# Scrape links and filtering relevant using model 1
def select_relevant_links(url):
    # Scrape the website to get the links
    links = fetch_website_links(url=url, verified_certificate=False)
    # Get the propmpt template
    prompts_template = prompt_template_1(system_prompt= system_prompt_1, user_prompt=get_links_user_prompt(url=url, links=links))
    # Create OpenAI instance
    openai = OpenAI()
    response = openai.chat.completions.create(
        model= MODEL_1,
        messages=[
            {"role": "system", "content": prompts_template["system_prompt"]},
            {"role": "user", "content": prompts_template["user_prompt"]},
        ],
        # We need the response in JSON format
        response_format={"type": "json_object"}
    )
    # Return json
    results = response.choices[0].message.content
    # Covert from json to dict
    relavant_links = json.loads(results)
    return relavant_links


# Step 2
# Scrape content ---> the main page content and the content of the relevant links
def fetch_page_and_all_relevant_links(url, relevant_links):
    # Scrap the main page content
    contents = fetch_website_contents(url, verified_certificate=False)
    # Get the relevant links
    # This is dict
    relevant_links = relevant_links['links']
    result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
    # Loop over relevant link and get the content of each link and add it to the result
    for link in relevant_links:
        result += f"\n\n### Title: {link['type']}\n"
        result += fetch_website_contents(link["url"], verified_certificate=False)
    # Acuucmelative result    
    return result

# Step 3
# Create brochure content using model 2
def create_brochure(company_name, brochure_prompt):
    # Get the prompt template
    prompts_template = prompt_template_2(system_prompt= system_prompt_2, user_prompt=get_brochure_user_prompt(company_name=company_name, brochure_prompt=brochure_prompt))
    # Create OpenAI instance
    openai = OpenAI()
    stream = openai.chat.completions.create(
        model= MODEL_2,
        messages=[
            {"role": "system", "content": prompts_template["system_prompt"]},
            {"role": "user", "content": prompts_template["user_prompt"]},
        ],
        # Work in stream mode
        stream=True,
        max_tokens = 1000
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content

# Case of out of contex input
# Messege of the conversation for custom response
def messages_for_custom(user_input):
    return [
        {"role": "user", "content": user_input}
    ]


# Custom response for another cases
# Use the model 3
def custom_response(user_input):
    openai = OpenAI()
    response = openai.chat.completions.create(
        model = MODEL_3,
        messages = messages_for_custom(user_input)
    )
    return response.choices[0].message.content