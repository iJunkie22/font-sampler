python setup.py py2exe > setup-log.txt
7z -aoa x dist\library.zip -o"dist\library\"
del dist\library.zip
cd dist\library\
7z a -tzip -mx9 "..\library.zip" -r
del *.* /s /q
rd *.* /s /q
cd ..
upx --best *.*
cd ..
del build /s /q
rd build /s /q
7z a -tzip -mx9 "dist.zip" -r dist\*.*
