-! modifiers-for-batch-parameters:  ~xx is modifier for %1 -> %~xx1   : also modifiers kommen beim %1 zwischen % und 1 (bzw.  0-9) und aendern das endergebnis!
- IF: if has got obviously no access to env-variables, which are defined in the same if-loop. So no references to them are allowed inside the same IF-loop.
- all jar-files in DIRx add to classpath: see ant_home\bin\lcp.bat (variables in For-loop are not persistent!)
- for-loop e.g.:
	- from script: for %%I in (*.*) do echo %%~ftzaI
	- from DOS/Shell: for %I in (*.*) do echo %~ftzaI
- for-loop-command:
	@echo off
	for %%i in (
	msg1
	msg2
	msg3
	)do echo SimpleQSenderTest.cmd  %%i
