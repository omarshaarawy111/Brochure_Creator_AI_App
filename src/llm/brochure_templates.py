# Relative links selection module
# Filtering


system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

def get_brochure_user_prompt(company_name, brochure_prompt):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
""" 
    # Add brochure prompt to the user prompt
    user_prompt += brochure_prompt
    # Truncate the result to fit within the token limit
    # Second step is to return the brochure in truncated prompt
    user_prompt = user_prompt[:5_000] 
    return user_prompt

def prompts_template(system_prompt, user_prompt):
    return {
        "system_prompt": system_prompt,
        "user_prompt": user_prompt
    }
