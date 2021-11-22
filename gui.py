from tkinter.constants import CENTER
import PySimpleGUI as sg
from PIL import Image, ImageTk
sg.theme('DarkBlue 12')
completedTotal = 0
currentStep = 0
stepInfo = ['gemaakte lampen:','stap 1', 'stap 2', 'stap 3','stap 4','stap 5','stap 6','stap 7','goed gedaan!']

filename = 'images\stap' + str(currentStep) + '.jpeg'
# Resize PNG file to size (300, 300)
size = (1000, 500)
im = Image.open(filename)
im = im.resize(size, resample=Image.BICUBIC)

def reload_image():
    filename = 'images\stap' + str(currentStep) + '.jpeg'
    # Resize PNG file to size (300, 300)
    size = (1000, 500)
    im = Image.open(filename)
    im = im.resize(size, resample=Image.BICUBIC)
    # Convert im to ImageTk.PhotoImage after window finalized
    image = ImageTk.PhotoImage(image=im)
    # update image in sg.Image
    window['-IMAGE-'].update(data=image)
    #verwijder hulp komt eraan text
    window['-Help-'].update('')

layout = [[sg.Text( key='-Info-',text_color = 'white',size=(40,1),font='Any 50',justification='center')],[sg.Text(key='-AOL-',text_color = 'white',size=(40,1),font='Any 50',justification='center')],
          [sg.ProgressBar(len(stepInfo)-1, orientation='h', size=(40, 40), border_width=4, key='-Progbar-',bar_color=['Green','Black'],visible=True)],
          [sg.Image(size=(1000, 500), key='-IMAGE-',)], 
          [sg.Button('Vorige stap'), sg.Button('Volgende stap')],
          [sg.Button('Help')],
          [sg.Text(key='-Help-',text_color = 'white',size=(40,1),font='Any 50',justification='center')]
          ]

window = sg.Window('Steps', layout, size=(1920,1080),finalize = True,  
# styling
default_button_element_size=(20,1),margins=(40,80),element_padding=(30,5),element_justification=CENTER,

no_titlebar=True,keep_on_top = True,right_click_menu = ['&Right', ['E&xit']] )

# Convert im to ImageTk.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)

# update image in sg.Image
window['-IMAGE-'].update(data=image)

window['-Info-'].update('Hallo! Vandaag gaan we een lamp in elkaar zetten')

while True:  # Event Loop
    event, values = window.read()
    
    #Auto restart if the array stepInfo is completed
    if currentStep == len(stepInfo)-1 and event == 'Volgende stap':
        #resets array
        currentStep = 0
        window['-Info-'].update(stepInfo[currentStep])
        #shows the total of completed lamps
        completedTotal += 1
        window['-AOL-'].update(completedTotal)
        window.Element('-AOL-').Update(visible=True)
        window['-Progbar-'].update_bar(currentStep)
        reload_image()
     
    #Volgende stap
    elif event == 'Volgende stap':
        #go to the next step in the array stepInfo
        currentStep += 1
        window['-Info-'].update(stepInfo[currentStep])
        #make amount of lamps invisible
        window.Element('-AOL-').Update(visible=False)
        window['-Progbar-'].update_bar(currentStep)
        reload_image()
       
    #Vorige stap
    if event == 'Vorige stap' and currentStep>1:
        #go to the previous step in the array stepInfo
        currentStep -= 1
        window['-Info-'].update(stepInfo[currentStep])
        #make amount of lamps invisible
        window.Element('-AOL-').Update(visible=False)
        window['-Progbar-'].update_bar(currentStep)
        reload_image()
       
    #help button
    if event == 'Help':
        window['-Help-'].update('Hulp komt eraan!')

    print(event, values)
    print (currentStep)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
