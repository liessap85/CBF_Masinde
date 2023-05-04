import re
string=open("preproinsulin-seq.txt").read()
new_str=re.sub("[^a-z]", "", string)
open("preproinsulin-seq-clean.txt", "w").write(new_str)


string2=open("preproinsulin-seq-clean.txt").read()
new_str2=(string2[0:24])
open("lsinsulin-seq-clean.txt", "w").write(new_str2)


new_str3=(string2(25:54])
open("binsulin-seq-clean.txt", "w").write(new_str3)


new_str4=(string2[55:89])
open("cinsulin-seq-clean.txt", "w").write(new_str4)


new_str5=(string2[90:110])
open("ainsulin-seq-clean.txt", "w").write(new_str5)
