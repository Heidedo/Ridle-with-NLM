# Using Natural Language Model to improve Classification task.
This repository has the code and results from my experiments with Ridle in combination with Natural Language Models.
All the experiments were performed under the supervision of Prof. Dr. Maribel Acosta Deibe

The goal of this project was to see, how a Language Model can enhance the Accuracy of a classification task, called Ridle. By adding information from Wikipedia articles, the program combines representation- and sentence embeddings to make even more accurate predictions. All the tasks were performed on Dbpedia datasets.

# Ridle (Relation - Instance Distribution Learning) 💻
Ridle is a tensorflow-based implementation of a supervised node classificaton model on directed relational graphs. The program learns a representation of an entity by creating embeddings. The main assumption is, that similar entities, that belong to the same class also share the same or similar relations. It learns the distribution of relations, which in turn allows for predicting instance types. It is composed of two components: 
1. A representation model based on instance-relation occurrences 
2. A neural network for predicting instance types based on learned entity representations.
![image](https://user-images.githubusercontent.com/81161341/148765750-7c447177-d4b1-4ce8-bc4e-7a89fa956e50.png)

Ridle achieved very good scores compared to other SOTA models, such as RDF2Vec, SDType, TransE and RESCAL and more. 

# Data preparation 📚
To use and improve the experiments performed on Ridle, we used the same datasets that were provided with Ridle. (see dataset folder) For the extraction of the data, the WikipediaAPI was used, which extracts either the summary, that is the first paragraph on a wikipedia article, or the content of the whole wikipedia page. To further improve the quality of the data, we ran a data cleaning program, which got rid of unnecessary information and text which wasn't written in English. The data was merged into a file with the format (Subject - Summary - Class --> see dataset folder for example).
