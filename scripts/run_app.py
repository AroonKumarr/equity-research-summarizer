from langchain_community.document_loaders import TextLoader


loader = TextLoader("data/nvda_news_1.txt")  # ✅ This works

data = loader.load()
#print(data)

#print(f"\n from here your will something elsee {data[0]}")

from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path="data/movies.csv")

data = loader.load()
print(len(data))
print(data[0])
print(data[0].page_content)
print(data[0].metadata)

loader = CSVLoader("data/movies.csv", source_column = "title")
data2 = loader.load()
print(data2[0])

from langchain_community.document_loaders import UnstructuredURLLoader

loader2 =  UnstructuredURLLoader(urls = [
    "https://www.moneycontrol.com/news/business/banks/hdfc-bank-re-appoints-sashidhar-jagdishan-as-md-ceo-for-3-years-11060371.html",
    "https://www.moneycontrol.com/news/business/markets/market-corner-what-changed-for-d-street-while-you-were-sleeping-11059861.html"
])

data3 = loader2.load()
print(len(data3))


from langchain.text_splitter import CharacterTextSplitter

# Taking some random text from wikipedia
text = """Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan.
It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Matt Damon, and Michael Caine.
Set in a dystopian future where humanity is embroiled in a catastrophic blight and famine, the film follows a group of astronauts...

Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007 and with
Kip Thorne, a Caltech theoretical physicist and 2017 Nobel laureate in Physics,[4] was an executive producer, acted as a scientific...
Cinematographer Hoyte van Hoytema shot it on 35 mm movie film in the Panavision anamorphic format and IMAX 70 mm. Principal phot...
Interstellar uses extensive practical and miniature effects, and the company Double Negative created additional digital effects.

Interstellar premiered in Los Angeles on October 26, 2014. In the United States, it was first releas...
It has been praised by astronomers for its scientific accuracy and portrayal of theoretical astroph...
"""

# Example: print first 200 characters
text[:200]



splitter = CharacterTextSplitter(
    separator = '\n',
    chunk_size = 200,
    chunk_overlap = 0
    
)
chunks = splitter.split_text(text)
print(len(text))

print(chunks)


for chunk in chunks:
    print(len(chunk))
    
    
    
from langchain.text_splitter import RecursiveCharacterTextSplitter

r_splitter = RecursiveCharacterTextSplitter(
    separators = ["\n\n","\n"," "],
    chunk_size = 200,
    chunk_overlap = 0
    
)
chunks2 = r_splitter.split_text(text)
print(len(chunks2))

chunks3 = text.split("\n\n")
for chunk4 in chunks3:
    print(len(chunk4))
    

first_split = chunks3[0]
print(first_split)

second_split = first_split.split("\n")

for chunk5 in second_split:
    print(len(chunk5))
    