{"filter":false,"title":"debug.py","tooltip":"/debug.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["def install_or_remove_packages(): ","    iOrR = “” ","    while iOrR != “I” and iOrR != “R”: ","        print(\"Would you like to install or remove packages? (I/R)\") ","        iOrR = input().upper()","    if iOrR == \"I\": ","        iOrR = \"install\"","    elif iOrR == \"R\": ","        iOrR = \"remove\"","    print(\"Enter a list of packages to install\") ","    print(\"The list should be separated by spaces, for example:\") ","    print(\" package1 package2 package3\") ","    print(\"Otherwise, input 'default' to \" + iOrR + \" the default packages listed in this program\") ","    packages = input().lower() ","    if packages == \"default\": ","        packages = defaultPackages","    if iOrR == \"install\": ","        os.system(\"sudo yum install \" + packages)","    elif iOrR == \"remove\": ","        while True: ","            print(\"Purge files after removing? (Y/N)\") ","            choice = input().upper() ","            if choice == \"Y\": ","                os.system(\"sudo apt-get --purge \" + iOrR + \" \" + packages) ","                break","            elif choice == \"N\": ","                os.system(\"sudo apt-get \" + iOrR + \" \" + packages) ","                break","        os.system(\"sudo apt autoremove\") ",""],"id":1}],[{"start":{"row":2,"column":39},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":3,"column":0},"end":{"row":3,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":8},"action":"remove","lines":["    "],"id":3},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "]},{"start":{"row":2,"column":39},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":11},"end":{"row":15,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1677332249862,"hash":"04877d4bd29609b2718f8539e7b0f22a8de118f1"}