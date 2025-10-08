import os
import pandas as pd
from langchain_core.documents import Document


def dataconveter():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'customer_support_kb.csv')
    
    product_data=pd.read_csv(DATA_PATH)
    
    data=product_data[["title","content"]]

    issue_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {
                'title': row['title'],
                'content': row['content']
            }
        # Append the object to the list
        issue_list.append(obj)

        
            
    docs = []
    for entry in issue_list:
        metadata = {"title": entry['title']}
        doc = Document(page_content=entry['content'], metadata=metadata)
        docs.append(doc)
    return docs
