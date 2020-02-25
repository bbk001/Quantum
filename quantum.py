import matplotlib.pyplot as plt

def numIntegration(epsilon):
    delta=0.0001 #timestep
    psi0=1 #initial psi
    psi1=1-delta**2*epsilon #psi_1
    psi=[psi0,psi1] #array keeps values of psi
    for i in range(100000): #loops through to find psi_j
        psi2=-psi0+2*psi1-2*delta**2*(epsilon-abs(i*delta))*psi1 #applies recursive formula
        psi0=psi1 #redefines psi's to run loop again
        psi1=psi2
        psi+=[psi1] #stores s=psi_j to array
    plt.plot(psi) #plots graph to determine whether function diverges up or down
    plt.show()



