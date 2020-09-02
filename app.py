#===============================================================================
import streamlit as st
from screens import *

import git
import os

if not os.path.exists(f"{os.getcwd()}/question_generation/"):
    git.Git(os.getcwd()).clone("https://github.com/patil-suraj/question_generation.git")

#===============================================================================

PAGE_CONFIG = {"page_title":"QG_QA_demo.io","page_icon":":shark:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)


# App start: 
def main():
    menu = ["Main", "Question Generation", "Question Answering"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    #===========================================================================
    # Main Page: 
    if choice == "Main":
        main_screen()

    #===========================================================================
    # QG Page: 
    if choice == "Question Generation":
        QG_screen()

    #===========================================================================
    # QA Page: 
    if choice == "Question Answering": 
        QA_screen()


if __name__ == '__main__':
    main()