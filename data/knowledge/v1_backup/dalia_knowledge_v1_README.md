# Dália — Base de Conhecimento v1

Data de compilação: 02/11/2026
Idioma: Português (Brasil)
Registros: 22
Formato principal recomendado para ingestão: JSONL
Formato auxiliar para inspeção: CSV

## Objetivo
Corpus inicial de conhecimento para recuperação (RAG) em um assistente conversacional informativo e de acolhimento sobre saúde gestacional, menstrual, saúde mental, violência contra a mulher e saúde sexual/reprodutiva.

## Arquivos
- `dalia_knowledge_v1.jsonl`: um registro JSON por linha, pronto para parsing.
- `dalia_knowledge_v1.csv`: versão tabular para revisão manual.
- `dalia_knowledge_v1_README.md`: documentação e cuidados de uso.

## Importante: RAG, não treinamento direto
Este corpus foi estruturado para recuperação de trechos relevantes (RAG). Não misture os textos como se fossem exemplos rotulados do classificador preditivo de risco materno. O modelo preditivo e a base conversacional têm objetivos, validações e métricas diferentes.

Pipeline sugerido:
1. Carregar o JSONL.
2. Separar `content` em documentos e preservar `id`, `domain`, `topic`, `urgency`, `source_org`, `source_title` e `source_url` como metadados.
3. Criar embeddings com modelo multilíngue/português adequado.
4. Indexar em FAISS/Chroma ou banco vetorial equivalente.
5. Recuperar poucos trechos relevantes por consulta, priorizando `urgency` quando houver sinais de risco.
6. Exibir fontes ao usuário ou manter rastreabilidade interna.
7. Atualizar e versionar o corpus quando as fontes mudarem.

## Regras de segurança essenciais
- Não diagnosticar, prescrever, ajustar doses nem orientar a interromper medicamentos.
- Não usar uma classificação de risco do modelo como diagnóstico ou decisão clínica.
- Em emergência obstétrica ou médica, orientar atendimento presencial urgente/SAMU 192.
- Em perigo imediato por violência, orientar Polícia Militar 190; Ligue 180 é canal de orientação e encaminhamento, não substitui emergência.
- Em risco suicida imediato ou tentativa/ferimento, orientar SAMU 192/UPA/pronto-socorro. CVV 188 é apoio emocional e não substitui emergência.
- Em revelação de violência: escutar, validar, respeitar autonomia, perguntar se é seguro conversar e não pressionar por denúncia ou separação.
- Em violência sexual, orientar atendimento de saúde o quanto antes; não exigir boletim de ocorrência como condição para atendimento.
- Não prometer sigilo absoluto sem garantias técnicas e legais.
- Coletar o mínimo de dados pessoais e sensíveis; realizar avaliação LGPD antes de qualquer uso real.

## Limitações desta versão
- É uma base inicial curada, não uma diretriz clínica completa.
- O conteúdo precisa de revisão por profissionais de saúde (obstetrícia, ginecologia, enfermagem, psicologia/psiquiatria e assistência social) antes de qualquer piloto com pessoas.
- As fontes e protocolos podem mudar; manter `source_url` e data de revisão.
- Informações de emergência devem ser conferidas com protocolos brasileiros e locais antes da publicação.
- O conteúdo não substitui protocolos institucionais, diretrizes clínicas ou julgamento profissional.

## Próximas melhorias
1. Adicionar fichas sobre ISTs, contracepção de emergência, amamentação, vacinação na gestação, diabetes/hipertensão gestacionais e menopausa.
2. Adicionar perguntas frequentes e exemplos de formulação em linguagem simples, revisados clinicamente.
3. Adicionar testes de segurança: tentativa de diagnóstico, pedido de dose de medicamento, ameaça de violência, risco suicida e alucinação de números/serviços.
4. Criar avaliação por domínio: precisão factual, recuperação da fonte correta, sensibilidade a sinais de alerta, encaminhamento seguro e qualidade do acolhimento.
5. Incluir data de revisão e versão em cada atualização.

## Fontes institucionais principais
- Ministério da Saúde — Saúde da Mulher: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/saude-da-mulher
- Ministério da Saúde — Pré-natal: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/g/gravidez/pre-natal
- Ministério da Saúde — Saúde materna: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/saude-da-mulher/saude-materna
- OMS — Menstrual health: https://www.who.int/news-room/fact-sheets/detail/menstrual-health
- ACOG — Abnormal uterine bleeding: https://www.acog.org/womens-health/faqs/abnormal-uterine-bleeding
- Ministério da Saúde — Endometriose: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/e/endometriose
- Ministério da Saúde — Depressão pós-parto: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/d/depressao-pos-parto
- Ministério da Saúde — Prevenção do suicídio: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/suicidio-prevencao/suicidio-prevencao
- OMS — Addressing violence against women in pre-service health training: https://iris.who.int/bitstream/handle/10665/366517/9789240064638-eng.pdf
- Ministério da Saúde — Violência sexual: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/saude-da-mulher/saude-sexual-e-reprodutiva/violencia-sexual
- Ministério das Mulheres — Ligue 180: https://www.gov.br/mulheres/pt-br/ligue180
