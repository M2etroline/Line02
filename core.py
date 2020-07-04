
""" I M P O R T
================================================================================
"""


# importing stuff

import time,math,random as ran,numpy as np,matplotlib.pyplot as mpl


""" A D D I T I O N A L   M A T H   F U N C T I O N S
================================================================================
"""


# calculating one of the three required vectors

def Vert(vector):
    return [-vector[1],-vector[0],(vector[0]*vector[1]*2)/vector[2]]


# vector product of two vectors

def vector_mult(v1,v2):
    return [ v1[1]*v2[2]-v1[2]*v2[1] , v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]]


# scaling vector down so its length is 1

def vector_to_versor(vector):
    div=math.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])
    return [vector[0]/div,vector[1]/div,vector[2]/div]


# whether the sign is positive or negative

def my_sign(x):
    if x>=0:
        return 1
    else:
        return -1


# correcting the 


def correct_angle(angle):
    
    if angle>180:
        return angle-180
    if angle<-180:
        return angle+180
    return angle


# displaying how much time is left

def how_much_time(tojm):
        if tojm<1:
            print(round(tojm*1000,2)," miliseconds left to compelete")
        else:
            if tojm<60: 
                print(round(tojm,2)," seconds left to compelete")
            else:
                if tojm<3600:
                    print(int(tojm//60)," minutes",int(tojm%60),"seconds left to compelete")
                else:
                    if tojm<86400:
                        print(round(tojm/3600,2)," hours left to compelete")
                    else:
                        if tojm<31536000:
                            print(round(tojm/86400,2)," days left to compelete")
                        else:
                            print(round(tojm/31536000,2)," years left to compelete")   


""" L O A D I N G   A N D   S A V I N G
================================================================================
"""


# loading the image

def loadtab(fil):
    res=[]
    a=0
    f=open(fil,'r')
    for line in f:
        tab=[]
        for i in line:
            if i!="\n":
                tab.append(int(i))
        res.append(tab)
    return res


# loading points

def loadpoints(fil):
    tab=[[],[],[]]
    res=[]
    f=open(fil,'r')
    a=""
    b=0
    for i in f:
        for d in i:
            if d=="@":
                tab[b].append(float(a))
                a=""
                b+=1        
            else:
                if d!=";":
                    a+=d
                else:
                    tab[b].append(float(a))
                    a=""
    tab[b].append(float(a))        
    for i in range(len(tab[0])):
        res.append([tab[0][i],tab[1][i],tab[2][i]])
    return res


# loading encryption key

def loadkey(file):
    
    tab=[]
    i=0
    
    f=open(file,'r')

    for d in f:
        
        if i<3:
            tab.append(float(d[4:-1]))
            
        if i==3:
            tab.append(float(d[6:-1]))
            
        if i==4:
            temp=d[8:-1].split()
            for z in range(3):
                temp[z]=float(temp[z])
            tab.append(temp)
            
        if i==5:
            tab.append(int(d[9:-1]))
            
        i+=1
        
    f.close()
    
    return tab


# saving decrypted image

def savtofil2d(tab,sav):
    
    f=open(sav,'w')
    for i in tab:
        for d in i:
            f.write(str(int(d)))
        f.write("\n")
    f.close()



# saving points to a file

def savtofil3d(tab,sav):
    ln=len(tab)
    f=open(sav,'w')
    a=""
    b=""
    c=""
    for i in range(ln):
        a+=(str(tab[i][0]))
        b+=(str(tab[i][1]))
        c+=(str(tab[i][2]))
        if i<ln-1:
            a+=(";")
            b+=(";")
            c+=(";")
    f.write(a+"@"+b+"@"+c)
    f.close()


""" T I E R   III   F U N C T I O N S
================================================================================
"""


# Visualising result

def visu(al_poi,cone_poi):
    
    tab1=[]
    tab2=[]
    tab3=[]
    atab1=[]
    atab2=[]
    atab3=[]
    
    all_poi=[item for item in al_poi if item not in cone_poi]
    
    for i in cone_poi:
        tab1.append(i[0])
        tab2.append(i[1])
        tab3.append(i[2])
        
    for i in all_poi:
        atab1.append(i[0])
        atab2.append(i[1])
        atab3.append(i[2])
        
    X = np.array(tab1)
    Y = np.array(tab2)
    Z = np.array(tab3)
    A = np.array(atab1)
    B = np.array(atab2)
    C = np.array(atab3)
    
    fig = mpl.figure()
    
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])
    
    ax.scatter(X,Y,Z,c='r',marker='o')
    ax.scatter(A,B,C,c='b',marker='^')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    mpl.show()

