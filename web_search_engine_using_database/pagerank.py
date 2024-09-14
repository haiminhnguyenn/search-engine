import sqlite3
import networkx as nx

#Connect to the sQLITE database
conn = sqlite3.connect('crawled_pages.db')
cursor = conn.cursor()

#Retreive the URLs of all the websites from the database
cursor.execute('SELECT url FROM pages')
urls = [ row[0] for row in cursor.fetchall()]

#Create an empty directed graph using networkx
graph = nx.DiGraph()

#Add the nodes to the graph
for url in urls:
    graph.add_node(url)

#Retrieve the outgoing links of each website from the database and add the edges to the graph
for url in urls:
    cursor.execute('SELECT outgoing_links FROM pages WHERE url = ?', (url,))
    outgoing_links = cursor.fetchone()[0].split(',')
    for link in outgoing_links:
        if link.startswith('http'):
            graph.add_edge(url, link)

#Calculate pagerank of the graph
pagerank = nx.pagerank(graph)

#Store the pagerank scores in the database
for url in urls:
    cursor.execute("UPDATE pages SET pagerank = ? WHERE url = ?",
                   (pagerank[url], url))
    
#commit the changes to the database
conn.commit()

#close the database connection
conn.close()