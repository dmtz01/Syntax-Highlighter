#Syntax Highlighter
#H. Daniel Martinez Rodriguez

import sys

def write(palabra, color, fileW):
    fileW.write("<span style=\"color: " + color + ";\">" + palabra + "</span>")

#documento1 -> input file, documento2 -> output file
documento1 = sys.argv[1]
documento2 = sys.argv[2]

fileR = open(documento1, 'r')
fileW = open(documento2, 'w')

#Se inicializa el elemento pre que comienza el archivo html
fileW.write("<pre class=\"python\" style=\"font-family:monospace;\">")

#Comienza a leer el archivo linea por linea
for line in fileR:
    
    #Iterador para los indices del string obtenido del archivo
    i = 0
    
    #Analiza cada caracter dentro del string i
    while i <= (len(line) - 1):

        #Variable para almacenar strings largos
        lex = ""

        #Se inserta tab
        if line[i] == "\t":
            fileW.write("\t")
            i += 1

        #Se inserta espacio
        elif line[i] == " ":
            fileW.write(" ")
            i += 1

        #Se inserta nueva linea
        elif line[i] == "\n":
            fileW.write("\n")
            i += 1
        
        #Se insertan dos puntos
        elif line[i] == ":":
            write(line[i], "black", fileW)
            i += 1

        #Se inserta un delimitador
        elif line[i] == '(' or line[i] == ')' or line[i] == '[' or line[i] == ']' or line[i] == '{' or line[i] == '}':
            write(line[i], "goldenrod", fileW)
            i += 1
        
        #Se inserta una variable
        elif line[i] == 'a' or line[i] == 'b' or line[i] == 'c' or line[i] == 'd' or line[i] == 'e' or line[i] == 'f' or line[i] == 'g' or line[i] == 'h' or line[i] == 'i' or line[i] == 'j' or line[i] == 'k' or line[i] == 'l' or line[i] == 'm' or line[i] == 'n' or line[i] == 'o' or line[i] == 'p' or line[i] == 'q' or line[i] == 'r' or line[i] == 's' or line[i] == 't' or line[i] == 'u' or line[i] == 'v' or line[i] == 'w' or line[i] == 'x' or line[i] == 'y' or line[i] == 'z' or line[i] == 'A' or line[i] == 'B' or line[i] == 'C' or line[i] == 'D' or line[i] == 'E' or line[i] == 'F' or line[i] == 'G' or line[i] == 'H' or line[i] == 'I' or line[i] == 'J' or line[i] == 'K' or line[i] == 'L' or line[i] == 'M' or line[i] == 'N' or line[i] == 'O' or line[i] == 'P' or line[i] == 'Q' or line[i] == 'R' or line[i] == 'S' or line[i] == 'T' or line[i] == 'U' or line[i] == 'V' or line[i] == 'W' or line[i] == 'X' or line[i] == 'Y' or line[i] == 'Z':
            lex += line[i]
            i += 1
            
            while True:

                if line[i] == '_' or line[i] == 'a' or line[i] == 'b' or line[i] == 'c' or line[i] == 'd' or line[i] == 'e' or line[i] == 'f' or line[i] == 'g' or line[i] == 'h' or line[i] == 'i' or line[i] == 'j' or line[i] == 'k' or line[i] == 'l' or line[i] == 'm' or line[i] == 'n' or line[i] == 'o' or line[i] == 'p' or line[i] == 'q' or line[i] == 'r' or line[i] == 's' or line[i] == 't' or line[i] == 'u' or line[i] == 'v' or line[i] == 'w' or line[i] == 'x' or line[i] == 'y' or line[i] == 'z' or line[i] == 'A' or line[i] == 'B' or line[i] == 'C' or line[i] == 'D' or line[i] == 'E' or line[i] == 'F' or line[i] == 'G' or line[i] == 'H' or line[i] == 'I' or line[i] == 'J' or line[i] == 'K' or line[i] == 'L' or line[i] == 'M' or line[i] == 'N' or line[i] == 'O' or line[i] == 'P' or line[i] == 'Q' or line[i] == 'R' or line[i] == 'S' or line[i] == 'T' or line[i] == 'U' or line[i] == 'V' or line[i] == 'W' or line[i] == 'X' or line[i] == 'Y' or line[i] == 'Z' or line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                    lex += line[i]
                    i += 1

                    if i > (len(line)-1):
                        write(lex, "black", fileW)
                        break
                    
                    #Se inserta la expresion completa
                    elif line[i] == " ":
                        if lex == 'import' or lex == 'True' or lex == 'False' or lex == 'None' or lex == 'and' or lex == 'or' or lex == 'not' or lex == 'in' or lex == 'is' or lex == 'if' or lex == 'elif' or lex == 'else' or lex == 'for' or lex == 'while' or lex == 'break' or lex == 'def' or lex == 'class' or lex == 'with' or lex == 'as' or lex == 'pass' or lex == 'lambda' or lex == 'return' or lex == 'yield' or lex == 'import' or lex == 'from' or lex == 'as' or lex == 'try' or lex == 'except' or lex == 'raise' or lex == 'finally' or lex == 'assert' or lex == 'async' or lex == 'await' or lex == 'del' or lex == 'global' or lex == 'nonlocal':
                            write(lex, "darkblue", fileW)
                            lex = ''
                        else:
                            write(lex, "skyblue", fileW)
                            lex = ''
                            break
                
                #Se inserta una funcion
                elif line[i] == '(':
                    write(lex, "gold", fileW)
                    
                    write(line[i], "goldenrod", fileW)
                    
                    lex = ''
                    i += 1

                else:
                    #Se inserta la expresion completa
                    if line[i] == " " or line[i] == "\n" or line[i] == ":":
                        if lex == 'import' or lex == 'True' or lex == 'False' or lex == 'None' or lex == 'and' or lex == 'or' or lex == 'not' or lex == 'in' or lex == 'is' or lex == 'if' or lex == 'elif' or lex == 'else' or lex == 'for' or lex == 'while' or lex == 'break' or lex == 'def' or lex == 'class' or lex == 'with' or lex == 'as' or lex == 'pass' or lex == 'lambda' or lex == 'return' or lex == 'yield' or lex == 'import' or lex == 'from' or lex == 'as' or lex == 'try' or lex == 'except' or lex == 'raise' or lex == 'finally' or lex == 'assert' or lex == 'async' or lex == 'await' or lex == 'del' or lex == 'global' or lex == 'nonlocal':
                            write(lex, "darkblue", fileW)
                            lex = ''
                            break

                        else:
                            write(lex, "skyblue", fileW)
                            lex = ''
                            break
                    
                    else:
                        write(lex, "skyblue", fileW)
                        lex = ''
                        break
        
        #Se inserta un string
        elif line[i] == '\"' or line[i] == '\'':
            lex += line[i]
            i += 1

            while True:

                if line[i-1] == '\\' and (line[i] == '\'' or line[i] == '\"') and line[i-2] != '\\':
                    lex += line[i]
                    i += 1

                elif line[i] == '<':
                    lex += "&lt"
                    i += 1

                elif line[i] == '>':
                    lex += "&gt"
                    i += 1

                elif line[i] == '\'' or line[i] == '\"' or not line[i+1]:
                    lex += line[i]
                    write(lex, "lightcoral", fileW)
                    i += 1
                    lex = ''
                    break

                else:
                    lex += line[i]
                    i += 1
        
        #Se inserta un comentario
        elif line[i] == "#":
            lex += line[i]
            i += 1

            while True:

                if line[i] == "\n" or not line[i+1]:
                    lex += line[i]
                    write(lex, "green", fileW)
                    i += 1
                    lex = ''
                    break
                
                else:
                    lex += line[i]
                    i += 1
        
        #Se insertan operadores y puntos
        elif line[i] == '+' or line[i] == '*' or line[i] == '/' or line[i] == '-' or line[i] == '.' or line[i] == ',':
            write(line[i], "darkslategray", fileW)
            i += 1
        
        #Se insertan asignadores
        elif line[i] == '=' or line[i] == '==' or line[i] == '!=' or line[i] == '<=' or line[i] == '>=':
            write(line[i], "lightslategray", fileW)
            i += 1

        #Asignador < (caso especial)
        elif line[i] == '<':
            write("&lt", "lightslategray", fileW)
            i += 1

        #Asignador > (caso especial)
        elif line[i] == '<':
            write("&gt", "lightslategray", fileW)
            i += 1
        
        #Se insertan numeros
        elif line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
            lex += line[i]
            i += 1
                        
            while True:
                if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                    lex += line[i]
                    i += 1
                    break
                else:
                    break
            
            if line[i] == 'e' or line[i] == 'E':
                lex += line[i]
                i += 1
                
                while True:
                    if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                        lex += line[i]
                        i += 1
                        
                        while True:
                            if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                                lex += line[i]
                                i += 1
                                break
                            else:
                                write(lex, "lightseagreen", fileW)
                                lex = ''
                                break
                    else:
                        write(lex, "firebrick", fileW)
                        break
            
            elif line[i] == '.':
                lex += line[i]
                write(lex, "lightseagreen", fileW)
                lex = ''
                i += 1
                
                if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                    lex += line[i]
                    i += 1
                
                    while True:
                        if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                            lex += line[i]
                            i += 1
                            break
                        else:
                            break

                    if line[i] == 'e' or line[i] == 'E':
                        lex += line[i]
                        i += 1
                        
                        while True:
                            if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                                lex += line[i]
                                i += 1
                                
                                while True:
                                    if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
                                        lex += line[i]
                                        i += 1
                                        break
                                    elif line[i] == '.':
                                        write(lex, "lightseagreen", fileW)
                                        lex = ''
                                        lex += line[i]
                                        i += 1
                                        while True:
                                            if line[i] == "\n":
                                                write(lex, "firebrick", fileW)
                                                lex = ''
                                                break
                                            else:
                                                lex += line[i]
                                                i += 1
                                        break
                                    else:
                                        write(lex, "lightseagreen", fileW)
                                        lex = ''
                                        break
                            else:
                                write(lex, "firebrick", fileW)
                                break
                else:
                    write(lex, "lightseagreen", fileW)
                    lex = ''
            else:
                write(lex, "lightseagreen", fileW)
                lex = ''
        
        #Se inserta cualquier otro tipo de dato
        else:
            write(line[i], "black", fileW)
            i += 1

#Se inicializa el elemento pre que cierra el archivo html
fileW.write("</pre>")

fileR.close()
fileW.close()