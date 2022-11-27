#ceu.es.
def camb_correo(correo):
    correo=correo.split('@')
    return correo[0]+"@ceu.es"
print(camb_correo("anarevalo@hotmail.com"))
