from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from llama_index.node_parser import SimpleNodeParser
from mk_service_context import custom_service_context

# user input, change the parameter values to customize your service context
my_service_context = custom_service_context(
    max_input_size=4096, num_outputs=512, max_chunk_overlap=0.2, 
    chunk_size_limit=600, model="gpt-3.5-turbo", temperature=0)

# helper
def construct_index(directory_path):
    # load in docs
    documents = SimpleDirectoryReader(directory_path).load_data()
    # parse the docs into nodes
    parser = SimpleNodeParser()
    nodes = parser.get_nodes_from_documents(documents)
    # construct index
    index = GPTVectorStoreIndex(nodes, service_context=my_service_context)
    # save
    index.storage_context.persist(persist_dir='index')

# main
input_dir = 'articles'
construct_index(input_dir)
