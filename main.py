# Steps:
# 1. Forming subject - predicate - object triples. Use Dependency Parsing to do this. Try spaCy.
# 2. Optional: Make schema containing list of possible entities and relations
# 3. Entity recognition - Named Entity Recognition (NER) can be used for now.
# 4. Entity resolution: Map detected entities to DBpedia. http://www.gianlucademartini.net/kg/KGs-2-NER.pdf
# 5. Relation recognition
# Use falcon project for entitry and relation linking.
# Detected entities will have multiple mappings with DBpedia. Rank them on the basis of ??


import knowledgeExtraction
import graphPopulation
import entityRecognitionLinking

inputText = u'Startup companies create jobs and innovation. Bill Gates supports entrepreneurship.'
#inputText = nlp(u"My name is Sundar. I am currently doing Master's in Artificial Intelligence at NUS. I love Natural Language Processing.")

# Step 1: Knowledge Extraction. Output: SOP triples
knowledgeExtractionObj = knowledgeExtraction.KnowledgeExtraction()
sop_list = knowledgeExtractionObj.retrieveKnowledge(inputText)
#list_sop = sop_list.as_doc()
sop_list_strings = []
for sop in sop_list:
    temp = []
    temp.append(sop[0].text)
    temp.append(sop[1].text)
    temp.append(sop[2].text)
    sop_list_strings.append(temp)

print(sop_list_strings)

# Step 2: Entity recognition and linking. This step needs to be linked.
entityRecognitionLinkingObj = entityRecognitionLinking.EntityRecognitionLinking()
entityRelJson = entityRecognitionLinkingObj.entityRecogLink(inputText)

entityLinkTriples = []
for sop in sop_list_strings:
    tempTriple = ['', '', '']
    for resource in entityRelJson['Resources']:
        if resource['@surfaceForm'] == sop[0]:
            tempTriple[0] = resource['@URI']
        if resource['@surfaceForm'] == sop[1]:
            tempTriple[1] = resource['@URI']
        if resource['@surfaceForm'] == sop[2]:
            tempTriple[2] = resource['@URI']
    entityLinkTriples.append(tempTriple)
print(entityLinkTriples)

# Step 3: Knowledge Graph creation.
graphPopulationObj = graphPopulation.GraphPopulation()
graphPopulationObj = graphPopulationObj.popGraph(
    sop_list_strings, entityLinkTriples)
# popGraph(sop_list)≠≠
