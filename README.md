# parse_GOs
parse_Gene_ontology_annotations_to_csv

The script split_gos.py parse the go.obo file (available at https://geneontology.org/docs/download-ontology/) to generate a csv file with the Gene Ontology (GO) annotations IDs,descriptions, and class (biological process-BP, cellular component-CC, and molecular function-MF), and will also produce separate csv files for each of the GO classes. 

usage: 
python3 split_gos.py go.obo
