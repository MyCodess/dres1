
	_______:  ---- Notes, samples,  ... for converting of texts with Regular expressions:

	_______:  --------- converting cmd/batch -> property-files:
- variable access: converting %xxx% to ${xxx} :   replacing  %\([^%]*\)%   with   ${\1}
- SET-lines in .cmd -> Properties: replacing  set *\(.*\)=.*   with  <property name=\"\1\"  value=\"\${env.\1\}\" />  ; and then replacing the right ENV.names
