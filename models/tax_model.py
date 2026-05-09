from odoo import models, fields

class TaxModel(models.Model):

    _name = 'gestoria.tax.model'
    _description = 'Catalogo de modelos fiscales'

    name = fields.Char(string= 'Nombre del modelo', required=True)
    code = fields.Char(string= 'Codigo', required=True)

    country_code = fields.Selection([ ('ES', 'España'), ('AD', 'Andorra')],default='ES',
    help='País fiscal',required=True)

    tax_area = fields.Selection([ ('iva', 'IVA'), ('igi', 'IGI'), ('retenciones', 'Retenciones'), 
    ('sociedades','Sociedades'), ('renta', 'Renta'), ('informativo', 'Informativo'), 
    ('cuentas_anuales', 'Cuentas anuales')],string='Área fiscal',default= 'iva')

    description = fields.Text(string= 'Descripcion')

    default_periodicity = fields.Selection([ ('mensual', 'Mensual'), ('trimestral', 'Trimestral'),
    ('semestral', 'Semestral'), ('anual', 'Anual') ],string= 'Periodo por defecto', default= 'mensual')

    requires_accounting_close = fields.Boolean(string= 'Requiere cierre contable')
    requires_client_approval = fields.Boolean(string= 'Requiere aprobación cliente')
    requires_payment = fields.Boolean(string= 'Puede generar pago')
    requires_attachment = fields.Boolean(string= 'Requiere justificante')
    active = fields.Boolean(string= 'Activo', default=True )

    presentation_channel = fields.Selection([ ('aeat', 'AEAT'), ('tributs_andorra', 'Tributs Andorra'), 
    ('manual', 'Manual'), ('otro', 'Otro')],string='Canal de presentación')

