import xlrd
from Arrays import Array3D
def main():
    a3 = Array3D(34,33,14) #34 AÑOS , 33 ESTADOS , 14 DATOS
    for anio in range(1985,2018,1):
        ruta = './Precipitacion/'+str(anio)+'Precip.xls'
        #print(ruta)
        archivo = xlrd.open_workbook(filename = ruta)
        hoja = archivo.sheet_by_index(0)
        for r in range(1,33,1):
            for c in range(0,14,1):
                #print(hoja.cell_value(r , c), end='')
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r , c))
    a = int(input('Año (1985-2018)'))
    e = int(input('Edo (1-32)'))
    m = int(input('Mes (1-12)'))

    #AÑO ESTADO MES
    print(f"En el estado {a3.get_item(a-1985,e,m-m)} llovio un promedio de {a3.get_item(a-1985,e,m)} centimetros cubicos en el mes de {a3.get_item(a-1985,e-e,m)} de {a} ")

    #ESTADO MES
    s = 0
    for an in range(0,34,1):
        i = a3.get_item(an,e,m)
        s = s + i
    d = s/33
    print(f"Del año 1985 al 2019 en el mes de {a3.get_item(a-1985,e-e,m)} del estado {a3.get_item(a-1985,e,m-m)} hay un promedio de {d} centimetros cubicos")

    #ESTADO
    s = 0
    sp = 0
    for an in range(0,34,1):
        for me in range(1,13,1):
            i = a3.get_item(an,e,me)
            s = s + i
        p = s/12
        sp = (sp + p)/33
    print(f"Del año 1985 al 2018 en todos los meses del estado de {a3.get_item(a-1985,e,m-m)} hay un promedio de {sp}")

    #promedio total
    s = 0
    sp = 0
    spp = 0 
    for an in range(0,34,1):
        for es in range(1,33,1):
            for me in range(1,13,1):
                i = a3.get_item(an,es,me)
                s = s + i
            p = s/12
            sp = (sp + p)/32
        spp = (spp + sp)/33
    print(f"El promedio total de todos los años, los meses y los estados de Mexico es de {spp}")
main()
