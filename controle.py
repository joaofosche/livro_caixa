from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="joaogfs21",
    database="livro_caixa",
)

def excluir_dados():
    linha = interface_dados.tableWidget.currentRow()
    interface_dados.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))




def funcao_principal():
    linha1 = interface.lineEdit.text()
    linha2 = interface.lineEdit_2.text()

    categoria = ""

    print("Produto:",linha1)
    print("Valor:",linha2)

    if interface.radioButton.isChecked():
        print("Categoria =ALIMENTO= selecionada.")
        categoria = "Alimento"
    elif interface.radioButton_2.isChecked():
        print("Categoria =CARRO= selecionada.")
        categoria = "Carro"
    elif interface.radioButton_3.isChecked():
        print("Categoria =LIMPEZA= selecionada.")
        categoria = "Limpeza"
    elif interface.radioButton_4.isChecked():
        print("Categoria =SAÚDE= selecionada.")
        categoria = "Saúde"
    elif interface.radioButton_5.isChecked():
        print("Categoria =VESTUÁRIO= selecionada.")
        categoria = "Vestuário"
    elif interface.radioButton_6.isChecked():
        print("Categoria =MANUTENÇÃO= selecionada.")
        categoria = "Manutenção"
    elif interface.radioButton_7.isChecked():
        print("Categoria =LUZ= selecionada.")
        categoria = "Luz"
    elif interface.radioButton_8.isChecked():
        print("Categoria =OUTROS= selecionada.")
        categoria = "Outros"

    cursor = banco.cursor()
    comando_SQL = "insert into produtos (produto, valor, categoria) values (%s,%s,%s)"
    dados = (str(linha1),str(linha2),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    interface.lineEdit.setText("")
    interface.lineEdit_2.setText("")

def tela_dados():
    interface_dados.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    interface_dados.tableWidget.setRowCount(len(dados_lidos))
    interface_dados.tableWidget.setColumnCount(4)

    for i in range (0, len(dados_lidos)):
        for j in range(0, 4):
            interface_dados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))




app = QtWidgets.QApplication([])
interface = uic.loadUi("interface.ui")
interface_dados = uic.loadUi("interface_dados.ui")
interface.pushButton.clicked.connect(funcao_principal)
interface.pushButton_2.clicked.connect(tela_dados)
interface_dados.pushButton.clicked.connect(excluir_dados)



interface.show()
app.exec()