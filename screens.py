#===============================================================================
import streamlit as st
from functions import *

import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

import numpy as np

from langdetect import detect

#===============================================================================

# Input variables  
models_dict_qg = Config.models_qg
models_dict_qa = Config.models_qa

demo_text_qg = Config.demo_text_qg
demo_text_qa = Config.demo_text_qa["context"]
demo_ques_qa = Config.demo_text_qa["question"]

language_lookup = Config.language_lookup


#===============================================================================

def QG_screen():
    st.title("Question Generation")	
    st.write("Question Generation (QG) aims to generate natural language, "\
            "questions based on given contents where the generated questions "\
            "need to be able to be answered by the contents.")
    #####################################
    st.subheader("Model selection")
    #### Model select and user input ####
    option_qg = st.selectbox("Select model size:",
                        (list(models_dict_qg.keys())))
    st.subheader("Provide context")
    user_input_qg = st.text_area("Please provide context text:", height=200,
                                value=f"{demo_text_qg}", max_chars=500)
    
    ######################################
    # List user context setence by setence
    sentences_qg = sent_tokenize(user_input_qg)
    list_context("Sentences", sentences_qg)

    ######################################
    #### Load the NLP model: ####
    nlp_qg  = modelsConfig_qg(option_qg)
    questions = nlp_qg(user_input_qg)
    
    st.write("**Question Generated:**")
    for i, question in enumerate(questions):
        st.write(f"{i+1}. {question}")


#===============================================================================

def QA_screen():
    st.title("Question Answering")
    st.write("Reading comprehension is the task of answering questions about "\
        "a passage of text to show that the system understands the passage.")
    #####################################
    #### Model select and user input ####
    st.subheader("Model selection")
    option_qa = st.selectbox("Select model:",
        (list(models_dict_qa.keys())))
    


    st.subheader("Provide context:")
    user_context_qa = st.text_area("Please provide text:", height=100,
                                value=f"{demo_text_qa}", max_chars=500)
    
    

    
    #####################################
    #### Context setence by setence ####
    sentences_qa = sent_tokenize(user_context_qa)
    list_context("Sentences", sentences_qa, checkbox=True)
    
    st.subheader("Provide the question(s):")
    user_question_qa = st.text_area("Please provide question text:", height=50,
                                value=f"{demo_ques_qa}", max_chars=200)
    

    questions = sent_tokenize(user_question_qa)


    #####################################
    #### Load the NLP model ####
    nlp_qa = modelsConfig_qa(option_qa)
    
    answers = {}
    for i, question in enumerate(questions):
        st.write(f"{i+1}. **Question**: {question}")
        answer = qa_compute_answer(nlp_qa, questions[i], 
                                    user_context_qa, models_dict_qa[option_qa])
        
        answers[answer] = answer_index(answer, user_context_qa)
        st.write(f"{i+1}. **Answer**: {answer}")


    #####################################
    #### Language detection ####

    if option_qa == "mrm8488/bert-multi-cased-finetuned-xquadv1 [multilingual]": 
        st.sidebar.markdown("**Note - This model is multilingual and support the following languages:**")
        st.sidebar.markdown(list(language_lookup.values()))
        st.sidebar.markdown("")
        
        st.sidebar.markdown("Context:")
        language_detect(user_context_qa,sidebar=True)
        st.sidebar.markdown("Question:")
        language_detect(user_question_qa,sidebar=True)

    #####################################
    #### Highlight answer in context ####
    st.subheader("Answer shown in context")
    num_answer = range(1, len(answers)+1)
    
    if len(num_answer) == 1: 
        index_range = answers[list(answers)[0]]
        write_answer(user_context_qa, index_range)
    
    elif len(num_answer) > 1:
        option_qa = st.selectbox("Select question in context:", list(num_answer))
        index_range = answers[list(answers)[option_qa-1]]
        write_answer(user_context_qa, index_range)


    #####################################


    
    
#===============================================================================

def main_screen():
    st.title("Question Answering & Question Generation")
    #####################################
    st.subheader("About :trophy:")
    st.write("Hello there and welcome!")
    st.write("In this prototype you are able to play around with "\
            "state-of-the-art NLP models in an easy user friendly environment.")
    st.write("There are two main task, namely; Question Answering and Question "\
            "Generation. Use the sidebar to navigate to them respectively.")
    
    #####################################
    st.subheader("Github :zap:")
    st.write("You can find the git repository for the app here:")
    st.write("https://github.com/JKrse/nlp_streamlit_QG_QA")

    #####################################
    st.subheader("COLAB :crocodile:")
    st.write("To play around with all of models can be both demanding in storage"\
            "(~6gb) and can be computationally. To cope with this a COLAB notebook has"\
            "been developed, which enables you to run the streamlit app through COLAB."\
            "Models are now stored and computationen made on using Google service.")
    st.write("https://colab.research.google.com/drive/1zjWn1OEvL_OJxQufjCnrtIIq25qT9DMz?usp=sharing")
    st.write("Note you will need to modify the script a little bit by adding"\
            "your own ngrok to generate the localhost server.")








