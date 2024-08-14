# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:04:54 2024

@author: msanchez
"""

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.button import MDRaisedButton
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
from kivy.properties import Clock
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

lista_mario = []
lista_mario_conceptos = []
lista_irene = []
lista_irene_conceptos = []

entradas_mario = 0
entradas_irene = 0

class Principal(Screen):                #Creación de la pantalla principal
    global entradas_mario, lista_mario, lista_mario_conceptos, lista_irene, lista_irene_conceptos, entradas_irene

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        
        #Recuadro Gris superior
        with self.canvas:
            Color(0.6, 0.6, 0.6, 0.8)
            self.rectangulo = Rectangle(size=(self.size[0], 0.15*self.size[1]), pos = (0,0.85*self.height))
            self.muestra = MDLabel(text = 'CASA SANCHEZ-TOLON',
                                font_name = 'Arial',
                                bold = True,
                                halign = 'center',
                                pos_hint = {'center_y':0.925})
            self.muestra.font_size = '42sp'
            
            self.add_widget(self.muestra)
        
        
    
        self.ecuacion = ''
        
        with self.canvas:
            Color(0.694, 0.98, 0.867, 1)
            self.rectangulo2 = Rectangle(size=(self.size[0]*0.5, 0.15*self.size[1]), pos = (self.size[0]*0.25,0.25*self.height))
            self.muestra_result = MDLabel(text = self.ecuacion , bold = True, halign = 'center', pos_hint = {'center_y':0.325})
            self.add_widget(self.muestra_result)
        
                
                
        #BOTON (MDRaisedButton). Definimos el botón y la posición
        self.botonmario = MDRaisedButton(text = 'Mario',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1), 
                                     line_color = (0,0,0,1),                                    
                                     pos_hint = {'center_x': 0.25, 'center_y': 0.7},
                                     md_bg_color = (0,0.871,0.988,1),
                                     on_press = lambda x: self.gastos_mario())

        self.add_widget(self.botonmario) #Metemos el botón dentro de la aplicación
        
        self.botonirene = MDRaisedButton(text = 'Irene',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),                                    
                                     pos_hint = {'center_x': 0.75, 'center_y': 0.7},
                                     md_bg_color = (1,0.824,0.949,1),
                                     on_press = lambda x: self.gastos_irene())
        
        
        self.add_widget(self.botonirene) #Metemos el botón dentro de la aplicación
        
        self.botonresumen = MDRaisedButton(text = 'Movimientos',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),
                                     pos_hint = {'center_x': 0.25, 'center_y': 0.15},
                                     md_bg_color = (0.98,0.945,0.694,1),
                                     on_press = lambda x: self.pasar_a_2())
        self.add_widget(self.botonresumen) #Metemos el botón dentro de la aplicación
        
        self.botonresultado = MDRaisedButton(text = 'Actualizar',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),
                                     pos_hint = {'center_x': 0.75, 'center_y': 0.15},
                                     md_bg_color = (0.98,0.875,0.694,1),
                                     on_press = lambda x: self.resultados())
        self.add_widget(self.botonresultado) #Metemos el botón dentro de la aplicación
        
        

    def resultados(self):
        global entradas_mario, lista_mario, lista_mario_conceptos, lista_irene, lista_irene_conceptos, entradas_irene
        
        suma_mario = sum(lista_mario)
        suma_mario_entre_2 = suma_mario/2
        
        suma_irene = sum(lista_irene)
        suma_irene_entre_2 = suma_irene/2
        
        if(suma_mario_entre_2 > suma_irene_entre_2):
            
            self.ecuacion = str('Irene debe: '+str(round((suma_mario_entre_2 - suma_irene_entre_2),2))+' €')
        
        elif(suma_mario_entre_2 < suma_irene_entre_2):
            
            self.ecuacion = str('Mario debe: '+str(round((suma_irene_entre_2 - suma_mario_entre_2),2))+' €')
        
        else:
            
            self.ecuacion = str('Estamos en paz')
            
        self.muestra_result.text = self.ecuacion
        self.muestra_result.font_size = '32sp'
        self.muestra_result.font_name = 'Bahnschrift'
    
    def on_size(self, *args):
        self.rectangulo.size = (self.size[0], 0.15*self.size[1])
        self.rectangulo.pos = (0, 0.85*self.height)
        
        self.rectangulo2.size = (self.size[0]*0.5, 0.15*self.size[1])
        self.rectangulo2.pos = (self.size[0]*0.25, 0.25*self.height)
        
        self.botonmario.size = (0.4*self.size[0], 0.15*self.size[1])
        self.botonmario.pos = (0.1, 0.85*self.height)
        
        self.botonirene.size = (0.4*self.size[0], 0.15*self.size[1])
        self.botonirene.pos = (0.6, 0.85*self.height)
        
        self.botonresumen.size = (0.4*self.size[0], 0.15*self.size[1])
        self.botonresumen.pos = (0.5, 0.85*self.height)
        
        self.botonresultado.size = (0.4*self.size[0], 0.15*self.size[1])
        self.botonresultado.pos = (0.6, 0.85*self.height)
        
        
    def gastos_mario(self):
        
        self.entrada1 = MDTextField(hint_text = 'Concepto',
                                 helper_text = 'Introduce el concepto del gasto',
                                 helper_text_mode = 'on_focus',
                                 pos_hint = {'center_x': 0.25, 'center_y': 0.5},
                                 size_hint = (0.4, None),
                                 on_text_validate = lambda x: self.validar1())
        self.add_widget(self.entrada1) #Metemos el botón dentro de la aplicación
        
        self.entrada2 = MDTextField(hint_text = 'Coste',
                                 helper_text = 'Introduce el importe del gasto',
                                 helper_text_mode = 'on_focus',
                                 pos_hint = {'center_x': 0.75, 'center_y': 0.5},
                                 size_hint = (0.4, None),
                                 on_text_validate = lambda x: self.validar2())
        self.add_widget(self.entrada2) #Metemos el botón dentro de la aplicación
    
    def gastos_irene(self):
        
        self.entrada3 = MDTextField(hint_text = 'Concepto',
                                 helper_text = 'Introduce el concepto del gasto',
                                 helper_text_mode = 'on_focus',
                                 pos_hint = {'center_x': 0.25, 'center_y': 0.5},
                                 size_hint = (0.4, None),
                                 on_text_validate = lambda x: self.validar3())
        self.add_widget(self.entrada3) #Metemos el botón dentro de la aplicación
        
        self.entrada4 = MDTextField(hint_text = 'Coste',
                                 helper_text = 'Introduce el importe del gasto',
                                 helper_text_mode = 'on_focus',
                                 pos_hint = {'center_x': 0.75, 'center_y': 0.5},
                                 size_hint = (0.4, None),
                                 on_text_validate = lambda x: self.validar4())
        self.add_widget(self.entrada4) #Metemos el botón dentro de la aplicación
        

    
    
    def validar1(self):
        self.entrada1.value = (self.entrada1.text)
   
        print(self.entrada1.text)
        
        
    def validar2(self):
        global lista_mario, lista_mario_conceptos
        
        self.entrada2.value = int((self.entrada2.text))
        lista_mario.append(self.entrada2.value)
        
        self.entrada1.value = (self.entrada1.text)
        lista_mario_conceptos.append(self.entrada1.value)
        
        
        self.remove_widget(self.entrada1)
        self.remove_widget(self.entrada2)
        
    def validar3(self):
       
        self.entrada3.value = (self.entrada3.text)    
    
    
    def validar4(self):
        global lista_irene, lista_irene_conceptos
        
        self.entrada4.value = int((self.entrada4.text))
        lista_irene.append(self.entrada4.value)
        
        self.entrada3.value = (self.entrada3.text)
        lista_irene_conceptos.append(self.entrada3.value)

        self.remove_widget(self.entrada3)
        self.remove_widget(self.entrada4)
    
        
    def pasar_a_2(self):
        global entradas_mario, lista_mario, entradas_irene, lista_irene
        
        self.manager.transition.direction = 'left'
        self.manager.current = 'Secundaria'
        entradas_mario = len(lista_mario)
        entradas_irene = len(lista_irene)
        
class Secundaria(Screen):
    global entradas_mario, lista_mario, lista_mario_conceptos, lista_irene, lista_irene_conceptos, entradas_irene
    def __init__(self, **kwargs):          
        super().__init__(**kwargs)

        
        
        self.boton3 = MDRaisedButton(text = 'Pasar a principal',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),
                                     pos_hint = {'center_x': 0.2, 'center_y': 0.15},
                                     md_bg_color = (0.98,0.875,0.694,1),
                                     on_press = lambda x: self.pasar_a_1()) 
        self.add_widget(self.boton3) #Añadimos el botón a la pantalla
        
        self.boton4 = MDRaisedButton(text = 'Actualizar',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),
                                     pos_hint = {'center_x': 0.80, 'center_y': 0.15},
                                     md_bg_color = (0.98,0.875,0.694,1),
                                     on_press = lambda x: self.actualizar())
        self.add_widget(self.boton4) #Añadimos el botón a la pantalla
        
        self.boton5 = MDRaisedButton(text = 'Borrar mes',
                                     font_size = 32,
                                     font_name = 'Bahnschrift',
                                     text_color = (0.04,0.04,0.04,1),
                                     line_color = (0,0,0,1),
                                     pos_hint = {'center_x': 0.5, 'center_y': 0.15},
                                     md_bg_color = (0.98,0.875,0.694,1),
                                     on_press = lambda x: self.salir())
        self.add_widget(self.boton5) #Añadimos el botón a la pantalla
        
    
    

    def on_size2(self, *args):
        self.boton3.size = (self.size[0]*0.25, 0.15*self.size[1])
        self.boton3.pos = (self.size[0]*0.25, 0.15*self.height)
        
        self.boton4.size = (self.size[0]*0.25, 0.15*self.size[1])
        self.boton4.pos = (self.size[0]*0.5, 0.15*self.height)
        
        self.boton5.size = (self.size[0]*0.25, 0.15*self.size[1])
        self.boton5.pos = (self.size[0]*0.75, 0.85*self.height)
        
        
    
    #Definimos lo que hace el botón. Transición a la derecha para pasar a la pantalla principal    
    def pasar_a_1(self):
        global lista_mario, lista_irene
        
        if lista_mario or lista_irene:
         
            self.manager.transition.direction = 'right'
            self.manager.current = 'Principal'    
            self.remove_widget(self.list_mario)
            self.remove_widget(self.list_ire)
            self.remove_widget(self.Scroll)
            self.remove_widget(self.Scroll_2)
            self.add_widget(self.boton4)
        
        else:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'Principal'    
            
           
        
    def actualizar(self):
        global entradas_mario, lista_mario, lista_mario_conceptos, entradas_irene, lista_irene, lista_entradas_irene
        
        if lista_mario or lista_irene:
        
        
            entradas_mario = len(lista_mario)
            entradas_irene = len(lista_irene)
            
            
            self.list_mario = MDList()
            
            for i in range(len(lista_mario)):   
                items = OneLineListItem(text=lista_mario_conceptos[i]+ '.  '+str(lista_mario[i]) + ' €')
                                    
                self.list_mario.add_widget(items)
                
            self.Scroll = ScrollView(pos_hint={"center_x": 0.25, 'center_y': 0.55}, size_hint= {0.45, 0.75})
            
            #self.contenedor_mario.add_widget(self.list_mario)
            self.Scroll.add_widget(self.list_mario)
            
            self.add_widget(self.Scroll)
            
            
            
            self.list_ire = MDList()
            for i in range(len(lista_irene)):
                items2 = OneLineIconListItem(text=lista_irene_conceptos[i]+ '.  '+str(lista_irene[i]) + ' €')
                self.list_ire.add_widget(items2)
            
            self.Scroll_2 = ScrollView(pos_hint={"center_x": 0.75, 'center_y': 0.55}, size_hint= {0.45, 0.75})
            
            #self.contenedor_mario.add_widget(self.list_mario)
            self.Scroll_2.add_widget(self.list_ire)
            
            self.add_widget(self.Scroll_2)
            
            self.remove_widget(self.boton4)
        
        else:
            
            self.manager.transition.direction = 'right'
            self.manager.current = 'Principal'  
        
    
    def salir(self):
        self.dialog = MDDialog(text='¿¿Seguro que quieres borrar los datos del mes??',
        buttons = [MDRaisedButton(text = 'SI', on_press = lambda x:self.borrar()),
                  MDRaisedButton(text='NO', on_press = lambda x: self.dialog.dismiss())])
        self.dialog.open()
        
    def borrar(self):
        global lista_mario, lista_mario_conceptos, lista_irene, lista_irene_conceptos, entradas_mario, entradas_irene
        
        lista_mario = []
        lista_mario_conceptos = []
        lista_irene = []
        lista_irene_conceptos = []

        entradas_mario = 0
        entradas_irene = 0
        
        self.remove_widget(self.list_mario)
        self.remove_widget(self.list_ire)
        self.remove_widget(self.Scroll)
        self.remove_widget(self.Scroll_2)
        
    
class AplicacionApp(MDApp):
    
    def build(self):
        
        SC = ScreenManager()
        SC.add_widget(Principal(name = 'Principal'))
        SC.add_widget(Secundaria(name = 'Secundaria'))
            
        self.theme_cls.theme_style = 'Light' #Color del fondo de la pantalla
        #self.theme_cls.primary_palette = 'Pink' #Color de la paleta
        
        
        
        
       
        
        return SC
        
    

AplicacionApp().run()