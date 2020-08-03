from time import sleep
import autoit
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup():
    global browser, url, user1, password1, user2, password2, pin
    browser = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path=r'C:\GitHub\lucasmsantini\estudoAutomatizaRW\venv\geckodriver.exe')
    browser.implicitly_wait(3)
    url = 'http://172.31.249.59:8082/'
    user1 = 'santini'
    password1 = '666'
    user2 = 'admin '
    password2 = '1234'
    pin = '666'

setup()



login_pin_option = 'login__arrow-buttons-wrapper'
login_seleciona_linguagem = '//*[@id="ndd-ng-language-selector"]'
login_select_es_es = '//*[@id="ndd-ng-option-Español"]'
login_select_pt_br = '//*[@id="ndd-ng-option-Português"]'
login_select_en_us = '//*[@id="ndd-ng-option-English"]'
login_botao_submit = 'login-button-submit'
upload_dropdown_second_item = '//*[@id="documents-pending-list-grid-header-actionbar-dropdown-options"]/div/ndd-ng-dropdown-option[2]'
upload_botao_up_sem_dropdown = '//*[@id="documents-action-upload"]'
upload_area_clicavel_para_selecionar_arquivo = '/html/body/ndd-app/ng-component/ndd-ng-off-side-screen/div/div[2]/ndd-ng-spinner/fieldset/div[1]/div/div/form/ndd-ng-upload/div/kendo-upload'
upload_botao_up_final = 'offside-screen-button-add'
docs_seleciona_primeiro_item = '//*[@id="k-grid0-checkbox0"]'
docs_botao_select_all = '/html/body/ndd-app/div/ndd-layout/div/ng-component/ndd-ng-spinner/fieldset/div/ndd-documents/div/ndd-ng-grid/section/div[2]/div/kendo-grid/div/div/div/table/thead/tr/th[1]/input'
docs_imprimir_sem_dropdown = '// *[ @ id = "documents-action-print"]'
docs_drop_down = '// *[@ id = "documents-pending-list-grid-header-actionbar-dropdown-btn"]'
docs_drop_down_first_item_IMPRIMIR = '//*[@id="documents-pending-list-grid-header-actionbar-dropdown-options"]/div/ndd-ng-dropdown-option[1]'
id_salvos = 'menu-saved'
input_pin = 'login-input-pin'
input_password = 'login-input-password'
input_username = 'login-input-username'
botao_user = '.layout__navbar__menu__data__fullname'
botao_sair = botao_sair = '.layout__offsidebar__footer__logout-btn'
botao_meusDocs = '// *[ @ id = "menu-pending"]'
botao_salvos = '//*[@id="menu-saved"]'
botao_ok_apos_imprimir = '//*[@id="ndd-ng-dialog-button-ok"]'
botao_imprimir_final = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[2]/ndd-ng-|1button[1]'
usuario_logado = '/html/body/ndd-app/div/ndd-layout/ndd-ng-offsidebar[1]/div/div/div[1]/div/ndd-layout-user-menu-header/div/div/div[2]/div[2]/span'
usuario_logado_email = '/html/body/ndd-app/div/ndd-layout/ndd-ng-offsidebar[1]/div/div/div[1]/div/ndd-layout-user-menu-header/div/div/div[2]/div[3]/span'
moeda_saldo_corporate = 'money-corporate-quota-value'
moeda_saldo_private = 'money-private-quota-value'
paginas_saldo_corporate = 'pages-corporate-quota-value'
paginas_saldo_private = 'pages-private-quota-value'
cor_saldo_corporate = ''
cor_saldo_private = ''

