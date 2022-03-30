# Using Natural Language Model to improve Classification task on DBpedia datasets.
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
To use and improve the experiments performed on Ridle, we used the same datasets that were provided with Ridle. (see dataset folder) For the extraction of the data, the WikipediaAPI was used, which extracts either the summary, that is the first paragraph on a wikipedia article, or the content of the whole wikipedia page. To further improve the quality of the data, we ran a data cleaning program, which got rid of unnecessary information and text which wasn't written in English. The data was merged into a file with the format (Subject - Summary - Class).
![image](https://user-images.githubusercontent.com/81161341/148771055-83ee2563-e941-49d7-950b-89f838b2f743.png)

# Experiments :wrench:
All the experiments were performed in jupyter notebook, with the same Sequential model, Ridle was using for its classification.
The first experiments were mainly about finding a useful way to combine the information from the representations that Ridle learned, with the information from the entities' wikipedia article. To usefully merge the two, we were thinking about concatenating the representation vector with a vector from a Language Model.

When it comes to Language Models, BERT is the current SOTA in many different tasks, because the Encoder Decoder model has the possibility to learn word representations simultaneously, so it is fast, and the context is better learned, since the model can learn the left to right and right to left context simultaneously 🡪 Deeply Bidirectional.
Another important factor is that you can use already trained models for your tasks, which is very useful if you don't have a good CPU/GPU that can process large amount of data.

For Ridle to work properly, we concatenated the entity representations with, sentence embeddings, created by sentenceBERT and ran the program on the default neural network settings with 1 hiddenlayer and GeLu as the activation function for the hidden layer.

We also experimented with different neural network structures to see, how the model performs with a different activation function such as ReLU or more hidden layers.
Finally the best settings were chosen and added together for a final run to see, if and how a Language Model can enhance a classification task.
# Evaluation :bar_chart:
Our results have shown, that combining linguistic features with an embedding approach can
enhance the performance of entity type prediction on knowledge graphs.

![image](https://user-images.githubusercontent.com/81161341/160786163-3392f6d2-9621-43ac-ade0-de807fdb1ad9.png)


On average, the extension of knowledge graph embeddings with language models has a
positive impact on entity type prediction. Many entities share the same relations, even if they
belong to different classes. Therefore the distinction between entities is more difficult if we
use a statistical approach. By adding semantic information, in the form of abstract summaries
transformed into embeddings, the model can make more accurate predictions on entity types.
Additionally, we tried a second language model to see how the performance changes, using
a sentence encoder with different parameters. Even though the sentence embeddings created
by the new sentence encoder achieved better scores than the SBERT embeddings, the concatenation with representation embeddings led to slightly worse F1-scores among most of the
datasets.

![image](https://user-images.githubusercontent.com/81161341/160786249-ef8e9184-9371-4dd9-a433-1baea07b7001.png)


Finally, we experimented with a different SBERT model. Analyzing the default model
and the enhanced model, the main differences were in the embedding size and the maximum
sequence length processed by the model. We have seen that the second model outperformed
the default model for most knowledge graphs tested. This might be because more significant
embeddings can encapsulate more detailed text representation, making it easier for the model
to predict instance types.

We have seen the difficulties of training and testing a classifier on incomplete knowledge
graphs. On the one hand, training on incomplete or false knowledge graphs also leads to false
classifications. Besides that, actual positively classified entities are marked as misclassified
due to missing information for some entities.
