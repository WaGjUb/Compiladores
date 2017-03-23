%{
#include <stdio.h>
int lineno = 1;
%}
 
line .*\n

%% /* Regras */
{line} { printf("%5d %s", lineno++, yytext); }

%%
int yywrap(){
	return 1;
}

int main(int argc, char *argv[]){
	yyin = fopen(argv[1], "r");
	yylex();
	fclose(yyin);
	return 0;
} 
