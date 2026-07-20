# file = open("data/college_rules.txt","r")
# text = file.read()
# file.close()
# print(len(text))
# chunks = text.split("\n\n")
# clean_chunks = []

# for chunk in chunks:

#     chunk = chunk.replace("----------------------------------------", "")

#     chunk = chunk.strip()

#     if chunk:

#         clean_chunks.append(chunk)
# for i, chunk in enumerate(chunks):
#     print("=" * 40)
#     print(f"chunks {i+1}")
#     print("=" * 40)
#     print(chunk)
#     print()

with open("data/college_rules.txt","r") as file:
    text = file.read()

print("Document Length: {len(text)} characters")

chunks = text.split("\n\n")

clean_chunks=[]
for chunk in chunks:
    chunk = chunk.replace("----------------------------------------", "")
    chunk = chunk.strip()
    if chunk:
        clean_chunks.append(chunk)
print("\n Total chunks: ", len(clean_chunks))

for i, chunk in enumerate(clean_chunks):
    print(f"Chunk : {i+1}")
    print(chunk)