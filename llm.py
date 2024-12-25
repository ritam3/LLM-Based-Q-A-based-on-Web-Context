from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

class Model:
    def __init__(self, model_name):
        self.model_name = model_name
        self.llm = OllamaLLM(model=model_name)

class Embed(Model):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.embeddings = (OllamaEmbeddings(model=model_name))

class V_store(Embed):
    def __init__(self, model_name, documents):
        super().__init__(model_name)
        self.vc_store = FAISS.from_documents(documents,self.embeddings)

class OllamaModel(V_store):
    def __init__(self, model_name: str, documents):
        super().__init__(model_name, documents)
        self.prompt2 = ChatPromptTemplate.from_template(
                        """
                        Answer the following question based on the provided context. You can use outside resource but try to answer with respect to the given context. If you use other resource then mention it as well:
                        <context>
                        {context}
                        </context>
                        """
                        )
        self.prompt1=ChatPromptTemplate.from_template(
                        """Question: {question}
                        Answer: Let's think step by step."""
                        )

    def result_context(self,query): 
        chain2 = create_stuff_documents_chain(self.llm,self.prompt2)
        retriever2 = self.vc_store.as_retriever()
        retrieval_chain2 = create_retrieval_chain(retriever2,chain2)
        result = retrieval_chain2.invoke({"input":query})
        return result['answer'], result['context']
    
    def result_without_context(self,query):
        chain = self.prompt1 | self.llm
        result = chain.invoke({"question":query})
        return result