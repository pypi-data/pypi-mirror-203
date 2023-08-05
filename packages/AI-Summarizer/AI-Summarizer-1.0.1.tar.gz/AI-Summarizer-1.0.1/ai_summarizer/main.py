import html2text
import os
import openai
import tiktoken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_number_of_tokens(text,model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def split_text_logically(A: str):
    """Split the text logically by sections, not by characters. If there is only one section uses subsections and so on.
    It works on markdown text. and it can be used progressively to split the text in smaller and smaller pieces as needed."""
    half_len = len(A) // 2
    for char in ['\n# ','\n## ','\n### ','\n#### ','\n##### ','\n###### ', '.\n', '\n', '.', ', ', ' ']:
        index_left = A.rfind(char, 10, half_len+10)
        index_right = A.find(char, half_len-10, len(A)-10)
        if index_left == -1:
            if index_right == -1:
                continue
            else:
                split_indices=index_right
                break
        else:
            if index_right == -1:
                split_indices=index_left
                break
            else:
                distance_left=half_len-index_left
                distance_right=index_right-half_len
                if distance_left<distance_right:
                    split_indices=index_left
                    break
                else:
                    split_indices=index_right
                    break 
    part_a=A[:split_indices]
    part_b=A[split_indices:]
    return part_a, part_b

def _recursive_merge_summarises_new(summary_1: str, summary_2: str):
    result="\n# \n"+summary_1+"\n# \n"+summary_2
    return result

def _recursive_summarize_text(text: str, filter: str = None, summary_length: int = 500,model="gpt-3.5-turbo"):
    if filter:
        prompt_content = f"""I need you to summarise some text which is part of a bigger document. 
            You should summarise the text by filtering out what does not follows this guidelines: 
            {filter}.
            
            The content is here:
            {text}
            
            Now create a summary. The result should not be longer than {summary_length} words. 
            Don't speak about the text, say directly what the text says.
            Also do not add conclusions or morals to the summary. Stick to the facts.
            Don't repeat yourself"""
    else:
        prompt_content = f"""I need you to summarise some text which is part of a bigger document. 
            
            The content is here:
            {text}
            
            Now create a summary. The result should not be longer than {summary_length} words. 
            Don't speak about the text, say directly what the text says.
            Also do not add conclusions or morals to the summary. Stick to the facts.
            Don't repeat yourself"""
        
    n_tokens=get_number_of_tokens(prompt_content,model=model)
    if n_tokens>4096:
        text_1,text_2=split_text_logically(text)
        summary_1=_recursive_summarize_text(text_1, filter, summary_length=summary_length,model=model)
        summary_2=_recursive_summarize_text(text_2, filter, summary_length=summary_length,model=model)
        summary=_recursive_merge_summarises_new(summary_1, summary_2)
        return summary
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[ {   "role": "user", "content": prompt_content}]
            )
    except Exception as e:
        print (e)
        input("Press any key to continue")
        return _recursive_summarize_text(text, filter, summary_length,model=model)
    
    finish_reason=response.choices[0].finish_reason
    if finish_reason == "length":
        text_1,text_2=split_text_logically(text)
        summary_1=_recursive_summarize_text(text_1, filter, summary_length=summary_length,model=model)
        summary_2=_recursive_summarize_text(text_2, filter, summary_length=summary_length,model=model)
        summary=_recursive_merge_summarises_new(summary_1, summary_2)
        return summary
    summary = response.choices[0].message.content
    return summary

def html_to_markdown(html_content,ignore_links=True):
    html_converter = html2text.HTML2Text()
    html_converter.ignore_links = ignore_links
    html_converter.ignore_images = True
    markdown_text = html_converter.handle(html_content)
    return markdown_text

def summarize_text(text:str, filter:str=None, summary_length:int=500,model="gpt-3.5-turbo"):
    markdown_content = html_to_markdown(text)
    summary=_recursive_summarize_text(markdown_content, filter, summary_length,model=model)
    while (len(summary.split())>summary_length*1.5):
        summary=_recursive_summarize_text(summary, filter,summary_length,model=model)
    return summary



