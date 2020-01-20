from frequency_search import closeness_search
data = "In a coherent paragraph, each sentence relates clearly to the topic sentence or controlling idea, but there is more to coherence than this. If a paragraph is coherent, each sentence flows smoothly into the next without obvious shifts or jumps. A coherent paragraph also highlights the ties between old information and new information to make the structure of ideas or arguments clear to the reader. Along with the smooth flow of sentences, a paragraph’s coherence may also be related to its length. If you have written a very long paragraph, one that fills a double-spaced typed page, for example, you should check it carefully to see if it should start a new paragraph where the original paragraph wanders from its controlling idea. On the other hand, if a paragraph is very short (only one or two sentences, perhaps), you may need to develop its controlling idea more thoroughly, or combine it with another paragraph."

df = closeness_search(data, preprocess_type='lem', thld=[0.1,0.9])

print(df.head())
