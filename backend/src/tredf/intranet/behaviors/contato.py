# Importa a interface para definir campos de formulário no Plone
# e outras dependências necessárias para o behavior.
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from tredf.intranet import _
from tredf.intranet.utils import validadores
from zope import schema
from zope.interface import provider


@provider(
    IFormFieldProvider
)  # Registra a classe como um provedor de campos de formulário no Plone
class IContato(model.Schema):
    """Define o schema para o behavior de contato."""

    model.fieldset(
        "contato",  # Nome do fieldset no formulário
        _("Contato"),  # Título do fieldset
        fields=[
            "email",  # Campo de email
            "telefone",  # Campo de telefone
        ],
    )

    # Campo de email com validação personalizada
    email = Email(
        title=_("Email"),
        required=True,
        constraint=validadores.is_valid_email,  # Valida se o email é válido
    )

    # Campo de telefone com validação personalizada
    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
        constraint=validadores.is_valid_telefone,  # Valida se o telefone é válido
    )