total_docs_printed = 'total-documents-value'
total_pages_printed = 'total-pages-value'
pg_print_botao_imprimir_final = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[2]/ndd-ng-button[1]'
pg_print_botao_sel_imp = '//*[@id="select-printer-button"]'
pg_print_seleciona_segunda_imp = '/html/body/ndd-app/ng-component/ndd-ng-off-side-screen/div/div[2]/ndd-ng-spinner/fieldset/div[1]/div/div/ndd-ng-grid/section/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[1]'
pg_print_botao_selec_imp_final = '//*[@id="docprint-btn-print"]'
pg_print_botao_selec_imp_e_salvar_final = '//*[@id="docprint-btn-print-and-save"]'
pg_print_imp_selecionada = '//*[@id="select-printer-input"]'
pg_print_botao_simplex = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[2]/div/ndd-ng-radio-button[2]/div[1]/fieldset/label'
pg_print_botao_duplex = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[2]/div/ndd-ng-radio-button[1]/div[1]/fieldset/label'
pg_print_botao_color = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[1]/div/ndd-ng-radio-button[2]/div[1]/fieldset/label'
pg_print_botao_mono = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[1]/div/ndd-ng-radio-button[1]/div[1]/fieldset/label'
id_botao_selecionar_impressora_final = 'offside-screen-button-add'
docs_clica_primeiro_item = '/html/body/ndd-app/div/ndd-layout/div/ng-component/ndd-ng-spinner/fieldset/div/ndd-documents/div/ndd-ng-grid/section/div[2]/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/a'
doc_prop_botao_editar = '//*[@id="ndd-ng-button-action"]'
doc_prop_seleciona_particular = '/html/body/ndd-app/div/ndd-layout/div/ng-component/div/ng-component/section/ndd-ng-spinner/fieldset/form/div[1]/ndd-jobs-assignment/form/ndd-ng-form-fieldset/fieldset/div/ndd-ng-form-fieldset/fieldset/div/ndd-ng-radio-button-group/div/ndd-ng-radio-button[1]/div[1]/fieldset/label'
doc_prop_salvar = '//*[@id="documents-edit-save-button"]'
doc_prop_data_hora_envio = 'documentinfodetail-dataitem-datetimeprint'
doc_prop_finalidade_pre_selecionada = 'documentinfodetail-dataitem-finality'
doc_prop_duplex_simplex = 'documentinfodetail-dataitem-isduplex'
doc_prop_tamanho_papel = 'documentinfodetail-dataitem-papersize'
doc_prop_paginas = 'documentinfodetail-dataitem-pages'
doc_prop_tamanho_job = 'documentinfodetail-dataitem-documentsize'
doc_prop_tipo = 'documentinfodetail-dataitem-type'
reprografia_color = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[1]/div/ndd-ng-radio-button[2]/div[1]'
reprografia_mono = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[1]/div/ndd-ng-radio-button[1]/div[1]'
reprografia_simplex = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[2]/div/ndd-ng-radio-button[2]/div[1]'
reprografia_duplex = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[1]/div[1]/ndd-ng-form-fieldset[1]/fieldset/div/ndd-ng-radio-button-group[2]/div/ndd-ng-radio-button[1]/div[1]'
pg_print_lista_jobs_Finalidade = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[6]/span'
pg_print_lista_jobs_Custo = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[5]/span'
pg_print_lista_jobs_pgColor = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[4]/span'
pg_print_lista_jobs_pgMono = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[3]/span'
pg_print_lista_jobs_Data = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[2]/span'
pg_print_lista_jobs_Nome = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[1]/span'
pg_print_lista_botao_Editar = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[7]/button[1]'
pg_print_lista_botao_Editar_todos = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[7]/button[1]'
pg_print_lista_botao_Excluir = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-spinner/fieldset/form/div[2]/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[7]/button[2]'
pg_print_lista_edit_botao_Particular = '/html/body/ndd-app/ng-component/ndd-ng-off-side-screen/div/div[2]/ndd-ng-spinner/fieldset/div[1]/div/div/form/div/ndd-jobs-assignment/form/ndd-ng-form-fieldset/fieldset/div/ndd-ng-form-fieldset/fieldset/div/ndd-ng-radio-button-group/div/ndd-ng-radio-button[1]/div[1]'
pg_print_lista_edit_botao_Corporativo = '/html/body/ndd-app/ng-component/ndd-ng-off-side-screen/div/div[2]/ndd-ng-spinner/fieldset/div[1]/div/div/form/div/ndd-jobs-assignment/form/ndd-ng-form-fieldset/fieldset/div/ndd-ng-form-fieldset/fieldset/div/ndd-ng-radio-button-group/div/ndd-ng-radio-button[2]/div[1]'
pg_print_lista_edit_botao_Atribuir = '/html/body/ndd-app/ng-component/ndd-ng-off-side-screen/div/div[2]/ndd-ng-spinner/fieldset/div[2]/div/div/ndd-ng-button[1]'
pg_print_botão_Voltar = '//*[@id="docprint-btn-back"]'
pg_print_botao_Confirmar_sair_alteracoes = '//*[@id="ndd-ng-dialog-button-ok"]'
pg_print_botao_Cancelar_sair_alteracoes = '//*[@id="ndd-ng-dialog-button-cancel"]'
politicas_bloqueado = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr/td[1]/span[2]/i'
politicas_liberado = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr[2]/td[1]/span[1]/i'
politicas_lista_qtde_a_imprmir = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[2]/span'
conversao_mono_checked = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr[1]/td[7]/ndd-ng-light-grid-column-wrapper/ng-component/span/form/ndd-ng-checkbox/div/fieldset/label/div'
conversao_duplex_checked = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/div[1]/ng-component/ndd-ng-form-fieldset/fieldset/div/ndd-ng-light-grid/div/div[1]/table/tbody/tr[1]/td[8]/ndd-ng-light-grid-column-wrapper/ng-component/span/form/ndd-ng-checkbox/div/fieldset/label/div'
botao_exibir_detalhes = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/ndd-documents-print-view-printing-summary/div/ndd-documents-print-view-printing-summary-message/div/a'
custo_corporativo = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/ndd-documents-print-view-printing-summary/div/ndd-ng-data/dl/div/ndd-ng-data-item[1]/dd/span'
custo_particular = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/fieldset/ndd-documents-print-view-printing-summary/div/ndd-ng-data/dl/div/ndd-ng-data-item[2]/dd/span'




