from IPython.display import display, HTML,Javascript
def sendmessage():
  c=input("Enter the country code").strip()
  a=input("Enter the contact number :")
  if len(a.strip())!=10:
    print("Try checking the number")
    sendmessage()
  else:
    try:
        b=input("Enter the text message")
        pop=f"window.open('https://wa.me/{c}{a.strip()}?text={b}')"
        display(Javascript(pop))
    except:
      print("Try checking the number")
      sendmessage()