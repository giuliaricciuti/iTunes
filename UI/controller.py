import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._selectedGenre = None

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()

        if self._view._txnMin.value is None or self._view._txnMin.value=="":
            self._view.txt_result.controls.append(ft.Text(
                "Inserisci un minimo", color='red'
            ))
            self._view.update_page()
            return
        if self._view._txtMax.value is None or self._view._txtMax.value=="":
            self._view.txt_result.controls.append(ft.Text(
                "Inserisci un massimo", color='red'
            ))
            self._view.update_page()
            return

        try:
            int(self._view._txnMin.value)
            int(self._view._txtMax.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserisci numeri interi", color = 'red'))
            self._view.update_page()
            return

        if self._selectedGenre is None:
            self._view.txt_result.controls.append(ft.Text(
                "Seleziona un genere", color='red'
            ))
            self._view.update_page()
            return

        min = int(self._view._txnMin.value)
        max = int(self._view._txtMax.value)
        self._model.creaGrafo(min, max, self._selectedGenre.GenreId)
        self._view.txt_result.controls.append(ft.Text(
            f"Grafo creato!\n#Vertici: {self._model.getNum()[0]}"
            f"\n#Archi: {self._model.getNum()[1]}"
        ))
        self._view.update_page()


    def getSelectedGenere(self, e):
        if e.control.data is None:
            self._selectedGenre = None
        else:
            self._selectedGenre = e.control.data

    def fillDD(self):
        for g in self._model.getAllGeneri():
            self._view._ddGenere.options.append(
                ft.dropdown.Option(text=g.Name, data = g, on_click = self.getSelectedGenere)
            )

    def handleAnalisiComp(self, e):
        pass

    def handleGetSetAlbum(self, e):
        pass


