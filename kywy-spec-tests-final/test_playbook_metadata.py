"""A playbook whose only purpose is its metadata: KAWA must store the agent
prompt and the skill references next to the usual inputs, outputs and
parameters. It is never executed by the tests (that would need the ai-agent
harness and real skills)."""
from kywy.client.kawa_decorators import KawaParameter, KawaTable
from kywy.client.kawa_playbook import kawa_playbook


@kawa_playbook(
    prompt=(
        'Read the credit RFQ enquiries in {messages}. For each one, extract a '
        'structured RFQ, resolving the counterparty against {clients}. Flag '
        'anything with a confidence below {threshold}.'
    ),
    skills=['chat-rfq-extraction', 'issuer-matching_k3n8fq2mz7@2'],
    inputs=[
        KawaTable('messages', {'message_id': str, 'message_text': str}),
        KawaTable('clients', {'client_id': str, 'client_legal_name': str}),
        KawaParameter('threshold', float, default=0.7),
    ],
    outputs=[
        KawaTable('parsed_rfqs', {
            'message_id': str,
            'client_id': str,
            'notional_usd': float,
            'needs_review': bool,
        }),
    ],
    description='Extracts structured credit RFQs from free-text enquiries',
    icon='MachineLearning',
    timeout=900,
)
def playbook():
    pass
