# DocBot interface observations (2026-11-11)

- Page: https://wwwdev.ebi.ac.uk/docbot/?selected=ontology_tools (Visual Framework chatbot, `vf-chatbot-standalone`).
- Each question creates a conversation (`POST /docbot/api/createConversation`) and streams the answer from `POST /docbot/api/conversation` as server-sent `data:` chunks; the final chunk carries `sources`, `message_id`, `conversation_id` and a `support_contact` whose `contact_url` is https://github.com/EBISPOT/ontotools-usecases/issues.
- The welcome panel loads `GET /docbot/api/get_predefined_questions?team=ontology_tools`. On 2026-11-11 it returned a `predefinedQA` map whose keys are the 44 questions of `docbot/Ontotools-docbot.tsv` and whose values are all empty objects, so no stored answers are served: four of the questions are offered as "Try asking me" suggestions, and every question is answered live by the model. The only textual difference from the TSV is question 34, which lacks the comma after "concept in mind" in the predefined list.
- Answers for OLS-05 and TRIO-01 were word-for-word identical to the 9 November 2026 captures although they were streamed afresh; whether a server-side cache or deterministic generation is responsible is not exposed by the interface.
- "New conversation" (Chat options menu) clears the transcript without a confirmation dialog; the "Good response" / "Bad response" buttons appear only once an answer is complete, which this run used as its completion signal.
- Typical time from sending a question to a complete answer: 5 to 15 seconds.
