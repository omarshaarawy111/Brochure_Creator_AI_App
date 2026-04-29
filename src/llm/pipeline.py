from src.llm.processor import *
import streamlit as st

# Last output next input
def brochure_pipeline(prompt):
    with st.status("Analyzing website...", expanded=True) as status:
        st.write("Step 1: Finding relevant links on the website...")
        # Step 1: Select relevant links
        relevant_links = select_relevant_links(prompt)
        
        st.write("Step 2: Fetching content from the main page and relevant links...")
        # Step 2: Fetch content from the main page and relevant links
        brochure_prompt = fetch_page_and_all_relevant_links(prompt, relevant_links)
        
        status.update(label="Website analyzed! Generating brochure...", state="complete", expanded=False)

    # Step 3: Create brochure content using model 2
    brochure_content = create_brochure(company_name=prompt, brochure_prompt=brochure_prompt)
    
    return brochure_content

def out_of_scope_response(prompt):
    out_of_contex = custom_response(prompt)
    return out_of_contex