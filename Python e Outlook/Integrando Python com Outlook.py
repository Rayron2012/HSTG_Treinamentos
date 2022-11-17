''''''

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'rayron2013@gmail.com'
mail.Subject = 'Email vindo do outlook'
mail.Body = 'Texto do corpo'
#ou mail.HTMLBody = '<p>Corpo do Email em HTML</p>'

# Anexos (pode colocar quantos quiser):
attachment  = r'C:\Users\rayro\OneDrive\GITHUB\HSTG_Treinamentes\Python e Outlook\Integrando Python com Outlook.py'
mail.Attachments.Add(attachment)

mail.Send()