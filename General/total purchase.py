#this programe finds total purchase
pizza1=float(input("prize of pizza1:"))
pizza2=float(input("prize of pizza2:"))
pizza3=float(input("prize of pizza3:"))
pizza4=float(input("prize of pizza4:"))
pizza5=float(input("prize of pizza5:"))
subtotal=pizza1+pizza2+pizza3+pizza4+pizza5
gst=subtotal/100*9
print("subtotal=",subtotal)
print("gst=",gst)
print("the total prize=",subtotal+gst)         