# comparing lists

def comparelist(tab,res):
    check=0
    for i in range(len(tab)):
        for d in range(len(tab[0])):
            if tab[i][d]!=res[i][d]:
                check+=1
    return check


# counting how many points are in the image

def count_points(tab):
    a=0
    for i in tab:
        for d in i:
            if d==1:
                a+=1
    return a


# checking where the ray has pierced the BOX

def pierce(xv,yv,zv,x,y,z,a,b,c):
    
    if xv!=0:
        xf=(a-x)/xv
        nxf=(-x)/xv
    
        yxf=float(format(y+yv*xf,'.12g'))
        zxf=float(format(z+zv*xf,'.12g'))
        nyxf=float(format(y+yv*nxf,'.12g'))
        nzxf=float(format(z+zv*nxf,'.12g'))
    
        if (yxf>=0 and xv>0 and yxf<=b):
            if (zxf>=0 and zxf<=c):
                return [a,yxf,zxf]
        if (x!=0 and xv<0 and nyxf>=0 and nyxf<=b):
            if (x!=0 and nzxf>=0 and nzxf<=c):
                return [0,nyxf,nzxf]
            
    if yv!=0:
        yf=(b-y)/yv
        nyf=(-y)/yv
        
        xyf=float(format(x+xv*yf,'.12g'))
        zyf=float(format(z+zv*yf,'.12g'))
        nxyf=float(format(x+xv*nyf,'.12g'))
        nzyf=float(format(z+zv*nyf,'.12g'))
  
        if (xyf>=0 and yv>0 and xyf<=a):
            if (zyf>=0 and zyf<=c):
                return [xyf,b,zyf]
        if (y!=0 and yv<0 and nxyf>=0 and nxyf<=a):
            if (y!=0 and nzyf>=0 and nzyf<=c):
                return [nxyf,0,nzyf]
    if zv!=0:
        zf=(c-z)/zv
        nzf=(-z)/zv
        
        xzf=float(format(x+xv*zf,'.12g'))
        yzf=float(format(y+yv*zf,'.12g'))
        nxzf=float(format(x+xv*nzf,'.12g'))
        nyzf=float(format(y+yv*nzf,'.12g'))

        if (xzf>=0 and zv>0 and xzf<=a):
            if (yzf>=0 and yzf<=b):
                return [xzf,yzf,c]
        if (z!=0 and zv<0 and nxzf>=0 and nxzf<=a):
            if (z!=0 and nyzf>=0 and nyzf<=b):
                return [nxzf,nyzf,0]
    print(xv,yv,zv,x,y,z,a,b,c)
    return -1


# checking if created cone is not cut too much

def eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
    
    ouch=pierce(main_direction[0],main_direction[1],main_direction[2],x,y,z,a,b,c)
    tes=math.sqrt( (x-ouch[0])*(x-ouch[0])+(y-ouch[1])*(y-ouch[1])+(z-ouch[2])*(z-ouch[2]))
    
    if math.fabs(rad-tes)>0.0001:
        return 0
    if lgt%2==0:
        gg=1
    else:
        gg=0
        
    tabzi=the_eye(lgt)
    
    for i in range(lgt):
        
        for d in range(lgt):
            
            dc=d-lgt//2
            ic=lgt//2-i
            
            if dc>=0:
                dc+=gg
            if ic<=0:
                ic-=gg
                
            for num in tabzi:
                if [ic,dc]==num[0]:
                    xeh=num[1]
                    heh=num[2]
                    break
                else:
                    xeh=0
                    heh=0
                    
            if math.fabs(dc)>=math.fabs(ic):
                kuk=math.fabs(dc)
            else:
                kuk=math.fabs(ic)
                
            fag=kuk/(lgt//2)
            angle_tg=math.tan(fov/2)
            
            vert_vec=vector_to_versor(Vert(main_direction))
            hori_vec=vector_to_versor(vector_mult(main_direction,vert_vec))
            
            final_x = main_direction[0]+hori_vec[0]*xeh*fag*angle_tg+vert_vec[0]*heh*fag*angle_tg
            final_y = main_direction[1]+hori_vec[1]*xeh*fag*angle_tg+vert_vec[1]*heh*fag*angle_tg
            final_z = main_direction[2]+hori_vec[2]*xeh*fag*angle_tg+vert_vec[2]*heh*fag*angle_tg
            
            ting=[final_x,final_y,final_z]
            
            stab=vector_to_versor(ting)
            
            ouch=pierce(stab[0],stab[1],stab[2],x,y,z,a,b,c)
            
            radius=math.sqrt( (x-ouch[0])*(x-ouch[0])+(y-ouch[1])*(y-ouch[1])+(z-ouch[2])*(z-ouch[2]))
            
            if radius<0.5*rad*math.fabs(math.tan(math.radians(90-fov/2))):
                return 0
            
    return 1


""" T I E R   II   F U N C T I O N S
================================================================================
"""


# calculating how many points will the program create

def calc_poi(main_direction,x,y,z,a,b,c,fov,n):
    centr=main_direction
    cent_p=pierce(centr[0],centr[1],centr[2],x,y,z,a,b,c)
    cent_r=math.sqrt( (x-cent_p[0])*(x-cent_p[0])+(y-cent_p[1])*(y-cent_p[1])+(z-cent_p[2])*(z-cent_p[2]))
    st_r=cent_r*math.tan(math.radians(fov/2))
    st_v=cent_r*st_r*st_r*math.pi/3
    n_poi=n*a*b*c/st_v
    return n_poi


# squaring tables

def sq_tab(tab,zenn):
    hgt=len(tab)
    lgt=len(tab[0])
    if hgt==lgt:
        return tab
    if hgt>lgt:
        res=[]
        dif=hgt-lgt
        pp=math.floor(dif/lgt*zenn)
        for i in range(hgt):
            temp=[]
            for d in range(dif):
                temp.append(0)
            res.append(temp)
        a=0
        while a<pp:
            mul=dif*hgt
            x=ran.randint(0,mul-1)
            if res[x//dif][x%dif]!=1:
                res[x//dif][x%dif]=1
                a+=1
        for i in range(len(res)):
            for d in res[i]:
                tab[i].append(d)
    else:
        res=[]
        dif=lgt-hgt
        pp=math.floor(dif/hgt*zenn)
        for d in range(dif):
            temp=[]
            for i in range(lgt):
                temp.append(0)
            res.append(temp)
        a=0
        while a<pp:
            mul=dif*lgt
            x=ran.randint(0,mul-1)
            if res[x//lgt][x%lgt]!=1:
                res[x//lgt][x%lgt]=1
                a+=1
        for i in res:
            tab.append(i)
    return 0


# angle distribution for coordinates

def the_eye(x):
    
    res=[]
    
    while x>0:
        
        s=x 
        p=s//2
        current_angle=-135
        fl=s%2
        j=-p
        i=-p
        
        while(j<p):
            
            while(i<p):
                
                angle_tangent=math.fabs(math.tan(math.radians(current_angle)))
                h_tangent=1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(i)
                v_tangent=angle_tangent*1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(j)
                check=[[i,j],h_tangent,v_tangent]
                
                if check not in res:
                    res.append(check)
                    
                if(True):
                    
                    angle_tangent=math.fabs(math.tan(math.radians(current_angle+180)))
                    h_tangent=1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(-i)
                    v_tangent=angle_tangent*1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(-j)
                    check=[[-i,-j],h_tangent,v_tangent]
                    
                    if check not in res:
                        res.append(check)

                    angle_tangent=math.fabs(math.tan(math.radians(current_angle+90)))
                    h_tangent=1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(-j)
                    v_tangent=angle_tangent*1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(i)
                    check=[[-j,i],h_tangent,v_tangent]
                    
                    if check not in res:
                        res.append(check)
                    
                    angle_tangent=math.fabs(math.tan(math.radians(current_angle+270)))
                    h_tangent=1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(j)
                    v_tangent=angle_tangent*1/math.sqrt(1+angle_tangent*angle_tangent)*my_sign(-i)
                    check=[[j,-i],h_tangent,v_tangent]
                    
                    if check not in res:
                        res.append(check)
                        
                current_angle+=90/(s-1)
                
                if i+1==0:
                    i+=2-fl
                else:
                    i+=1
                    
            if j+1==0:
                j+=2-fl
            else:
                j+=1
                
            current_angle=-135
            s-=2
            p=s//2
            
        x-=2
        
    return res


# main function searching for correct cone location   

def aspecialf(p,a,b,c,lgt,zenn):
    
    std_tan=math.tan(math.radians(40))
    zet=min([a,b,c])
    v_a=a*b*c
    v_s=(zet**3)*std_tan**2*math.pi/3
    nnn=zenn*v_a/v_s
    
    print("Minimal number of points required : ",nnn)
    
    for stirr in range(1000):
        
        fov=ran.random()*70+10
        tanr=math.tan(math.radians(fov/2))/std_tan
        rad=zet*(1/(tanr*tanr*p))**(1/3)
        
        for i in range(100):
            
            r=ran.randint(0,5)
            main_direction=vector_to_versor([ran.random(),ran.random(),ran.random()])
            
            if r==0:
                
                bd=ran.random()*b
                cd=ran.random()*c
                
                x=a-(rad*main_direction[0])
                y=bd+(rad*(main_direction[1]))
                z=cd+(rad*(main_direction[2]))
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return a,bd,cd,x,y,z,main_direction,fov
            if r==1:
                
                bd=ran.random()*b
                cd=ran.random()*c
                
                x=0-(rad*main_direction[0])
                y=bd+(rad*(main_direction[1]))
                z=cd+(rad*(main_direction[2]))
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return 0,bd,cd,x,y,z,main_direction,fov
            if r==2:
                
                ad=ran.random()*a
                cd=ran.random()*c
                
                x=ad+(rad*(main_direction[0]))
                y=b-(rad*main_direction[1])
                z=cd+(rad*(main_direction[2]))
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return ad,b,cd,x,y,z,main_direction,fov
            if r==3:
                
                ad=ran.random()*a
                cd=ran.random()*c
                
                x=ad+(rad*(main_direction[0]))
                y=0-(rad*main_direction[1])
                z=cd+(rad*(main_direction[2]))
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return ad,0,cd,x,y,z,main_direction,fov
            if r==4:
                
                ad=ran.random()*a
                bd=ran.random()*b
                
                x=ad+(rad*(main_direction[0]))
                y=bd*b+(rad*(main_direction[1]))
                z=c-(rad*main_direction[2])
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return ad,bd,z,x,y,z,main_direction,fov
            if r==5:
                
                ad=ran.random()*a
                bd=ran.random()*b
                
                x=ad+(rad*(main_direction[0]))
                y=bd+(rad*(main_direction[1]))
                z=0-(rad*main_direction[2])
                
                if x>=0 and x<=a and y>=0 and y<=b and z>=0 and z<=c:
                    if eije(x,y,z,fov,lgt,a,b,c,rad,main_direction):
                        return ad,bd,0,x,y,z,main_direction,fov
                    
    print("Failed to find the eye location")
    
    return ["z"]


""" T I E R   I   F U N C T I O N S
================================================================================
"""

    
# encrypting
        
def encrypting(tab,lgt,a,b,c,p,zenn,noise,key):
    
    res=[]
    
    if key==[]:
        
        while True:
            dud=aspecialf(p,a,b,c,lgt,zenn)
            if dud[0]!="z":
                break
            else:
                input("Do you want to try again?")
                
        x=dud[3]
        y=dud[4]
        z=dud[5]
        main_direction=dud[6]
        fov=dud[7]
        
    else:
        
        x=key[0]
        y=key[1]
        z=key[2]
        fov=key[3]
        main_direction=key[4]

    if lgt%2==0:
        gg=1
    else:
        gg=0

    tabzi=the_eye(lgt)

    tabx=[]
    taby=[]
    
    for i in range(lgt):
        
        for d in range(lgt):
            
            if tab[i][d]==1:
                
                dc=d-lgt//2
                ic=lgt//2-i

                if dc>=0:
                    dc+=gg
                if ic<=0:
                    ic-=gg
                    
                for num in tabzi:
                    if [dc,ic]==num[0]:
                        xeh=num[1]
                        heh=num[2]
                        break
                    else:
                        xeh=0
                        heh=0
                        
                if math.fabs(dc)>=math.fabs(ic):
                    kuk=math.fabs(dc)
                else:
                    kuk=math.fabs(ic)
                    
                angle_tg=math.tan(math.radians(fov/2))
                fag=kuk/(lgt//2)
                
                vert_vec=vector_to_versor(Vert(main_direction))
                hori_vec=vector_to_versor(vector_mult(main_direction,vert_vec))
                
                final_x = main_direction[0]+hori_vec[0]*xeh*fag*angle_tg+vert_vec[0]*heh*fag*angle_tg
                final_y = main_direction[1]+hori_vec[1]*xeh*fag*angle_tg+vert_vec[1]*heh*fag*angle_tg
                final_z = main_direction[2]+hori_vec[2]*xeh*fag*angle_tg+vert_vec[2]*heh*fag*angle_tg
            
                ting=[final_x,final_y,final_z]
                
                stab=vector_to_versor(ting)
                
                ouch=pierce(stab[0],stab[1],stab[2],x,y,z,a,b,c)
                
                radius=math.sqrt( (x-ouch[0])*(x-ouch[0])+(y-ouch[1])*(y-ouch[1])+(z-ouch[2])*(z-ouch[2]))
                skal=math.sqrt(ran.random())*radius
                
                res.append([x+stab[0]*skal,y+stab[1]*skal,z+stab[2]*skal])
                
    res_copy=res.copy()
    
    n_poi=calc_poi(main_direction,x,y,z,a,b,c,fov,len(res))
    
    drott=0
    ddd=0
    
    print("Points added outside of the cone  : ",math.ceil(n_poi-zenn))
    
    while drott<math.ceil(n_poi-zenn):

        noix=ran.random()*a
        noiy=ran.random()*b
        noiz=ran.random()*c
        
        radd=vector_to_versor([noix-x,noiy-y,noiz-z])
        fff=main_direction[0]*radd[0]+main_direction[1]*radd[1]+main_direction[2]*radd[2]
        
        if math.fabs(fff-1)<0.00001:
            ang_2w=0
        else:
            ang_2w=math.degrees(math.acos(fff))
            
        if ang_2w>fov/2:
            res.append([noix,noiy,noiz])
            drott+=1
        else:
            ddd+=1
            
    for i in range(math.ceil(n_poi*noise)):

        
        noix=ran.random()*a
        noiy=ran.random()*b
        noiz=ran.random()*c
        
        res.append([noix,noiy,noiz])
        
    ran.shuffle(res)
    
    return [res,x,y,z,fov,main_direction,lgt,res_copy]


# decrypting

def scan_space(tab,x,y,z,fov,main_direction,lgt):
    
    res=np.zeros((lgt,lgt))
    tabzi=the_eye(lgt)
    
    if lgt%2==0:
        gg=1
    else:
        gg=0
        
    flag=1
    dok=len(tab)
    angle_tab=[]
    
    for i in range(lgt):
        
        for d in range(lgt):
            
            dc=d-lgt//2
            ic=lgt//2-i
            
            if dc>=0:
                dc+=gg
            if ic<=0:
                ic-=gg
                
            for num in tabzi:
                if [ic,dc]==num[0]:
                    xeh=num[1]
                    heh=num[2]
                    break
                else:
                    xeh=0
                    heh=0
                    
            if math.fabs(dc)>=math.fabs(ic):
                kuk=math.fabs(dc)
            else:
                kuk=math.fabs(ic)
                
            angle_tg=math.tan(math.radians(fov/2))
            fag=kuk/(lgt//2)
            
            vert_vec=vector_to_versor(Vert(main_direction))
            
            hori_vec=vector_to_versor(vector_mult(main_direction,vert_vec))

            final_x = main_direction[0]+hori_vec[0]*xeh*fag*angle_tg+vert_vec[0]*-heh*fag*angle_tg
            final_y = main_direction[1]+hori_vec[1]*xeh*fag*angle_tg+vert_vec[1]*-heh*fag*angle_tg
            final_z = main_direction[2]+hori_vec[2]*xeh*fag*angle_tg+vert_vec[2]*-heh*fag*angle_tg
            
            ting=[final_x,final_y,final_z]
            
            stabd=vector_to_versor(ting)
            
            angle_tab.append([stabd,d,lgt-i-1])
            
    for g in tab:
        
        if flag==2:
            tojm=(time.perf_counter()-tim1)*dok
            how_much_time(tojm)
            flag=0
            
        if flag==1:
            tim1=time.perf_counter()
            flag+=1
            
        dist=math.sqrt( (x-g[0])*(x-g[0])+(y-g[1])*(y-g[1])+(z-g[2])*(z-g[2]))
        zium=vector_to_versor([g[0]-x,g[1]-y,g[2]-z])
        
        for disco in angle_tab:
            stab=disco[0]
            win=zium[0]*stab[0]+zium[1]*stab[1]+zium[2]*stab[2]
            if int(win)==1:
                angle_2w=0
            else:
                angle_2w=math.acos(win)
            angd=math.tan(math.fabs(angle_2w))*dist
            if angd<0.0001 and (angd>0 or angd==0):
                res[disco[1]][disco[2]]=1
                
    return res


""" M A I N   F U N C T I O N S
================================================================================
"""


def main(n,lod,sav,p,noise,key=None):
    
    if n==1:
        
        print("Starting encryption.")
        tab=loadtab(lod)
        zenn=count_points(tab)
        sq_tab(tab,zenn)
        lgt=len(tab)
        zenn=count_points(tab)
        print("Points located inside of the cone : ",zenn)
        points=encrypting(tab,lgt,10,10,10,p,zenn,noise,[])
        print("Total number of points generated  : ",len(points[0]))
        f=open("key.txt",'w')
        savtofil3d(points[0],sav)
        
        f.write("x = "+str(points[1])+"\n")
        f.write("y = "+str(points[2])+"\n")
        f.write("z = "+str(points[3])+"\n")
        f.write("fov = "+str(points[4])+"\n")
        f.write("vector = "+str(points[5][0])+" "+str(points[5][1])+" "+str(points[5][2])+"\n")
        f.write("length = "+str(points[6])+"\n")
        
        f.close()
        
        print("Encryption finished! Result saved to",sav)

        # Visualisation of results
        
        #visu(points[0],points[7])
        
        return tab
    
    if n==2:
        
        print("Starting decryption.")
        tab=loadpoints(lod)
        keytab=loadkey(key)
        res=scan_space(tab,keytab[0],keytab[1],keytab[2],keytab[3],keytab[4],keytab[5])
        savtofil2d(res,sav)
        print("Decryption finished! Result saved to",sav)
        
        return res
    
    if n==3:
        
        print("Starting encryption.")
        tab=loadtab(lod)
        zenn=count_points(tab)
        sq_tab(tab,zenn)
        lgt=len(tab)
        zenn=count_points(tab)
        print("Points located inside of the cone : ",zenn)
        keytab=loadkey(key)
        points=encrypting(tab,lgt,10,10,10,p,zenn,noise,keytab)
        print("Total number of points generated  : ",len(points[0]))
        savtofil3d(points[0],sav)
        print("Encryption finished! Result saved to",sav)
        visu(points[0],points[7])
        
        return tab


""" A C T I V A T I N G 
================================================================================
"""


