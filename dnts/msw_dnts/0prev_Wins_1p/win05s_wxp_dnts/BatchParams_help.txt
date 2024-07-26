-! Geben Sie CALL /? oder FOR /? ein, um herauszufinden, welche Formate gültig sind. Auflistung-Hilfe.
Verwenden von BatchparameternSie können Batchparameter überall innerhalb einer Batchdatei verwenden, um Informationen zu den Umgebungseinstellungen zu extrahieren.
Cmd.exe stellt die Batchparameter-Erweiterungsvariablen %0 bis %9 bereit. Wenn Sie Batchparameter in einer Batchdatei verwenden, wird %0 durch den Batchdateinamen ersetzt, und %1 bis %9 werden durch die entsprechenden Argumente ersetzt, die Sie in der Befehlszeile eingeben. Sie müssen den Befehl shift verwenden, um auf Argumente jenseits von %9 zuzugreifen. Weitere Informationen zum Befehl shift finden Sie unter Shift. Der Batchparameter %* ist ein Platzhalterverweis auf alle Argumente, mit Ausnahme von %0, die an die Batchdatei weitergegeben werden.
Geben Sie beispielsweise Folgendes in eine Batchdatei namens Meinbatch.bat ein, um den Inhalt von Ordner1 in Ordner2 zu kopieren, wobei %1 durch den Wert Ordner1 und %2 durch den Wert Ordner2 ersetzt wird:
xcopy %1\*.* %2
Geben Sie Folgendes ein, um die Datei auszuführen:
meinbatch.bat C:\ordner1 D:\ordner2
Dies hat dieselbe Auswirkung wie das Eingeben des Folgenden in die Batchdatei:
xcopy C:\ordner1 \*.* D:\ordner2 
Sie können auch Parameter mit Batchparametern verwenden. Parameter verwenden die aktuellen Laufwerk- und Verzeichnisinformationen, um den Batchparameter zu einem teilweisen oder vollständigen Datei- oder Verzeichnisnamen zu erweitern. Geben Sie das Prozentzeichen (%) gefolgt von einer Tilde (~) ein, und geben Sie dann den entsprechenden Parameter ein (d. h. %~Parameter), um einen Parameter zu verwenden.
Die folgende Tabelle listet die Parameter auf, die Sie als Erweiterung verwenden können.
Parameter Beschreibung 
%~1 Erweitert %1, wobei umgebende Anführungszeichen (") entfernt werden 
%~f1 Erweitert %1 zu einer vollständig qualifizierten Pfadbezeichnung. 
%~d1 Erweitert %1 zu einem Laufwerkbuchstaben.  
%~p1 Erweitert %1 zu einem Pfad. 
%~n1 Erweitert %1 zu einem Dateinamen.  
%~x1 Erweitert %1 zu einer Dateinamenerweiterung. 
%~s1 Erweitert den Pfad, so dass nur der kurze Dateiname enthalten ist. 
%~a1 Erweitert %1 zu Dateiattributen. 
%~t1 Erweitert %1 zu den Datums- und Uhrzeitangaben der Datei. 
%~z1 Erweitert %1 zu der Größe der Datei. 
%~$PATH:1 Durchsucht die in der Umgebungsvariablen PATH aufgeführten Verzeichnisse und erweitert %1 zu dem vollständig qualifizierten Namen des ersten gefundenen Verzeichnisses. Wurde der Name der Umgebungsvariablen nicht definiert oder die Datei nicht gefunden, gibt der Parameter eine leere Zeichenfolge zurück. 
Die folgende Tabelle listet mögliche Kombinationen aus Parametern und Kennzeichnern auf, die Sie verwenden können, um zusammengesetzte Ergebnisse zu erhalten.
Parameter Beschreibung 
%~dp1 Erweitert %1 zu einem Laufwerkbuchstaben mit Pfadangabe. 
%~nx1 Erweitert %1 zu einem Dateinamen mit Erweiterung. 
%~dp$PATH:1 Durchsucht die in der Umgebungsvariablen PATH aufgeführten Verzeichnisse und erweitert %1 zu dem Laufwerkbuchstaben und Pfad des ersten gefundenen Verzeichnisses. 
%~ftza1 Erweitert %1 zu einer dir-ähnlichen Ausgabezeile. 
 Anmerkung
In den vorherigen Beispielen können Sie %1 und PATH durch andere Batchparameterwerte ersetzen. 
Der Parameter %* ist ein eindeutiger Parameter, der alle in einer Batchdatei weitergegebenen Argumente darstellt. Sie können diesen Parameter nicht in Verbindung mit dem Parameter %~ verwenden. Die Syntax %~ muss durch einen gültigen Argumentwert abgeschlossen sein.
Sie können Batchparameter nicht auf die gleiche Weise ändern wie Umgebungsvariablen. Sie können Werte nicht suchen und ersetzen oder untergeordnete Zeichenfolgen untersuchen. Sie können jedoch den Parameter einer Umgebungsvariablen zuweisen und dann diese ändern.
