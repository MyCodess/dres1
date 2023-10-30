==== FOR exp.:
- /L  :Loop ; /F  :FileProcessing ;  /R  :Recursive ; /D  :Directories; 
- simple: for %f in (*.txt) do echo ----%f 
-! die Modifications of env-var INSIDE a for-loop are NOT accessible to the loop-itself !! The loop reads the value always again and again from the parent-cmd and returns ONLY the end modification of the env-var back to the parent-cmd. so DURING the loop the env-var will be RESET again to its value from parent-cmd !!~:)
-! FOR-Loop-Variables are CASE-SENSITIVE and must be represented with an ALPHA value, such as %A, %B, or %C.
- properties-file executing for setting env-variables (and ignoring comment-lines "#"): 
	- for  /F "eol=#" %%i in (t1.properties) do set %%i
	- see also in help the exp-descriptin:  for /F "eol=; tokens=2,3* delims=," %i in (meineDat.txt) do @echo %i %j %k
	- do NOT use any special chars/spaces/./....
	- only simple properties-lines without considering comments: 	for  /F %%i in (t1.properties) do set %%i
- processing/parsing the CONTENT of files OR literal Strings see /F switch (eg. setting variaables from properties-files)
- loop with counter: for  /L %%i in (0,2,16) do echo %%i
	:for /L {%% | %}variable in (start#,step#,end#) do command [CommandLineOptions]
- only directories:   for  /D  %%i in (*) do echo %%i
- only files:  for  %%i in (*) do echo %%i   (is default. so dafeult does NOT handle directories!!)
- recursive: for  /R  %%i in (*) do echo %%i
##________________________________________  ___________________________


#####  ==========  from wxp-Help: For
For
Führt den angegebenen Befehl für jede Datei einer Gruppe von Dateien aus.
Syntax
for {%Variable|%%Variable} in (Gruppe) do Befehl [Befehlszeilenoptionen]
Parameter
{%Variable|%%Variable} 
Erforderlich. Stellt einen ersetzbaren Parameter dar. Verwenden Sie %Variable, wenn Sie den Befehl for über die Eingabeaufforderung ausführen möchten. Verwenden Sie %%Variable, wenn Sie den Befehl for in einer Batchdatei ausführen möchten. Variablen berücksichtigen Groß-/Kleinschreibung und müssen durch einen Alphawert, z. B. %A, %B oder %C, dargestellt werden. 
(Gruppe) 
Erforderlich. Gibt eine oder mehrere Dateien, Verzeichnisse, Wertebereiche oder Zeichenfolgen an, die mit dem angegebenen Befehl bearbeitet werden sollen. Die Klammern müssen angegeben werden. 
Befehl 
Erforderlich. Gibt den Befehl an, der für alle in (Gruppe) angegebenen Dateien, Verzeichnisse, Wertebereiche oder Zeichenfolgen ausgeführt werden soll. 
Befehlszeilenoptionen 
Gibt alle Befehlszeilenoptionen an, die Sie zusammen mit dem angegebenen Befehl verwenden möchten. 
/?
Zeigt Hilfe an der Eingabeaufforderung an. 
Hinweise
Verwenden von for 
Sie können den Befehl for in einer Batchdatei oder direkt an der Eingabeaufforderung verwenden.
Verwenden von Stapelverarbeitungsparametern 
Die folgenden Attribute gelten für den Befehl for:
Der Befehl for ersetzt %Variable bzw. %%Variable nacheinander durch jede der in Gruppe angegebenen Zeichenfolgen, bis der Befehl für alle Dateien ausgeführt wurde. 
Variablennamen in for-Anweisungen sind globale Variablen. Dabei ist die Groß-/Kleinschreibung relevant, so dass insgesamt höchstens 52 Variablen aktiv sein können. 
Um Verwechslungen mit den Batchparametern %0 bis %9 zu vermeiden, können Sie für Variable jedes beliebige Zeichen, ausgenommen jedoch die Ziffern 0 bis 9, verwenden. In einfachen Batchdateien ist ein einzelnes Zeichen, wie beispielsweise %%f, ausreichend. 
In komplexen Batchdateien können Sie auch mehrere Werte für Variable verwenden, um verschiedene ersetzbare Variablen voneinander unterscheiden zu können. 
Angeben einer Gruppe von Dateien 
Der Parameter Gruppe kann eine einzelne oder mehrere Gruppen von Dateien beinhalten. Sie können Dateigruppen mit Platzhalterzeichen (d. h. * und ?) angeben. Die folgenden Beispiele sind gültige Dateigruppen: 
(*.doc)
(*.doc *.txt *.me)
(jan*.doc jan*.rpt feb*.doc feb*.rpt)
(ar??1991.* ap??1991.*)
Wenn Sie den Befehl for ausführen, wird der erste Wert in Gruppe für %Variable bzw. %%Variable eingesetzt, und dann verarbeitet der angegebene Befehl diesen Wert. Dieser Vorgang wird so lange wiederholt, bis alle Dateien (bzw. Dateigruppen), die dem Wert in Gruppe entsprechen, verarbeitet wurden.
Verwenden der Schlüsselwörter in und do 
in und do sind keine Parameter, müssen jedoch im Befehl for angegeben werden. Wenn Sie eines dieser Schlüsselwörter nicht eingegeben haben, wird eine Fehlermeldung angezeigt.
Verwenden weiterer Formen des Befehls for 
Wenn Befehlserweiterungen verfügbar sind (wie dies standardmäßig der Fall ist), werden die folgenden Formen des Befehls for ebenfalls unterstützt:
Nur Verzeichnisse 
Wenn Gruppe Platzhalterzeichen (* und ?) enthält, wird der angegebene Befehl statt für eine bestimmte Gruppe von Dateien in einem angegebenen Verzeichnis für alle Verzeichnisse ausgeführt, auf die die Angabe in Gruppe zutrifft. Für diesen Befehl gilt die folgende Syntax: 
for /D {%% | %}Variable in (Gruppe) do Befehl [Befehlszeilenoptionen] 
Rekursiv 
Durchläuft die Verzeichnisstruktur unter [Laufwerk:]Pfad und führt die for-Anweisung in jedem Verzeichnis der Struktur aus. Wenn nach /R kein Verzeichnis angegeben wird, wird das aktuelle Verzeichnis verwendet. Wird für Gruppe nur ein Punkt (.) angegeben, wird lediglich die Verzeichnisstruktur aufgelistet. Für diesen Befehl gilt die folgende Syntax: 
for /R [[Laufwerk :]Pfad] {%% | %}Variable in (Gruppe) do Befehl [Befehlszeilenoptionen]
Durchlaufen eines Wertebereichs 
Verwenden Sie eine iterative Variable, um den Anfangswert (Anfang#) anzugeben und anschließend einen bestimmten Wertebereich zu durchlaufen, bis der Endwert (Ende#) erreicht wird. /L führt die Iteration aus und vergleicht dabei Anfang# mit Ende#. Solange Anfang# kleiner als Ende# ist, wird der Befehl ausgeführt. Wenn die iterative Variable Ende# überschreitet, verlässt die Eingabeaufforderung die Schleife. Sie können auch mit einem negativen Wert für Schritt# einen Wertebereich in abfallender Reihenfolge durchlaufen. (1,1,5) generiert beispielsweise die Sequenz 1 2 3 4 5 und (5,-1,1) generiert die Sequenz (5 4 3 2 1). Für diesen Befehl gilt die folgende Syntax: 
for /L {%% | %}Variable in (Anfang#,Schritt#,Ende#) do Befehl [Befehlszeilenoptionen]
Iteration und Dateianalyse 
Sie verwenden die Dateianalyse, um Befehlsausgaben, Zeichenfolgen und Dateiinhalte zu verarbeiten. Verwenden Sie iterative Variablen, um den Inhalt oder die Zeichenfolgen zu bestimmen, den/die Sie untersuchen möchten, und verwenden Sie die verschiedenen Analyseschlüsselwörter-Optionen, um die Auswertung weiter zu modifizieren. Verwenden Sie die Analyseschlüsselwörter-Option token, um anzugeben, welche Tokens als Iteratorvariablen weitergegeben werden sollen. Beachten Sie, dass /F bei der Verwendung ohne die Option token nur das erste Token untersucht.
Bei der Dateianalyse werden Ausgabe, Zeichenfolge oder Dateiinhalt gelesen, in einzelne Textzeilen aufgeteilt, und jede Zeile wird in null oder mehrere Tokens ausgewertet. Anschließend wird die for-Schleife aufgerufen, wobei der Wert der Iteratorvariable auf das Token gesetzt wird. Standardmäßig übergibt /F das erste mit Leerzeichen umgebene Token aus jeder Zeile jeder Datei. Leere Zeilen werden übersprungen. Die unterschiedlichen Syntaxformen sind dabei:
for /F ["Analyseschlüsselwörter"] {%% | %}Variable in (Dateinamensatz) do Befehl [Befehlszeilenoptionen]
for /F ["Analyseschlüsselwörter"] {%% | %}Variable in ("LiteraleZeichenfolge") do Befehl [Befehlszeilenoptionen]
for /F ["Analyseschlüsselwörter"] {%% | %}Variable in ('Befehl') do Befehl [Befehlszeilenoptionen]
Das Argument Dateinamensatz gibt eine oder mehrere Dateinamen an. Jede Datei wird geöffnet, gelesen und verarbeitet, bevor die nächste Datei aus dem Dateinamensatz bearbeitet wird. Geben Sie "Analyseschlüsselwörter" an, um das Standardverhalten bei der Auswertung zu überschreiben. Hierbei handelt es sich um eine Zeichenfolge in Anführungszeichen, die ein oder mehrere Schlüsselwörter enthält, mit denen Sie verschiedene Analyseoptionen angeben. 
Wenn Sie die Option usebackq verwenden, gelten die folgenden Syntaxformen:
for /F ["usebackqAnalyseschlüsselwörter"] {%% | %}Variable in ("Dateinamensatz") do Befehl [Befehlszeilenoptionen]
for /F ["usebackqAnalyseschlüsselwörter"] {%% | %}Variable in ('LiteraleZeichenfolge') do Befehl [Befehlszeilenoptionen]
for /F ["usebackqAnalyseschlüsselwörter"] {%% | %}Variable in (`Befehl`) do Befehl [Befehlszeilenoptionen]
Die folgende Tabelle listet die Analyseschlüsselwörter auf, die Sie als Analyseschlüsselwörter verwenden können.
Schlüsselwort Beschreibung 
eol=c Gibt ein Zeilenendezeichen (End-Of-Line) an (nur ein Zeichen). 
skip=n Gibt an, wie viele Zeilen am Anfang einer Datei übersprungen werden sollen. 
delims=xxx Gibt einen Trennzeichensatz an. Dieser ersetzt den Standard-Trennzeichensatz aus Leerzeichen und Tabulator. 
tokens=x,y,m-n Gibt an, welche Tokens aus jeder Zeile bei jeder Iteration an den Rumpf der for-Anweisung übergeben werden. Als Ergebnis davon werden zusätzliche Variablennamen zugewiesen. Die Form m-n gibt den Bereich vom m-ten bis zum n-ten Token an. Wenn das letzte Zeichen in der Zeichenfolge tokens= ein Sternchen (*) ist, wird eine weitere Variable zugewiesen, die den übrigen Text der Zeile nach dem zuletzt geparsten Token empfängt. 
usebackq Gibt an, dass Sie bei der Angabe von Dateinamen in Dateinamensatz Anführungszeichen verwenden können; eine Zeichenfolge in schrägen, einzelnen Anführungszeichen wird als Befehl ausgeführt, und eine Zeichenfolge in einfachen Anführungszeichen ist ein literaler Zeichenfolgenbefehl. 
Ersetzen von Variablen 
Die Ersetzungsparameter für Verweise auf for-Variablen wurden verbessert. Die folgende Tabelle enthält die optionale Syntax (für eine beliebige Variable I).
Variable mit Parameter Beschreibung 
%~I Erweitert %I und entfernt alle umschließenden Anführungszeichen (""). 
%~fI Erweitert %I zu einer voll gekennzeichneten Pfadbezeichnung. 
%~dI Erweitert %I nur zu einem Laufwerkbuchstaben. 
%~pI Erweitert %I nur zu einem Pfad. 
%~nI Erweitert %I nur zu einem Dateinamen. 
%~xI Erweitert %I nur zu einer Dateinamenerweiterung. 
%~sI Erweitert %I zu einem Pfad, der nur kurze Pfad- und Dateinamen enthält. 
%~aI Erweitert %I zu den Dateiattributen der Datei. 
%~tI Erweitert %I zu Datum und Uhrzeit der Datei. 
%~zI Erweitert %I zur Größe der Datei. 
%~$PATH:I Durchsucht die in der Umgebungsvariablen PATH aufgeführten Verzeichnisse und erweitert %I zu dem voll gekennzeichneten Namen der ersten Übereinstimmung. Wurde der Name der Umgebungsvariablen nicht festgelegt oder die Datei nicht gefunden, gibt der Parameter eine leere Zeichenfolge zurück. 
Die folgende Tabelle enthält die Parameterkombinationen, die Sie verwenden können, um zusammengesetzte Ergebnisse zu erhalten.
Variable mit kombinierten Parametern Beschreibung 
%~dpI Erweitert %I nur zu einem Laufwerkbuchstaben und Pfad. 
%~nxI Erweitert %I nur zu einem Dateinamen mit Erweiterung. 
%~fsI Erweitert %I zu einem vollständigen Pfad mit kurzen Namen. 
%~dp$PATH:I Durchsucht die in der Umgebungsvariablen PATH aufgeführten Verzeichnisse und erweitert %I zu dem Laufwerkbuchstaben und Pfad der ersten Übereinstimmung. 
%~ftzaI Erweitert %I zu einer dir-ähnlichen Ausgabezeile. 
In den oben aufgeführten Beispielen können Sie für %I und PATH auch andere gültige Werte verwenden. Ein gültiger for-Variablenname beendet die Syntax %~.
Indem Sie die Variablennamen in Großbuchstaben schreiben, z. B. %I, machen Sie Ihren Code besser lesbar und vermeiden Verwechslungen mit den Parametern, die die Groß-/Kleinschreibung nicht berücksichtigen.
Analysieren einer Zeichenfolge 
Sie können die for /F-Funktionalität zur Analyse auch direkt für eine Zeichenfolge verwenden, indem Sie den Dateinamensatz in Klammern in einfache Anführungszeichen setzen (z. B. 'Dateinamensatz'). Dateinamensatz wird dann wie eine einzelne Zeile von Eingabedaten aus einer Datei behandelt und anschließend analysiert.
Analysieren von Ausgabedaten 
Sie können den Befehl for /F verwenden, um die Ausgabe eines Befehls zu analysieren, indem Sie den Dateinamensatz in Klammern durch eine Zeichenfolge ersetzen, die in schräge einzelne Anführungszeichen (Graviszeichen) eingeschlossen ist. Diese Zeichenfolge wird als Befehlszeile betrachtet und von einer untergeordneten Cmd.exe ausgeführt. Die Ausgabe dieses Befehls wird dann wie eine normale Datei analysiert. 
Beispiele
In einer Batchdatei verwenden Sie folgende Syntax: 
for %%Variable in (Gruppe) do Befehl [Befehlszeilenoption]
Um mithilfe der ersetzbaren Variable %f den Inhalt aller im aktuellen Verzeichnis enthaltenen Dateien mit der Erweiterung DOC oder TXT anzuzeigen, geben Sie Folgendes ein. 
for %f in (*.doc *.txt) do type %f 
Im voranstehenden Beispiel wird jede Datei im aktuellen Verzeichnis, die die Erweiterung DOC oder TXT hat, für die Variable %f eingesetzt, bis der Inhalt jeder Datei angezeigt worden ist. Wenn Sie diesen Befehl in einer Batchdatei verwenden möchten, ersetzen Sie %f jeweils durch %%f. Andernfalls wird die Variable ignoriert, und es wird eine Fehlermeldung angezeigt. 
Um eine Datei zu analysieren und dabei die Kommentarzeilen zu überlesen, geben Sie Folgendes ein:
for /F "eol=; tokens=2,3* delims=," %i in (meineDat.txt) do @echo %i %j %k
Mit diesem Befehl wird die Datei MeineDat.txt zeilenweise eingelesen, wobei Zeilen, die mit einem Semikolon beginnen, überlesen und das zweite bzw. dritte Token jeder Zeile an den Rumpf der FOR-Schleife übergeben werden. Als Trennzeichen für Tokens werden das Komma und das Leerzeichen festgelegt. Im Rumpf der FOR-Anweisung wird %i verwendet, um das zweite Token abzurufen, %j für das dritte Token und %k für alle folgenden Tokens. Wenn der angegebene Dateiname Leerzeichen enthält, setzen Sie den Text in Anführungszeichen (z. B. "Name der Datei"). Um Anführungszeichen zu verwenden, müssen Sie usebackq angeben. Ansonsten werden die Anführungszeichen so interpretiert, als ob sie eine zu analysierende literale Zeichenfolge definieren.
%i wird in der FOR-Anweisung explizit deklariert, und %j und %k werden implizit über die Option tokens= deklariert. Sie können mit tokens= bis zu 26 Tokens deklarieren, vorausgesetzt, in der Anweisung wird nicht versucht, Variablen zu deklarieren, deren Wert höher als 'z' bzw. 'Z' ist.
Um die Ausgabe eines Befehls zu analysieren, indem Sie Dateinamensatz in Klammern setzen, geben Sie Folgendes ein:
for /F "usebackq delims==" %i IN (`satz`) DO @echo %i 
Durch die Verwendung dieser Anweisung werden die Umgebungsvariablen der aktuellen Umgebung aufgelistet.
Formatierungslegende
Format Bedeutung 
Kursiv  Informationen, die der Benutzer angeben muss 
Fett  Elemente, die der Benutzer genau wie gezeigt eingeben muss 
Ellipse (...) Parameter, der in einer Befehlszeile mehrmals wiederholt werden kann 
In eckigen Klammern ([]) Optionale Elemente 
In geschweiften Klammern ({}); Auswahlmöglichkeiten durch einen senkrechten Strich (|) getrennt. Beispiel: {gerade|ungerade} Gruppe von Auswahlmöglichkeiten, aus denen der Benutzer nur eine wählen darf 
Schriftart Courier  Code oder Programmausgabe 
Verwandte Themen
