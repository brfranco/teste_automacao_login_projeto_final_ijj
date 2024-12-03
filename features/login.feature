Feature: Login

  Scenario: Successful login
    Given que estou na página de login
    When eu insiro credenciais válidas
    Then eu devo ser redirecionado para o painel

  Scenario: Unsuccessful login
    Given que estou na página de login
    When eu insiro credenciais inválidas
    Then eu devo ver uma mensagem de erro