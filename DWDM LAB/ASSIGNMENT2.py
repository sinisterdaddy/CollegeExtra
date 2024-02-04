m=int(input("Enter value of m : "))  

n=int(input("Enter value of n : "))  

k=int(input("Enter value of k : "))  

w = np.random.rand(m,n)  

x = np.random.rand(n,k) #z  

z=np.dot(w,x) #sigmoid  

ex=np.exp(-z)  

sigmoid=1/(1+ex)  

print("The result of the sigmoid function is")  

print(sigmoid) 
# n=int(input("Enter size of y : "))  

# y=np.random.randint(2, size=n)  

# print("The vector y is")  

# print(y)  

# ycap=np.random.rand(n)  

# print("The vector ycap is")  

# print(ycap) 

# a=(y )@np.log(ycap)  

# b=(1-y)@np.log(1-ycap)  

# O = -(1/n)*(a+b)  

# print("the value of O is ",O) 