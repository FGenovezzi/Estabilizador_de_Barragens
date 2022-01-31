from tkinter import *

bar = Tk()
bar.title('Estabilidade')

img = PhotoImage(file="./bar1.png")

i = Label(bar,image=img)
i.img=img
i.grid(row=0,columnspan=5)

Label(bar,text='A=').grid(row=1,column=0,)
Label(bar,text='B=').grid(row=1,column=2,)
Label(bar,text='C=').grid(row=2,column=0,)
Label(bar,text='D=').grid(row=2,column=2,)
Label(bar,text='E=').grid(row=3,column=0,)
Label(bar,text='F=').grid(row=3,column=2,)
Label(bar,text='G=').grid(row=4,column=0,)
Label(bar,text='H=').grid(row=4,column=2,)
Label(bar,text='Peso específico da água (γa)=').grid(row=5,columnspan=3,)
Label(bar,text='Peso específico do conc. (γc)=').grid(row=6,columnspan=3,)
Label(bar,text='Coeficiente de Atrito=').grid(row=7,columnspan=3,)
Label(bar,text='C.S. Tombamento=').grid(row=8,columnspan=3,)
Label(bar,text='C.S. Arrastamento=').grid(row=9,columnspan=3,)

a0 = Entry(bar); a0.grid(row=1,column=1)
b0 = Entry(bar); b0.grid(row=1,column=3)
c0 = Entry(bar); c0.grid(row=2,column=1)
d0 = Entry(bar); d0.grid(row=2,column=3)
e0 = Entry(bar); e0.grid(row=3,column=1)
f0 = Entry(bar); f0.grid(row=3,column=3)
g0 = Entry(bar); g0.grid(row=4,column=1)
h0 = Entry(bar); h0.grid(row=4,column=3)
ya0 = Entry(bar); ya0.grid(row=5,column=3)
yc0 = Entry(bar); yc0.grid(row=6,column=3)
fi0 = Entry(bar); fi0.grid(row=7,column=3)
ct0 = Entry(bar); ct0.grid(row=8,column=3)
ca0 = Entry(bar); ca0.grid(row=9,column=3)

def calculo():

    a = float(a0.get());b = float(b0.get());c = float(c0.get());d = float(d0.get());e = float(e0.get());f = float(f0.get());g = float(g0.get());h = float(h0.get())
    y=float(ya0.get());yc=float(yc0.get());fi=float(fi0.get());ct=float(ct0.get());ca=float(ca0.get())

    h1 = float(y*a*a/2)
    h2 = float(y*e*e/2)
    v1 = float((y*f*a*a)/(2*(a+b)))
    v2 = float((y*h*e*e)/(2*(a+b-d)))
    w1 = float(f*(a+b)*yc/2)
    w2 = float(g*(a+b)*yc)
    w3 = float((h*(a+b-d)*yc/2))                        #CÁLCULOS
    u1 = float((f+g+h)*y*e)
    u2 = float((y*a-y*e)*(f+g+h))/2
    u =  float(u1+u2)
    sh = float(h1-h2)
    sv = float(v1+v2+w1+w2+w3-u1-u2)
    ma = float(h1*(1/3)*a+u1*(f+g+h)/2+u2*(2/3)*(f+g+h))
    if f == 0:
        mr = float(w1*((1/3)*f+g+h)+w2*((g/2)+h)+w3*((2/3)*h)+v2*((1/3)*((h*e)/(a+b-d)))+h2*e*(1/3))
    else:
        mr = float(v1*((2/3)*((a+b)/f)+f-((a+b)/f)+g+h)+w1*((1/3)*f+g+h)+w2*((g/2)+h)+w3*((2/3)*h)+v2*((1/3)*((h*e)/(a+b-d)))+h2*e*(1/3))

          
    nj = Toplevel()
    nj.title('Resultado')
    
    foto = PhotoImage(file="./bar2.png")
    f = Label(nj,image=foto)
    f.foto=foto
    f.grid(row=0,columnspan=5)
           
    Label(nj,text='H1= {:.3f}, H2= {:.3f}, V1= {:.3f}, V2= {:.3f}, W1= {:.3f}, W2= {:.3f}, W3= {:.3f}, U= {:.3f}'.format(h1,h2,v1,v2,w1,w2,w3,u)).grid(row=1)
    Label(nj,text='').grid(row=2)
    Label(nj,text='Σ Forças Horizontais= {:.3f}'.format(sh)).grid(row=3)
    Label(nj,text='Σ Forças Verticas= {:.3f}'.format(sv)).grid(row=4)
    Label(nj,text='Σ Momentos Resistentes= {:.3f}'.format(mr)).grid(row=5)
    Label(nj,text='Σ Momentos Atuantes= {:.3f}'.format(ma)).grid(row=6)

    ctc = float(mr/ma)
    cac = float((sv*fi)/sh)
    Label(nj,text='').grid(row=7)
    if ctc<=ct:
        Label(nj,text='O seu coeficiente de segurança ao TOMBAMENTO é {:.3f}, abaixo de {}. Portanto NÃO OK'.format(ctc,ct)).grid(row=8)
    else:
        Label(nj,text='O seu coeficiente de segurança ao TOMBAMENTO é {:.3f}, acima de {}. Portanto OK!'.format(ctc,ct)).grid(row=8)
        
    if cac<=ca:
        Label(nj,text='O seu coeficiente de segurança ao ESCORREGAMENTO é {:.3f}, abaixo de {}. Portanto NÃO OK'.format(cac,ca)).grid(row=9)
    else:
        Label(nj,text='O seu coeficiente de segurança ao ESCORREGAMENTO é {:.3f}, acima de {}. Portanto OK!'.format(cac,ca)).grid(row=9)

   
    nj.mainloop()

Button(bar,text='Calcular!',command=calculo).grid(row=10,columnspan=5)



bar.mainloop()
