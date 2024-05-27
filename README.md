# Intelligent Assistant for Data Analysis and Information Retrieval

## Overview
This project implements an intelligent assistant that aids in data analysis and information retrieval tasks. It leverages various tools and libraries for processing data, querying information, and interacting with users.

## Features
- Note Taking: Users can save notes using the provided note_engine.
- Population Data Analysis: Analyze world population and demographics using the population_data tool.
- Canada Information: Retrieve detailed information about Canada using the canada_data tool.
- Board Game Details: Get detailed information about the board game "Root" using the root_data tool.
- Natural Language Processing: The assistant utilizes OpenAI's GPT-3.5 model for natural language understanding and generation.

## Dependencies
- Python 3.x
- llama_index: A package for managing document indexes and query engines.
- pandas: Library for data manipulation and analysis.
- dotenv: Library for loading environment variables from a .env file.
- prompts: Module for providing prompts and instructions to the assistant.
- note_engine: Module for saving notes.
- pdf: Module providing query engines for PDF documents.
- llm: OpenAI library for language model interactions.

## Usage
1. Upon running "main.py", the assistant will prompt you to enter your query or command.
2. Enter your query or command and press Enter.
3. The assistant will process your input, perform the requested action, and provide the result.
4. Repeat steps 1-3 for further interaction.
