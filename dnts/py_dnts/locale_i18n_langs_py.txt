______________ locale, encoding/UTF8/ascii/unicode/..., langs, countries, ... py1: _____________
##________________________________________  ___________________________


#####  ==========  queries... locale:
	- OS-default-locale??:  import locale ;  locale.getpreferredencoding()  ##--: returns system/OS current charset/encoding
##________________________________________  ___________________________


#####  ==========  chars-listings-coll.: (see pydoc string)
	----- DATA
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    whitespace = '\t\n\x0b\x0c\r '
	----- generating chars-listings/tables:
	adapt this line to get your target listing:   chars = "".join(chr(x) for x in range(128))
	eg ascii:  ASCII-table-full = "".join(chr(x) for x in range(128))  ##--include also the non-printables !
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
