import ply.lex as lex

#palavras reservadas
reserved = {"se": "SE", "então": "ENTAO","senão": "SENAO","fim": "FIM", "repita":"REP", "flutuante": "FLOAT","retorna": "RET","até": "ATE", "leia": "LEIA","escreve": "ESCREVE", "inteiro": "INT"}
#tokens
tokens = ['NUM','SOMA', 'SUB', 'MUL', 'DIV', 'IGUAL', 'VIRG', 'ATRIB', 'MENOR', 'MAIOR', 'MENEQ', 'MAIREQ', 'ABREPAR', 'FECHAPAR', 'DOISPTS', 'ABRECOL', 'FECHACOL', 'ID'] + list(reserved.values())

#expressores regulares
t_NUM = r'([0-9]+)(\.)?([0-9]+)?(e)?([0-9]+)?'
t_SOMA = r'\+'
t_SUB = r'\-'   
t_MUL = r'\*'
t_DIV = r'\/'
t_IGUAL = r'\='
t_VIRG = r'\,'
t_ATRIB = r'\:\='
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MENEQ = r'\<\='
t_MAIREQ = r'\>\='
t_ABREPAR = r'\('
t_FECHAPAR = r'\)'
t_DOISPTS = r'\:'
t_ABRECOL = r'\['
t_FECHACOL = r'\]'

#expressao de ID
def t_ID(t):
    r'[a-zà-úA-ZÀ-Ú][a-zà-úA-ZÀ-Ú0-9]*'

    t.type = reserved.get(t.value,'ID')
    return t

#comentario
def t_COMMENT(t):
    r'\(\{[^\}]*\}\)'
    pass
    
#nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#erro quando caracter não fizer parte dos tokens
def t_error(t):
    print("Caracter inválido na linha {0} posição {1} - {2}".format(t.lineno,t.lexpos, t.value[0]))

#caracteres que devem ser ignorados
t_ignore = ' \t\r'

#cria o lexer
lexer = lex.lex()

a = "inteiro: int\nflutuante: dan\ndan = 10\nse i < 10 então:"
lexer.input(a)

for tok in lexer:
    print(tok)
