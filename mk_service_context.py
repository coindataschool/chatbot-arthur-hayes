from llama_index import LLMPredictor, PromptHelper, ServiceContext
from langchain.chat_models import ChatOpenAI

def custom_service_context(
    max_input_size, num_outputs, max_chunk_overlap, 
    chunk_size_limit, model="gpt-3.5-turbo", temperature=0):
    
    # max_input_size: int 
    # num_outputs: int
    # max_chunk_overlap: a ratio between 0 and 1
    # chunk_size_limit: int
    
    # define LLM
    llm_predictor = LLMPredictor(
        llm = ChatOpenAI(temperature=temperature, 
                         model_name=model, 
                         max_tokens=num_outputs)
    )
    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, 
        chunk_size_limit=chunk_size_limit)
    
    # make and return service context
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, 
        prompt_helper=prompt_helper,
        # embed_model=embedding_llm,
    )
    return service_context

