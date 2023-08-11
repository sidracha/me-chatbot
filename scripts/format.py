import json

input_files = ["data1", "data2", "data3"]
output_file = "../training_data/training_data.json"


count = 0

out = []

instruction = "Respond to this message sent by a human."

for file in input_files:

    f = open("../training_data/"+file+".txt", "r")
    lines = f.readlines()

    for line in lines:
        sentences = line.split("%%%")
        if len(sentences) < 2:
            continue
        
        obj = {"intruction": instruction, "input": sentences[1].strip(), "output": sentences[0].strip()}
        

        print(sentences[1])
        print(sentences[0])
        print("\n")
        count += 1
        out.append(obj)


print(count)

of = open(output_file, "w")
json_str = json.dumps(out)
of.write(json_str)

