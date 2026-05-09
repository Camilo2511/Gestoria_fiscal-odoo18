from odoo import models, fields 

class FiscalProfile(models.Model):
    
    _name = 'gestoria.fiscal.profile'
    _description = 'Perfil Fiscal del Cliente'
    
    partner_id = fields.Many2one('res.partner', string = 'Cliente',required=True)

    #Tipo seleccion
    country_code = fields.Selection([ ('ES', 'España'), ('AD', 'Andorra')],default='ES',
    help='País fiscal',required=True)

    fiscal_year_closing_month = fields.Selection([ ('mes_de_cierre', 'Mes de cierre fiscal')])

    tax_regime = fields.Selection([('general', 'General'),('simplificado', 'Simplificado'),
    ('recargo_equivalencia','Recargo de equivalencia'), ('exento', 'Exento'), 
    ('prorrata','Prorrata')],string='Régimen fiscal',required=True)

    vat_periodicity = fields.Selection([ ('mensual', 'Mensual'), ('trimestral', 'Trimestral'), 
    ('anual','Anual'), ('no_aplica', 'no aplica')])

    igi_periodicity = fields.Selection([ ('mensual', 'Mensual'), ('trimestral', 'Trimestral'), 
    ('semestral', 'Semestral'), ('anual', 'Anual'), ('no_aplica', 'no aplica')])

    withholding_periodicity = fields.Selection([ ('mensual', 'Mensual'), ('trimestral', 'Trimestral'), 
    ('anual', 'Anual'), ('no_aplica', 'no aplica')])

    tax_agency_authorization_status = fields.Selection([ ('no_solicitado', 'No solicitado'), 
    ('solicitado', 'Solicitado'), ('activo', 'Activo'), ('caducado', 'Caducado')])


   #Tipo Booleano
    corporate_tax_applicable = fields.Boolean(string = 'Aplica impuesto sociedades')
    income_tax_applicable = fields.Boolean(string = 'Aplica IRPF / renta')
    intracommunity_operations = fields.Boolean(string = 'Operaciones intracomunitarias')
    sii_applicable = fields.Boolean(string = 'Aplica SII España')
    re_applicable = fields.Boolean(string ='Recargo de equivalencia')
    pro_rata_applicable = fields.Boolean(string = 'Prorrata IVA')
    oss_applicable = fields.Boolean(string = 'OSS')
    rental_withholding_applicable = fields.Boolean(string = 'Retenciones de alquiler')
    professional_withholding_applicable = fields.Boolean(string = 'Retenciones profesionales')
    employee_withholding_applicable = fields.Boolean(string = 'Retenciones trabajadores')

#TIPO DATE Y text
    certificate_expiration_date = fields.Date(string = 'Fecha vencimiento certificado')
    notes = fields.Text(string= 'Notas')
    

    fiscal_representative_id = fields.Many2one('res.partner', string='Representante fiscal')


