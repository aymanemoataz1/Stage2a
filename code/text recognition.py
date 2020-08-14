ex="ADROIT\n\nSOLAR + ENERGY + DESIGN\n\n \n\n1135 GARNET Ave, STE 32\nSAN DieGo, CA 92109\n\nUtaw WHITE (T) 858.483.3568 x16\na a x\nMECHANICAL ENGINEER (C) 858.692.6261\nPE, LEED AP (F) 858.492.7772\nUTAW@ADROITSOLAR.COM CA Lic 488255 Hi Lic 29995\n\nWWW.ADROITSOLAR.COM"
l=[]
ex1=str()
for i in ex:

    if i!="\n":
        ex1+=i        
    else:
        if ex1!=str():
           l.append(ex1)
           ex1=str()
        
 