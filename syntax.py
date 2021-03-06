import string

# SYNTAX SETTINGS
VARIABLES       = string.ascii_letters + string.digits

OPENING_BRACKET = '('
CLOSING_BRACKET = ')'
BRACKETS        = [OPENING_BRACKET, CLOSING_BRACKET]

AND_OPERATOR    = '&'
OR_OPERATOR     = '|'
XOR_OPERATOR    = '^'
NOT_OPERATOR    = '~'
IMPL_OPERATOR   = '>'
XNOR_OPERATOR   = '='
OPERATORS       = [AND_OPERATOR, OR_OPERATOR, XOR_OPERATOR, NOT_OPERATOR, IMPL_OPERATOR, XOR_OPERATOR]

TRUE_CONSTANT   = '1'
FALSE_CONSTANT  = '0'
CONSTANTS       = [TRUE_CONSTANT, FALSE_CONSTANT]
