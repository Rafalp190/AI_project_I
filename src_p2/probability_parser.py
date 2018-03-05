from pyparsing import *

def probability_parser(directory) :
	

	COMMA      = Literal(",").suppress()
	EQUALS     = Literal("=").suppress()
	LPAREN     = Literal("(").suppress()
	RPAREN     = Literal(")").suppress()
	INIT       = Literal("P").suppress()
	PIPE       = Literal("|")
	NEG        = Literal("!")
	DECDOT     = Literal(".")
	DIGITS     = "0123456789"
	NUMBER     = Word( DIGITS )
	VAR        = Word( alphas ) 
	PROB       = INIT + LPAREN + Group(Optional(NEG) + VAR + Optional( OneOrMore(COMMA +  Optional(NEG) + VAR) ) + Optional( PIPE + OneOrMore( Optional(NEG)+ VAR + Optional( COMMA) ))) + RPAREN + EQUALS + Group(NUMBER + DECDOT + NUMBER)

	file = open(directory)
	lines = file.read().splitlines()


	parsed_lines = []
	for l in lines:

		try:
			results = PROB.parseString( l )
			res_array = [list(results[0])]
			prob = float(''.join(results[1]))
			res_array.append(prob)
			parsed_lines.append(res_array),
		except ParseException:
			print('ERR')


	file.close()
	return parsed_lines