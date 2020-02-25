import matplotlib.pyplot as plt

def numIntegration(epsilon):
    delta=0.0001
    psi0=1
    psi1=1-delta**2*epsilon
    psi=[psi0,psi1]
    for i in range(100000):
        psi2=-psi0+2*psi1-2*delta**2*(epsilon-abs(i*delta))*psi1
        psi0=psi1
        psi1=psi2
        psi+=[psi1]
    plt.plot(psi)
    plt.show()



