import GUI
import logging as logg

if __name__=="__main__":
    try:
        logg.info('Inside Main - Calling GUI')
        GUI_obj = GUI.GUI()
        GUI_obj.create_GUI()
    except Exception as er:
        logg.exception('Exception occured in main {}'.format(er))
        raise er


