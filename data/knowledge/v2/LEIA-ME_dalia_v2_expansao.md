# Dália v2 — lote complementar de conhecimento

## Conteúdo
Este pacote contém 19 registros complementares para a base de conhecimento (RAG) da Dália.

- `dalia_knowledge_v2_expansao.jsonl`: formato recomendado para ingestão RAG, um objeto JSON por linha.
- `dalia_knowledge_v2_expansao.csv`: versão tabular para inspeção.
- Domínios: menstrual, saúde mental, violência, saúde sexual e reprodutiva, gestacional e segurança clínica.

## Importante
Este pacote é um lote complementar, não a base consolidada. Ele não inclui os 22 registros originais nem os seis registros GEST_005 a SEX_003 criados anteriormente na conversa. Integre os lotes somente após validar IDs e conteúdo.

Este material é educativo e informativo. Não é protocolo clínico, instrumento diagnóstico, prescrição nem substituto de revisão por profissionais habilitados. Antes de qualquer piloto com usuários, cada conteúdo clínico deve passar por revisão profissional, validação das fontes, revisão de linguagem, avaliação de risco e análise de privacidade/LGPD.

## Esquema
Mantidos os 10 campos existentes:
`id`, `domain`, `topic`, `title`, `content`, `keywords`, `urgency`, `source_org`, `source_title`, `source_url`.

O campo `urgency` foi mantido por compatibilidade com a v1. Ele ainda mistura prioridade clínica, escopo e governança; recomenda-se migrar futuramente para campos separados, como `urgency_level` e `scope`.

## Revisões recomendadas
1. Verificar se cada URL continua vigente no momento da implantação.
2. Revisar recomendações dependentes de calendário, faixa etária, prazo ou protocolo.
3. Revisar especialmente contracepção, PEP/PrEP, vacinação, rastreamento e encaminhamentos.
4. Não usar conteúdo recuperado como decisão clínica automática.
5. Registrar responsável pela revisão, data da revisão e versão do documento.

## Fontes
As URLs oficiais estão registradas em cada linha do JSONL/CSV. Fontes consultadas incluem Ministério da Saúde, Ministério das Mulheres e Biblioteca Virtual em Saúde do Ministério da Saúde.
Data de pesquisa e montagem: 04/11/2026.
