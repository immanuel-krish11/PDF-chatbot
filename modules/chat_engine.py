"""
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain

from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


load_dotenv() 

# create a function which combines llm and memory
def create_qa_chain(vector_store):
    llm = ChatOpenAI(model="gpt-4o-mini")
    retriever = vector_store.as_retriever(search_kwargs = {"k" : 3})

    prompt = PromptTemplate( 
        template= " You are a helpful assistant.
    Answer only from the provided transcript context.
    If the context is insufficient, just say you don't know.

    {context}
    Question: {question} ",
    input_variables=['context', 'question']
    )


    # creating chain to combine documents
    document_chain = create_stuff_documents_chain(llm, prompt)

    # creating the final retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    qa_chain = retrieval_chain
    # qa_chain = retrieval_qa.from_chain_type(
    #     llm = llm,
    #     retriever = retriever,
    #     return_source_document = True
    # )
    return qa_chain
    # return retrieval_chain


"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_classic.schema import Document

def create_qa_chain(vector_store):
    """
    Manually builds a retrieval + LLM QA pipeline without using create_retrieval_chain.
    """
    llm = ChatOpenAI(model="gpt-4o-mini")
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Define the prompt template
    prompt = PromptTemplate(
        template=(
            "You are a helpful assistant. "
            "Answer only using the provided transcript context. "
            "If the context is insufficient, say you don't know.\n\n"
            "Context:\n{context}\n\n"
            "Question: {question}"
        ),
        input_variables=["context", "question"]
    )

    # Define a function that will handle retrieval and answering
    def qa_chain(question: str):
        # Step 1: Retrieve relevant chunks
        # docs = retriever._get_relevant_documents(question)
        docs = retriever.invoke(question)


        # Step 2: Combine text from documents into one context string
        context = "\n\n".join([doc.page_content for doc in docs])

        # Step 3: Format the prompt
        formatted_prompt = prompt.format(context=context, question=question)

        # Step 4: Run the LLM
        llm_response = llm.invoke(formatted_prompt)

        # Step 5: Return both the answer and the source documents
        return {
            "answer": llm_response.content,
            "sources": docs
        }

    # Return the qa_chain function so it can be used directly
    return qa_chain

