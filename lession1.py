from email_slicer import emailSlicer, printMessage

def main():
  emails = ["pqan112@gmail.com", "anpham1122000@gmail.com", "anprovip112@gmail.com"]

  for email in emails:
    username, domain = emailSlicer(email)
    printMessage(username, domain)

if __name__ == "__main__": 
  main()