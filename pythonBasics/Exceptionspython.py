ItemsInCart=0

#2 Items will be added to cart.

if ItemsInCart != 2:
    pass
    #raise Exception("Product cart count not matching")

assert (ItemsInCart == 0)


try:
    with open("test1.txt", "r") as reader:
        reader.read()

#except:
  #  print("Failure of Testcase 1")

except Exception as e:
    print(e)

finally:
    print("cleaning up Resources")
