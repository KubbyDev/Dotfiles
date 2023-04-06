type aliases_list.txt > %userprofile%\macros.doskey

reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"%userprofile%\macros.doskey\"" /f
reg query "HKCU\Software\Microsoft\Command Processor" /v Autorun

pause