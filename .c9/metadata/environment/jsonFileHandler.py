{"filter":false,"title":"jsonFileHandler.py","tooltip":"/jsonFileHandler.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":11},"action":"insert","lines":["import json"],"id":1}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":27},"action":"insert","lines":["def readJsonFile(fileName):"],"id":4}],[{"start":{"row":1,"column":27},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":16},"action":"insert","lines":["data=\"\"     "],"id":6}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":16},"action":"remove","lines":["    "],"id":7},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":2,"column":11},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]},{"start":{"row":3,"column":4},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":9}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["∫"],"id":10}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"remove","lines":["∫"],"id":11}],[{"start":{"row":4,"column":0},"end":{"row":8,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"],"id":13}],[{"start":{"row":8,"column":15},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":15}],[{"start":{"row":0,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["import json","def readJsonFile(fileName):","    data=\"\"","    ","def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data","    ",""],"id":18},{"start":{"row":0,"column":0},"end":{"row":9,"column":15},"action":"insert","lines":["import json","","def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":11},"end":{"row":9,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1726624442291,"hash":"90c7c775e5ad173f1e75e558c64b4e27a488ccc5"}