# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright © 2017 Easy
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
#
# LICENSE: MIT

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import json

class Contacts (Screen):
'''

   contacts_list= [{'name': 'Владимир Путенович', 'wallet': 'plotinologevadeg'},
                   {'name': 'Налогонеплотельщик', 'wallet': 'vadegs'}
                                                                                 ]
   for contact in contacts_list:
       contact_text=(contact['name'])+'\n'+'wallet: '  + (contact['wallet'])
       print(contact_text)
       lb = Label(text= contact_text)

       def __init__(self, **kwargs):
           self.ids.fl.ids.scr.ids.mdl.add_widget(lb)

'''