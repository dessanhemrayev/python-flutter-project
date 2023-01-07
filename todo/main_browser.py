import flet as ft


class Task(ft.UserControl):
    def __init__(self, input_text,remove_task):
        super().__init__()
        self.input = input_text
        self.remove_task  =  remove_task

    def build(self):
        self.task_cb = ft.Checkbox(label=self.input, expand=True)
        self.edit_tf = ft.TextField(value=self.input, expand=True)
        self.task_view = ft.Row(
            visible=True,
            controls=[
                self.task_cb,
                ft.IconButton(icon=ft.icons.CREATE_OUTLINED,
                              on_click=self.edit_clicked),
                ft.IconButton(icon=ft.icons.DELETE_OUTLINED,
                              on_click=self.remove_clicked)
            ])

        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.edit_tf,
                ft.IconButton(icon=ft.icons.CHECK, on_click=self.save_clicked),
            ])

        return ft.Column(controls=[self.task_view, self.edit_view])

    def edit_clicked(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()

    def remove_clicked(self, e):
        self.remove_task(self)

    def save_clicked(self, e):
        self.task_cb.label = self.edit_tf.value
        self.task_view.visible = True
        self.edit_view.visible = False
        self.update()


class ToDo(ft.UserControl):
    def build(self):
        self.input = ft.TextField(
            hint_text="What should be done?", expand=True)
        self.tasks = ft.Column()

        view = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                         controls=[
                             ft.Text(value="ToDos",
                                     style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                             ft.Row(
                                 controls=[
                                     self.input,
                                     ft.FloatingActionButton(
                                         icon=ft.icons.ADD, on_click=self.add_clicked)
                                 ]
                             ),
                             self.tasks
                         ]
                         )
        return view

    def add_clicked(self, e):
        if self.input.value != '':
            task = Task(self.input.value,self.remove_task)
            self.tasks.controls.append(task)
            self.input.value = ''
            self.update()
        else:
            pass

    def remove_task(self,task):
        self.tasks.controls.remove(task)
        self.update()

def main(page: ft.Page):
    page.window_height = 600
    page.window_width = 400

    page.title = "My ToDO"
    todo = ToDo()
    page.add(todo)


ft.app(target=main, view=ft.WEB_BROWSER,port=5000)