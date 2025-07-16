from nicegui import ui

class mis_contenedores:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.tabla = ui.table(columns=self.columns, rows=self.rows, row_key='nombre').classes('text-black text-center')
        self.tabla.add_slot('body-cell-estado', '''
            <q-td :props="props">
                <q-badge :color="props.value == 'Detenido' ? 'red' : 'green'">
                    {{ props.value }}
                </q-badge>
            </q-td>
        ''')
        self.tabla.add_slot('body-cell-link', '''
            <q-td :props="props">
                <a :href="props.value" target="_blank" v-if="props.value">ABRIR</a>
            </q-td>
        ''')

    def get_tabla(self):
        return self.tabla

    def get_rows(self):
        return self.rows

    def set_rows(self, rows):
        self.tabla.__setattr__('rows', rows)
        self.rows = rows