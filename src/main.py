from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader("/Users/saksham/Projects/Langchain-test/data/raw/sample_data/30_pages_struct.pdf")
data = loader.load()
print(data)

load = PyPDFLoader('/Users/saksham/Projects/Langchain-test/data/raw/sample_data/new-solution-to-the-midas-touch-problem-identification-of-visual-commands-via-extraction-of-focal-fixations.pdf')
page = load.load_and_split()

print(page)