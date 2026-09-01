# IA — Dália

Módulo de Inteligência Artificial do **Dália**, projeto desenvolvido com o objetivo de oferecer suporte inteligente às usuárias por meio de **Processamento de Linguagem Natural (PLN)** e **Machine Learning**.

A IA faz parte do ecossistema do Dália, uma aplicação voltada ao acompanhamento do ciclo menstrual e do período gestacional, com foco em situações de vulnerabilidade e segurança.

---

## Sobre o projeto

O módulo de IA está sendo desenvolvido em **Python**, utilizando **Jupyter Notebook** para exploração, tratamento e análise dos dados.

A proposta é permitir que, futuramente, a usuária possa interagir com o Dália utilizando **linguagem natural**, fazendo perguntas ou descrevendo situações sem precisar navegar por uma série de menus.

O desenvolvimento foi dividido em etapas:

1. Exploração dos dados
2. Limpeza e preparação
3. Análise exploratória
4. Treinamento dos modelos
5. Avaliação e comparação
6. Desenvolvimento da interação por linguagem natural
7. Integração da IA ao aplicativo

Atualmente, o foco principal está na **análise e treinamento dos modelos**, enquanto a interface conversacional será desenvolvida posteriormente.

---

## Tecnologias utilizadas

* **Python**
* **Jupyter Notebook**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Machine Learning**
* **Processamento de Linguagem Natural (PLN)**

Para a futura camada de linguagem natural, está prevista a utilização de técnicas como:

* Normalização de texto
* Tokenização
* Vetorização **TF-IDF**
* Classificação de intenções

---

## Estrutura do projeto

```text
IA_Dalia/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_exploracao.ipynb
│   ├── 02_limpeza.ipynb
│   ├── 03_analise.ipynb
│   └── 04_modelo.ipynb
│
├── models/
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
│
└── README.md
```

A estrutura separa os dados, experimentos, modelos treinados e código-fonte, facilitando a manutenção e evolução do projeto.

---

## Dataset

Para o desenvolvimento inicial do modelo foi utilizado um dataset disponibilizado pelo **Kaggle**, contendo informações relacionadas a gestantes e seus respectivos níveis de risco.

O dataset original possui:

* **1.014 registros**
* **7 colunas**
* Ausência de um identificador individual

As variáveis são:

| Variável | Descrição |
| :--- | :--- |
| `Age` | Idade |
| `SystolicBP` | Pressão arterial sistólica |
| `DiastolicBP` | Pressão arterial diastólica |
| `BS` | Nível de glicose no sangue |
| `BodyTemp` | Temperatura corporal |
| `HeartRate` | Frequência cardíaca |
| `RiskLevel` | Classificação do nível de risco |

A variável `RiskLevel` é o **alvo (target)** da classificação e possui três categorias:

* `low risk`
* `mid risk`
* `high risk`

---

## Fluxo de desenvolvimento

```text
             DATASET
                │
                ▼
       ┌─────────────────┐
       │   Exploração    │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │     Limpeza     │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │     Análise     │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │    Treinamento  │
       └────────┬────────┘
                ▼
       ┌─────────────────┐
       │    Avaliação    │
       └─────────────────┘
```

## Autores

<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/ana-beatriz-de-oliveira-alves-388b312b1/">
        <img src="https://github.com/ana-bia07.png" width="150px;" alt="Carolina Nascimento" /><br>
        <sub><b>Ana Beatriz</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/theycallmenat/">
        <img src="https://github.com/nouveauromance.png" width="150px;" alt="Natali Mendonça" /><br>
        <sub><b>Natali Mendonça</b></sub>
      </a>
    </td>
        <td align="center">
      <a href="https://www.linkedin.com/in/rayane-barros-22a9622a5/">
        <img src="https://github.com/RayaneBarrosM.png" width="150px;" alt="Natali Mendonça" /><br>
        <sub><b>Rayane Barros</b></sub>
      </a>
    </td>
  </tr>
</table>

<p align="center">
  © Todos os direitos reservados, 2026
</p>