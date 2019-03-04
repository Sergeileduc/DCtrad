@ECHO OFF
REM Find and smallify CBZ files

ECHO Création du dossier Smaller_comics
IF NOT EXIST Smaller_comics MKDIR Smaller_comics

ECHO Je cherche des fichiers CBZ

for %%F in (*.cbz) do (
ECHO J'ai trouvé %%F
REM Extract...
"C:\Program Files\7-zip\7z" e "%%F" -o"%%~nF" *.jpg *.jpeg *.png -r
REM Does the directory exist? has 7zip created it correctly?
	IF EXIST "%%~nF" (
	REM Change directory, create zip of contents of directory...
	PUSHD "%%~nF"
	IF EXIST Thumbs.db DEL /F /S /Q Thumbs.db
	ECHO Conversion des jpg en qualité inférieure.
	for %%I in (*.jpg *.jpeg) do (
		magick "%%I" -quality 60 -geometry x1920 "%%I"
	)
	for %%I in (*.png) do (
		magick "%%I" -geometry x1920 "%%I"
	)
	REM "C:\Program files\GIMP 2\bin\gimp-console-2.10" -i -d -f -c -b "(batch-save-quality \"*.jpg\" 0.6)" -b "(gimp-quit 0)"
	POPD
	ECHO %cd%
	ECHO Je crée %%~nF.cbz dans le dossier Smaller_comics
	"C:\Program Files\7-Zip\7z.exe" a -tzip "Smaller_comics\%%~nF.cbz" "%%~nF"
	RMDIR "%%~nF" /S /Q
	)
)

for %%F in (*.cbr) do (
ECHO J'ai trouvé %%F
REM Extract...
"C:\Program Files\7-zip\7z" e "%%F" -o"%%~nF" *.jpg *.jpeg *.png -r
REM Does the directory exist? has 7zip created it correctly?
	IF EXIST "%%~nF" (
	REM Change directory, create zip of contents of directory...
	PUSHD "%%~nF"
	IF EXIST Thumbs.db DEL /F /S /Q Thumbs.db
	ECHO Conversion des jpg en qualité inférieure.
	for %%I in (*.jpg *.jpeg) do (
		magick "%%I" -quality 60 -geometry x1920 "%%I"
	)
	for %%I in (*.png) do (
		magick "%%I" -geometry x1920 "%%I"
	)
	REM "C:\Program files\GIMP 2\bin\gimp-console-2.10" -i -d -f -c -b "(batch-save-quality \"*.jpg\" 0.6)" -b "(gimp-quit 0)"
	POPD
	ECHO Je crée %%~nF.cbr dans le dossier Smaller_comics
	"C:\Program Files\WinRAR\rar.exe" a -ma4 "Smaller_comics\%%~nF.cbr" "%%~nF"
	RMDIR "%%~nF" /S /Q
	)
)
	
PAUSE