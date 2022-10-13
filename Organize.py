#estas son las librerias que hay que importar
from distutils import extension
from PIL import Image            # esta libreria se importa aparte por cmd con este comando """ pip install Pillow """
import os

# CARPETAS EN ESCARGAS
fd = "D:\\CARPETA CENTRAL\\Descargas 2\\"                            #fd     = descargas     
fid= "D:\\CARPETA CENTRAL\\Descargas 2\\1.-IMAGENES\\"               #fid    = imagenes      JPEG, JPG, PNG, WEBP, HTM, JPG_LARGE, SVG, GIF, EML, 
fad= "D:\\CARPETA CENTRAL\\Descargas 2\\2.-ARCHIVOS\\"               #fad    = archivos      PDF, DOCX, DOC, TXT, PPTM, PPTX, 
fcorel= "D:\\CARPETA CENTRAL\\Descargas 2\\3.-COREL\\"               #fcorel = archivos      CDR, 
fphotoshop= "D:\\CARPETA CENTRAL\\Descargas 2\\4.-PHOTOSHOP\\"       #fphot..= archivos      PSD, AI, INDD,
fflexi= "D:\\CARPETA CENTRAL\\Descargas 2\\5.-FLEXI\\"               #fflexi = archivos      EPS, FS,
fdc= "D:\\CARPETA CENTRAL\\Descargas 2\\6.-COMPRIMIDOS\\"            #cd     = comprimidos   ZIP, RAR.
fpd= "D:\\CARPETA CENTRAL\\Descargas 2\\7.-PROGRAMAS\\"              #fdp    = programas     EXE, 

""" 
OJO: SE DEBEN CREAR LAS SIGUIENTES CARPETAS CARPETAS 
IMAGENES, PROGRAMAS, COMPRIMIDOS, ARCHIVOS, COREL, FLEXI, PHOTOSHOP
EN LA CARPETA DONDE TRABAJARA EL SCRIT

NOTA: tambien las extenciones deben escribirse tanto en mayuscula como en minusculas """


for filename in os.listdir(fd):
        name, extension = os.path.splitext(fd + filename)

        
        #1.-imagenes
        if extension in [".JPEG", ".JPG", ".PNG", ".WEBP", ".HTM", ".JPG_LARGE", ".SVG", ".GIF", ".EML", ".jpeg", ".jpg", ".png", ".webp", ".htm", ".jpg_large", ".svg", ".gif", ".eml",]:
           fid = "D:\\CARPETA CENTRAL\\Descargas 2\\1.-IMAGENES\\"
           os.rename(fd + filename, fid + filename)

        #2.-archivos
        if extension in [".docx", ".doc", ".pdf", ".xlsx", ".pptx", ".txt", ".pptm", ".DOCX", ".PDF", ".DOC", ".TXT", ".PPTM", ".XLSX", ".PPTX"]:
           fad = "D:\\CARPETA CENTRAL\\Descargas 2\\2.-ARCHIVOS\\"
           os.rename(fd + filename, fad + filename)

        #3.-corel
        if extension in [".CDR", ".cdr"]:
           fcorel = "D:\\CARPETA CENTRAL\\Descargas 2\\3.-COREL\\"
           os.rename(fd + filename, fcorel + filename)

        #4.-photoshop
        if extension in [".PSD", ".AI", ".INDD", ".psd", ".ai", ".indd"]:
           fphotoshop = "D:\\CARPETA CENTRAL\\Descargas 2\\4.-PHOTOSHOP\\"
           os.rename(fd + filename, fphotoshop + filename)

        #5.-flexi
        if extension in [".eps", ".fs", ".EPS", ".FS"]:
           fflexi = "D:\\CARPETA CENTRAL\\Descargas 2\\5.-FLEXI\\" 
           os.rename(fd + filename, fflexi + filename)

        #6.-comprimidos
        if extension in [".zip", ".rar", ".RAR", ".ZIP"]:
           fdc = "D:\\CARPETA CENTRAL\\Descargas 2\\6.-COMPRIMIDOS\\"
           os.rename(fd + filename, fdc + filename)

        #7.-programas
        if extension in [".exe", ".EXE"]:
           fpd = "D:\\CARPETA CENTRAL\\Descargas 2\\7.-PROGRAMAS\\"
           os.rename(fd + filename, fpd + filename)

#FIN 
