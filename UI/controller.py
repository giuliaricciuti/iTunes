import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._n = None
        self._album = None

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        self._n = self._view._txtInDurata.value
        if self._n is None or self._n=="":
            self._view.txt_result.controls.append(
                ft.Text("inserisci la durata", color='red')
            )
            self._view.update_page()
            return
        try:
            int(self._n)
        except ValueError:
            self._view.txt_result.controls.append(
                ft.Text("inserisci un intero", color='red')
            )
            self._view.update_page()
            return
        self._model.creaGrafo(int(self._n))
        self._view.txt_result.controls.append(ft.Text(f"grafo creato con {self._model.getNum()[0]} vertici e "
                                              f"{self._model.getNum()[1]} archi"))
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
        self._view._ddAlbum.options.clear()
        album = self._model._album
        for a in album:
            self._view._ddAlbum.options.append(ft.dropdown.Option(
                text = a.Title,
                data = a,
                on_click=self.getSelectedAlbum
            ))

    def getSelectedAlbum(self, e):
        if e.control.data is None:
            self._album = None
        else:
            self._album = e.control.data
        print(self._album)

    def handleAnalisiComp(self, e):
        if self._album is None:
            self._view.txt_result.controls.append(
                ft.Text("inserisci un album", color='red')
            )
            self._view.update_page()
            return
        res = self._model.getBilancio(self._album)
        for r in res:
            self._view.txt_result.controls.append(
                ft.Text(f"{r[0].Title}, bilancio={r[1]}"))
        self._view.update_page()


    def handleGetSetAlbum(self, e):
        pass