import requests
from bs4 import BeautifulSoup
import networkx as nx

urls = [
    "http://127.0.0.1:5000/a",
    "http://127.0.0.1:5000/b",
    "http://127.0.0.1:5000/c",
    "http://127.0.0.1:5000/d",
    "http://127.0.0.1:5000/e"
]

outgoing_links = {}

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [link.get("href") for link in soup.find_all("a") if link.get("href")]
    outgoing_links[url] = links
    
G = nx.DiGraph()

for node, link in outgoing_links.items():
    G.add_node(node)
    
    for link in links:
        G.add_edge(node, link)
        
pagerank = nx.pagerank(G, weight="weight")

ranked_results = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
top_results = ranked_results[:4]
print(top_results)