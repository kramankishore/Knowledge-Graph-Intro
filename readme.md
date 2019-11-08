## Find full article here:

https://medium.com/@k.ramankishore/a-knowledge-graph-implementation-tutorial-for-beginners-3c53e8802377

## Pre-requisites:

Python (https://www.python.org/downloads/)

Neo4j and it's prerequisites like Java (https://neo4j.com/download/)

## Steps:

1. Clone the repo onto your machine.

2. Create and switch to a virual environment:

   ```
   pip install virtualenv (if you already don't have virtualenv)
   virtualenv env
   source env/bin/activate (command may vary depending on the OSs)
   ```

3. Install python packages:

   ```
   pip install -r requirements.txt
   ```

4. Run the code:

   ```
   python main.py
   ```

5. Open Neo4j browser: http://localhost:7474/browser/

6. Enter the below command and execute it to see the Knowledge Graph:

   ```
   Match(n)
   Return(n)
   ```

7. The generated Knowledge Graph should look like:

   ![Knowledge Graph Basic](https://github.com/kramankishore/Knowledge-Graph-Intro/blob/master/result/Knowledge_Graph_Basic.png)

#

Note:

- The text used for demonstration is:

### Startup companies create jobs and innovation. Bill Gates supports entrepreneurship.

- To delete all nodes in your Neo4j (in case you are experimenting), explicitly call the function delete_all_nodes in graphPopulation.py
