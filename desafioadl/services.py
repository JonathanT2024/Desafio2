from desafioadl.models import Tarea, SubTarea

# creamos tareas y sub
def crear_nueva_tarea(texto:str):
    tarea = Tarea(descripcion=texto)
    tarea.save()
    imprimir_en_pantalla()

def crear_sub_tarea(texto:str, idtarea:int):
    tarea_encontrada = Tarea.objects.get(id=idtarea)
    subtarea = SubTarea(descripcion=texto, tarea=tarea_encontrada)
    subtarea.save()
    imprimir_en_pantalla()

# eliminar tareas y sub

def elimina_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea) 
    t.eliminada = True
    t.save()

def elimina_sub_tarea(idsubtarea:int):
    st = SubTarea.objects.get(id=idsubtarea) 
    st.eliminada = True
    st.save()

# Recuperar Tareas

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas

# imprimir tarea

def imprimir_en_pantalla():
    tareas = recupera_tareas_y_sub_tareas()
    for t in tareas:
        print (f'[{t.id}] {t.descripcion}')
    for sub_tarea in t.subtareas.filter(eliminada=False):
        print (f' [{sub_tarea.id}] {sub_tarea.descripcion}')