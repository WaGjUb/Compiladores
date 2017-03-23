%{
#include <stdio.h>
int lineno = 1;
%}
%option noyywrap
line .*\n

%% /* Regras */
{line} { printf("%5d %s", lineno++, yytext); }

%%
int main(int argc, char *argv[]){
	yylex();
	return();
} 
