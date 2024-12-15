#!/usr/bin/perl -w
##-	USAGE:  prove [-v]  $0
#	prove basicallay just evaluates the OUTPUT of the script!
#	prove interpreted the output of the script as it would the output of a real test. In fact, there's no effective difference—a real test might produce that exact output.
#	see:  Perl_Testing__A_Developers_Notebook_Ore_0507.chm--CH.1.3--#->Interpreting-test-results

#### this ist exactly the outout of another script-test. by printint to stdout, "prove" just evaluates it, as if it were the test-output!:
print <<END_HERE;
1..9
ok 1
not ok 2
#     Failed test (t/sample_output.t at line 10)
#          got: '2'
#     expected: '4'
ok 3
ok 4 - this is test 4
not ok 5 - test 5 should look good too
not ok 6 # TODO fix test 6
# I haven't had time add the feature for test 6
ok 7 # skip these tests never pass in examples
ok 8 # skip these tests never pass in examples
ok 9 # skip these tests never pass in examples
END_HERE