def logout():
    browser.find_element_by_css_selector(botao_user).click()
    sleep(1)
    browser.find_element_by_css_selector(botao_sair).click()


def login_user_pass1():
    browser.get(url)
    sleep(3)
    browser.find_element_by_id().send_keys(user1)
    browser.find_element_by_id(input_password).send_keys(password1)
    browser.find_element_by_id(login_botao_submit).click()
    sleep(4)
    logout()


def login_user_pass2():
    browser.get(url)
    sleep(3)
    browser.find_element_by_id(input_username).send_keys(user2)
    browser.find_element_by_id(input_password).send_keys(password2)
    browser.find_element_by_id(login_botao_submit).click()
    sleep(4)
    logout()


def login_pin():
    sleep(1)
    browser.get(url)
    print('--- LOGIN --- PIN ---------------------------------')
    sleep(2)
    browser.find_element_by_class_name(login_pin_option).click()
    sleep(2)
    browser.find_element_by_id(input_pin).send_keys(pin)
    browser.find_element_by_id(login_botao_submit).click()
    sleep(1)

def linguagem_portugues():
    sleep(1)
    browser.get(url)
    browser.find_element_by_class_name(login_pin_option).click()
    sleep(1)
    browser.find_element_by_xpath(login_seleciona_linguagem).click()
    sleep(1)
    browser.find_element_by_xpath(login_select_es_esselect_pt_br).click()
    sleep(1)


def linguagem_ingles():
    sleep(1)
    browser.get(url)
    browser.find_element_by_class_name(login_pin_option).click()
    sleep(1)
    browser.find_element_by_xpath(login_seleciona_linguagem).click()
    sleep(1)
    browser.find_element_by_xpath(login_select_en_us).click()
    sleep(1)


def linguagem_espanhol():
    sleep(1)
    browser.get(url)
    browser.find_element_by_class_name(login_pin_option).click()
    sleep(1)
    browser.find_element_by_xpath(login_seleciona_linguagem).click()
    sleep(1)
    browser.find_element_by_xpath(login_select_es_es).click()
    sleep(1)


