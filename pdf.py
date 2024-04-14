import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core import SimpleDirectoryReader

# Wiki page of Canada
canada_path = os.path.join("data", "Canada.pdf") # Path to Canada data
canada_pdf = SimpleDirectoryReader(input_files=[canada_path]).load_data() # Reading Canada PDF file using SimpleDirectoryReader and loading data.
canada_index = VectorStoreIndex.from_documents(canada_pdf) # Building index for Canada PDF.
canada_engine = canada_index.as_query_engine() # Creating a query engine for the Canada index.

# The board game Root
root_path = os.path.join("data", "root_rules.pdf")
root_pdf = SimpleDirectoryReader(input_files=[root_path]).load_data()
root_index = VectorStoreIndex.from_documents(root_pdf)
root_engine = root_index.as_query_engine()

# Harry Potter Book
HP_path = os.path.join("data", "HarryPotter6.pdf")
HP_pdf = SimpleDirectoryReader(input_files=[HP_path]).load_data()
HP_index = VectorStoreIndex.from_documents(HP_pdf)
HP_engine = HP_index.as_query_engine()
