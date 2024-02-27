# Chat PDF AI

![]()

I developed an application that allows users to upload PDFs and query their content using Langchain and Streamlit. As an example, I used my own master's thesis and asked the bot some questions about the text. This application supports multiple PDF files.

* Streamlit is a Python library that allows you to create interactive web applications for data analysis simply and quickly.

* LangChain is an open-source orchestration framework for developing applications with large language models (LLMs).

The application uses a variety of libraries to extract text from PDFs: it splits the text into chunks, creates a storage vector for the text chunks (embeddings), creates a conversation chain using OpenAI's LLM, and reads with user input. The application also uses a variety of techniques to improve the relevance of the bot's responses, including using a pre-trained language model, an information retrieval system, and learning over time.

The application is able to understand the context of the PDF and generate answers that are relevant to the user's questions. This makes the application more useful and interactive than an application that is not able to understand the context of the PDF.

This aplication version works locally.