def upload():
    #browser.find_element_by_xpath(dropdown).click()  # botão dropdown (TODO if) dropdown
    #browser.find_element_by_xpath(dropdown_second_item_upload).click()  #segundo item - UPLOAD (TODO if) dropdown
    browser.find_element_by_xpath(upload_botao_up_sem_dropdown).click()
    sleep(1)
    browser.find_element_by_xpath(upload_area_clicavel_para_selecionar_arquivo).click()  # clicar na área pra abrir a janela de escolha de arquiv
    sleep(1)
    path = "C:\\GitHub\\lucasmsantini\\estudoAutomatizaRW\\venv\\test.pdf"
    autoit.send(path)
    autoit.send("{ENTER}")
    sleep(1)
    browser.find_element_by_id(upload_botao_up_final).click()
    sleep(2)


def test_meus_docs_seleciona_somente_um_e_manda_imprimir(login_pin):
    #browser.maximize_window()
    browser.find_element_by_xpath(botao_meusDocs).click()  # botão meusDocs
    browser.find_element_by_xpath(docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
    ##browser.find_element_by_xpath(impimir_sem_dropdown).click()  # imprimir sem dropdown
    browser.find_element_by_xpath(docs_drop_down).click()  # botão dropdown (TODO if)
    browser.find_element_by_xpath(docs_drop_down_first_item_IMPRIMIR).click()  #primeiro item - Imprimir (TODO if)
    sleep(1)
    browser.find_element_by_xpath(botao_imprimir_final).click()  # botão imprimir final
    browser.find_element_by_xpath(botao_ok_apos_imprimir).click()  #botao OK após imprimir
    logout()


def test_meus_docs_seleciona_somente_um_e_deleta():
    login_pin()
    #browser.maximize_window()
    browser.find_element_by_xpath(botao_meusDocs).click()  # botão meusDocs
    browser.find_element_by_xpath(docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
    #browser.find_element_by_id('documents-action-delete').click()  # Deletar sem dropdown
    browser.find_element_by_xpath(docs_drop_down).click()  # botão dropdown (TODO if)
    browser.find_element_by_xpath(docs_drop_down_first_item_IMPRIMIR).click()  #quart item - Excluir (TODO if)
    sleep(2)
    browser.find_element_by_id(botao_ok_apos_imprimir).click()  #botao OK após Eccluir
    sleep(5)
    logout()


def test_meus_docs_seleciona_todos(login_pin):
    #browser.maximize_window()
    login_pin.browser.find_element_by_xpath(botao_meusDocs).click()  # botão meusDocs
    browser.find_element_by_xpath(docs_botao_select_all).click()  # botão seleciona TODOS
    #browser.find_element_by_xpath(docs_imprimir_sem_dropdown).click()  # imprimir sem dropdown
    browser.find_element_by_xpath(docs_drop_down).click()  # botão dropdown (TODO if) dropdown
    browser.find_element_by_xpath(docs_drop_down_first_item_IMPRIMIR).click()  #primeiro item - Imprimir (TODO if) ddropdown
    sleep(1)
    #browser.find_element_by_xpath(botao_imprimir_final).click()  # botão imprimir final
    #browser.find_element_by_xpath(botao_ok_apos_imprimir).click()  #botao OK após imprimir
    logout()


def test_meus_docs_salvos_seleciona_somente_um():
    login_pin()
    #browser.maximize_window()
    browser.find_element_by_xpath(botao_salvos).click()  # botão meusDocs
    browser.find_element_by_xpath(botao_salvos).click()  # botão meusDocs Salvos
    browser.find_element_by_xpath(docs_seleciona_primeiro_item).click()  # botão seleciona o 1º item
    #browser.find_element_by_xpath(impprimir_sem_dropdown).click()  # imprimir sem dropdown
    browser.find_element_by_xpath(docs_drop_down).click()  # botão dropdown (TODO if)
    browser.find_element_by_xpath(docs_drop_down_first_item_IMPRIMIR).click()  #primeiro item - Imprimir (TODO if)
    sleep(1)
    browser.find_element_by_xpath(botao_imprimir_final).click()  # botão imprimir final
    logout()


def test_meus_docs_upload():
    login_pin()
    browser.maximize_window()
    browser.find_element_by_xpath().click(botao_meusDocs)
    upload()

def func_verifica_se_impressora_foi_selecionada_corretamente():
    login_pin()
    browser.find_element_by_xpath(botao_meusDocs).click()
    sleep(2)
    print_impressora_selecionada = browser.find_element_by_xpath(pg_print_imp_selecionada).get_property('value')
    print('---------------------- Impressora selecionada (Original): ', print_impressora_selecionada)
    sleep(1)
    browser.find_element_by_xpath(pg_print_botao_sel_imp).click()
    sleep(1)
    browser.find_element_by_xpath(pg_print_seleciona_segunda_imp).click()
    sleep(1)
    browser.find_element_by_xpath(pg_print_botao_selec_imp_final).click()
    sleep(1)
    print_impressora_selecionada_apos_alterar = browser.find_element_by_xpath(pg_print_imp_selecionada).get_property('value')
    print('---------------------- Impressora selecionada (Alterada): ', print_impressora_selecionada_apos_alterar)

    if print_impressora_selecionada != print_impressora_selecionada_apos_alterar:
        print('------------------- Imressora alterada com sucesso ----------------------')
    else:
        print('------------------- Impressora não alterada - ERRO ----------------------')


def func_verifica_se_tem_salvos():
    print('Xpath salvos: ,', botao_salvos)

    detect_salvos = browser.find_element_by_xpath(botao_salvos).get_attribute('id')
    print('salvos: ,', detect_salvos)

    if detect_salvos == id_salvos:
        return botao_salvos
        print('Tem salvos')
    else:
        return False
        print('Não tem Salvos')


def propriedades_doc_altera_finalidade():
    login_pin()
    browser.find_element_by_xpath(botao_meusDocs).click()
    sleep(2)
    browser.find_element_by_xpath(docs_clica_primeiro_item).click()
    sleep(1)
    fin_doc = browser.find_element_by_id(doc_prop_finalidade_pre_selecionada).text
    print (fin_doc)
    dup_doc = browser.find_element_by_id(doc_prop_duplex_simplex).text
    print (dup_doc)
    browser.find_element_by_xpath(doc_prop_botao_editar)
    sleep(1)
    browser.find_element_by_xpath(doc_prop_seleciona_particular).click()
    browser.find_element_by_xpath(doc_prop_salvar).click()


def verifica_saldo():
    login_pin()
    saldo_c = browser.find_element_by_id(moeda_saldo_corporate).text
    saldo_p = browser.find_element_by_id(moeda_saldo_private).text
    tot_docs = browser.find_element_by_id(total_docs_printed).text
    tot_page = browser.find_element_by_id(total_pages_printed).text
    print(saldo_c)
    print(saldo_p)
    print(tot_docs)
    print(tot_page)
    browser.find_element_by_xpath(botao_meusDocs).click()
    sleep(2)
    browser.find_element_by_xpath(pg_print_botao_sel_imp).click()
    sleep(1)
    browser.find_element_by_xpath(pg_print_seleciona_segunda_imp).click()
    sleep(1)
    browser.find_element_by_id(pg_print_botao_selec_imp_final).click()
    sleep(1)
    browser.find_element_by_css_selector(botao_user).click()
    sleep(1)
    userlogado = browser.find_element_by_xpath(usuario_logado).text
    print(userlogado)
    emaillogado = browser.find_element_by_xpath(usuario_logado_email).text
    print(emaillogado)
    if emaillogado == '-':
        print('Não tem email')
    else:
        return emaillogado


def test_convertions():
    login_pin()
    sleep(2)
    browser.find_element_by_xpath(botao_salvos).click()
    sleep(2)
    browser.find_element_by_xpath(docs_seleciona_primeiro_item).click()

    browser.find_element_by_xpath(docs_imprimir_sem_dropdown).click()
    sleep(1)

    convertDuplex = browser.find_element_by_xpath(pg_print_botao_duplex).value_of_css_property('background-color')
    print('Cor do botão Duplex: ', convertDuplex)

    convertSimplex = browser.find_element_by_xpath(reprografia_simplex).value_of_css_property('background-color')
    print('Cor do botão Simplex: ', convertSimplex)

    convertMono = browser.find_element_by_xpath(pg_print_botao_mono).value_of_css_property('background-color')
    print('Cor do botão Mono: ', convertMono)

    convertColor = browser.find_element_by_xpath(reprografia_color).value_of_css_property('background-color')
    print('Cor do botão Color: ', convertColor)
    logout()

    '''
    convertMono = browser.find_element_by_id('print-convert-to-mono').get_attribute('id') and \
                  browser.find_element_by_css_selector('.ndd-ng-radio-button--checked').text
    print('convertMono: ', convertMono)
    convertMono_DetectSelection = browser.find_element_by_css_selector('.ndd-ng-radio-button--checked').text
    print('convertMono_D: ', convertMono_DetectSelection)
    convertMono_DetectSelection1 = browser.find_element_by_xpath('//div[contains(@class="ndd-ng-radio-button ndd-ng-radio-button--checked")]')
    
    print('convertMono_D1: ', convertMono_DetectSelection1)
    convertColor = browser.find_element_by_id('print-convert-to-color')
    print('convertColor: ', convertColor)
    convertColor1 = browser.find_element_by_id('print-convert-to-color').get_attribute('id') and \
                    browser.find_element_by_css_selector('.ndd-ng-radio-button--checked').text
    print('convertColor1: ', convertColor1)
    convertColor_DetectSelection = browser.find_element_by_class_name('ng-touched').text
    print('convertColor: ', convertColor_DetectSelection)

    convertDuplex2 = browser.find_element_by_xpath(pg_print_botao_duplex).find_elements_by_css_selector('.ndd-ng-radio-button--checked')
    print('convertDuplex2: ', convertDuplex2)

    convertDuplex3 = browser.find_element_by_xpath(pg_print_botao_duplex)
    print('convertDuplex3: ', convertDuplex3)

    convertDuplex4 = browser.find_element_by_css_selector('.ndd-ng-radio-button--checked').get_attribute('id')
    print('convertDuplex4: ', convertDuplex4)
    sleep(1)

    convertDuplex5 = str(browser.find_element(By.XPATH(pg_print_botao_duplex)))
    print('convertDuplex5: ', convertDuplex5)

    convertDuplex6 = str(browser.find_element(By.XPATH('//div[@class="ndd-ng-radio-button--checked"]')))
    print('convertDuplex6: ', convertDuplex6)

    convertDuplex7 = browser.find_element(By.XPATH('//div[@class="ndd-ng-radio-button--checked"]')).getCssValue("background-color")
    print('convertDuplex7: ', convertDuplex7)

    convertDuplex8 = browser.find_element(By.XPATH('//div[@class="ndd-ng-radio-button--checked"]')).getCssValue("color");
    print('convertDuplex8: ', convertDuplex8)
    '''


def test_atribuir():
    login_pin()
    sleep(2)
    browser.find_element_by_xpath(botao_salvos).click()
    sleep(2)
    browser.find_element_by_xpath(docs_seleciona_primeiro_item).click()
    browser.find_element_by_xpath(docs_imprimir_sem_dropdown).click()
    sleep(1)
    browser.find_element_by_xpath(pg_print_lista_botao_Editar_todos).click()
    browser.find_element_by_xpath(pg_print_lista_edit_botao_Corporativo).click()
    browser.find_element_by_xpath(pg_print_lista_edit_botao_Atribuir).click()


def test_politicas():
    cont = 0

    login_pin()
    sleep(2)
    browser.find_element_by_xpath(botao_meusDocs).click()
    print('--- Acessando meus docs ---------------------------')
    sleep(2)
    browser.find_element_by_xpath(docs_botao_select_all).click()
    print('--- Selecionando todos ----------------------------')
    browser.find_element_by_xpath(docs_imprimir_sem_dropdown).click()
    print('--- Clique no botão imprimir-----------------------')
    sleep(1)
    browser.find_element_by_xpath(pg_print_lista_botao_Editar_todos).click()
    print('--- Editar lista pra print ------------------------')
    sleep(1)
    browser.find_element_by_xpath(pg_print_lista_edit_botao_Corporativo).click()
    print('--- Atribuindo para corporativo -------------------')
    browser.find_element_by_xpath(pg_print_lista_edit_botao_Atribuir).click()
    print('--- Click botão atribuir --------------------------')
    sleep(1)
    browser.find_element_by_xpath(pg_print_botao_selec_imp_final).click()
    print('--- confirmando alterações ------------------------')
    sleep(2)

    politicas_qtde_total = int(browser.find_element_by_xpath(politicas_lista_qtde_a_imprmir).text[0])
    print('--- Buscando lista --------------------------------')
    print('--- Qtde de docs na lista: ', politicas_qtde_total)

    # Selecionar todos os elementos que possuem os xpaths das políticas
    politicas_block = browser.find_elements_by_xpath(politicas_bloqueado)#.get_property('title')
    politicas_liber = browser.find_elements_by_xpath(politicas_liberado)#.get_property('title')
    print('pol block_: ', politicas_block)
    print('pol block_: ', politicas_liber)
    print('----- FOR IT --------------------------------------')

    # Para cada aparição, printar as informações
    for pol in politicas_block:
        politicas_block = browser.find_element_by_xpath(politicas_bloqueado).get_property('title')
        teste = pol.find_element_by_xpath(politicas_bloqueado).get_property('title')
        print('pol: ', pol.get_property('title'))
        print(politicas_block)
        print(teste)
    print('---------------------------------------------------')
    for pol in politicas_liber:
        politicas_liber = browser.find_element_by_xpath(politicas_liberado).get_property('title')
        teste = pol.find_element_by_xpath(politicas_liberado).get_property('title')
        print('pol: ', pol.get_property('title'))
        print(politicas_liber)
        print(teste)

    #browser.find_element_by_xpath(pg_print_botão_Voltar).click()
    #browser.find_element_by_xpath(pg_print_botao_Confirmar_sair_alteracoes).click()

def test_politicas_conversoes():
    test_politicas()
    sleep(1)
    print('--- Aguardando informações da tela----------------')
    browser.find_element_by_xpath(pg_print_botao_selec_imp_final).click()
    print('--- Click Botão Imprimir  ------------------------')
    sleep(2)
    print('----------CONVERSÕES------------------------------')
    politicas_qtde_total = int(browser.find_element_by_xpath(politicas_lista_qtde_a_imprmir).text[0])
    print ('Qtde de docs na lista: ', politicas_qtde_total)
    print('--------------------------------------------------')

    botao_convertMono = browser.find_element_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark').get_property('name')
    print('.get_property("name") ',botao_convertMono)
    botao_convertMono2 = browser.find_elements_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark')
    print('find_elentS ',botao_convertMono2)
    botao_convertMono3 = browser.find_element_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark').get_property('value')
    print('.get_property("value") ',botao_convertMono3)
    botao_convertMono4 = browser.find_element_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark').is_selected()
    print('.is_selected() ',botao_convertMono4)
    botao_convertMono5 = browser.find_element_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark').is_enabled()
    print('.is_enabled() ',botao_convertMono5)
    botao_convertMono6 = browser.find_element_by_css_selector('.ndd-ng-checkbox .ndd-ng-checkbox__input--checkmark').is_displayed()
    print('.is_displayed() ',botao_convertMono6)

    if botao_convertMono == 'False':
        botao_convertMono.click()
    print('--- if botao_convertmono --------------------------')
    sleep(3)

    print('--- FOR - IN --------------------------------------')
    for lista in botao_convertMono2:
        print(lista)
    browser.find_element_by_xpath(botao_exibir_detalhes).click()
    print('---------------------------------------------------')
    print('Custo total Corporativo: ',browser.find_element_by_xpath(custo_porporativo).text)
    print('Custo total Particular: ',browser.find_element_by_xpath(custo_particular).text)
    #for botao in botao_convertMono:

spinner_loading = '/html/body/ndd-app/div/ndd-layout/div/ng-component/section/ndd-ng-spinner/div'
test_politicas_conversoes()

print('Teste finalizado --------------------------------------')

