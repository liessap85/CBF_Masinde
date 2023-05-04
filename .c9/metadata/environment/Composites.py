{"filter":false,"title":"Composites.py","tooltip":"/Composites.py","undoManager":{"mark":65,"position":65,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":38},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:"],"id":1}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["C"],"id":2},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["B"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["F"]}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["-"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["M"]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"remove","lines":["M"],"id":4}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":[" "],"id":5},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["M"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["a"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["s"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["i"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["n"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["d"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"remove","lines":[" "],"id":7}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["/"],"id":8}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"remove","lines":[" "],"id":9}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"remove","lines":[" "],"id":10}],[{"start":{"row":0,"column":50},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]},{"start":{"row":1,"column":4},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":4},"end":{"row":3,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":12}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":3,"column":38},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":24},"action":"insert","lines":["myInventoryList = []"],"id":15}],[{"start":{"row":4,"column":24},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":25,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":17}],[{"start":{"row":3,"column":38},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":38},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":22}],[{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":24},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "],"id":25},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":[" "],"id":26}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":27},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":38},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":[" "],"id":28},{"start":{"row":0,"column":50},"end":{"row":1,"column":2},"action":"remove","lines":["","  "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"remove","lines":[" "],"id":29},{"start":{"row":3,"column":20},"end":{"row":4,"column":3},"action":"remove","lines":["","   "]}],[{"start":{"row":0,"column":50},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":38},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":20},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":32}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":33}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":34}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":35}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "],"id":36}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":37}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":38}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"],"id":40},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["u"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":41},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["t"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["h"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["r"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["u"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["g"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["h"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":[" "],"id":42},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["l"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["i"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["s"],"id":43},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["i"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["l"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["m"],"id":44},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["y"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["V"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["e"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["h"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["i"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["c"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["l"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":[" "],"id":45},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["a"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["n"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":[" "],"id":46},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["p"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"remove","lines":["r"],"id":47}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["r"],"id":48},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["i"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["n"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":[" "],"id":49},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"remove","lines":["t"],"id":50}],[{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["i"],"id":51},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["t"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":["r"],"id":52}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["t"],"id":53}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":["t"],"id":54}],[{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["e"],"id":55},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["m"]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":56},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["#"]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["O"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["p"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["e"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":[" "],"id":57},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["c"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["s"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["v"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":[" "],"id":58},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["a"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["c"],"id":60},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["o"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["p"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":[" "],"id":61},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["d"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["t"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["e"],"id":62}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["a"],"id":63}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":[" "],"id":64},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["f"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["o"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":[" "],"id":65},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["e"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["a"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["c"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["h"]}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":[" "],"id":66},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["e"]},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["n"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["t"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["r"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":50},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1678301298914,"hash":"7514079559bbf72f77c955d1f5a1fde9e8290d37"}