# ToTrack

Learnings from 1.0

the dictionary works well. But it might be useful to split tasks in each date to a 'Done': {}, and a 'ToDo': {}-category to ease splitting up tasks in the 2 frames, so to determine if we should populate the Done / ToDo-frames, we just run dictionary[date]['Done'].__len__()-function, and func > 0 means we should populate. if ..['Done'].__len()__() and ..['ToDo'].__len__() == 0, post 'No Tasks today!'


Instead of constructing a label, 2 buttons and a checkbutton for each task, we should have an overridden new element called 'Task' or so, that creates a frame with 2 buttons, a check button and a label inside, to easily con-/de-struct tasks.

Window should automatically resize to accomodate tasks

New task-name entry skal have en 'Enter' event, så man kan trykke <Enter> i stedet for at trykke på 'Add'-Button.

