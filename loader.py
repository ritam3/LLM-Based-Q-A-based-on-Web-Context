from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from urllib.request import urlopen
from urllib.error import *

class Doc_loader:
    def __init__(self,url:str):
        self.url = url
        self.res = ""
        self.documents = None

    def verify(self):
        print(self.url)
        try:
            html = urlopen(self.url)
            return "Url is Valid"
            
        except HTTPError as e:
            return "HTTP error "+str(e)
            
        except URLError as e:
            return "Opps ! Page not found! "+str(e)
        
        
    
    def load(self):
        loader = WebBaseLoader(self.url)
        docs = loader.load()
        return docs

    def split(self):
        docs = self.load()
        if docs is not None:
            split = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
            self.documents = split.split_documents(docs)
    
