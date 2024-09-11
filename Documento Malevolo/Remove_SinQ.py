# Script usato per rimuovere garbage dalle stringhe offuscate. 
# Ogni volta che viene incontrato il pattern spazzatura, viene sostituito da una stringa vuota. 
# Lo script è eseguito in loop finquando non viene più individuato il pattern di garbage.

var_string = " *** INSERIRE STRINGA DA DEOFFUSCARE *** "
present = True

while present:
    var_string = str.replace(var_string, "SinQ", "")
    if "SinQ" not in var_string:
        present = False 
        
print(var_string)
