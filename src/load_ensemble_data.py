def load_ensemble_data():
    ensemble_data = dict()
    with open("mini_list.tsv","r") as openfile:
        for index,lines in enumerate(openfile):
            if index == 0:
                labels = ["iiii"]+lines.replace("\n","").split("\t")[1:]
            else:
                row = lines.replace("\n","").split("\t")
                uniprot_id = row[1]
                ensemble_data[uniprot_id] = dict()
                for j,label in enumerate(labels):
                    ensemble_data[uniprot_id][label] = row[j]
    return ensemble_data,labels
