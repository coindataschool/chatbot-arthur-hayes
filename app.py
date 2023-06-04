import streamlit as st
from llama_index import StorageContext, load_index_from_storage

# --- App Layout --- #

st.set_page_config(page_title='Arthur Hayes AI 🧠', layout='wide', page_icon = '🤖')

with st.sidebar:
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
       "This chatbot is powered by GPT-3.5-turbo and trained on the following essays by Arthur Hayes:"
    )
    st.markdown(
        "- [Patience is beautiful](https://cryptohayes.substack.com/p/patience-is-beautiful)"
    )
    st.markdown("Sample Questions to Ask:")
    st.markdown("1. Do you like coffee?")
    st.markdown("2. When will the market go up?")
    st.markdown("3. Will Bitcoin retest $20,000?")
    st.markdown("4. Will Fed's 2% core inflation target happen in 2023? Do NOT give any reasons.")
    st.markdown("5. What's your prediction of inflation?")
    st.markdown("6. Do you think raising interest rates will cause inflation to fall?")    
    st.markdown("7. How much deficits per year will become the norm for the US Federal Government in the next decade?")
    st.markdown("8. What will happen if the Fed cuts rates?")
    st.markdown("9. How will the fiat liquidity situation evolve in the coming months?")
    st.markdown("10. How does the Fed exert influence?")
    st.markdown("11. How does the US Treasury exert influence?")
    st.markdown("12. How does the US Banking System exert influence?")
    st.markdown("13. What is the most crucial function of the banking system?")
    st.markdown("14. How does the US Federal Government exert influence?")
    st.markdown("15. How do private businesses and individuals exert influence?")
    st.markdown("16. How do foreigners exert influence?")
    st.markdown("17. Why have foreigners been net-selling US Treasury debt?")
    st.markdown("18. Quantity of money vs price of money, which is more important in your opinion? Do NOT explain yourself.")
    st.markdown("19. What is an inverted yield curve?")
    st.markdown("20. Has the US Treasury been issuing the lion's share of debt at the long-end or short-end?")
    st.markdown("21. Since 2002, on a total return basis, has gold outperformed the price of oil? What about Long-term US Treasuries?")
    st.markdown("22. Why hasn't Yield curve control started in America? Give 3 reasons.")
    

st.title("🤖 Arthur Hayes AI 🧠")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# --- App Engine --- #

# initialize session states
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []
if "just_sent" not in st.session_state:
    st.session_state["just_sent"] = False
if "temp" not in st.session_state:
    st.session_state["temp"] = ""
    
# define helpers
def clear_text():
    st.session_state["temp"] = st.session_state["input"]
    st.session_state["input"] = ""
    
def get_text():
    """
    Get the user input text.

    Returns:
        (str): The text entered by the user
    """
    input_text = st.text_input(
        "You: ", st.session_state["input"], key="input", 
        placeholder="What do you want to ask King Arthur?", 
        on_change=clear_text, label_visibility='hidden')    
    input_text = st.session_state["temp"]
    return input_text

# get user input
user_input = get_text()

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="index")

# load index
index = load_index_from_storage(storage_context).as_query_engine()

# generate output, add the input/output to the session
if user_input:
    response = index.query(user_input)
    output = response.response
    st.info(user_input,icon="🧐")
    st.success(output, icon="🤖")
    
# display conversation history
with st.expander("Conversation", expanded=True):
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        st.info(st.session_state["past"][i],icon="🧐")
        st.success(st.session_state["generated"][i], icon="🤖")