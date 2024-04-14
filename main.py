from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import canada_engine, root_engine


load_dotenv() # Loading OpenAI API key (environment variables) from .env file 

population_path = os.path.join("data", "population.csv") # Constructing the path to the population.csv file.
population_df = pd.read_csv(population_path) # Reading population data into a pandas DataFrame.

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
) # Creating a PandasQueryEngine for querying population data.
population_query_engine.update_prompts({"pandas_prompt": new_prompt}) # Updating prompts for the PandasQueryEngine.

# Creating a list of tools including note saving, querying population data, and querying PDF data.
tools = [
    note_engine, # Tool for querying population data.
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ), # Tool for querying Canada PDF data.
    QueryEngineTool(
        query_engine=canada_engine,
        metadata=ToolMetadata(
            name="canada_data",
            description="this gives detailed information about canada the country",
        ),
    ), # Tool for querying root_rules PDF data.
    QueryEngineTool(
        query_engine=root_engine,
        metadata=ToolMetadata(
            name="root_data",
            description="this gives detailed information about the board game root",
        ),
    ),
    QueryEngineTool(
        query_engine=HP_engine,
        metadata=ToolMetadata(
            name="HarryPotter6",
            description="this gives detailed information about the sixth harry potter book",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613") # Creating an instance of OpenAI with a specified model.
# Creating a ReActAgent with the defined tools, OpenAI instance, and a verbose setting.
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt) # Querying the agent with the user's input prompt.
    print(result) # Printing the result of the agent's query.
